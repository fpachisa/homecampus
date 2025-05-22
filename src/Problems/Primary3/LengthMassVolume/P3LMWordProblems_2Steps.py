'''
Created on May 20, 2013
Module: P3LMWordProblems_2Steps
Generates the 2 Steps word problems on Length Mass Volume for Primary 3

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

class P3LMWordProblems_2Steps:
    
    def __init__(self):
        pass
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:["ProblemType1",],2:["ProblemType2",],3:["ProblemType3",],4:["ProblemType4",],5:["ProblemType5",],
                            6:["ProblemType6",],7:["ProblemType7",],8:["ProblemType8",],9:["ProblemType9",],10:["ProblemType10",],
                            11:["ProblemType11",],12:["ProblemType12",],13:["ProblemType13",],14:["ProblemType14",],15:["ProblemType15",],
                            16:["ProblemType16",],17:["ProblemType17",],18:["ProblemType18",],19:["ProblemType19",],20:["ProblemType20",],
                            21:["ProblemType21",],
                            }
        self.GenerateProblemType = {1:[self.GenerateProblemType1()],2:[self.GenerateProblemType2()],3:[self.GenerateProblemType3()],
                                    4:[self.GenerateProblemType4()],5:[self.GenerateProblemType5()],6:[self.GenerateProblemType6()],
                                    7:[self.GenerateProblemType7()],8:[self.GenerateProblemType8()],
                                    9:[self.GenerateProblemType9()],10:[self.GenerateProblemType10()],
                                    11:[self.GenerateProblemType11()],12:[self.GenerateProblemType12()],13:[self.GenerateProblemType13()],
                                    14:[self.GenerateProblemType14()],15:[self.GenerateProblemType15()],16:[self.GenerateProblemType16()],
                                    17:[self.GenerateProblemType17()],18:[self.GenerateProblemType18()],
                                    19:[self.GenerateProblemType19()],20:[self.GenerateProblemType20()],
                                    21:[self.GenerateProblemType21()],
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
        #return self.GenerateProblemType1()
        
    def GenerateTestProblem(self,problem_type):
        self.ProblemType = {"ProblemType1":self.GenerateProblemType1(),"ProblemType2":self.GenerateProblemType2(),"ProblemType3":self.GenerateProblemType3(),
                            "ProblemType4":self.GenerateProblemType4(),"ProblemType5":self.GenerateProblemType5(),"ProblemType6":self.GenerateProblemType6(),
                            "ProblemType7":self.GenerateProblemType7(),"ProblemType8":self.GenerateProblemType8(),"ProblemType9":self.GenerateProblemType9(),
                            "ProblemType10":self.GenerateProblemType10(),
                            "ProblemType11":self.GenerateProblemType11(),"ProblemType12":self.GenerateProblemType12(),"ProblemType13":self.GenerateProblemType13(),
                            "ProblemType14":self.GenerateProblemType14(),"ProblemType15":self.GenerateProblemType15(),"ProblemType16":self.GenerateProblemType16(),
                            "ProblemType17":self.GenerateProblemType17(),"ProblemType18":self.GenerateProblemType18(),"ProblemType19":self.GenerateProblemType19(),
                            "ProblemType20":self.GenerateProblemType20(),"ProblemType21":self.GenerateProblemType21(),
                            }
        return self.ProblemType[problem_type]

    def GenerateProblemType1(self):       
        '''e.g.:
        [Person.Girlname] had some <peanuts>.
        After packing <them> into 7 packets of 150 g each, she had 195 g of <peanuts> left.
        Find the mass of <peanuts> she had in the beginning.
        Give your answer in kilograms and grams.
        (Write your answer as in the example below.
        Example: 5 kg 678 g)'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.GirlName)
        
        self.items = [
                      ['peanuts','them'],
                      ['raisins','them'],
                      ['pasta shells','them'],
                      ['buttons','them'],
                      ['beads','them'],
                      ['rings','them'],
                      ['cherry tomatoes','them'],
                      ['shallots','them'],
                      ['play dough','it'],
                      ['coloured sand','them']
                    ]
        
        self.item = random.choice(self.items)
        
        self.number1 = randint(5,9)
        self.number2 = random.randrange(100,200,10)
        self.number3 = randint(self.number1*self.number2+510,self.number1*self.number2+700)

        self.problem = "%s had some %s.<br>"%(self.name,self.item[0])
        self.problem = self.problem + "After packing %s into %d packets of %d g each, she had %d g of %s left.<br>"%(self.item[1],self.number1,self.number2,self.number3-self.number1*self.number2,self.item[0])
        self.problem = self.problem + "Find the mass of %s she had in the beginning.<br>"%(self.item[0])
        self.problem = self.problem + "Give your answer in kilograms and grams.<br><br>"
        self.problem = self.problem + "(Write your answer as in the example below.<br>Example: 1 kg 293 g)"
        
        self.number = self.number3
                   
        div,mod = divmod(self.number,1000)
        
        self.answer = "%d kg %d g"%(div,mod)
        
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.number1,self.number2,self.number3-self.number1*self.number2,self.item[0],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType1",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":4,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType1(self,problem,answer,number1,number2,number3,item0,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
        
        #beginning of model
        if number2==number3:
            firstBrace = 'small'
            firstCellWidth = 48
            secondBrace = 'small'
            secondCellWidth = 48
            totalBrace = 'small'+str(number1+1)
        elif number2 > number3:
            firstBrace = 'medium'
            firstCellWidth = 90
            secondBrace = 'small'
            secondCellWidth = 50
            totalBrace = 'medium'+str(number1)+'small1'
        else:
            firstBrace = 'small'
            firstCellWidth = 50
            secondBrace = 'medium'
            secondCellWidth = 100
            totalBrace = 'medium1small'+str(number1)

        self.color1 = random.choice(['aqua','blueviolet','cornflowerblue','cyan','darkmagenta','deepskyblue','dodgerblue','skyblue','turquoise'])
        self.color2 = random.choice(['brown','chocolate','coral','darkorange','orange','salmon','darksalmon','deeppink','firebrick','indianred'])
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>%d g</td>"%(number2)
        for x in range(1, number1):
            self.solution_text = self.solution_text + "<td>&nbsp;</td>"
        self.solution_text = self.solution_text + "<td>%d g</td>"%(number3)
        self.solution_text = self.solution_text + "</tr>"

        self.solution_text = self.solution_text + "<tr><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td>"%(firstBrace)
        for x in range(1, number1):
            self.solution_text = self.solution_text + "<td>&nbsp;</td>"
        self.solution_text = self.solution_text + "<td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td>"%(secondBrace)
        self.solution_text = self.solution_text + "</tr>"

        self.solution_text = self.solution_text + "<tr>"
        for x in range(0, number1):
            self.solution_text = self.solution_text + "<td style='background-color:%s;height:25px;border:white solid 1px;width:%dpx'>&nbsp;</td>"%(self.color1,firstCellWidth)
        self.solution_text = self.solution_text + "<td style='background-color:%s;height:25px;border:white solid 1px;width:%dpx'>&nbsp;</td>"%(self.color2,secondCellWidth)
        self.solution_text = self.solution_text + "</tr>"

        self.solution_text = self.solution_text + "<tr><td colspan=%d><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(number1+1,totalBrace)
        self.solution_text = self.solution_text + "<tr><td colspan=%d>?</td></tr>"%(number1+1)
        self.solution_text = self.solution_text + "</table><br><br>"
        #end of model
        
        #beginning of steps
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;"
        self.solution_text = self.solution_text + "%d g &nbsp;&times;&nbsp; %d &nbsp;=&nbsp; %d g"%(number2,number1,number2*number1)
        self.solution_text = self.solution_text + "<br>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;"
        self.solution_text = self.solution_text + "She packed %d g of %s."%(number2*number1,item0)
        self.solution_text = self.solution_text + "<br><br><br>"
        self.solution_text = self.solution_text + "</font>"
        
        self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td>%d g &nbsp;+&nbsp; %d g</td><td style='padding-left:0px;padding-right:0px;'>=</td><td>%d g</td></tr>"%(number2*number1,number3,number2*number1+number3)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-left:0px;padding-right:0px;'>=</td><td>%s</td></tr>"%(answer)
        self.solution_text = self.solution_text + "</table>"
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;"
        self.solution_text = self.solution_text + "She had %s of %s in the beginning."%(answer,item0)
        self.solution_text = self.solution_text + "</font>"
        #end of steps
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType2(self):       
        '''e.g.:
        [Person.Boyname] <is competing in a race>.
        He has to <run> from Point A to Point B and back.
        The distance between Point A and Point B is 21 km.
        How much further must he <run to finish the race>, if he has already <run> 18 km?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.BoyName)
        
        self.items = [
                        ['is competing in a race','run','run to finish the race','run',randint(10,42),'run','further to finish the race'],
                        ['is competing in a cycle race','cycle','cycle to finish the race','cycled',randint(10,50),'cycle','further to finish the race'],
                        ['is doing his daily jog','jog','jog','jogged',randint(5,12),'jog','further'],
                        ['is out doing his daily exercise','walk','walk','walked',randint(3,6),'walk','further'],
                        ['has participated in a bike race','bike','bike to finish the race','biked',randint(10,50),'bike','further to finish the race'],
                        ['has participated in a car race','drive','drive to finish the race','driven',randint(50,100),'drive','further to finish the race'],
                        ['has participated in a rowing race','row','row to finish the race','rowed',randint(10,20),'row','further to finish the race'],
                        ['is competing in a hurdle race','run over hurdles','run to finish the race','run',randint(2,5),'run','further to finish the race'],
                        ['is competing in a skipping race','skip','skip to finish the race','skipped',randint(2,5),'skip','further to finish the race'],
                        ['has participated in a horse riding race','ride his horse','ride his horse to finish the race','ridden',randint(5,12),'ride','further to finish the race']
                    ]
        
        self.item = random.choice(self.items)
        
        self.number1 = self.item[4]
        self.number2 = (self.number1 * randint(120,180))/100
        
        self.problem = "%s %s.<br>"%(self.name,self.item[0])
        self.problem = self.problem + "He has to %s from Point A to Point B and back.<br>"%(self.item[1])
        self.problem = self.problem + "The distance between Point A and Point B is %d km.<br>"%(self.number1)
        self.problem = self.problem + "How much further must he %s, if he has already %s %d km?"%(self.item[2],self.item[3],self.number2)
        
        self.answer = self.number1*2 - self.number2
        
        self.unit = "km"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.number1,self.number2,self.item[5],self.item[6],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType2",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType2(self,problem,answer,number1,number2,item5,item6,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        #beginning of model
        if number1<number2:
            self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
            self.solution_text = self.solution_text + "<tr><td style='width:150px;padding-bottom:0px;'>%d km</td><td style='width:50px'>&nbsp;</td><td style='width:100px'>&nbsp;</td></tr>"%(number1)
            self.solution_text = self.solution_text + "<tr><td colspan=3 style='padding-top:0px;padding-bottom:0px;'><img src='/images/explanation/P3_LMV_2SWP_PT2_a.png' /></td></tr>"
            self.solution_text = self.solution_text + "<tr><td colspan=2 style='padding-top:0px;'>%d km</td><td style='padding-top:0px;'>?</td></tr>"%(number2)
            self.solution_text = self.solution_text + "</table><br><br>"
        else:
            self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
            self.solution_text = self.solution_text + "<tr><td style='width:150px;padding-bottom:0px;'>%d km</td><td style='width:50px'>&nbsp;</td><td style='width:100px'>&nbsp;</td></tr>"%(number1)
            self.solution_text = self.solution_text + "<tr><td colspan=3 style='padding-top:0px;padding-bottom:0px;'><img src='/images/explanation/P3_LMV_2SWP_PT2_b.png' /></td></tr>"
            self.solution_text = self.solution_text + "<tr><td colspan=2 style='padding-top:0px;'>%d km</td><td style='padding-top:0px;'>?</td></tr>"%(number2)
            self.solution_text = self.solution_text + "</table><br><br>"
        #end of model
        
        #beginning of steps
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;"
        self.solution_text = self.solution_text + "%d km &nbsp;&times;&nbsp; 2 &nbsp;=&nbsp; %d km"%(number1,number1*2)
        self.solution_text = self.solution_text + "<br>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;"
        self.solution_text = self.solution_text + "The total distance from Point A to Point B and back is %d km."%(number1*2)
        self.solution_text = self.solution_text + "<br><br>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;"
        self.solution_text = self.solution_text + "%d km &nbsp;&minus;&nbsp; %d km &nbsp;=&nbsp; %d km"%(number1*2,number2,answer)
        self.solution_text = self.solution_text + "<br>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;"
        self.solution_text = self.solution_text + "He must %s %d km %s."%(item5,answer,item6)
        self.solution_text = self.solution_text + "</font>"
        #end of steps

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType3(self):       
        '''e.g.:
        [Person.Name] <has> a <dictionary> and 3 <identical diaries>.
        The mass of the <dictionary> is 1 kg 975 g.
        The 3 <diaries> are 1075 g lighter than the <dictionary>.
        What is the mass of each <diary>?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.PersonName)
        
        self.items = [
                        ['has','dictionary','identical diaries','diaries','diary',random.randrange(1005,1995,5)],
                        ['bought','tub of ice cream','bags of nuts','bags of nuts','bag of nut',random.randrange(1005,1995,5)],
                        ['bought','carton of notebooks','boxes of pens','boxes of pens','box of pens',random.randrange(1005,2995,5)],
                        ['has','cinder block','identical bricks','bricks','brick',random.randrange(2005,4995,5)],
                        ['bought','box of curry puffs','bags of marshmallows','bags of marshmallows','bag of marshmallows',random.randrange(1005,2995,5)],
                        ['bought','watermelon','bottles of chocolate sauce','bottles of chocolate sauce','bottle of chocolate sauce',random.randrange(3005,4995,5)],
                        ['bought','turkey','packets of sausages','packets of sausages','packet of sausages',random.randrange(3005,5995,5)],
                        ['has','pail of paint','tins of polish','tins of polish','tin of polish',random.randrange(1005,1995,5)],
                        ['has','bag of clay','identical board games','board games','board game',random.randrange(1005,1995,5)],
                        ['has','bag of soil','packets of plant food','packets of plant food','packet of plant food',random.randrange(1005,1995,5)]
                    ]
        
        self.item = random.choice(self.items)
        
        self.number1 = self.item[5]
        self.numbers = random.choice([[3,random.randrange(200,300,5)],[4,random.randrange(100,225,5)],[5,random.randrange(100,200,5)],[6,random.randrange(50,150,5)],
                        [7,random.randrange(50,100,5)],[8,random.randrange(50,100,5)],[9,random.randrange(50,100,5)],])
        self.number2 = self.numbers[0]
        self.number3 = self.numbers[1]
        
        div1,mod1 = divmod(self.number1,1000)
        
        self.problem = "%s %s a %s and %d %s.<br>"%(self.name,self.item[0],self.item[1],self.number2,self.item[2])
        self.problem = self.problem + "The mass of the %s is %d kg %d g.<br>"%(self.item[1],div1,mod1)
        self.problem = self.problem + "The %d %s are %d g lighter than the %s.<br>"%(self.number2,self.item[3],self.number1-self.number2*self.number3,self.item[1])
        self.problem = self.problem + "What is the mass of each %s?"%(self.item[4])
        
        self.answer = self.number3
        
        self.unit = "g"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.number1,self.number2,self.number1-self.number2*self.number3,self.item[1],self.item[3],self.item[4],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType3",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType3(self,problem,answer,number1,number2,number3,item1,item3,item4,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        div1,mod1 = divmod(number1,1000)
        #beginning of model
        #number1 = mass of bigger object in kg and g
        #number3 = difference in masses
        #number2 = count of smaller object
        #answer = 1 unit mass of smaller object
        if answer>=number3:
            smallObjectBrace = 'small'
            smallObjectCellWidth = 51
            differenceBrace = 'small'
            differenceCellWidth = 51
            totalBrace = 'small'+str(number2+1)
        else:
            smallObjectBrace = 'small'
            smallObjectCellWidth = 54
            differenceBrace = 'large'
            differenceCellWidth = 150
            totalBrace = 'large1small'+str(number2)

        self.color1 = random.choice(['aqua','blueviolet','cornflowerblue','cyan','darkmagenta','deepskyblue','dodgerblue','skyblue','turquoise'])
        self.color2 = random.choice(['brown','chocolate','coral','darkorange','orange','salmon','darksalmon','deeppink','firebrick','indianred'])
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d>%d kg %d g</td></tr>"%(number2+1,div1,mod1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d style='padding-bottom:5px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(number2+1,totalBrace)
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td><td colspan=%d style='background-color:%s;height:25px;border:white solid 1px'>&nbsp;</td></tr>"%(item1,number2+1,self.color1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td>"%(item3)
        for x in range(0, number2):
            self.solution_text = self.solution_text + "<td style='background-color:%s;height:25px;border:white solid 1px;width:%dpx'>&nbsp;</td>"%(self.color2,smallObjectCellWidth)
        self.solution_text = self.solution_text + "<td>&nbsp;</td></tr>"

        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td>"
        self.solution_text = self.solution_text + "<td><img src='/images/explanation/P3_model_down_brace_%s.png' /></td>"%(smallObjectBrace)
        for x in range(1, number2):
            self.solution_text = self.solution_text + "<td style='width:%dpx'>&nbsp;</td>"%(smallObjectCellWidth)
        self.solution_text = self.solution_text + "<td><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(differenceBrace)
        
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td>"
        self.solution_text = self.solution_text + "<td>?</td>"
        for x in range(1, number2):
            self.solution_text = self.solution_text + "<td style='width:%dpx'>&nbsp;</td>"%(smallObjectCellWidth)
        self.solution_text = self.solution_text + "<td>%d g</td></tr>"%(number3)
        self.solution_text = self.solution_text + "</table><br><br>"
        #end of model

        #beginning of steps
        self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td>%d kg %d g &nbsp;&minus;&nbsp; %d g</td><td style='padding-left:0px;padding-right:0px;'>=</td><td>%d g &nbsp;&minus;&nbsp; %d g</td></tr>"%(div1,mod1,number3,number1,number3)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-left:0px;padding-right:0px;'>=</td><td>%d g</td></tr>"%(number1-number3)
        self.solution_text = self.solution_text + "</table>"
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;"
        self.solution_text = self.solution_text + "The total mass of the %d %s is %d g."%(number2,item3,number1-number3)
        self.solution_text = self.solution_text + "</font><br><br><br>"

        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;"
        self.solution_text = self.solution_text + "%d g &nbsp;&divide;&nbsp; %d &nbsp;=&nbsp; %d g"%(number1-number3,number2,answer)
        self.solution_text = self.solution_text + "<br>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;"
        self.solution_text = self.solution_text + "The mass of each %s is %d g."%(item4,answer)
        self.solution_text = self.solution_text + "</font>"
        #end of steps

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType4(self):       
        '''e.g.:
        [Person.Girlname] had 7 m 80 cm of <ribbon>.
        She <used> 250 cm of it <to tie a gift>.
        Then she cut the remaining <ribbon> into 2 equal pieces.
        What was the length of each piece?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.GirlName)
        
        self.items = [
                        ['ribbon','used','to tie a gift'],
                        ['wire','gave','to her brother'],
                        ['pipe','used','to fix a leakage'],
                        ['string','used','to mend a frock'],
                        ['pole','gave away','to a friend'],
                        ['cable','gave','to her sister'],
                        ['wooden log','used','to make a bench'],
                        ['rope','used','to tie a box'],
                        ['fishing line','tied','to her fishing rod'],
                        ['wallpaper','used','to cover a wall']
                    ]
        
        self.item = random.choice(self.items)
        
        self.number1 = random.randrange(305,995,5)
        div1,mod1 = divmod(self.number1,100)
        while mod1 == 0:
            self.number1 = random.randrange(305,995,5)
            div1,mod1 = divmod(self.number1,100)
            
        self.number2 = (self.number1 * randint(40,60))/100
        self.number3 = randint(2,9)
        
        div2,mod2 = divmod((self.number1-self.number2),self.number3)
        self.number2 = self.number2 + mod2 
        
        self.problem = "%s had %d m %d cm of %s.<br>"%(self.name,div1,mod1,self.item[0])
        self.problem = self.problem + "She %s %d cm of it %s.<br>"%(self.item[1],self.number2,self.item[2])
        self.problem = self.problem + "Then she cut the remaining %s into %d equal pieces.<br>"%(self.item[0],self.number3)
        self.problem = self.problem + "What was the length of each piece?"
        
        self.answer = div2
        
        self.unit = "cm"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,self.answer,self.number1,self.number2,self.number3,self.item[0],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType4",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType4(self,problem,answer,number1,number2,number3,item0,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        div1,mod1 = divmod(number1,100)
        #beginning of model
        #number1 = total length in m and cm
        #number2 = amount used in cm
        #number3 = count of pieces
        #answer = size of 1 piece
        if number2==answer:
            firstCellBrace = 'small'
            firstCellWidth = 51
            secondCellBrace = 'small'
            secondCellWidth = 51
            totalBrace = 'small'+str(number3+1)
        elif number2>answer:
            firstCellBrace = 'large'
            firstCellWidth = 150
            secondCellBrace = 'small'
            secondCellWidth = 54
            totalBrace = 'large1small'+str(number3)

        else:
            firstCellBrace = 'small'
            firstCellWidth = 50
            secondCellBrace = 'medium'
            secondCellWidth = 98
            totalBrace = 'medium'+str(number3)+'small1'

        self.color1 = random.choice(['aqua','blueviolet','cornflowerblue','cyan','darkmagenta','deepskyblue','dodgerblue','skyblue','turquoise'])
        self.color2 = random.choice(['brown','chocolate','coral','darkorange','orange','salmon','darksalmon','deeppink','firebrick','indianred'])
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td colspan=%d>%d m %d cm</td></tr>"%(number3+1,div1,mod1)
        self.solution_text = self.solution_text + "<tr><td colspan=%d style='padding-bottom:5px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(number3+1,totalBrace)
        self.solution_text = self.solution_text + "<tr><td style='background-color:%s;height:25px;border:white solid 1px;width:%dpx'>&nbsp;</td>"%(self.color1,firstCellWidth)
        for x in range(0, number3):
            self.solution_text = self.solution_text + "<td style='background-color:%s;height:25px;border:white solid 1px;width:%dpx'>&nbsp;</td>"%(self.color2,secondCellWidth)
        self.solution_text = self.solution_text + "</tr>"

        self.solution_text = self.solution_text + "<tr>"
        self.solution_text = self.solution_text + "<td><img src='/images/explanation/P3_model_down_brace_%s.png' /></td>"%(firstCellBrace)
        self.solution_text = self.solution_text + "<td><img src='/images/explanation/P3_model_down_brace_%s.png' /></td>"%(secondCellBrace)
        for x in range(0, number3-1):
            self.solution_text = self.solution_text + "<td style='width:%dpx'>&nbsp;</td>"%(secondCellWidth)
        self.solution_text = self.solution_text + "</tr>"
        
        self.solution_text = self.solution_text + "<tr>"
        self.solution_text = self.solution_text + "<td>%d cm</td>"%(number2)
        self.solution_text = self.solution_text + "<td>?</td>"
        for x in range(0, number3-1):
            self.solution_text = self.solution_text + "<td style='width:%dpx'>&nbsp;</td>"%(secondCellWidth)
        self.solution_text = self.solution_text + "</tr>"
        self.solution_text = self.solution_text + "</table><br><br>"
        #end of model

        #beginning of steps
        self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td>%d m %d cm &nbsp;&minus;&nbsp; %d cm</td><td style='padding-left:0px;padding-right:0px;'>=</td><td>%d cm &nbsp;&minus;&nbsp; %d cm</td></tr>"%(div1,mod1,number2,number1,number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-left:0px;padding-right:0px;'>=</td><td>%d cm</td></tr>"%(number1-number2)
        self.solution_text = self.solution_text + "</table>"
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;"
        self.solution_text = self.solution_text + "The total length of the remaining %s was %d cm."%(item0,number1-number2)
        self.solution_text = self.solution_text + "</font><br><br><br>"

        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;"
        self.solution_text = self.solution_text + "%d cm &nbsp;&divide;&nbsp; %d &nbsp;=&nbsp; %d cm"%(number1-number2,number3,answer)
        self.solution_text = self.solution_text + "<br>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;"
        self.solution_text = self.solution_text + "The length of each piece of %s was %d cm."%(item0,answer)
        self.solution_text = self.solution_text + "</font>"
        #end of steps

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType5(self):       
        '''e.g.:
        [Person.Unclename] had 13 empty <pails>, each of capacity 3 l.
        He also had a <barrel> containing 27 l of <water>.
        He poured out all the <water> from the <barrel> to completely fill some of the <pails>.
        In the end, how many <pails> were left empty?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.UncleName)
        
        self.items = [
                        ['pails','barrel','water',randint(20,50),randint(3,9),'pail'],
                        ['pails','barrel','paint',randint(20,50),randint(3,9),'pail'],
                        ['pails','fish tank','water',randint(20,99),randint(3,9),'pail'],
                        ['bottles','dispenser','jasmine tea',randint(10,20),randint(2,5),'bottle'],
                        ['bottles','container','sugar syrup',randint(6,20),randint(2,5),'bottle'],
                        ['bottles','tank','chocolate milk',randint(20,50),randint(2,5),'bottle'],
                        ['cans','barrel','petrol',randint(20,99),randint(3,9),'can'],
                        ['cans','drum','gasoline',randint(50,99),randint(2,5),'can'],
                        ['pots','canister','milk',randint(20,50),randint(2,5),'pot'],
                        ['jugs','cooler','fruit punch',randint(10,20),randint(2,5),'jug']
                    ]
        
        self.item = random.choice(self.items)
        
        self.number1 = self.item[3]
        self.number2 = self.item[4]        
        div1,mod1 = divmod(self.number1,self.number2)
        self.number1 = self.number1 - mod1       
        self.number3 = randint(3,10) 
        
        self.problem = "%s had %d empty %s, each of capacity %d <font class='litreFont'>l</font> .<br>"%(self.name,self.number3+div1,self.item[0],self.number2)
        self.problem = self.problem + "He also had a %s containing %d <font class='litreFont'>l</font>&nbsp; of %s.<br>"%(self.item[1],self.number1,self.item[2])
        self.problem = self.problem + "He poured out all the %s from the %s to completely fill some of the %s.<br>"%(self.item[2],self.item[1],self.item[0])
        self.problem = self.problem + "In the end, how many %s were left empty?"%(self.item[0])
        
        self.answer = self.number3
        
        self.unit = self.item[0]
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5(self.problem,self.answer,self.number3+div1,self.number1,self.number2,self.item[0],self.item[2],self.item[5],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType5",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType5(self,problem,answer,number3,number1,number2,item0,item2,item5,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        #beginning of model
        self.color1 = random.choice(['brown','chocolate','coral','darkorange','orange','salmon','darksalmon','deeppink','firebrick','indianred'])
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td colspan=5>%d <font class='litreFont'>l</font></td></tr>"%(number1)
        self.solution_text = self.solution_text + "<tr><td colspan=5 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_small5.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='background-color:%s;height:20px;border:white solid 1px;width:50px;padding-bottom:5px;'>%d <font class='litreFont'>l</font></td><td style='background-color:%s;height:20px;border:white solid 1px;width:50px;padding-bottom:5px;'>%d <font class='litreFont'>l</font></td><td colspan=2 style='height:20px;border:white solid 1px;width:50px;padding-bottom:5px;'>. . . . .</td><td style='background-color:%s;height:20px;border:white solid 1px;width:50px;padding-bottom:5px'>%d <font class='litreFont'>l</font></td></tr>"%(self.color1,number2,self.color1,number2,self.color1,number2)
        self.solution_text = self.solution_text + "<tr><td colspan=5><img src='/images/explanation/P3_model_down_brace_small5.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td colspan=5>? (a)</td></tr>"
        self.solution_text = self.solution_text + "</table><br><br>"
        #end of model
        
        #beginning of steps
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;"
        self.solution_text = self.solution_text + "%d &nbsp;&divide;&nbsp; %d &nbsp;=&nbsp; %d &nbsp;(a)"%(number1,number2,number1/number2)
        self.solution_text = self.solution_text + "<br>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;"
        self.solution_text = self.solution_text + "%d <font class='litreFont'>l</font>&nbsp; of %s could fill %d %s completely."%(number1,item2,number1/number2,item0)
        self.solution_text = self.solution_text + "<br><br>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;"
        self.solution_text = self.solution_text + "%d &nbsp;&minus;&nbsp; %d &nbsp;=&nbsp; %d"%(number3,number1/number2,answer)
        self.solution_text = self.solution_text + "<br>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;"
        if answer==1:
            self.solution_text = self.solution_text + "In the end, %d %s was left empty."%(answer,item5)
        else:
            self.solution_text = self.solution_text + "In the end, %d %s were left empty."%(answer,item0)
        self.solution_text = self.solution_text + "</font>"
        #end of steps

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType6(self):       
        '''e.g.:      
        [Person.Girlname] has 7 <balls of yarn>.
        Each <ball> has 3 m 10 cm of <yarn>.
        She uses two <balls of yarn for a craft project>.
        How many centimetres of <yarn> has she left?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.GirlName)
        
        self.items = [
                        ['balls of yarn','ball','yarn','balls of yarn for a craft project','yarn'],
                        ['balls of wire','ball','wire','balls of wire to make a lamp shade','wire'],
                        ['balls of jute rope','ball','rope','balls of rope to decorate a basket','rope'],
                        ['rolls of lace','roll','lace','rolls of lace to border her dress','lace'],
                        ['rolls of adhesive tape','roll','adhesive tape','rolls of adhesive tape to stick a painting to a wall','adhesive tape'],
                        ['rolls of gift wrapper','roll','gift wrapper','rolls of gift wrapper to wrap some gifts','gift wrapper'],
                        ['rolls of wallpaper','roll','wallpaper','rolls of wallpaper to cover a wall','wallpaper'],
                        ['spools of elastic band','spool','elastic band','spools of elastic band for a tailoring project','elastic band'],
                        ['spools of thread','spool','thread','spools of thread to stitch some curtains','thread'],
                        ['spools of fabric','spool','fabric','spools of fabric to a make some cushion covers','fabric']
                    ]
        
        self.item = random.choice(self.items)
        
        self.number1 = randint(4,9)
        self.number2 = randint(2,self.number1-2)
        self.number3 = random.randrange(105,395,5)
        div3,mod3 = divmod(self.number3,100)
        while mod3 == 0:
            self.number3 = random.randrange(105,995,5)
            div3,mod3 = divmod(self.number3,100)
            
        self.numbers = {2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven"}
        
        self.problem = "%s has %d %s.<br>"%(self.name,self.number1,self.item[0])
        self.problem = self.problem + "Each %s has %d m %d cm of %s.<br>"%(self.item[1],div3,mod3,self.item[2])
        self.problem = self.problem + "She uses %s %s.<br>"%(self.numbers[self.number2],self.item[3])
        self.problem = self.problem + "How many centimetres of %s has she left?"%(self.item[2])
        
        self.answer = self.number3 * (self.number1-self.number2)
        
        self.unit = "cm"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6(self.problem,self.answer,self.number1,self.number2,self.number3,self.item[0],self.item[2],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType6",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType6(self,problem,answer,number1,number2,number3,item0,item2,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        div3,mod3 = divmod(number3,100)
        #beginning of model
        self.color1 = random.choice(['brown','chocolate','coral','darkorange','orange','salmon','darksalmon','deeppink','firebrick','indianred'])
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2 style='text-align:left;'>%d m %d cm</td></tr>"%(div3,mod3)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_small.png' /></td></tr>"

        self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td>"%(item0)
        for x in range(0, number2):
            self.solution_text = self.solution_text + "<td style='background-color:%s;height:25px;border:white solid 1px;width:50px;'>&nbsp;</td>"%(self.color1)
        for x in range(number2,number1):
            self.solution_text = self.solution_text + "<td style='background-color:%s;height:25px;border:white solid 1px;width:50px;'>left</td>"%(self.color1)
        self.solution_text = self.solution_text + "</tr>"
        
        #the blanks are put in place to ensure that the cell does not shrink when the dialog window is resized to small
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d><img src='/images/explanation/P3_model_small%d_blank.png' /></td><td colspan=%d><img src='/images/explanation/P3_model_down_brace_small%d.png' /></td></tr>"%(number2,number2,number1-number2,number1-number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d>&nbsp;</td><td colspan=%d>?</td></tr>"%(number2,number1-number2)
        self.solution_text = self.solution_text + "</table><br>"
        #end of model

        #beginning of steps
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;"
        self.solution_text = self.solution_text + "%d &nbsp;&minus;&nbsp; %d &nbsp;=&nbsp; %d"%(number1,number2,number1-number2)
        self.solution_text = self.solution_text + "<br>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;"
        self.solution_text = self.solution_text + "She has %d %s left."%(number1-number2,item0)
        self.solution_text = self.solution_text + "</font><br><br><br>"

        self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td>%d m %d cm &nbsp;&times;&nbsp; %d</td><td style='padding-left:0px;padding-right:0px;'>=</td><td>%d cm &nbsp;&times;&nbsp; %d</td></tr>"%(div3,mod3,number1-number2,number3,number1-number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-left:0px;padding-right:0px;'>=</td><td>%d cm</td></tr>"%(answer)
        self.solution_text = self.solution_text + "</table>"
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;"
        self.solution_text = self.solution_text + "She has %d cm of %s left."%(answer,item2)
        self.solution_text = self.solution_text + "</font><br><br><br>"
        #end of steps

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType7(self):       
        '''e.g.:      
        <A refrigerator> has a mass of 63 kg.
        It is 3 times as heavy as <a microwave oven>.
        Find the total mass of the <refrigerator> and the <microwave oven>.'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.GirlName)
        
        self.items = [
                        ['A refrigerator','a microwave oven','refrigerator','microwave oven',randint(50,100),randint(5,9)],
                        ['A table','a stool','table','stool',randint(10,50),randint(2,9)],
                        ['A wooden log','a rock','wooden log','rock',randint(10,100),randint(2,9)],
                        ['A container','a carton','container','carton',randint(50,200),randint(5,9)],
                        ['A bed frame','a mattress','bed frame','mattress',randint(50,200),randint(5,9)],
                        ['A book shelf','a box of books','book shelf','box of books',randint(50,100),randint(2,9)],
                        ['An iron sheet','an aluminium sheet','iron sheet','aluminium sheet',randint(10,200),randint(2,9)],
                        ['A TV console','a TV set','TV console','TV set',randint(50,150),randint(5,9)],
                        ['A baby elephant','a dog','baby elephant','dog',randint(110,250),randint(5,9)],
                        ['A baby rhinoceros','a fish','baby rhinoceros','fish',randint(50,200),randint(5,9)]
                    ]
        
        self.item = random.choice(self.items)
        
        self.number1 = self.item[4]
        self.number2 = self.item[5]
        div1,mod1 = divmod(self.number1,self.number2)
        
        self.number1 = self.number1 - mod1    
                
        self.problem = "%s has a mass of %d kg.<br>"%(self.item[0],self.number1)
        self.problem = self.problem + "It is %d times as heavy as %s.<br>"%(self.number2,self.item[1])
        self.problem = self.problem + "Find the total mass of the %s and the %s."%(self.item[2],self.item[3])
        
        self.answer = self.number1 + div1
        
        self.unit = "kg"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7(self.problem,self.answer,self.number1,self.number2,self.item[2],self.item[3],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType7",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType7(self,problem,answer,number1,number2,item2,item3,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        #beginning of model
        self.colors = random.choice([['tomato','orange'],['blueviolet','violet'],['purple','plum'],['darkturquoise','dodgerblue'],['mediumorchid','mediumpurple'],['chocolate','burlywood'],['deeppink','lightpink']])
        self.color1 = self.colors[0]
        self.color2 = self.colors[1]
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;width:50px;'>&nbsp;</td><td colspan=%d>&nbsp;</td><td>&nbsp;&nbsp;</td><td rowspan=3 style='padding:0;padding-top:3px;vertical-align:middle'><img src='/images/explanation/P3_model_right_brace_small.png' /></td><td rowspan=3 style='padding:0;vertical-align:middle'>&nbsp;?</td></tr>"%(item3,self.color1,number2-1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td>"%(item2)
        for x in range(0, number2):
            self.solution_text = self.solution_text + "<td style='background-color:%s;height:25px;border:white solid 1px;width:50px;'>&nbsp;</td>"%(self.color2)
        self.solution_text = self.solution_text + "</tr>"
        
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d><img src='/images/explanation/P3_model_down_brace_small%d.png' /></td></tr>"%(number2,number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d>%d kg</td></tr>"%(number2,number1)
        self.solution_text = self.solution_text + "</table><br><br>"
        #end of model

        #beginning of steps
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;"
        self.solution_text = self.solution_text + "%d kg &nbsp;&divide;&nbsp; %d &nbsp;=&nbsp; %d kg"%(number1,number2,number1/number2)
        self.solution_text = self.solution_text + "<br>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;"
        self.solution_text = self.solution_text + "The mass of the %s is %d kg."%(item3,number1/number2)
        self.solution_text = self.solution_text + "<br><br>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;"
        self.solution_text = self.solution_text + "%d kg &nbsp;+&nbsp; %d kg &nbsp;=&nbsp; %d kg"%(number1,number1/number2,answer)
        self.solution_text = self.solution_text + "<br>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;"
        self.solution_text = self.solution_text + "The total mass of the %s and the %s is %d kg."%(item2,item3,answer)
        self.solution_text = self.solution_text + "</font>"
        #end of steps

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType8(self):       
        '''e.g.:      
        [Person.Boyname] has a <jug> containing 525 ml of <fruit punch>.
        He also has 6 <cups>, each containing 175 ml of <fruit punch>.
        He pours all the <fruit punch> from the 6 <cups> into the <jug> and fills it to the brim.
        Find the capacity of the <jug> in litres and millilitres.
        (Write your answer as in the example below.
        Example: 5 l 679 ml)'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.BoyName)
        
        self.items = [
                        ['jug','fruit punch','cups',random.randrange(100,250,5),randint(3,6),'cup'],
                        ['can','milk','glasses',random.randrange(100,250,5),randint(3,6),'glass'],
                        ['jar','water','glasses',random.randrange(100,250,5),randint(3,6),'glass'],
                        ['pot','tomato soup','bowls',random.randrange(100,200,5),randint(3,6),'bowl'],
                        ['jug','cranberry juice','cups',random.randrange(100,200,5),randint(3,6),'cup'],
                        ['bottle','apple cider','cans',random.randrange(100,200,5),randint(3,6),'can'],
                        ['flask','perfume','vials',random.randrange(50,100,5),randint(6,9),'vial'],
                        ['flask','ink','bottles',random.randrange(50,100,5),randint(6,9),'bottle'],
                        ['pail','enamel paint','tins',random.randrange(200,500,5),randint(3,4),'tin'],
                        ['tin','cooking oil','bottles',random.randrange(200,500,5),randint(3,4),'bottle']
                    ]
        
        self.item = random.choice(self.items)
        
        self.number1 = random.randrange(800,1200,5)
        self.number2 = self.item[3]
        self.number3 = self.item[4]  
                
        self.problem = "%s has a %s containing %d <font class='litreFont'>ml</font>&nbsp; of %s.<br>"%(self.name,self.item[0],self.number1,self.item[1])
        self.problem = self.problem + "He also has %d %s, each containing %d <font class='litreFont'>ml</font>&nbsp; of %s.<br>"%(self.number3,self.item[2],self.number2,self.item[1])
        self.problem = self.problem + "He pours all the %s from the %d %s into the %s and fills it to the brim.<br>"%(self.item[1],self.number3,self.item[2],self.item[0])
        self.problem = self.problem + "Find the capacity of the %s in litres and millilitres.<br><br>"%(self.item[0])
        self.problem = self.problem + "(Write your answer as in the example below.Example: 2 <font class='litreFont'>l</font>&nbsp; 275 <font class='litreFont'>ml</font>)"
        
        self.number = self.number1 + self.number2*self.number3
        
        div,mod = divmod(self.number,1000)
        
        self.answer = "%d l %d ml"%(div,mod)
        self.answer1 = "%d <font class='litreFont'>l</font>&nbsp; %d <font class='litreFont'>ml</font>"%(div,mod)
        
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType8(self.problem,self.answer,self.answer1,self.number1,self.number2,self.number3,self.item[0],self.item[1],self.item[2],self.item[5],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType8",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType8(self,problem,answer,answer1,number1,number2,number3,item0,item1,item2,item5,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer1),unit)

        #beginning of model
        self.colors = random.choice([['tomato','orange'],['blueviolet','violet'],['purple','plum'],['darkturquoise','dodgerblue'],['mediumorchid','mediumpurple'],['chocolate','burlywood'],['deeppink','lightpink']])
        self.color1 = self.colors[0]
        self.color2 = self.colors[1]
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>%d <font class='litreFont'>ml</font></td><td>%d <font class='litreFont'>ml</font></td></tr>"%(number1,number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_large.png' /></td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_small.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td>"%(item0)
        self.solution_text = self.solution_text + "<td style='background-color:%s;height:25px;border:white solid 1px;'>&nbsp;</td>"%(self.color1)
        for x in range(1,number3+1):
            self.solution_text = self.solution_text + "<td style='background-color:%s;height:25px;border:white solid 1px;width:48px;'><font style='font-size:0.8em'>%s %d</font></td>"%(self.color2,item5,x)
        self.solution_text = self.solution_text + "</tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d><img src='/images/explanation/P3_model_down_brace_large1small%d.png' /></td></tr>"%(number3+1,number3)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d>?</td></tr>"%(number3+1)
        self.solution_text = self.solution_text + "</table><br>"
        #end of model

        #beginning of steps
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;"
        self.solution_text = self.solution_text + "%d <font class='litreFont'>ml</font> &nbsp;&times;&nbsp; %d &nbsp;=&nbsp; %d <font class='litreFont'>ml</font>"%(number2,number3,number2*number3)
        self.solution_text = self.solution_text + "<br>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;"
        self.solution_text = self.solution_text + "The %d %s contain a total of %d <font class='litreFont'>ml</font>&nbsp; of %s."%(number3,item2,number2*number3,item1)
        self.solution_text = self.solution_text + "<br><br>"
        self.solution_text = self.solution_text + "</font>"
        
        self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td>%d <font class='litreFont'>ml</font> &nbsp;+&nbsp; %d <font class='litreFont'>ml</font></td><td style='padding-left:0px;padding-right:0px;'>=</td><td>%d <font class='litreFont'>ml</font></td></tr>"%(number1,number2*number3,number1+number2*number3)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-left:0px;padding-right:0px;'>=</td><td>%s</td></tr>"%(answer1)
        self.solution_text = self.solution_text + "</table>"
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;"
        self.solution_text = self.solution_text + "The capacity of the %s is %s ."%(item0,answer1)
        self.solution_text = self.solution_text + "</font>"
        #end of steps

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType9(self):       
        '''e.g.:      
        [Person.Name1] and [Person.Name2] have a total of 280 g of <sugar>.
        [Person.Name2] gives 20 g of <sugar> to [Person.Name1].
        In the end, [Person.Name2] has 3 times as much <sugar> as [Person.Name1].
        How much <sugar> does [Person.Name1] have at first?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.names = random.sample(PersonName.PersonName,2)
        
        self.items = ['sugar','popcorn kernels','brown rice','coloured stones','mixed nuts','seashells','bird food','chocolate chips','bread flour','cake mix']
        
        self.item = random.choice(self.items)
        
        self.number1 = random.randrange(20,50,10)
        self.number2 = random.randrange(10,40,10)
        self.number3 = randint(2,8)
        self.number4 = (self.number1+self.number2) * (self.number3+1)  
                
        self.problem = "%s and %s have a total of %d g of %s.<br>"%(self.names[0],self.names[1],self.number4,self.item)
        self.problem = self.problem + "%s gives %d g of %s to %s.<br>"%(self.names[1],self.number2,self.item,self.names[0])
        self.problem = self.problem + "In the end, %s has %d times as much %s as %s.<br>"%(self.names[1],self.number3,self.item,self.names[0])
        self.problem = self.problem + "How much %s does %s have at first?"%(self.item,self.names[0])
        
        self.answer = self.number1
        
        self.unit = "g"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType9(self.problem,self.answer,self.number2,self.number3,self.number4,self.names,self.item,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType9",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType9(self,problem,answer,number2,number3,number4,name,item,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        #beginning of model
        self.colors = random.choice([['tomato','orange'],['blueviolet','violet'],['purple','plum'],['darkturquoise','dodgerblue'],['mediumorchid','mediumpurple'],['chocolate','burlywood'],['deeppink','lightpink']])
        self.color1 = self.colors[0]
        self.color2 = self.colors[1]
        
        self.solution_text = "<font class='ExplanationFont'>In the end,<br></font>"
        self.solution_text = self.solution_text + "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td style='width:50px;'>&nbsp;</td><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td>"%(name[1])
        for x in range(0,number3):
            self.solution_text = self.solution_text + "<td style='background-color:%s;height:25px;border:white solid 1px;width:50px;'>&nbsp;</td>"%(self.color1)
        self.solution_text = self.solution_text + "<td>&nbsp;&nbsp;</td><td rowspan=3 style='padding:0;padding-top:3px;vertical-align:middle'><img src='/images/explanation/P3_model_right_brace_small.png' /></td><td rowspan=3 style='padding:0;vertical-align:middle;white-space:nowrap;'>&nbsp;%d g</td></tr>"%(number4)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='width:50px;'>&nbsp;</td><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;width:50px;'>&nbsp;</td></tr>"%(name[0],self.color2)
        
        self.solution_text = self.solution_text + "<tr><td style='width:50px;'>&nbsp;</td><td>&nbsp;</td><td><img src='/images/explanation/P3_model_down_brace_small.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='width:50px;'>&nbsp;</td><td>&nbsp;</td><td>? (a)</td></tr>"
        self.solution_text = self.solution_text + "</table><br>"
        #end of model
        
        #beginning of steps
        #number4 = total
        #number3 = number of times
        #number2 = amount given
        self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>%d units</td><td style='padding-left:0px; padding-right:0px; padding-top:3px'><img src='/images/explanation/right_arrow_2.png' /></td><td style='text-align:left'>%d g</td></tr>"%(number3+1,number4)
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>1 unit</td><td style='padding-left:0px; padding-right:0px; padding-top:3px'><img src='/images/explanation/right_arrow_2.png' /></td><td style='text-align:left'>%d g &nbsp;&divide;&nbsp; %d</td></tr>"%(number4,number3+1)
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px;text-align:right'>=</td><td style='text-align:left'>%d g &nbsp;(a)</td></tr>"%(number4/(number3+1))
        self.solution_text = self.solution_text + "</table>"
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;"
        self.solution_text = self.solution_text + "%s has %d g of %s in the end."%(name[0],number4/(number3+1),item)
        self.solution_text = self.solution_text + "</font>"
        self.solution_text = self.solution_text + "<br><br><br>"

        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;"
        self.solution_text = self.solution_text + "%d g &nbsp;&minus;&nbsp; %d g &nbsp;=&nbsp; %d g"%(number4/(number3+1),number2,answer)
        self.solution_text = self.solution_text + "<br>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;"
        self.solution_text = self.solution_text + "%s has %d g of %s at first."%(name[0],answer,item)
        self.solution_text = self.solution_text + "</font>"
        #end of steps

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType10(self):       
        '''e.g.:      
        [Person.Name1] has a <roll of paper> 350 cm long.
        [Person.Name2] has a <roll of paper> that is 55 cm longer than [Person.Name1]'s <roll of paper>.
        What is the total length of the two <rolls of paper>?
        Give your answer in metres and centimetres.
        (Write your answer as in the example below.
        Example: 5 m 67 cm)'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.names = random.sample(PersonName.PersonName,2)
        
        self.items = [['roll of paper','rolls of paper'],['roll of cloth','rolls of cloth'],['pipe','pipes'],['pole','poles'],['cardboard','cardboards'],['carpet','carpets'],['rug','rugs'],['table','tables'],['tape','tapes'],['cord','cords']]
        
        self.item = random.choice(self.items)
        
        self.number1 = randint(100,300)
        self.number2 = randint(100,300)
        self.number = self.number1*2 + self.number2
        div,mod = divmod(self.number,100)
        
        while mod == 0:
            self.number1 = randint(100,300)
            div,mod = divmod(self.number1*2+self.number2,100)
                
        self.problem = "%s has a %s %d cm long.<br>"%(self.names[0],self.item[0],self.number1)
        self.problem = self.problem + "%s has a %s that is %d cm longer than %s's %s.<br>"%(self.names[1],self.item[0],self.number2,self.names[0],self.item[0])
        self.problem = self.problem + "What is the total length of the two %s?<br>"%(self.item[1])
        self.problem = self.problem + "Give your answer in metres and centimetres.<br><br>"
        self.problem = self.problem + "(Write your answer as in the example below.<br>Example: 5 m 67 cm)"
        
        self.answer = "%d m %d cm"%(div,mod)
        
        self.unit = ""
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType10(self.problem,self.answer,self.number1,self.number2,self.names,self.item[0],self.item[1],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType10",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":3,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType10(self,problem,answer,number1,number2,name,item0,item1,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        #beginning of model
        if number1==number2:
            firstBrace = 'medium'
            secondBrace = 'medium'
        elif number1>number2:
            firstBrace = 'large'
            secondBrace = 'medium'
        else:
            firstBrace = 'medium'
            secondBrace = 'large'

        self.colors = random.choice([['tomato','orange'],['blueviolet','violet'],['purple','plum'],['darkturquoise','dodgerblue'],['mediumorchid','mediumpurple'],['chocolate','burlywood'],['deeppink','lightpink']])
        self.color1 = self.colors[0]
        self.color2 = self.colors[1]
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>%d cm</td></tr>"%(number1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(firstBrace)
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;'>&nbsp;</td><td>&nbsp;</td><td>&nbsp;&nbsp;</td><td rowspan=3 style='padding:0;padding-top:3px;vertical-align:middle'><img src='/images/explanation/P3_model_right_brace_small.png' /></td><td rowspan=3 style='padding:0;vertical-align:middle;white-space:nowrap;'>&nbsp;?</td></tr>"%(name[0],self.color1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td><td style='background-color:%s;height:25px;border-top:white solid 1px;border-bottom:white solid 1px;border-left:white solid 1px;border-right:white dotted 1px;'>&nbsp;</td><td style='background-color:%s;height:25px;border-top:white solid 1px;border-bottom:white solid 1px;border-right:white solid 1px;'>&nbsp;</td></tr>"%(name[1],self.color2,self.color2)
        
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>&nbsp;</td><td><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(secondBrace)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>&nbsp;</td><td>%d cm</td></tr>"%(number2)
        self.solution_text = self.solution_text + "</table><br><br>"
        #end of model

        #beginning of steps
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;"
        self.solution_text = self.solution_text + "%d cm &nbsp;+&nbsp; %d cm &nbsp;=&nbsp; %d cm"%(number1,number2,number1+number2)
        self.solution_text = self.solution_text + "<br>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;"
        self.solution_text = self.solution_text + "The length of %s's %s is %d cm."%(name[0],item0,number1+number2)
        self.solution_text = self.solution_text + "<br><br>"
        self.solution_text = self.solution_text + "</font>"
        
        self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td>%d cm &nbsp;+&nbsp; %d cm</td><td style='padding-left:0px;padding-right:0px;'>=</td><td>%d cm</td></tr>"%(number1,number1+number2,number1+number1+number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-left:0px;padding-right:0px;'>=</td><td>%s</td></tr>"%(answer)
        self.solution_text = self.solution_text + "</table>"
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;"
        self.solution_text = self.solution_text + "The total length of the two %s is %s."%(item1,answer)
        self.solution_text = self.solution_text + "</font>"
        #end of steps

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType11(self):       
        '''e.g.:      
        A <cat> has a mass of 15 kg.
        A <dog> is <twice> as heavy as the <cat>.
        A <fish> is 12 kg lighter than the <dog>.
        What is the mass of the <fish>?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.items = [
                        ['cat','dog','fish',randint(5,10),randint(2,4)],
                        ['sack of oats','sack of rice','sack of corn',randint(10,15),randint(2,4)],
                        ['carton','barrel','box',randint(10,15),randint(2,9)],
                        ['crate of soda cans','crate of milk bottles','crate of bananas',randint(5,10),randint(2,5)],
                        ['bag of marbles','bag of stones','bag of sand',randint(2,5),randint(3,9)],
                        ['suitcase','container','trunk',randint(15,30),randint(2,9)],
                        ['coffee table','sofa set','TV console',randint(10,20),randint(2,5)],
                        ['shoe rack','cabinet','bookshelf',randint(10,20),randint(2,9)],
                        ['box of magazines','box of tiles','box of wooden blocks',randint(10,20),randint(2,9)],
                        ['baby','boy','girl',randint(5,10),randint(2,5)],
                    ]        
        self.item = random.choice(self.items)
        
        self.number1 = self.item[3]
        self.number2 = self.item[4]
        self.number = randint(self.number1+1,self.number1*self.number2-2)
        self.number3 = self.number1*self.number2 - self.number
        
        self.numbers = {2:"twice",3:"thrice",4:"four times",5:"five times",6:"six times",7:"seven times",8:"eight times",9:"nine times"}
                
        self.problem = "A %s has a mass of %d kg.<br>"%(self.item[0],self.number1)
        self.problem = self.problem + "A %s is %s as heavy as the %s.<br>"%(self.item[1],self.numbers[self.number2],self.item[0])
        self.problem = self.problem + "A %s is %d kg lighter than the %s.<br>"%(self.item[2],self.number3,self.item[1])
        self.problem = self.problem + "What is the mass of the %s?"%(self.item[2])

        self.answer = self.number
        
        self.unit = "kg"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType11(self.problem,self.answer,self.item,self.number1,self.number2,self.number3,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType11",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType11(self,problem,answer,item,number1,number2,number3,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        #beginning of model
        #number1 = mass of baby
        #number2 = number of times
        self.colors = random.choice([['tomato','orange'],['blueviolet','violet'],['purple','plum'],['darkturquoise','dodgerblue'],['mediumorchid','mediumpurple'],['chocolate','burlywood'],['deeppink','lightpink']])
        self.color1 = self.colors[0]
        self.color2 = self.colors[1]
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp</td><td>%d kg</td></tr>"%(number1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_small.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;width:50px;'>&nbsp;</td></tr>"%(item[0],self.color1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td>"%(item[1])
        for x in range(0,number2):
            self.solution_text = self.solution_text + "<td style='background-color:%s;height:25px;border:white solid 1px;width:50px;'>&nbsp;</td>"%(self.color2)
        self.solution_text = self.solution_text + "</tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d><img src='/images/explanation/P3_model_down_brace_small%d.png' /></td></tr>"%(number2,number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d>? (a)</td></tr>"%(number2)
        self.solution_text = self.solution_text + "</table><br>"
        #end of model

        #beginning of steps
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;"
        self.solution_text = self.solution_text + "%d kg &nbsp;&times;&nbsp; %d &nbsp;=&nbsp; %d kg &nbsp;(a)"%(number1,number2,number1*number2)
        self.solution_text = self.solution_text + "<br>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;"
        self.solution_text = self.solution_text + "The mass of the %s is %d kg."%(item[1],number1*number2)
        self.solution_text = self.solution_text + "<br><br>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;"
        self.solution_text = self.solution_text + "%d kg &nbsp;&minus;&nbsp; %d kg &nbsp;=&nbsp; %d kg"%(number1*number2,number3,answer)
        self.solution_text = self.solution_text + "<br>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;"
        self.solution_text = self.solution_text + "The mass of the %s is %d kg."%(item[2],answer)
        self.solution_text = self.solution_text + "</font>"
        #end of steps

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType12(self):       
        '''e.g.:      
        Mr Ali, <a wholesale supplier>, had some <red beans> for sale.
        He packed and sold 6 <sacks> of <red beans> each of mass 11 kg.
        In the end, he had 12 kg of <red beans> left.
        What was the total mass of <red beans> he had at first?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.UncleName)
        
        self.items = [
                        ['a wholesaler','red beans','sacks','sack'],
                        ['a wholesaler','walnuts','sacks','sack'],
                        ['a wholesaler','cement','bags','bag'],
                        ['a supplier','rock salt','bags','bag'],
                        ['a supplier','barley','sacks','sack'],
                        ['a supplier','cheese','blocks','block'],
                        ['a supplier','milk powder','cartons','carton'],
                        ['a farmer','meat','cartons','carton'],
                        ['a farmer','mandarins','cartons','carton'],
                        ['a farmer','pumpkins','boxes','box']
                    ]        
        self.item = random.choice(self.items)
        
        flag = randint(0,1) #Changed by Mumtaz to ensure the visual correctness of model units
        if flag==0: #number1 will be greater than number3
            self.number1 = randint(15,25)
            self.number3 = self.number1 - randint(5,10)
        else:
            self.number3 = randint(15,25)
            self.number1 = self.number3 - randint(5,10)
        self.number2 = randint(2,9)
                
        self.problem = "%s, %s, had some %s for sale.<br>"%(self.name,self.item[0],self.item[1])
        self.problem = self.problem + "He packed and sold %d %s of %s each of mass %d kg.<br>"%(self.number2,self.item[2],self.item[1],self.number1)
        self.problem = self.problem + "In the end, he had %d kg of %s left.<br>"%(self.number3,self.item[1])
        self.problem = self.problem + "What was the total mass of %s he had at first?"%(self.item[1])

        self.answer = self.number1*self.number2 + self.number3
        
        self.unit = "kg"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType12(self.problem,self.answer,self.number1,self.number2,self.number3,self.item[1],self.item[3],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType12",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType12(self,problem,answer,number1,number2,number3,item1,item3,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        #beginning of model
        #number1 = amount packed into each packet
        #number2 = count of packets
        #number3 = amount left
        if number1>number3:
            firstBrace = 'medium'
            firstCellWidth = 98
            secondBrace = 'small'
            totalBrace = 'medium%dsmall1'%(number2)
        else:
            firstBrace = 'small'
            firstCellWidth = 52
            secondBrace = 'medium'
            totalBrace = 'medium1small%d'%(number2)
        
        self.colors = random.choice([['tomato','orange'],['blueviolet','violet'],['purple','plum'],['darkturquoise','dodgerblue'],['mediumorchid','mediumpurple'],['chocolate','burlywood'],['deeppink','lightpink']])
        self.color1 = self.colors[0]
        self.color2 = self.colors[1]
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>%d kg</td><td colspan=%d>&nbsp;</td><td>%d kg</td></tr>"%(number1,number2-1,number3)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td><td colspan=%d>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(firstBrace,number2-1,secondBrace)
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px;white-space:nowrap'>%s</td>"%(item1)
        for x in range(1,number2+1):
            self.solution_text = self.solution_text + "<td style='background-color:%s;height:25px;border:white solid 1px;width:%dpx;'><font style='font-size:0.8em'>%s %d</font></td>"%(self.color1,firstCellWidth,item3,x)
        self.solution_text = self.solution_text + "<td style='background-color:%s;height:25px;border:white solid 1px;'><font style='font-size:0.8em'>left</font></td>"%(self.color2)
        self.solution_text = self.solution_text + "</tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(number2+1,totalBrace)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d>?</td></tr>"%(number2+1)
        self.solution_text = self.solution_text + "</table><br>"
        #end of model

        #beginning of steps
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;"
        self.solution_text = self.solution_text + "%d kg &nbsp;&times;&nbsp; %d &nbsp;=&nbsp; %d kg"%(number1,number2,number1*number2)
        self.solution_text = self.solution_text + "<br>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;"
        self.solution_text = self.solution_text + "He sold %d kg of %s altogether."%(number1*number2,item1)
        self.solution_text = self.solution_text + "<br><br>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;"
        self.solution_text = self.solution_text + "%d kg &nbsp;+&nbsp; %d kg &nbsp;=&nbsp; %d kg"%(number1*number2,number3,answer)
        self.solution_text = self.solution_text + "<br>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;"
        self.solution_text = self.solution_text + "He had %d kg of %s at first."%(answer,item1)
        self.solution_text = self.solution_text + "</font>"
        #end of steps
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType13(self):       
        '''e.g.:      
        [Person.Boyname] had 595 ml of <sugarcane juice in a jug>.
        He <drank> 115 ml of the <sugarcane juice> and poured the rest equally into 4 <cups>.
        How much <sugarcane juice> was there in each <cup>?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.BoyName)
        
        self.items = [
                        ['sugarcane juice in a jug','drank','sugarcane juice','cups','sugarcane juice','cup'],
                        ['coffee shake in a jar','gave','coffee shake to his sister','glasses','coffee shake','glass'],
                        ['paint in a pail','used','paint to paint a pot','tins','paint','tin'],
                        ['water in a pitcher','drank','water','bottles','water','bottle'],
                        ['tea in a kettle','spilled','tea from the kettle','teacups','tea','teacup'],
                        ['shampoo in a can','spilled','shampoo from the can','bottles','shampoo','bottle'],
                        ['body lotion in a bottle','gave','body lotion to his mother','jars','body lotion','jar'],
                        ['honey in a pot','used','honey','jars','honey','jar'],
                        ['tomato soup in a saucepan','gave','tomato soup to his brother','bowls','tomato soup','bowl'],
                        ['glycerine in a flask','used','glycerine','bottles','glycerine','bottle']
                    ]        
        self.item = random.choice(self.items)
        
        self.numbers = random.choice([[2,random.randrange(100,200,5)],[3,random.randrange(100,200,5)],[4,random.randrange(100,200,5)],
                        [5,random.randrange(100,150,5)],[6,random.randrange(100,120,5)],[7,random.randrange(100,120,5)],
                        ])
        self.number1 = self.numbers[0]
        self.number2 = self.numbers[1]
        self.number3 = random.randrange(100,200,5)
        self.number4 = self.number1*self.number2+self.number3
                
        self.problem = "%s had %d <font class='litreFont'>ml</font>&nbsp; of %s.<br>"%(self.name,self.number4,self.item[0])
        self.problem = self.problem + "He %s %d <font class='litreFont'>ml</font>&nbsp; of the %s and poured the rest equally into %d %s.<br>"%(self.item[1],self.number3,
                                                                                                                                          self.item[2],self.number1,self.item[3])
        self.problem = self.problem + "How much %s was there in each %s?"%(self.item[4],self.item[5])

        self.answer = self.number2
        
        self.unit = "<font class='litreFont'>ml</font>"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType13(self.problem,self.answer,self.number1,self.number3,self.number4,self.item[3],self.item[4],self.item[5],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType13",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType13(self,problem,answer,number1,number3,number4,item3,item4,item5,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        #beginning of model
        if answer>number3:
            firstBrace = 'small'
            secondBrace = 'medium'
            secondCellWidth = 98
            totalBrace = 'medium%dsmall1'%(number1)
        else:
            firstBrace = 'medium'
            secondBrace = 'small'
            secondCellWidth = 52
            totalBrace = 'medium1small%d'%(number1)

        self.colors = random.choice([['tomato','orange'],['blueviolet','violet'],['purple','plum'],['darkturquoise','dodgerblue'],['mediumorchid','mediumpurple'],['chocolate','burlywood'],['deeppink','lightpink']])
        self.color1 = self.colors[0]
        self.color2 = self.colors[1]
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>%d <font class='litreFont'>ml</font></td><td>?</td></tr>"%(number3)
        self.solution_text = self.solution_text + "<tr><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(firstBrace,secondBrace)
        self.solution_text = self.solution_text + "<tr><td style='background-color:%s;height:25px;border:white solid 1px;'></td>"%(self.color1)
        for x in range(1,number1+1):
            self.solution_text = self.solution_text + "<td style='background-color:%s;height:25px;border:white solid 1px;width:%dpx;'><font style='font-size:0.8em'>%s %d</font></td>"%(self.color2,secondCellWidth,item5,x)
        self.solution_text = self.solution_text + "</tr>"
        self.solution_text = self.solution_text + "<tr><td colspan=%d><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(number1+1,totalBrace)
        self.solution_text = self.solution_text + "<tr><td colspan=%d>%d <font class='litreFont'>ml</font></td></tr>"%(number1+1,number4)
        self.solution_text = self.solution_text + "</table><br>"
        #end of model
        
        #beginning of steps
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;"
        self.solution_text = self.solution_text + "%d <font class='litreFont'>ml</font> &nbsp;&minus;&nbsp; %d <font class='litreFont'>ml</font> &nbsp;=&nbsp; %d <font class='litreFont'>ml</font>"%(number4,number3,number4-number3)
        self.solution_text = self.solution_text + "<br>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;"
        self.solution_text = self.solution_text + "He poured a total of %d <font class='litreFont'>ml</font>&nbsp; of %s into the %d %s."%(number4-number3,item4,number1,item3)
        self.solution_text = self.solution_text + "<br><br>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;"
        self.solution_text = self.solution_text + "%d <font class='litreFont'>ml</font> &nbsp;&divide;&nbsp; %d &nbsp;=&nbsp; %d <font class='litreFont'>ml</font>"%(number4-number3,number1,answer)
        self.solution_text = self.solution_text + "<br>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;"
        self.solution_text = self.solution_text + "Each %s had %d <font class='litreFont'>ml</font>&nbsp; of %s."%(item5,answer,item4)
        self.solution_text = self.solution_text + "</font>"
        #end of steps

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType14(self):       
        '''e.g.:      
        [Person.Girlname] bought 710 g of <meat>.
        She made 5 <meatloaves with it> and had 215 g of <meat> left.
        How many grams of <meat> did she use for a <meatloaf>?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.GirlName)
        
        self.items = [
                        ['meat','meatloaves with it','meatloaf','meatloaves'],
                        ['cheese','pizzas with it','pizza','pizzas'],
                        ['cakemix','minicakes with it','minicake','minicakes'],
                        ['crabmeat','crabcakes with it','crabcake','crabcakes'],
                        ['flour','loaves of bread with it','loaf of bread','loaves of bread'],
                        ['clay','identical pots with it','pot','pots'],
                        ['play dough','identical pen holders with it','pen holder','pen holders'],
                        ['glass tiles','identical mosaic lampshades with them','mosaic lampshade','mosaic lampshades'],
                        ['coloured sand','identical sand paintings with it','sand painting','sand paintings'],
                        ['beads','identical necklaces with them','necklace','necklaces']
                    ]        
        self.item = random.choice(self.items)
        
        self.numbers = random.choice([[2,random.randrange(50,150,5)],[3,random.randrange(50,150,5)],[4,random.randrange(50,150,5)],
                        [5,random.randrange(50,150,5)],[6,random.randrange(50,120,5)],[7,random.randrange(50,120,5)],
                        ])
        self.number1 = self.numbers[0]
        self.number2 = self.numbers[1]
        self.number3 = random.randrange(100,200,5)
        self.number4 = self.number1*self.number2+self.number3
                
        self.problem = "%s bought %d g of %s.<br>"%(self.name,self.number4,self.item[0])
        self.problem = self.problem + "She made %d %s and had %d g of %s left.<br>"%(self.number1,self.item[1],self.number3,self.item[0])
        self.problem = self.problem + "How many grams of %s did she use for a %s?"%(self.item[0],self.item[2])

        self.answer = self.number2
        
        self.unit = "g"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType14(self.problem,self.answer,self.number1,self.number3,self.number4,self.item[0],self.item[2],self.item[3],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType14",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType14(self,problem,answer,number1,number3,number4,item0,item2,item3,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        #beginning of model
        #number1 = count of containers
        #number2 = answer = amount packed into each container
        #number3 = amount left
        #number4 = total amount
        number2 = answer
        if number2>number3:
            firstBrace = 'medium'
            firstCellWidth = 98
            secondBrace = 'small'
            totalBrace = 'medium%dsmall1'%(number1)
        else:
            firstBrace = 'small'
            firstCellWidth = 52
            secondBrace = 'medium'
            totalBrace = 'medium1small%d'%(number1)
        
        self.colors = random.choice([['tomato','orange'],['blueviolet','violet'],['purple','plum'],['darkturquoise','dodgerblue'],['mediumorchid','mediumpurple'],['chocolate','burlywood'],['deeppink','lightpink']])
        self.color1 = self.colors[0]
        self.color2 = self.colors[1]
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>?</td><td colspan=%d>&nbsp;</td><td>%d g</td></tr>"%(number1-1,number3)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td><td colspan=%d>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(firstBrace,number1-1,secondBrace)
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px;white-space:nowrap'>%s</td>"%(item0)
        for x in range(1,number1+1):
            self.solution_text = self.solution_text + "<td style='background-color:%s;height:25px;border:white solid 1px;width:%dpx;'>&nbsp;</td>"%(self.color1,firstCellWidth)
        self.solution_text = self.solution_text + "<td style='background-color:%s;height:25px;border:white solid 1px;'>&nbsp;</td>"%(self.color2)
        self.solution_text = self.solution_text + "</tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(number1+1,totalBrace)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d>%d g</td></tr>"%(number1+1,number4)
        self.solution_text = self.solution_text + "</table><br>"
        #end of model

        #beginning of steps
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;"
        self.solution_text = self.solution_text + "%d g &nbsp;&minus;&nbsp; %d g &nbsp;=&nbsp; %d g"%(number4,number3,number4-number3)
        self.solution_text = self.solution_text + "<br>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;"
        self.solution_text = self.solution_text + "She used a total of %d g of %s for the %d %s."%(number4-number3,item0,number1,item3)
        self.solution_text = self.solution_text + "<br><br>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;"
        self.solution_text = self.solution_text + "%d g &nbsp;&divide;&nbsp; %d &nbsp;=&nbsp; %d g"%(number4-number3,number1,answer)
        self.solution_text = self.solution_text + "<br>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;"
        self.solution_text = self.solution_text + "She used %d g of %s for a %s."%(answer,item0,item2)
        self.solution_text = self.solution_text + "</font>"
        #end of steps

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType15(self):       
        '''e.g.:      
        [Person.Girlname] cut a <ball of beaded string> that she bought from [Person.Unclename] into 7 equal pieces.
        [Person.Unclename] had made 3 such <balls> from 945 cm of <rope>.
        What was the length of one piece of <beaded string> that [Person.Girlname] got?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.names = [random.choice(PersonName.GirlName),random.choice(PersonName.UncleName)]
        
        self.items = [
                        ['ball of beaded string','balls','beaded string','ball'],
                        ['ball of yarn','balls','yarn','ball'],
                        ['spool of kitestring','spools','kitestring','spool'],
                        ['spool of fishing line','spools','fishing line','spool'],
                        ['roll of plastic string','rolls','plastic string','roll'],
                        ['roll of lace','rolls','lace','roll'],
                        ['roll of ribbon','rolls','ribbon','roll'],
                        ['roll of tape','rolls','tape','roll'],
                        ['bundle of cord','bundles','cord','bundle'],
                        ['bundle of wire','bundles','wire','bundle']
                    ]        
        self.item = random.choice(self.items)
        
        self.numbers = random.choice([[2,randint(2,9),randint(40,50)],[3,randint(2,8),randint(30,40)],[4,randint(2,7),randint(25,35)],
                        [5,randint(2,6),randint(20,30)],])
        self.number1 = self.numbers[1]
        self.number2 = self.numbers[0]
        self.number3 = self.numbers[2]*self.number1*self.number2
                
        self.problem = "%s cut a %s that she bought from %s into %d equal pieces.<br>"%(self.names[0],self.item[0],self.names[1],self.number1)
        self.problem = self.problem + "%s had made %d such %s from %d cm of %s.<br>"%(self.names[1],self.number2,self.item[1],self.number3,self.item[2])
        self.problem = self.problem + "What was the length of one piece of %s that %s got?"%(self.item[2],self.names[0])

        self.answer = self.numbers[2]
        
        self.unit = "cm"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType15(self.problem,self.answer,self.number1,self.number2,self.number3,self.item[0],self.item[2],self.item[3],self.names,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType15",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType15(self,problem,answer,number1,number2,number3,item0,item2,item3,name,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        #beginning of model
        #number1 = count of pieces from a roll
        #number2 = count of rolls
        #number3 = total amount
        #answer = length of one piece

        self.color1 = random.choice(['aqua','blueviolet','cornflowerblue','cyan','darkmagenta','deepskyblue','dodgerblue','skyblue'])
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>? (a)</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_medium.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr>"
        for x in range(1,number2+1):
            self.solution_text = self.solution_text + "<td style='background-color:%s;height:25px;border:white solid 1px;width:98px;'><font style='font-size:0.8em'>%s %d</font></td>"%(self.color1,item3,x)
        self.solution_text = self.solution_text + "</tr>"
        self.solution_text = self.solution_text + "<tr><td colspan=%d><img src='/images/explanation/P3_model_down_brace_medium%s.png' /></td></tr>"%(number2,number2)
        self.solution_text = self.solution_text + "<tr><td colspan=%d>%d cm</td></tr>"%(number2,number3)
        self.solution_text = self.solution_text + "</table><br>"
        #end of model
        
        #beginning of steps
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;"
        self.solution_text = self.solution_text + "%d cm &nbsp;&divide;&nbsp; %d &nbsp;=&nbsp; %d cm"%(number3,number2,number3/number2)
        self.solution_text = self.solution_text + "<br>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;"
        self.solution_text = self.solution_text + "The length of each %s that %s made was %d cm."%(item0,name[1],number3/number2)
        self.solution_text = self.solution_text + "<br><br>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;"
        self.solution_text = self.solution_text + "%d cm &nbsp;&divide;&nbsp; %d &nbsp;=&nbsp; %d cm"%(number3/number2,number1,answer)
        self.solution_text = self.solution_text + "<br>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;"
        self.solution_text = self.solution_text + "The length of one piece of %s that %s got was %d cm."%(item2,name[0],answer)
        self.solution_text = self.solution_text + "</font>"
        #end of steps

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType16(self):       
        '''e.g.:      
        A <box of filled with cookies> had a mass of 700 g.
        When [Person.Name] removed half the <cookies from the box>, the mass of the <box> became 370 g.
        What was the mass of the empty <box>?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.PersonName)
     
        self.items = [['box filled with cookies','cookies from the box','box',randint(300,500),randint(30,70),'cookies','box of cookies'],
                      ['box filled with chocolates','chocolates from the box','box',randint(300,500),randint(30,70),'chocolates','box of chocolates'],
                      ['tin filled with biscuits','biscuits from the tin','tin',randint(300,500),randint(30,70),'biscuits','tin of biscuits'],
                      ['tin filled with crackers','crackers from the tin','tin',randint(300,500),randint(30,70),'crackers','tin of crackers'],
                      ['basket filled with pears','pears from the basket','basket',randint(1000,2000),randint(100,300),'pears','basket of pears'],
                      ['basket filled with beans','beans from the basket','basket',randint(1000,2000),randint(100,300),'beans','basket of beans'],
                      ['crate filled with plums','plums from the crate','crate',randint(1000,2000),randint(100,300),'plums','crate of plums'],
                      ['crate filled with lemons','lemons from the crate','crate',randint(1000,2000),randint(100,300),'lemons','crate of lemons'],
                      ['carton filled with notebooks','notebooks from the carton','carton',randint(2000,4000),randint(200,400),'notebooks','carton of notebooks'],
                      ['carton filled with T-shirts','T-shirts from the carton','carton',randint(2000,4000),randint(200,400),'T-shirts','carton of T-shirts']
                      ]        
        
        self.item = random.choice(self.items)
        
        self.number1 = self.item[3]
        self.number2 = self.item[4]
        self.number3 = self.number1 + self.number2
        self.number4 = self.number1*2+self.number2
                
        self.problem = "A %s had a mass of %d g.<br>"%(self.item[0],self.number4)
        self.problem = self.problem + "When %s removed half the %s, the mass of the %s <br>became %d g.<br>"%(self.name,self.item[1],self.item[2],self.number3)
        self.problem = self.problem + "What was the mass of the empty %s?"%(self.item[2])

        self.answer = self.number2
        
        self.unit = "g"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType16(self.problem,self.answer,self.number3,self.number4,self.item[2],self.item[5],self.item[6],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType16",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType16(self,problem,answer,number3,number4,item2,item5,item6,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        #beginning of model
        self.colors = random.choice([['tomato','orange'],['blueviolet','violet'],['purple','plum'],['darkturquoise','dodgerblue'],['mediumorchid','mediumpurple'],['chocolate','burlywood'],['deeppink','lightpink']])
        self.color1 = self.colors[0]
        self.color2 = self.colors[1]
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=3>%d g</td></tr>"%(number4)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=3 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_large2small1.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px;white-space:nowrap'>mass of<br>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;width:48px;'><font style='font-size:0.8em'>empty %s</font></td>"%(item6,self.color1,item2)
        self.solution_text = self.solution_text + "<td style='background-color:%s;height:25px;border-top:white solid 1px;border-bottom:white solid 1px;border-left:white solid 1px;border-right:white dotted 1px;white-space:nowrap;width:145px;'><font style='font-size:0.8em'>half the %s</font></td>"%(self.color2,item5)
        self.solution_text = self.solution_text + "<td style='background-color:%s;height:25px;border-top:white solid 1px;border-bottom:white solid 1px;border-right:white solid 1px;white-space:nowrap;width:155px;'><font style='font-size:0.8em'>half the %s</font></td>"%(self.color2,item5)
        self.solution_text = self.solution_text + "</tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:0px'><img src='/images/explanation/P3_model_down_brace_small.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:0px'>?</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2><img src='/images/explanation/P3_model_down_brace_large1small1.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2>%d g</td></tr>"%(number3)
        self.solution_text = self.solution_text + "</table><br><br>"
        #end of model

        #beginning of steps
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;"
        self.solution_text = self.solution_text + "%d g &nbsp;&minus;&nbsp; %d g &nbsp;=&nbsp; %d g"%(number4,number3,number4-number3)
        self.solution_text = self.solution_text + "<br>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;"
        self.solution_text = self.solution_text + "The mass of half the %s was %d g."%(item5,number4-number3)
        self.solution_text = self.solution_text + "<br><br>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;"
        self.solution_text = self.solution_text + "%d g &nbsp;&minus;&nbsp; %d g &nbsp;=&nbsp; %d g"%(number3,number4-number3,answer)
        self.solution_text = self.solution_text + "<br>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;"
        self.solution_text = self.solution_text + "The mass of the empty %s was %d g."%(item2,answer)
        self.solution_text = self.solution_text + "</font>"
        #end of steps

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType17(self):       
        '''e.g.:      
        A <diary> is 250 <g> heavier than a <storybook>.
        The total mass of the <diary> and a <dictionary> is 900 <g>.
        The <dictionary> is 2 times as heavy as the <diary>.
        Find the mass of the <storybook>.'''

        self.complexity_level = "easy"
        self.HCScore = 3
     
        self.items = [['diary','storybook','dictionary','g',randint(700,999),randint(2,4),randint(40,100)],
                      ['can of evaporated milk','bottle of coffee powder','tin of milk powder','g',randint(700,999),randint(2,4),randint(40,100)],
                      ['bar of soap','tube of toothpaste','bottle of shampoo','g',randint(700,999),randint(2,4),randint(40,100)],
                      ['bag of chips','packet of candies','box of grapes','g',randint(700,999),randint(2,4),randint(40,100)],
                      ['log','cinder block','rock','kg',randint(200,500),randint(5,8),randint(5,15)],
                      ['sack','box','trunk','kg',randint(300,600),randint(5,8),randint(5,20)],
                      ['girl','baby','man','kg',randint(100,150),randint(2,4),randint(5,10)],
                      ['watermelon','pineapple','jackfruit','kg',randint(20,40),randint(2,4),randint(1,3)],
                      ['turkey','fish','lamb','kg',randint(40,100),randint(5,8),randint(1,3)],
                      ['table','chair','sofa','kg',randint(40,100),randint(5,8),randint(1,3)]]
                
        self.item = random.choice(self.items)
        
        self.number1 = self.item[4]
        self.number2 = self.item[5]
        self.number3 = self.item[6]
        div1,mod1 = divmod(self.number1,self.number2+1)
        self.number1 = self.number1 - mod1
        self.number4 = div1 - self.number3 
        
        self.problem = "A %s is %d %s heavier than a %s.<br>"%(self.item[0],self.number4,self.item[3],self.item[1])
        self.problem = self.problem + "The total mass of the %s and a %s is %d %s.<br>"%(self.item[0],self.item[2],self.number1,self.item[3])
        self.problem = self.problem + "The %s is %d times as heavy as the %s.<br>"%(self.item[2],self.number2,self.item[0])
        self.problem = self.problem + "Find the mass of the %s."%(self.item[1])

        self.answer = self.number3
        
        self.unit = self.item[3]
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType17(self.problem,self.answer,self.number1,self.number2,self.number4,self.item[0],self.item[1],self.item[2],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType17",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType17(self,problem,answer,number1,number2,number4,item0,item1,item2,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        #beginning of model
        #number1 = 900
        #number2 = times as heavy
        #number3 = answer
        #number4 = 250
        #item0 = diary
        #item1 = storybook
        #item2 = dictionary
        self.colors = random.choice([['tomato','orange'],['blueviolet','violet'],['purple','plum'],['darkturquoise','dodgerblue'],['mediumorchid','mediumpurple'],['chocolate','burlywood'],['deeppink','lightpink']])
        self.color1 = self.colors[0]
        self.color2 = self.colors[1]
        
        if answer>number4:
            firstBrace = 'small'
            secondBrace = 'extrasmall'
        else:
            firstBrace = 'extrasmall'
            secondBrace = 'small'
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>?</td><td>%d %s</td></tr>"%(number4,unit)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(firstBrace,secondBrace)
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px;white-space:nowrap;'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;'>&nbsp;</td></tr>"%(item1,self.color1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px;white-space:nowrap;'>%s</td><td style='background-color:%s;height:25px;border-left:white solid 1px;border-top:white solid 1px;border-bottom:white solid 1px;border-right:white dotted 1px;'>&nbsp;</td><td style='background-color:%s;height:25px;border-top:white solid 1px;border-bottom:white solid 1px;border-right:white solid 1px;'>&nbsp;</td><td colspan=%d>&nbsp;</td><td>&nbsp;&nbsp;</td><td rowspan=3 style='padding:0;padding-top:3px;vertical-align:middle'><img src='/images/explanation/P3_model_right_brace_small.png' /></td><td rowspan=3 style='padding:0;vertical-align:middle;white-space:nowrap'>&nbsp;%d %s</td></tr>"%(item0,self.color2,self.color2,number2-1,number1,unit)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px;white-space:nowrap;'>%s</td><td colspan=2 style='background-color:%s;height:25px;border:white solid 1px;'>&nbsp;</td>"%(item2,self.color2)
        for x in range(1,number2):
            self.solution_text = self.solution_text + "<td style='background-color:%s;height:25px;border:white solid 1px;width:86px;'>&nbsp;</td>"%(self.color2)
        self.solution_text = self.solution_text + "</tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2>&nbsp;</td><td colspan=%d><img src='/images/explanation/P3_model_small%dextrasmall%d_blank.png' /></td></tr>"%(number2-1,number2-1,number2-1)
        self.solution_text = self.solution_text + "</table><br><br>"
        #end of model

        #beginning of steps
        #number2 = as many times
        self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>%d units</td><td style='padding-left:0px; padding-right:0px; padding-top:3px'><img src='/images/explanation/right_arrow_2.png' /></td><td style='text-align:left'>%d %s</td></tr>"%(number2+1,number1,unit)
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>1 unit</td><td style='padding-left:0px; padding-right:0px; padding-top:3px'><img src='/images/explanation/right_arrow_2.png' /></td><td style='text-align:left'>%d %s &nbsp;&divide;&nbsp; %d</td></tr>"%(number1,unit,number2+1)
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px;text-align:right'>=</td><td style='text-align:left'>%d %s</td></tr>"%(number1/(number2+1),unit)
        self.solution_text = self.solution_text + "</table>"
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;"
        self.solution_text = self.solution_text + "The mass of the %s is %d %s."%(item0,number1/(number2+1),unit)
        self.solution_text = self.solution_text + "</font>"
        self.solution_text = self.solution_text + "<br><br><br>"

        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;"
        self.solution_text = self.solution_text + "%d %s &nbsp;&minus;&nbsp; %d %s &nbsp;=&nbsp; %d %s"%(number1/(number2+1),unit,number4,unit,answer,unit)
        self.solution_text = self.solution_text + "<br>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;"
        self.solution_text = self.solution_text + "The mass of the %s is %d %s."%(item1,answer,unit)
        self.solution_text = self.solution_text + "</font>"
        #end of steps

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType18(self):       
        '''e.g.:      
        The total volume of <juice in a jug> and 5 <glasses> is 1125 ml.
        If each <glass> has 125 ml of <juice>, find the volume of <juice in the jug>.'''

        self.complexity_level = "easy"
        self.HCScore = 3
     
        self.items = [['juice in a jug','glasses','glass','juice','juice in the jug',random.randrange(100,250,5),random.randrange(500,2000,5),'jug'],
                      ['barley water in a bottle','cups','cup','barley water','barley water in the bottle',random.randrange(100,200,5),random.randrange(500,2000,5),'bottle'],
                      ['milk in a jug','mugs','mug','milk','milk in the jug',random.randrange(100,250,5),random.randrange(500,2000,5),'jug'],
                      ['coconut oil in a can','bottles','bottle','coconut oil','coconut oil in the can',random.randrange(200,300,5),random.randrange(500,5000,5),'can'],
                      ['syrup in a can','bottles','bottle','syrup','syrup in the can',random.randrange(200,300,5),random.randrange(500,5000,5),'can'],
                      ['tangerine juice in a dispenser','cups','cup','tangerine juice','tangerine juice in the dispenser',random.randrange(100,200,5),random.randrange(500,5000,5),'dispenser'],
                      ['lemonade in a cooler','glasses','glass','lemonade','lemonade in the cooler',random.randrange(200,300,5),random.randrange(500,5000,5),'cooler'],
                      ['buttermilk in a container','cups','cup','buttermilk','buttermilk in the container',random.randrange(100,200,5),random.randrange(500,5000,5),'container'],
                      ['perfume in a flask','vials','vial','perfume','perfume in the flask',random.randrange(50,100,5),random.randrange(500,1000,5),'flask'],
                      ['mushroom soup in a pot','bowls','bowl','mushroom soup','mushroom soup in the pot',random.randrange(100,200,5),random.randrange(500,1000,5),'pot']]
                
        self.item = random.choice(self.items)
        
        self.number1 = randint(2,9)
        self.number2 = self.item[5]
        self.number3 = self.item[6]
        self.number4 = self.number1*self.number2+self.number3
        
        self.problem = "The total volume of %s and %d %s is %d <font class='litreFont'>ml</font> .<br>"%(self.item[0],self.number1,self.item[1],self.number4)
        self.problem = self.problem + "If each %s has %d <font class='litreFont'>ml</font>&nbsp; of %s, find the volume of %s."%(self.item[2],self.number2,self.item[3],self.item[4])

        self.answer = self.number3
        
        self.unit = "<font class='litreFont'>ml</font>"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType18(self.problem,self.answer,self.number1,self.number2,self.number4,self.item[1],self.item[2],self.item[3],self.item[4],self.item[7],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType18",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType18(self,problem,answer,number1,number2,number4,item1,item2,item3,item4,item7,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        #beginning of model
        self.colors = random.choice([['tomato','orange'],['blueviolet','violet'],['purple','plum'],['darkturquoise','dodgerblue'],['mediumorchid','mediumpurple'],['chocolate','burlywood'],['deeppink','lightpink']])
        self.color1 = self.colors[0]
        self.color2 = self.colors[1]
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>?</td><td>%d <font class='litreFont'>ml</font></td></tr>"%(number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_large.png' /></td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_small.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px;white-space:nowrap'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;'><font style='font-size:0.8em'>%s</font></td>"%(item3,self.color1,item7)
        for x in range(1,number1+1):
            self.solution_text = self.solution_text + "<td style='background-color:%s;height:25px;border:white solid 1px;width:48px;'><font style='font-size:0.8em'>%s %d</font></td>"%(self.color2,item2,x)
        self.solution_text = self.solution_text + "</tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d><img src='/images/explanation/P3_model_down_brace_large1small%s.png' /></td></tr>"%(number1+1,number1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d>%d <font class='litreFont'>ml</font></td></tr>"%(number1+1,number4)
        self.solution_text = self.solution_text + "</table><br>"
        #end of model

        #beginning of steps
        #item3 = juice
        #item1 = glasses
        #item4 = juice in the jug
        #number2 = 125
        #number1 = 5
        #number4 = 1125 ml
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;"
        self.solution_text = self.solution_text + "%d <font class='litreFont'>ml</font> &nbsp;&times;&nbsp; %d &nbsp;=&nbsp; %d <font class='litreFont'>ml</font>"%(number2,number1,number2*number1)
        self.solution_text = self.solution_text + "<br>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;"
        self.solution_text = self.solution_text + "Total volume of %s in the %d %s is %d <font class='litreFont'>ml</font> ."%(item3,number1,item1,number2*number1)
        self.solution_text = self.solution_text + "<br><br>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;"
        self.solution_text = self.solution_text + "%d <font class='litreFont'>ml</font> &nbsp;&minus;&nbsp; %d <font class='litreFont'>ml</font> &nbsp;=&nbsp; %d <font class='litreFont'>ml</font>"%(number4,number2*number1,answer)
        self.solution_text = self.solution_text + "<br>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;"
        self.solution_text = self.solution_text + "The volume of %s is %d <font class='litreFont'>ml</font> ."%(item4,answer)
        self.solution_text = self.solution_text + "</font>"
        #end of steps

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType19(self):       
        '''e.g.:      
        <A merchant> had 80 <m> of <fabric>.
        She <sold> 31 <m> of the <fabric> and cut the remaining <fabric> equally into 7 <m> long pieces.
        How many pieces did she get?'''

        self.complexity_level = "easy"
        self.HCScore = 3
     
        self.items = [['A merchant','fabric','sold','fabric','fabric','m',randint(20,50),randint(5,25)],
                      ['A tailor','elastic band','used','elastic band','elastic band','m',randint(20,50),randint(5,25)],
                      ['A seller','jute rope','sold','rope','rope','m',randint(20,50),randint(5,25)],
                      ['A shopkeeper','butter paper','sold','butter paper to a baker','butter paper','m',randint(20,50),randint(5,25)],
                      ['A wholesaler','lace','gave','lace to a friend','lace','m',randint(20,20),randint(20,50)],
                      ['An interior designer','wallpaper','used','wallpaper to decorate a house','wallpaper','m',randint(20,50),randint(5,25)],
                      ['A teacher','wire','gave','wire to his pupils','wire','cm',randint(100,500),randint(30,50)],
                      ['A girl','ribbon','used','ribbon to make a bow','ribbon','cm',randint(20,50),randint(10,30)],
                      ['A student','craft paper','used','paper for a project','paper','cm',randint(100,300),randint(5,25)],
                      ['A girl','sticky tape','used','tape to stick photos in an album','tape','cm',randint(100,300),randint(5,15)]]                

        self.item = random.choice(self.items)
        
        self.number1 = self.item[6]
        self.number2 = self.item[7]
        self.number3 = randint(5,9)
        self.number4 = self.number2*self.number3+self.number1
        
        self.problem = "%s had %d %s of %s.<br>"%(self.item[0],self.number4,self.item[5],self.item[1])
        self.problem = self.problem + "She %s %d %s of the %s and cut the remaining %s equally into %d %s long pieces.<br>"%(self.item[2],self.number1,self.item[5],self.item[3],
                                                                                                                             self.item[4],self.number3,self.item[5])
        self.problem = self.problem + "How many pieces did she get?"

        self.answer = self.number2
        
        self.unit = "pieces"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType19(self.problem,self.answer,self.number1,self.number3,self.number4,self.item[1],self.item[2],self.item[4],self.item[5],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType19",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType19(self,problem,answer,number1,number3,number4,item1,item2,item4,item5,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        #beginning of model
        self.colors = random.choice([['tomato','orange'],['blueviolet','violet'],['purple','plum'],['darkturquoise','dodgerblue'],['mediumorchid','mediumpurple'],['chocolate','burlywood'],['deeppink','lightpink']])
        self.color1 = self.colors[0]
        self.color2 = self.colors[1]
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>%d %s</td><td colspan=5>?</td></tr>"%(number1,item5)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_large1.png' /></td><td colspan=5 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_small5.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px;white-space:nowrap'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;'>%s</td>"%(item1,self.color1,item2)
        self.solution_text = self.solution_text + "<td style='background-color:%s;height:20px;border:white solid 1px;width:50px;padding-bottom:5px;'>%d %s</td><td style='background-color:%s;height:20px;border:white solid 1px;width:50px;padding-bottom:5px;'>%d %s</td><td colspan=2 style='height:20px;border:white solid 1px;width:50px;padding-bottom:5px;'>. . . . .</td><td style='background-color:%s;height:20px;border:white solid 1px;width:50px;padding-bottom:5px;'>%d %s</td></tr>"%(self.color2,number3,item5,self.color2,number3,item5,self.color2,number3,item5)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=6><img src='/images/explanation/P3_model_down_brace_large1small6.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=6>%d %s</td></tr>"%(number4,item5)
        self.solution_text = self.solution_text + "</table><br>"
        #end of model
        
        #beginning of steps
        #number4 = 80
        #number1 = 31
        #number3 = 7
        #item5 = m
        #item4 = fabric
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;"
        self.solution_text = self.solution_text + "%d %s &nbsp;&minus;&nbsp; %d %s &nbsp;=&nbsp; %d %s"%(number4,item5,number1,item5,number4-number1,item5)
        self.solution_text = self.solution_text + "<br>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;"
        self.solution_text = self.solution_text + "She had %d %s of %s left."%(number4-number1,item5,item4)
        self.solution_text = self.solution_text + "<br><br>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;"
        self.solution_text = self.solution_text + "%d %s &nbsp;&divide;&nbsp; %d %s &nbsp;=&nbsp; %d"%(number4-number1,item5,number3,item5,answer)
        self.solution_text = self.solution_text + "<br>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;"
        self.solution_text = self.solution_text + "She got %d pieces."%(answer)
        self.solution_text = self.solution_text + "</font>"
        #end of steps

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType20(self):       
        '''e.g.:      
        [Person.Girlname] makes some <lemonade> using 60 ml of <lemon juice> and 300 ml of <water>.
        She pours the <lemonade> equally into 6 <cups>.
        Find the volume of <lemonade> in each <cup>.'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.GirlName)
     
        self.items = [['lemonade','lemon juice','water','cups','cup',randint(3,6),randint(50,150)],
                      ['milk shake','rose syrup','milk','glasses','glass',randint(3,6),randint(50,150)],
                      ['fruit punch','mixed juice','water','glasses','glass',randint(3,6),randint(50,150)],
                      ['beverage','orange juice','soda','cups','cup',randint(3,6),randint(50,150)],
                      ['mango yogurt','mango pulp','yogurt','cups','cup',randint(3,6),randint(50,180)],
                      ['sauce','chilli sauce','tomato ketchup','bottles','bottle',randint(3,6),randint(100,180)],
                      ['orange paint','yellow paint','red paint','cans','can',randint(3,6),randint(100,200)],
                      ['soup','tomato puree','water','bowls','bowl',randint(3,6),randint(100,180)],
                      ['perfume','oils','chemicals','vials','vial',randint(3,6),randint(50,100)],
                      ['hair oil','almond oil','coconut oil','bottles','bottle',randint(3,6),randint(100,140)]]

        self.item = random.choice(self.items)
        
        self.number1 = self.item[5]
        self.number2 = self.item[6]
        self.number3 = ((self.number1*self.number2) * randint(15,40))/100
        self.number4 = (self.number1*self.number2) - self.number3
        
        self.problem = "%s makes some %s using %d <font class='litreFont'>ml</font>&nbsp; of %s and %d <font class='litreFont'>ml</font>&nbsp; of %s.<br>"%(self.name,self.item[0],self.number3,self.item[1],self.number4,self.item[2])
        self.problem = self.problem + "She pours the %s equally into %d %s.<br>"%(self.item[0],self.number1,self.item[3])
        self.problem = self.problem + "Find the volume of %s in each %s."%(self.item[0],self.item[4])

        self.answer = self.number2
        
        self.unit = "<font class='litreFont'>ml</font>"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType20(self.problem,self.answer,self.number1,self.number3,self.number4,self.item[0],self.item[1],self.item[2],self.item[4],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType20",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType20(self,problem,answer,number1,number3,number4,item0,item1,item2,item4,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        #beginning of model1
        self.colors = random.choice([['tomato','orange'],['blueviolet','violet'],['purple','plum'],['darkturquoise','dodgerblue'],['mediumorchid','mediumpurple'],['chocolate','burlywood'],['deeppink','lightpink']])
        self.color1 = self.colors[0]
        self.color2 = self.colors[1]
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>%d <font class='litreFont'>ml</font></td><td>%d <font class='litreFont'>ml</font></td></tr>"%(number3,number4)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_medium.png' /></td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_large1small1.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px;white-space:nowrap'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;'>&nbsp;</td><td style='background-color:%s;height:25px;border:white solid 1px;'>&nbsp;</td></tr>"%(item0,self.color1,self.color2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2><img src='/images/explanation/P3_model_down_brace_large1medium1small1.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2>? (a)</td></tr>"
        self.solution_text = self.solution_text + "</table><br>"
        #end of model1

        #beginning of steps1
        #number3 = 60
        #number4 = 300
        #number1 = 6
        #item0 = lemonade
        #item4 = cup
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;"
        self.solution_text = self.solution_text + "%d <font class='litreFont'>ml</font> &nbsp;+&nbsp; %d <font class='litreFont'>ml</font> &nbsp;=&nbsp; %d <font class='litreFont'>ml</font> &nbsp;(a)"%(number3,number4,number3+number4)
        self.solution_text = self.solution_text + "<br>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;"
        self.solution_text = self.solution_text + "She makes %d <font class='litreFont'>ml</font>&nbsp; of %s."%(number3+number4,item0)
        self.solution_text = self.solution_text + "<br><br>"
        #end of steps1
        
        #beginning of model2
        self.solution_text = self.solution_text + "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>%d <font class='litreFont'>ml</font></td></tr>"%(number3+number4)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_large1medium1small1.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px;white-space:nowrap'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;padding-top:0px;padding-bottom:0px;'><img src='/images/explanation/P3_model_cut%d.png' /></td></tr>"%(item0,self.color2,number1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:left'><img src='/images/explanation/P3_model_down_brace%d.png' /></td></tr>"%(number1)
        self.solution_text = self.solution_text + "</table><br>"
        #end of model2

        #beginning of steps2
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;"
        self.solution_text = self.solution_text + "%d <font class='litreFont'>ml</font> &nbsp;&divide;&nbsp; %d &nbsp;=&nbsp; %d <font class='litreFont'>ml</font>"%(number3+number4,number1,answer)
        self.solution_text = self.solution_text + "<br>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;"
        self.solution_text = self.solution_text + "The volume of %s in each %s is %d <font class='litreFont'>ml</font> ."%(item0,item4,answer)
        self.solution_text = self.solution_text + "</font>"
        #end of steps2

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType21(self):       
        '''e.g.:
        [Person.Boyname]'s <house> is 4 times as far from the <amusement park> as it is from the <playground>.
        Find the distance between his <house> and the <amusement park>.'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.BoyName)
     
        self.items = [
                        ['house','amusement park','beach',random.choice([['P3LMWP_HAB_786',786,4],['P3LMWP_HAB_630',630,4],['P3LMWP_HAB_960',960,5],['P3LMWP_HAB_528',528,5],['P3LMWP_HAB_855',855,6],['P3LMWP_HAB_940',940,6]])],
                        ['hotel','cinema','shopping centre',random.choice([['P3LMWP_HCS_735',735,4],['P3LMWP_HCS_570',570,4],['P3LMWP_HCS_976',976,5],['P3LMWP_HCS_564',564,5],['P3LMWP_HCS_830',830,6],['P3LMWP_HCS_925',925,6]])],
                        ['shop','pharmacy','carpark',random.choice([['P3LMWP_SPC_576',576,4],['P3LMWP_SPC_738',738,4],['P3LMWP_SPC_964',964,5],['P3LMWP_SPC_656',656,5],['P3LMWP_SPC_825',825,6],['P3LMWP_SPC_630',630,6]])],
                        ['school','video arcade','bookshop',random.choice([['P3LMWP_SVB_490',490,3],['P3LMWP_SVB_714',714,3],['P3LMWP_SVB_873',873,4],['P3LMWP_SVB_750',750,4],['P3LMWP_SVB_844',844,5],['P3LMWP_SVB_680',680,5]])],
                        ['hostel','school','train station',random.choice([['P3LMWP_HST_582',582,3],['P3LMWP_HST_764',764,3],['P3LMWP_HST_948',948,4],['P3LMWP_HST_675',675,4],['P3LMWP_HST_816',816,5],['P3LMWP_HST_620',620,5]])],
                        ['house','supermarket','bus stop',random.choice([['P3LMWP_HBS_510',510,3],['P3LMWP_HBS_728',728,3],['P3LMWP_HBS_927',927,4],['P3LMWP_HBS_690',690,4],['P3LMWP_HBS_800',800,5],['P3LMWP_HBS_616',616,5]])],
                        ['workplace','cafe','gym',random.choice([['P3LMWP_WCG_436',436,3],['P3LMWP_WCG_764',764,3],['P3LMWP_WCG_924',924,4],['P3LMWP_WCG_732',732,4],['P3LMWP_WCG_820',820,5],['P3LMWP_WCG_552',552,5]])],
                        ['school','sports shop','library',random.choice([['P3LMWP_SSL_654',654,7],['P3LMWP_SSL_540',540,7],['P3LMWP_SSL_833',833,8],['P3LMWP_SSL_637',637,8],['P3LMWP_SSL_968',968,9],['P3LMWP_SSL_720',720,9]])],
                        ['house','mall','playground',random.choice([['P3LMWP_HMP_480',480,7],['P3LMWP_HMP_726',726,7],['P3LMWP_HMP_910',910,8],['P3LMWP_HMP_770',770,8],['P3LMWP_HMP_872',872,9],['P3LMWP_HMP_640',640,9]])],
                        ['workplace','post office','taxi stand',random.choice([['P3LMWP_WPT_468',468,7],['P3LMWP_WPT_792',792,7],['P3LMWP_WPT_945',945,8],['P3LMWP_WPT_742',742,8],['P3LMWP_WPT_856',856,9],['P3LMWP_WPT_576',576,9]])]
                        ]

        self.item = random.choice(self.items)
        self.number1 = self.item[3][1]
        self.number2 = self.item[3][2]
        
        self.problem = "%s's %s is %d times as far from the %s as it is from the %s.<br>"%(self.name,self.item[0],self.number2,self.item[1],self.item[2])
        self.problem = self.problem + "Find the distance between his %s and the %s.<br><br>"%(self.item[0],self.item[1])
        self.problem = self.problem + "<img src='/images/P3ProblemImages/"+self.item[3][0]+".png'>"

        self.answer = self.number1*self.number2/(self.number2-1)
        
        self.unit = "m"
        self.dollar_unit = ""      
            
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType21(self.problem,self.answer,self.number1,self.number2,self.item[0],self.item[1],self.item[2],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType21",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,'unit':self.unit,
                'dollar_unit':self.dollar_unit}

    def ExplainType21(self,problem,answer,number1,number2,item0,item1,item2,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        #beginning of model
        self.colors = random.choice([['tomato','orange'],['blueviolet','violet'],['purple','plum'],['darkturquoise','dodgerblue'],['mediumorchid','mediumpurple'],['chocolate','burlywood'],['deeppink','lightpink']])
        self.color1 = self.colors[0]
        self.color2 = self.colors[1]

        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d>?</td></tr>"%(number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d style='padding-bottom:3px;text-align:left;'><img src='/images/explanation/P3_model_distance_arrow%d.png' /></td></tr>"%(number2+1,number2)
        self.solution_text = self.solution_text + "<tr><td><font style='font-size:0.8em;white-space:nowrap;'>%s</font></td><td colspan=2 style='white-space:nowrap;'><font style='font-size:0.8em;'>%s</font></td><td colspan=%d>&nbsp;</td><td style='white-space:nowrap;'><font style='font-size:0.8em;'>%s</font></td></tr>"%(item0,item2,number2-2,item1)
        self.solution_text = self.solution_text + "<tr><td style='padding-top:0px;padding-bottom:0px;'>&nbsp;</td><td style='padding-top:0px;padding-bottom:0px;'><img src='/images/explanation/P3_model_distance.png' /></td>"
        for x in range(1,number2):
            self.solution_text = self.solution_text + "<td style='padding-top:0px;padding-bottom:0px;'><img src='/images/explanation/P3_model_distance.png' /></td>"
        self.solution_text = self.solution_text + "<td style='text-align:left;padding-top:0px;padding-bottom:0px;'><img src='/images/explanation/P3_model_distance_end.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>&nbsp;</td><td colspan=%d style='text-align:left;'><img src='/images/explanation/P3_model_distance_arrow%d.png' /></td></tr>"%(number2,number2-1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>&nbsp;</td><td colspan=%d>%d m</td></tr>"%(number2-1,number1)
        self.solution_text = self.solution_text + "</table><br><br>"
        #end of model
        
        #beginning of steps
        #number2 = how many times
        #number1 = 960
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;"
        self.solution_text = self.solution_text + "%d m &nbsp;&divide;&nbsp; %d &nbsp;=&nbsp; %d m"%(number1,number2-1,number1/(number2-1))
        self.solution_text = self.solution_text + "<br>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;"
        self.solution_text = self.solution_text + "The distance between his %s and the %s is %d m."%(item0,item2,number1/(number2-1))
        self.solution_text = self.solution_text + "<br><br><br>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;"
        self.solution_text = self.solution_text + "%d m &nbsp;&times;&nbsp; %d &nbsp;=&nbsp; %d m"%(number1/(number2-1),number2,answer)
        self.solution_text = self.solution_text + "<br>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;"
        self.solution_text = self.solution_text + "The distance between his %s and the %s is %d m."%(item0,item1,answer)
        self.solution_text = self.solution_text + "</font>"
        #end of steps

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain
   
    def checkAnswer(self,template,answer,InputAnswer,CheckAnswer):
        if CheckAnswer == 1:
            try:
                return (int(answer)==int(InputAnswer))
            except ValueError:
                return False
        elif CheckAnswer == 2:
            try:
                answer1 = string.join(str(answer).split(),"")
                '''If user enter answer as 1l 007 ml that should also be correct'''
                if len(answer1.partition("l")[2])==4:
                    answer2 = answer1.partition("l")[0]+"l0"+answer1.partition("l")[2]
                elif len(answer1.partition("l")[2])==3:
                    answer2 = answer1.partition("l")[0]+"l00"+answer1.partition("l")[2]
                else:
                    answer2 = answer1
                InputAnswer = string.join(str(InputAnswer).split(),"")
                return answer1.capitalize() == InputAnswer.capitalize() or answer2.capitalize() == InputAnswer.capitalize()
            except ValueError:
                return False
        elif CheckAnswer == 3:
            try:
                answer1 = string.join(str(answer).split(),"")
                '''If user enter answer as 1m 04 cm that should also be correct'''
                if len(answer1.partition("m")[2])==3:
                    answer2 = answer1.partition("m")[0]+"m0"+answer1.partition("m")[2]
                else:
                    answer2 = answer1
                InputAnswer = string.join(str(InputAnswer).split(),"")
                return answer1.capitalize() == InputAnswer.capitalize() or answer2.capitalize() == InputAnswer.capitalize()
            except ValueError:
                return False
        elif CheckAnswer == 4:
            try:
                answer1 = string.join(str(answer).split(),"")
                '''If user enter answer as 1kg 007 g that should also be correct'''
                if len(answer1.partition("kg")[2])==3:
                    answer2 = answer1.partition("kg")[0]+"kg0"+answer1.partition("kg")[2]
                elif len(answer1.partition("kg")[2])==2:
                    answer2 = answer1.partition("kg")[0]+"kg00"+answer1.partition("kg")[2]
                else:
                    answer2 = answer1
                InputAnswer = string.join(str(InputAnswer).split(),"")
                return answer1.capitalize() == InputAnswer.capitalize() or answer2.capitalize() == InputAnswer.capitalize()
            except ValueError:
                return False
        elif CheckAnswer == 5:
            try:
                answer1 = string.join(str(answer).split(),"")
                '''If user enter answer as 1km 007 m that should also be correct'''
                if len(answer1.partition("km")[2])==3:
                    answer2 = answer1.partition("km")[0]+"km0"+answer1.partition("km")[2]
                elif len(answer1.partition("km")[2])==2:
                    answer2 = answer1.partition("km")[0]+"km00"+answer1.partition("km")[2]
                else:
                    answer2 = answer1
                InputAnswer = string.join(str(InputAnswer).split(),"")
                return answer1.capitalize() == InputAnswer.capitalize() or answer2.capitalize() == InputAnswer.capitalize()
            except ValueError:
                return False
          
