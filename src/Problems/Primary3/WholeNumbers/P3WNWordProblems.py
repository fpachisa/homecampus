'''
Created on Apr 04, 2013
Module: P3WNWordProblems
Generates the Word Problems for Primary 3

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

class P3WNWordProblems:
    
    def __init__(self):
        pass
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:["ProblemType1"],2:["ProblemType2"],3:["ProblemType3"],4:["ProblemType4"],5:["ProblemType5"],
                            6:["ProblemType6"],7:["ProblemType7"],8:["ProblemType8"],9:["ProblemType9"],10:["ProblemType10"],
                            11:["ProblemType11"],12:["ProblemType12"],13:["ProblemType13"],14:["ProblemType14"],15:["ProblemType15"],
                            16:["ProblemType16"],17:["ProblemType17"],18:["ProblemType18"],19:["ProblemType19"],20:["ProblemType20"],
                            21:["ProblemType21"],22:["ProblemType22"],23:["ProblemType23"],24:["ProblemType24"],25:["ProblemType25"],
                            26:["ProblemType26"],27:["ProblemType27"],28:["ProblemType28"],29:["ProblemType29"],30:["ProblemType30"],
                            31:["ProblemType31"],32:["ProblemType32"],33:["ProblemType33"],34:["ProblemType34"],35:["ProblemType35"],
                            36:["ProblemType36"],37:["ProblemType37"],38:["ProblemType38"],39:["ProblemType39"],40:["ProblemType40"],
                            41:["ProblemType41"],42:["ProblemType42"],43:["ProblemType43"],44:["ProblemType44"],45:["ProblemType45"],
                            46:["ProblemType46"],47:["ProblemType47"],
                            }
        self.GenerateProblemType = {1:[self.GenerateProblemType1(),],2:[self.GenerateProblemType2(),],3:[self.GenerateProblemType3(),],
                                    4:[self.GenerateProblemType4(),],5:[self.GenerateProblemType5(),],6:[self.GenerateProblemType6(),],
                                    7:[self.GenerateProblemType7(),],8:[self.GenerateProblemType8(),],9:[self.GenerateProblemType9(),],10:[self.GenerateProblemType10(),],
                                    11:[self.GenerateProblemType11(),],12:[self.GenerateProblemType12(),],13:[self.GenerateProblemType13(),],
                                    14:[self.GenerateProblemType14(),],15:[self.GenerateProblemType15(),],16:[self.GenerateProblemType16(),],
                                    17:[self.GenerateProblemType17(),],18:[self.GenerateProblemType18(),],19:[self.GenerateProblemType19(),],20:[self.GenerateProblemType20(),],
                                    21:[self.GenerateProblemType21(),],22:[self.GenerateProblemType22(),],23:[self.GenerateProblemType23(),],
                                    24:[self.GenerateProblemType24(),],25:[self.GenerateProblemType25(),],26:[self.GenerateProblemType26(),],
                                    27:[self.GenerateProblemType27(),],28:[self.GenerateProblemType28(),],29:[self.GenerateProblemType29(),],30:[self.GenerateProblemType30(),],
                                    31:[self.GenerateProblemType31(),],32:[self.GenerateProblemType32(),],33:[self.GenerateProblemType33(),],
                                    34:[self.GenerateProblemType34(),],35:[self.GenerateProblemType35(),],36:[self.GenerateProblemType36(),],
                                    37:[self.GenerateProblemType37(),],38:[self.GenerateProblemType38(),],39:[self.GenerateProblemType39(),],40:[self.GenerateProblemType40(),],
                                    41:[self.GenerateProblemType41(),],42:[self.GenerateProblemType42(),],43:[self.GenerateProblemType43(),],
                                    44:[self.GenerateProblemType44(),],45:[self.GenerateProblemType45(),],46:[self.GenerateProblemType46(),],
                                    47:[self.GenerateProblemType47(),],
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
        #return self.GenerateProblemType8() #reorder the questions so the same kind of questions are not presented in a sequence
        
    def GenerateTestProblem(self,problem_type):
        self.ProblemType = {"ProblemType1":self.GenerateProblemType1(),"ProblemType2":self.GenerateProblemType2(),"ProblemType3":self.GenerateProblemType3(),
                            "ProblemType4":self.GenerateProblemType4(),"ProblemType5":self.GenerateProblemType5(),"ProblemType6":self.GenerateProblemType6(),
                            "ProblemType7":self.GenerateProblemType7(),"ProblemType8":self.GenerateProblemType8(),"ProblemType9":self.GenerateProblemType9(),
                            "ProblemType10":self.GenerateProblemType10(),
                            "ProblemType11":self.GenerateProblemType11(),"ProblemType12":self.GenerateProblemType12(),"ProblemType13":self.GenerateProblemType13(),
                            "ProblemType14":self.GenerateProblemType14(),"ProblemType15":self.GenerateProblemType15(),"ProblemType16":self.GenerateProblemType16(),
                            "ProblemType17":self.GenerateProblemType17(),"ProblemType18":self.GenerateProblemType18(),"ProblemType19":self.GenerateProblemType19(),
                            "ProblemType20":self.GenerateProblemType20(),
                            "ProblemType21":self.GenerateProblemType21(),"ProblemType22":self.GenerateProblemType22(),"ProblemType23":self.GenerateProblemType23(),
                            "ProblemType24":self.GenerateProblemType24(),"ProblemType25":self.GenerateProblemType25(),"ProblemType26":self.GenerateProblemType26(),
                            "ProblemType27":self.GenerateProblemType27(),"ProblemType28":self.GenerateProblemType28(),"ProblemType29":self.GenerateProblemType29(),
                            "ProblemType30":self.GenerateProblemType30(),
                            "ProblemType31":self.GenerateProblemType31(),"ProblemType32":self.GenerateProblemType32(),"ProblemType33":self.GenerateProblemType33(),
                            "ProblemType34":self.GenerateProblemType34(),"ProblemType35":self.GenerateProblemType35(),"ProblemType36":self.GenerateProblemType36(),
                            "ProblemType37":self.GenerateProblemType37(),"ProblemType38":self.GenerateProblemType38(),"ProblemType39":self.GenerateProblemType39(),
                            "ProblemType40":self.GenerateProblemType40(),
                            "ProblemType41":self.GenerateProblemType41(),"ProblemType42":self.GenerateProblemType42(),"ProblemType43":self.GenerateProblemType43(),
                            "ProblemType44":self.GenerateProblemType44(),"ProblemType45":self.GenerateProblemType45(),"ProblemType46":self.GenerateProblemType46(),
                            "ProblemType47":self.GenerateProblemType47(),                            
                            }
        return self.ProblemType[problem_type]

    def GenerateProblemType1(self):       
        '''e.g.:
        [Person.Girlname 1] and [Person.Girlname 2] <were making jewellery using beads>.
        [Person.Girlname 1] <used> 5224 <beads to make a bracelet>.
        [Person.Girlname 2] <used> 2028 more / fewer <beads> than [Person.Girlname 1] <to make a necklace>.
        How many <beads> did [Person.Girlname 2] <use>?'''

        self.complexity_level = "easy"
        self.HCScore = 3

        self.names = random.sample(PersonName.GirlName,2)
        
        self.items = [['were making jewellery using beads','used','beads to make a bracelet','beads','to make a necklace','use'],
                      ['were making mosaics using stones','used','stones to make her mosaic','stones','to make her mosaic','use'],
                      ['were making art projects using dried leaves','used','dried leaves for her project','dried leaves','for her project','use'],
                      ['were making curry puffs to sell at a food fest','made','curry puffs','curry puffs','','make'],
                      ['were selling tickets to a school festival','sold','tickets in her neighbourhood','tickets','in her neighbourhood','sell'],
                      ['were selling coupons at a carnival at school','sold','coupons','coupons','','sell'],
                      ['were collecting recyclable items for a community project','collected','items','items','','collect'],
                      ['were collecting books for a book drive','collected','books','books','','collect'],
                      ['were collecting can tabs','collected','can tabs','can tabs','','collect'],
                      ['were collecting toys for charity','collected','toys','toys','','collect'],
                      ['were planting trees for an environment project','planted','trees','trees','','plant']]
        
        self.item = random.choice(self.items)
        
        self.number1 = randint(4000,6000)
        self.diff = randint(1000,3000)       
        
        self.flag = randint(1,2)
        
        self.problem = "%s and %s %s.<br><br>"%(self.names[0],self.names[1],self.item[0])
        self.problem = self.problem + "%s %s %d %s.<br><br>"%(self.names[0],self.item[1],self.number1,self.item[2])
        if self.flag == 1:
            self.problem = self.problem + "%s %s %d more %s than %s %s.<br><br>"%(self.names[1],self.item[1],self.diff,self.item[3],
                                                                                  self.names[0],self.item[4])
            self.answer = self.number1 + self.diff
        elif self.flag == 2:
            self.problem = self.problem + "%s %s %d fewer %s than %s %s.<br><br>"%(self.names[1],self.item[1],self.diff,self.item[3],
                                                                                  self.names[0],self.item[4])
            self.answer = self.number1 - self.diff
            
        self.problem = self.problem + "How many %s did %s %s?"%(self.item[3],self.names[1],self.item[5])
        
        self.unit = self.item[3]
        self.dollar_unit = ""
          
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.names,self.item[1],self.item[3],self.flag,self.number1,self.diff,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType1",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,
                'unit':self.unit,'dollar_unit':self.dollar_unit}

    def ExplainType1(self,problem,answer,names,item1,item3,flag,number1,diff,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        self.colors = random.choice([['tomato','orange'],['blueviolet','violet'],['purple','plum'],['darkturquoise','dodgerblue'],['mediumorchid','mediumpurple'],['chocolate','burlywood'],['deeppink','lightpink']])
        self.color1 = self.colors[0]
        self.color2 = self.colors[1]
        
        if flag == 1:
            #beginning of model
            if number1>=diff:
                firstBrace = 'medium'
                secondBrace = 'small'
            else:
                firstBrace = 'small'
                secondBrace = 'medium'
            self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>%d</td><td>%d</td></tr>"%(number1,diff)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(firstBrace,secondBrace)
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;'>&nbsp;</td><td>&nbsp;</td></tr>"%(names[0],self.color1)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td></tr>"
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td><td colspan=2 style='background-color:%s;height:25px;border:white solid 1px;'>&nbsp;</td></tr>"%(names[1],self.color2)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_large.png' /></td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2>?</td></tr>"
            self.solution_text = self.solution_text + "</table><br><br>"
            #end of model

            self.solution_text = self.solution_text + "<font class='ExplanationFont'>%d &nbsp;+&nbsp; %d &nbsp;=&nbsp; %d<br><br>"%(number1,diff,answer)
            self.solution_text = self.solution_text + "%s %s %d %s."%(names[1],item1,answer,item3)
            self.solution_text = self.solution_text + "</font>" 
        else:
            #beginning of model
            if answer>=diff:
                firstBrace = 'medium'
                secondBrace = 'small'
            else:
                firstBrace = 'small'
                secondBrace = 'medium'
            self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2>%d</td></tr>"%(number1)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_large.png' /></td></tr>"
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td><td colspan=2 style='background-color:%s;height:25px;border:white solid 1px;'>&nbsp;</td></tr>"%(names[0],self.color2)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td></tr>"
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;'>&nbsp;</td><td>&nbsp;</td></tr>"%(names[1],self.color1)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_%s.png' /></td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(firstBrace,secondBrace)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>?</td><td>%d</td></tr>"%(diff)
            self.solution_text = self.solution_text + "</table><br><br>"
            #end of model

            self.solution_text = self.solution_text + "<font class='ExplanationFont'>%d &nbsp;&minus;&nbsp; %d &nbsp;=&nbsp; %d<br><br>"%(number1,diff,answer)
            self.solution_text = self.solution_text + "%s %s %d %s."%(names[1],item1,answer,item3)
            self.solution_text = self.solution_text + "</font>" 

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType2(self):  #2-step
        '''e.g.:
        [Person.Boyname 1] and [Person.Boyname 2] <enjoy collecting stamps>.
        [Person.Boyname 1] <has> 5224 <stamps in his collection>.
        [Person.Boyname 1] <has> 2028 more / fewer <stamps> than [Person.Boyname 2] <in his collection>.
        How many <stamps do the two boys have> altogether?'''

        self.complexity_level = "easy"
        self.HCScore = 3

        self.names = random.sample(PersonName.BoyName,2)
        
        self.items = [['enjoy collecting stamps','has','stamps in his collection','has','stamps','in his collection','stamps do the two boys have','The two boys have'],
                      ['like collecting seashells','collected','seashells','','seashells','','seashells did the two boys collect','The two boys collected'],
                      ['love collecting bird feathers','has','bird feathers in his scrap book','bird feathers','feathers','in his scrap book','feathers do the two boys have','The two boys have'],
                      ['enjoy making art projects with icecream sticks','used','icecream sticks to make a model treehouse','icecream sticks','icecream sticks','to make a model ship','icecream sticks did the two boys use for their art projects','The two boys used'],
                      ['each bought a box of thumbtacks','had','thumbtacks in his box','thumbtacks','thumbtacks','in his box','thumbtacks did the two boys have in their boxes','The two boys had'],
                      ['like to collect coins','has','coins in his collection','coins','coins','in his collection','coins do the two boys have','The two boys have'],
                      ['sold souvenirs at a night market','sold','souvenirs at his stall','souvenirs','souvenirs','at his stall','souvenirs did the two boys sell','The two boys sold'],
                      ['are sports merchandise suppliers','supplied','baseball bats to a sports shop','baseball bats','baseball bats','to another sports shop','baseball bats did they supply to the two sports shops','They supplied'],
                      ['helped a farmer harvest mangoes last season','picked','mangoes','mangoes','mangoes','','mangoes did the two boys pick','The two boys picked'],
                      ['sold lemonade at a summer carnival','sold','glasses of lemonade','glasses of lemonade','glasses of lemonade','','glasses of lemonade did the two boys sell','The two boys sold']]
        
        self.item = random.choice(self.items)

        self.number1 = randint(2000,4250)
        self.diff = randint(500,1500)       
        
        self.flag = randint(1,2)
        self.problem = "%s and %s %s.<br><br>"%(self.names[0],self.names[1],self.item[0])
        self.problem = self.problem + "%s %s %d %s.<br><br>"%(self.names[0],self.item[1],self.number1,self.item[2])
        if self.flag == 1:
            self.problem = self.problem + "%s %s %d more %s than %s %s.<br><br>"%(self.names[1],self.item[1],self.diff,self.item[4],
                                                                                  self.names[0],self.item[5])
            self.answer = self.number1 + self.number1 + self.diff
        elif self.flag == 2:
            self.problem = self.problem + "%s %s %d fewer %s than %s %s.<br><br>"%(self.names[1],self.item[1],self.diff,self.item[4],
                                                                                  self.names[0],self.item[5])
            self.answer = self.number1 + self.number1 - self.diff
            
        self.problem = self.problem + "How many %s altogether?"%(self.item[6])
        
        self.unit = self.item[4]
        self.dollar_unit = ""
          
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.names,self.item[1],self.item[4],self.item[7],self.flag,self.number1,self.diff,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType2",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,
                'unit':self.unit,'dollar_unit':self.dollar_unit}

    def ExplainType2(self,problem,answer,names,item1,item4,item7,flag,number1,diff,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)
        
        self.colors = random.choice([['tomato','orange'],['blueviolet','violet'],['purple','plum'],['darkturquoise','dodgerblue'],['mediumorchid','mediumpurple'],['chocolate','burlywood'],['deeppink','lightpink']])
        self.color1 = self.colors[0]
        self.color2 = self.colors[1]


        if flag == 1:
            #beginning of model
            if number1>=diff:
                firstBrace = 'medium'
                secondBrace = 'small'
            else:
                firstBrace = 'small'
                secondBrace = 'medium'
            self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>%d</td><td>%d</td></tr>"%(number1,diff)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(firstBrace,secondBrace)
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;'>&nbsp;</td><td>&nbsp;</td><td>&nbsp;&nbsp;</td><td rowspan=3 style='padding:0;padding-top:3px;vertical-align:middle'><img src='/images/explanation/P3_model_right_brace_small.png' /></td><td rowspan=3 style='padding:0;vertical-align:middle'>&nbsp;?</td></tr>"%(names[0],self.color1)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td></tr>"
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td><td colspan=2 style='background-color:%s;height:25px;border:white solid 1px;'>&nbsp;</td></tr>"%(names[1],self.color2)
            self.solution_text = self.solution_text + "</table><br><br><br>"
            #end of model
            self.solution_text = self.solution_text + "<font class='ExplanationFont'>%d &nbsp;+&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number1,diff,number1+diff)
            intermediateAnswer = number1 + diff
        else:
            #beginning of model
            if number1-diff>=diff:
                firstCellWidth = 100
                secondBrace = 'small'
            else:
                firstCellWidth = 50
                secondBrace = 'medium'
            self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2>%d</td></tr>"%(number1)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_large.png' /></td></tr>"
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td><td colspan=2 style='background-color:%s;height:25px;border:white solid 1px;'>&nbsp;</td><td>&nbsp;&nbsp;</td><td rowspan=3 style='padding:0;padding-top:3px;vertical-align:middle'><img src='/images/explanation/P3_model_right_brace_small.png' /></td><td rowspan=3 style='padding:0;vertical-align:middle'>&nbsp;?</td></tr>"%(names[0],self.color2)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td></tr>"
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;width:%dpx'>&nbsp;</td><td>&nbsp;</td></tr>"%(names[1],self.color1,firstCellWidth)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(secondBrace)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>&nbsp;</td><td>%d</td></tr>"%(diff)
            self.solution_text = self.solution_text + "</table><br><br><br>"
            #end of model
            self.solution_text = self.solution_text + "<font class='ExplanationFont'>%d &nbsp;&minus;&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number1,diff,number1-diff)
            intermediateAnswer = number1 - diff

        self.solution_text = self.solution_text + "%s %s %d %s.<br><br>"%(names[1],item1,intermediateAnswer,item4)
        
        self.solution_text = self.solution_text + "%d &nbsp;+&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number1,intermediateAnswer,answer)
        self.solution_text = self.solution_text + "%s %d %s altogether."%(item7,answer,item4)
        self.solution_text = self.solution_text + "</font>" 

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType3(self):       
        '''e.g.:
        [Person.Unclename] bought a <sofa set> and a <coffee table>.
        The <sofa set> cost $1200 and the <coffee table> cost $300 less than the <sofa set>.
        How much did he pay for the two items altogether?'''

        self.complexity_level = "easy"
        self.HCScore = 3

        self.name = random.choice(PersonName.UncleName)
        
        self.items = [['sofa','table'],['couch','recliner'],['bed frame','mattress'],['television set','DVD player'],
                      ['refrigerator','microwave oven'],['washer','dryer'],['computer','printer'],['camera','phone'],
                      ['guitar','microphone'],['book shelf','cupboard']]
        
        self.item = random.choice(self.items)

        self.number1 = randint(1000,2000)
        self.number2 = randint(200,800)       
        self.diff = self.number1 - self.number2
        
        self.flag = randint(1,2)
        
        self.problem = "%s bought a %s and a %s.<br><br>"%(self.name,self.item[0],self.item[1])
        if self.flag == 1:
            self.problem = self.problem + "The %s cost $%d and the %s cost $%d less than the %s.<br><br>"%(self.item[0],self.number1,self.item[1],self.diff,self.item[0])
        else:
            self.problem = self.problem + "The %s cost $%d and the %s cost $%d more than the %s.<br><br>"%(self.item[1],self.number2,self.item[0],self.diff,self.item[1])
        
        self.problem = self.problem + "How much did he pay for the two items altogether?"
        
        self.answer = self.number1 + self.number2
        
        self.unit = ""
        self.dollar_unit = "$"
          
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.item[0],self.item[1],self.flag,self.number1,self.number2,self.diff,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType3",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,
                'unit':self.unit,'dollar_unit':self.dollar_unit}

    def ExplainType3(self,problem,answer,item0,item1,flag,number1,number2,diff,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        self.colors = random.choice([['tomato','orange'],['blueviolet','violet'],['purple','plum'],['darkturquoise','dodgerblue'],['mediumorchid','mediumpurple'],['chocolate','burlywood'],['deeppink','lightpink']])
        self.color1 = self.colors[0]
        self.color2 = self.colors[1]

        if flag == 1:
            #beginning of model
            if number2>=diff:
                firstCellWidth = 100
                secondBrace = 'small'
            else:
                firstCellWidth = 50
                secondBrace = 'medium'
            self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2>$%d</td></tr>"%(number1)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_large.png' /></td></tr>"
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td><td colspan=2 style='background-color:%s;height:25px;border:white solid 1px;'>&nbsp;</td><td>&nbsp;&nbsp;</td><td rowspan=3 style='padding:0;padding-top:3px;vertical-align:middle'><img src='/images/explanation/P3_model_right_brace_small.png' /></td><td rowspan=3 style='padding:0;vertical-align:middle'>&nbsp;?</td></tr>"%(item0,self.color2)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td></tr>"
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;width:%dpx'>&nbsp;</td><td>&nbsp;</td></tr>"%(item1,self.color1,firstCellWidth)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(secondBrace)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>&nbsp;</td><td>$%d</td></tr>"%(diff)
            self.solution_text = self.solution_text + "</table><br><br>"
            #end of model
            self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
            self.solution_text = self.solution_text + "$%d &nbsp;&minus;&nbsp; $%d &nbsp;=&nbsp; $%d<br>"%(number1,diff,number1-diff)
            self.solution_text = self.solution_text + "The %s cost $%d.<br><br>"%(item1,number2)
        else:
            #beginning of model
            if number2>=diff:
                firstBrace = 'medium'
                secondBrace = 'small'
            else:
                firstBrace = 'small'
                secondBrace = 'medium'
            self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$%d</td><td>$%d</td></tr>"%(number2,diff)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(firstBrace,secondBrace)
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;'>&nbsp;</td><td>&nbsp;</td><td>&nbsp;&nbsp;</td><td rowspan=3 style='padding:0;padding-top:3px;vertical-align:middle'><img src='/images/explanation/P3_model_right_brace_small.png' /></td><td rowspan=3 style='padding:0;vertical-align:middle'>&nbsp;?</td></tr>"%(item1,self.color1)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td></tr>"
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td><td colspan=2 style='background-color:%s;height:25px;border:white solid 1px;'>&nbsp;</td></tr>"%(item0,self.color2)
            self.solution_text = self.solution_text + "</table><br><br><br>"
            #end of model
            self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
            self.solution_text = self.solution_text + "$%d &nbsp;+&nbsp; $%d &nbsp;=&nbsp; $%d<br>"%(number2,diff,number2+diff)
            self.solution_text = self.solution_text + "The %s cost $%d.<br><br>"%(item0,number1)
        
        self.solution_text = self.solution_text + "$%d &nbsp;+&nbsp; $%d &nbsp;=&nbsp; $%d<br>"%(number1,number2,answer)
        self.solution_text = self.solution_text + "He paid $%d for the two items altogether."%(answer)
        self.solution_text = self.solution_text + "</font>" 

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType4(self):       
        '''e.g.:
        [Person.Unclename] bought a <sofa set> and a <coffee table>.
        The <sofa set> cost $1200 and the <coffee table> cost $900.
        If he had $2000 at first, how much money had he left after paying for the two items?'''

        self.complexity_level = "easy"
        self.HCScore = 3

        self.name = random.choice(PersonName.UncleName)
        
        self.items = [['sofa','table'],['couch','recliner'],['bed frame','mattress'],['television set','DVD player'],
                      ['refrigerator','microwave oven'],['washer','dryer'],['computer','printer'],['camera','phone'],
                      ['guitar','microphone'],['book shelf','cupboard']]
        
        self.item = random.choice(self.items)

        self.number1 = randint(1000,2000)
        self.number2 = randint(200,800)       
        self.initial = ((self.number1+self.number2)/1000+1)*1000 + randint(0,1)*500
                
        self.problem = "%s bought a %s and a %s.<br><br>"%(self.name,self.item[0],self.item[1])
        self.problem = self.problem + "The %s cost $%d and the %s cost $%d.<br><br>"%(self.item[0],self.number1,self.item[1],self.number2)
        self.problem = self.problem + "If he had $%d at first, how much money had he left after paying for the two items?"%(self.initial)
        
        self.answer = self.initial - (self.number1 + self.number2)
        
        self.unit = ""
        self.dollar_unit = "$"
          
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,self.answer,self.item[0],self.item[1],self.number1,self.number2,self.initial,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType4",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,
                'unit':self.unit,'dollar_unit':self.dollar_unit}

    def ExplainType4(self,problem,answer,item0,item1,number1,number2,initial,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        self.colors = random.choice([['tomato','orange'],['blueviolet','violet'],['purple','plum'],['darkturquoise','dodgerblue'],['mediumorchid','mediumpurple'],['chocolate','burlywood'],['deeppink','lightpink']])
        self.color1 = self.colors[0]
        self.color2 = self.colors[1]

        # Check the values of the 3 amounts
        if number1==number2:
            firstCell = 'medium'
            secondCell = 'medium'
            if number1==answer:
                thirdCell = 'medium'
                upBrace = 'medium3'
            elif number1>answer:
                thirdCell = 'small'
                upBrace = 'medium2small1'
            else:
                thirdCell = 'large'
                upBrace = 'large1medium2'
        elif number1>number2:
            if answer<number2:
                firstCell = 'large'
                secondCell = 'medium'
                thirdCell = 'small'
                upBrace = 'large1medium1small1'
            elif answer<number1 and answer>number2:
                firstCell = 'large'
                secondCell = 'small'
                thirdCell = 'medium'
                upBrace = 'large1medium1small1'
            elif answer>number1:
                firstCell = 'medium'
                secondCell = 'small'
                thirdCell = 'large'
                upBrace = 'large1medium1small1'
            elif answer==number2:
                firstCell = 'large'
                secondCell = 'medium'
                thirdCell = 'medium'
                upBrace = 'large1medium2'
            elif answer==number1:
                firstCell = 'medium'
                secondCell = 'small'
                thirdCell = 'medium'
                upBrace = 'medium2small1'
        elif number1<number2:
            if answer>number2:
                firstCell = 'small'
                secondCell = 'medium'
                thirdCell = 'large'
                upBrace = 'large1medium1small1'
            elif answer<number2 and answer>number1:
                firstCell = 'small'
                secondCell = 'large'
                thirdCell = 'medium'
                upBrace = 'large1medium1small1'
            elif answer<number1:
                firstCell = 'medium'
                secondCell = 'large'
                thirdCell = 'small'
                upBrace = 'large1medium1small1'
            elif answer==number2:
                firstCell = 'small'
                secondCell = 'medium'
                thirdCell = 'medium'
                upBrace = 'medium2small1'
            elif answer==number1:
                firstCell = 'medium'
                secondCell = 'large'
                thirdCell = 'medium'
                upBrace = 'large1medium2'

        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0'>"
        self.solution_text = self.solution_text + "<tr><td colspan=3>$%s</td></tr>"%initial
        self.solution_text = self.solution_text + "<tr><td colspan=3 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(upBrace)
        self.solution_text = self.solution_text + "<tr><td style='background-color:%s;height:25px;border:white solid 1px;'></td><td style='background-color:%s;border:white solid 1px;'></td><td style='border:white solid 1px;'><font style='font-size:0.8em;'>left</font></td></tr>"%(self.color1,self.color2)
        self.solution_text = self.solution_text + "<tr><td><img src='/images/explanation/P3_model_down_brace_%s.png' /></td><td><img src='/images/explanation/P3_model_down_brace_%s.png' /></td><td><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(firstCell,secondCell,thirdCell)
        self.solution_text = self.solution_text + "<tr><td>$%s</td><td>$%s</td><td>?</td></tr>"%(number1,number2)
        self.solution_text = self.solution_text + "</table><br><br>"

        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "$%d &nbsp;+&nbsp; $%d &nbsp;=&nbsp; $%d<br>"%(number1,number2,number1+number2)
        self.solution_text = self.solution_text + "The %s and the %s cost $%d altogether.<br><br>"%(item0,item1,number1+number2)
        
        self.solution_text = self.solution_text + "$%d &nbsp;&minus;&nbsp; $%d &nbsp;=&nbsp; $%d<br>"%(initial,number1+number2,answer)
        self.solution_text = self.solution_text + "He had $%d left after paying for the two items."%(answer)
        self.solution_text = self.solution_text + "</font>" 

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType5(self):       
        '''e.g.:
        <There are> 2659 <pupils in a primary school>.
        1298 <of them are girls>.
        How many more / fewer <boys than girls are there in the school>?'''

        self.complexity_level = "easy"
        self.HCScore = 3

        self.name = random.choice(PersonName.UncleName)
        
        self.items = [['There were','pupils in a primary school','of them were girls','boys than girls were there in the school','boys','There were ','boys than girls in the school','girls'],
                      ['','children participated in a drawing competition','of them were boys ','girls than boys participated in the competition','girls','','girls than boys participated in the competition','boys'],
                      ['An amusement park received','visitors','of them were children','adults than children did the park receive','adults','The park received ','adults than children','children'],
                      ['An animal zoo received','visitors','of them were children','adults than children did the zoo receive','adults','The zoo received ','adults than children','children'],
                      ['There were','residents in a town','of them were adults','children than adults were there in the town','children','There were ','children than adults in the town','adults'],
                      ['','spectators attended a magic show','of them were adults','children than adults attended the magic show','children','','children than adults attended the magic show','adults'],
                      ['','people went to see a circus','of them were adults','children than adults went to see the circus','children','','children than adults went to see the circus','adults'],
                      ['','adults voted in an election','of them were men','women than men voted in the election','women','','women than men voted in the election','men'],
                      ['There were','spectators at a national parade','of them were children','adults than children were at the parade','adults','There were ','adults than children at the parade','children'],
                      ['There were','employees at a company','of them were men','women than men were at the company','women','There were ','women than men at the company','men']]
                
        self.item = random.choice(self.items)

        self.number1 = randint(1000,1500)
        self.number2 = randint(1000,1500)
        
        while self.number1 == self.number2:
            self.number2 = randint(1000,1500)
        
        self.problem = "%s %d %s.<br><br>"%(self.item[0],(self.number1+self.number2),self.item[1])
        self.problem = self.problem + "%d %s.<br><br>"%(self.number1,self.item[2])
        if self.number1 > self.number2:
            self.problem = self.problem + "How many fewer %s?"%(self.item[3])
            #self.unit = "fewer "+self.item[3]
        else:
            self.problem = self.problem + "How many more %s?"%(self.item[3])
            #self.unit = "more "+self.item[3]
            
        self.answer = abs(self.number1-self.number2)
        self.unit = self.item[4]

        self.dollar_unit = ""
          
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5(self.problem,self.answer,self.number1,self.number2,self.item[4],self.item[5],self.item[6],self.item[7],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType5",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,
                'unit':self.unit,'dollar_unit':self.dollar_unit}

    def ExplainType5(self,problem,answer,number1,number2,item4,item5,item6,item7,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        self.colors = random.choice([['tomato','orange'],['blueviolet','violet'],['purple','plum'],['darkturquoise','dodgerblue'],['mediumorchid','mediumpurple'],['chocolate','burlywood'],['deeppink','lightpink']])
        self.color1 = self.colors[0]
        self.color2 = self.colors[1]

        if number1>number2:
            #beginning of model
            if number2>=answer:
                firstCellWidth = 100
                secondBrace = 'small'
            else:
                firstCellWidth = 50
                secondBrace = 'medium'
            self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2>%d</td></tr>"%(number1)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_large.png' /></td></tr>"
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td><td colspan=2 style='background-color:%s;height:25px;border:white solid 1px;'>&nbsp;</td><td>&nbsp;&nbsp;</td><td rowspan=3 style='padding:0;padding-top:3px;vertical-align:middle'><img src='/images/explanation/P3_model_right_brace_small.png' /></td><td rowspan=3 style='padding:0;vertical-align:middle'>&nbsp;%d</td></tr>"%(item7,self.color2,number1+number2)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td></tr>"
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;width:%dpx'>&nbsp;</td><td>&nbsp;</td></tr>"%(item4,self.color1,firstCellWidth)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(secondBrace)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>&nbsp;</td><td>?</td></tr>"
            self.solution_text = self.solution_text + "</table><br><br>"
            #end of model
            self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
            self.solution_text = self.solution_text + "%d &nbsp;&minus;&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number1+number2,number1,number2)
            self.solution_text = self.solution_text + "There were %d %s.<br><br>"%(number2,item4)
            self.solution_text = self.solution_text + "%d &nbsp;&minus;&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number1,number2,answer)
            self.solution_text = self.solution_text + "%s%d fewer %s."%(item5,answer,item6)
            self.solution_text = self.solution_text + "</font>"
        else:
            #beginning of model
            if number1>=answer:
                firstBrace = 'medium'
                secondBrace = 'small'
            else:
                firstBrace = 'small'
                secondBrace = 'medium'
            self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>%d</td><td>?</td></tr>"%(number1)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(firstBrace,secondBrace)
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;'>&nbsp;</td><td>&nbsp;</td><td>&nbsp;&nbsp;</td><td rowspan=3 style='padding:0;padding-top:3px;vertical-align:middle'><img src='/images/explanation/P3_model_right_brace_small.png' /></td><td rowspan=3 style='padding:0;vertical-align:middle'>&nbsp;%d</td></tr>"%(item7,self.color1,number1+number2)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td></tr>"
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td><td colspan=2 style='background-color:%s;height:25px;border:white solid 1px;'>&nbsp;</td></tr>"%(item4,self.color2)
            self.solution_text = self.solution_text + "</table><br><br><br>"
            #end of model
            self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
            self.solution_text = self.solution_text + "%d &nbsp;&minus;&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number1+number2,number1,number2)
            self.solution_text = self.solution_text + "There were %d %s.<br><br>"%(number2,item4)
            self.solution_text = self.solution_text + "%d &nbsp;&minus;&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number2,number1,answer)
            self.solution_text = self.solution_text + "%s%d more %s."%(item5,answer,item6)
            self.solution_text = self.solution_text + "</font>" 

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType6(self):       
        '''e.g.:
        <A farmer sold> 3456 <radishes> on <Saturday> and <Sunday>.
        <He sold> 1234 of them on <Saturday>.
        How many more / fewer <radishes did he sell> on <Saturday> than on <Sunday>?'''

        self.complexity_level = "easy"
        self.HCScore = 3

        self.name = random.choice(PersonName.UncleName)
        
        self.items = [['A farmer sold','radishes','He sold','radishes did he sell'],
                      ['A grocery store sold','eggs','It sold','eggs did it sell'],
                      ['A shop sold','hair clips','It sold','hair clips did it sell'],
                      ['A fruit supplier supplied','pears','He supplied','pears did he supply'],
                      ['A farmer supplied','chickens','He supplied','chickens did he supply'],
                      ['A baker baked','cupcakes','He baked','cupcakes did he bake'],
                      ['A hawker centre sold','plates of noodles','It sold','plates of noodles did it sell'],
                      ['A water park received','people','It received','people did it receive'],
                      ['A funfair received','people','It received','people did it receive'],
                      ['A theme park received','visitors','It received','visitors did it receive'],
                      ['An animal safari park received','visitors','It received','visitors did it receive'],
                      ['A museum received','visitors','It received','visitors did it receive'],
                      ['A shopping mall received','shoppers','It received','shoppers did it receive']]
                
        self.item = random.choice(self.items)

        self.number1 = randint(1000,1500)
        self.number2 = randint(1000,1500)
        
        while self.number1 == self.number2:
            self.number2 = randint(1000,1500)
        
        self.days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
        
        self.Day1Index = randint(0,6)
        if self.Day1Index == 6:
            self.Day2Index = 0
        else:
            self.Day2Index = self.Day1Index + 1  
        
        self.problem = "%s %d %s on %s and %s.<br><br>"%(self.item[0],(self.number1+self.number2),self.item[1],self.days[self.Day1Index],self.days[self.Day2Index])
        self.problem = self.problem + "%s %d of them on %s.<br><br>"%(self.item[2],self.number1,self.days[self.Day1Index])
        if self.number1 > self.number2:
            self.problem = self.problem + "How many more %s on %s than on %s?"%(self.item[3],self.days[self.Day1Index],self.days[self.Day2Index])
        else:
            self.problem = self.problem + "How many fewer %s on %s than on %s?"%(self.item[3],self.days[self.Day1Index],self.days[self.Day2Index])
            
        self.answer = abs(self.number1-self.number2)
        
        firstDay = self.days[self.Day1Index]
        secondDay = self.days[self.Day2Index]

        self.unit = self.item[1]
        self.dollar_unit = ""
          
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6(self.problem,self.answer,self.number1,self.number2,self.item[1],self.item[2],firstDay,secondDay,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType6",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,
                'unit':self.unit,'dollar_unit':self.dollar_unit}

    def ExplainType6(self,problem,answer,number1,number2,item1,item2,firstDay,secondDay,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        self.colors = random.choice([['tomato','orange'],['blueviolet','violet'],['purple','plum'],['darkturquoise','dodgerblue'],['mediumorchid','mediumpurple'],['chocolate','burlywood'],['deeppink','lightpink']])
        self.color1 = self.colors[0]
        self.color2 = self.colors[1]

        if number1>number2:
            #beginning of model
            if number2>=answer:
                firstCellWidth = 100
                secondBrace = 'small'
            else:
                firstCellWidth = 50
                secondBrace = 'medium'
            self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2>%d</td></tr>"%(number1)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_large.png' /></td></tr>"
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td><td colspan=2 style='background-color:%s;height:25px;border:white solid 1px;'>&nbsp;</td><td>&nbsp;&nbsp;</td><td rowspan=3 style='padding:0;padding-top:3px;vertical-align:middle'><img src='/images/explanation/P3_model_right_brace_small.png' /></td><td rowspan=3 style='padding:0;vertical-align:middle'>&nbsp;%d</td></tr>"%(firstDay,self.color2,number1+number2)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td></tr>"
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;width:%dpx'>&nbsp;</td><td>&nbsp;</td></tr>"%(secondDay,self.color1,firstCellWidth)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(secondBrace)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>&nbsp;</td><td>?</td></tr>"
            self.solution_text = self.solution_text + "</table><br><br>"
            #end of model
            self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
            self.solution_text = self.solution_text + "%d &nbsp;&minus;&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number1+number2,number1,number2)
            self.solution_text = self.solution_text + "%s %d %s on %s.<br><br>"%(item2,number2,item1,secondDay)
            self.solution_text = self.solution_text + "%d &nbsp;&minus;&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number1,number2,answer)
            self.solution_text = self.solution_text + "%s %d more %s on %s than on %s."%(item2,answer,item1,firstDay,secondDay)
            self.solution_text = self.solution_text + "</font>"
        else:
            #beginning of model
            if number1>=answer:
                firstBrace = 'medium'
                secondBrace = 'small'
            else:
                firstBrace = 'small'
                secondBrace = 'medium'
            self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>%d</td><td>?</td></tr>"%(number1)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(firstBrace,secondBrace)
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;'>&nbsp;</td><td>&nbsp;</td><td>&nbsp;&nbsp;</td><td rowspan=3 style='padding:0;padding-top:3px;vertical-align:middle'><img src='/images/explanation/P3_model_right_brace_small.png' /></td><td rowspan=3 style='padding:0;vertical-align:middle'>&nbsp;%d</td></tr>"%(firstDay,self.color1,number1+number2)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td></tr>"
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td><td colspan=2 style='background-color:%s;height:25px;border:white solid 1px;'>&nbsp;</td></tr>"%(secondDay,self.color2)
            self.solution_text = self.solution_text + "</table><br><br><br>"
            #end of model
            self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
            self.solution_text = self.solution_text + "%d &nbsp;&minus;&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number1+number2,number1,number2)
            self.solution_text = self.solution_text + "%s %d %s on %s.<br><br>"%(item2,number2,item1,secondDay)
            self.solution_text = self.solution_text + "%d &nbsp;&minus;&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number2,number1,answer)
            self.solution_text = self.solution_text + "%s %d fewer %s on %s than on %s."%(item2,answer,item1,firstDay,secondDay)
            self.solution_text = self.solution_text + "</font>" 

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType7(self):       
        '''e.g.:
        <A primary school has> 2658 <pupils>.
        <A secondary school has> 300 <more / fewer> <pupils than the primary school>.
        What is the total number of <pupils in the two schools>?'''

        self.complexity_level = "easy"
        self.HCScore = 3

        self.name = random.choice(PersonName.UncleName)
        
        self.items = [['A primary school has','pupils','A secondary school has','pupils than the primary school','pupils in the two schools','The secondary school has','primary school','secondary school'],
                      ['Town A has','residents','Town B has','residents than Town A','residents in the two towns','Town B has','Town A','Town B'],
                      ['A clothes company employs','workers','A shoes company employs','workers than the clothes company','workers employed by the two companies','The shoes company employs','clothes company','shoes company'],
                      ['Tank A has','fishes','Tank B has','fishes than Tank A','fishes in the two tanks','Tank B has','Tank A','Tank B'],
                      ['Park A has','trees','Park B has','trees than Park A','trees in the two parks','Park B has','Park A','Park B'],
                      ['Wildlife Sanctuary A has','animals','Wildlife Sanctuary B has','animals than Wildlife Sanctuary A','animals at the two wildlife sanctuaries','Wildlife Sanctuary B has','Santuary A','Sanctuary B'],
                      ['College A enrols','students','College B enrols','students than College A','students enrolled by the two colleges','College B enrols','College A','College B'],
                      ['A school library carries','books','A public library carries','books than the school library','books carried by the two libraries','The public library carries','school library','public library'],
                      ['Warehouse A stores','computers','Warehouse B stores','computers than Warehouse A','computers in the two warehouses','Warehouse B stores','Warehouse A','Warehouse B'],
                      ['Store A sold','toys','Store B sold','toys than Store A','toys sold by the two stores','Store B sold','Store A','Store B'],
                      ['Store A sold','cans of milk','Store B sold','cans of milk than Store A','cans of milk sold by the two stores','Store B sold','Store A','Store B'],
                      ['Farmer A has','hens','Farmer B has','hens than Farmer A','hens that the two farmers have','Farmer B has','Farmer A','Farmer B'],
                      ['Bakery A sold','muffins','Bakery B sold','muffins than Bakery A','muffins sold by the two bakeries','Bakery B sold','Bakery A','Bakery B'],
                      ['Ship A has','passengers','Ship B has','passengers than Ship A','passengers on the two ships','Ship B has','Ship A','Ship B']]
                
        self.item = random.choice(self.items)

        self.number1 = randint(2000,3000)
        self.number2 = randint(2000,3000)
        
        self.diff = abs(self.number1 - self.number2)
        
        while self.number1 == self.number2:
            self.number2 = randint(2000,3000)
        
        self.problem = "%s %d %s.<br><br>"%(self.item[0],self.number1,self.item[1])
        if self.number1 > self.number2:
            self.problem = self.problem + "%s %d fewer %s.<br><br>"%(self.item[2],self.diff,self.item[3])
        else:
            self.problem = self.problem + "%s %d more %s.<br><br>"%(self.item[2],self.diff,self.item[3])
        
        self.problem = self.problem + "What is the total number of %s?"%(self.item[4])   
        
        self.answer = self.number1+self.number2

        self.unit = self.item[1]
        self.dollar_unit = ""
          
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7(self.problem,self.answer,self.number1,self.number2,self.diff,self.item[1],self.item[4],self.item[5],self.item[6],self.item[7],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType7",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,
                'unit':self.unit,'dollar_unit':self.dollar_unit}

    def ExplainType7(self,problem,answer,number1,number2,diff,item1,item4,item5,item6,item7,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        self.colors = random.choice([['tomato','orange'],['blueviolet','violet'],['purple','plum'],['darkturquoise','dodgerblue'],['mediumorchid','mediumpurple'],['chocolate','burlywood'],['deeppink','lightpink']])
        self.color1 = self.colors[0]
        self.color2 = self.colors[1]

        if number1>number2:
            #beginning of model
            if number2>=diff:
                firstCellWidth = 100
                secondBrace = 'small'
            else:
                firstCellWidth = 50
                secondBrace = 'medium'
            self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2>%d</td></tr>"%(number1)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_large.png' /></td></tr>"
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td><td colspan=2 style='background-color:%s;height:25px;border:white solid 1px;'>&nbsp;</td><td>&nbsp;&nbsp;</td><td rowspan=3 style='padding:0;padding-top:3px;vertical-align:middle'><img src='/images/explanation/P3_model_right_brace_small.png' /></td><td rowspan=3 style='padding:0;vertical-align:middle'>&nbsp;?</td></tr>"%(item6,self.color2)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td></tr>"
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;width:%dpx'>&nbsp;</td><td>&nbsp;</td></tr>"%(item7,self.color1,firstCellWidth)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(secondBrace)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>&nbsp;</td><td>%d</td></tr>"%(diff)
            self.solution_text = self.solution_text + "</table><br><br>"
            #end of model
            self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
            self.solution_text = self.solution_text + "%d &nbsp;&minus;&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number1,diff,number2)
        else:
            #beginning of model
            if number1>=diff:
                firstBrace = 'medium'
                secondBrace = 'small'
            else:
                firstBrace = 'small'
                secondBrace = 'medium'
            self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>%d</td><td>%d</td></tr>"%(number1,diff)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(firstBrace,secondBrace)
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;'>&nbsp;</td><td>&nbsp;</td><td>&nbsp;&nbsp;</td><td rowspan=3 style='padding:0;padding-top:3px;vertical-align:middle'><img src='/images/explanation/P3_model_right_brace_small.png' /></td><td rowspan=3 style='padding:0;vertical-align:middle'>&nbsp;?</td></tr>"%(item6,self.color1)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td></tr>"
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td><td colspan=2 style='background-color:%s;height:25px;border:white solid 1px;'>&nbsp;</td></tr>"%(item7,self.color2)
            self.solution_text = self.solution_text + "</table><br><br><br>"
            #end of model
            self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
            self.solution_text = self.solution_text + "%d &nbsp;+&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number1,diff,number2)

        self.solution_text = self.solution_text + "%s %d %s.<br><br>"%(item5,number2,item1)
        
        self.solution_text = self.solution_text + "%d &nbsp;+&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number1,number2,answer)
        self.solution_text = self.solution_text + "The total number of %s is %d."%(item4,answer)
        self.solution_text = self.solution_text + "</font>" 

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType8(self):       
        '''e.g.:
        [Person.Unclename] <had> $1234< at first>.
        He <spent> $675 <on some furniture. He then received a salary of> $2345 <>.
        how much money <has he> now?'''

        self.complexity_level = "easy"
        self.HCScore = 3

        self.name = random.choice(PersonName.UncleName)
        
        self.items = [['had',' at first','spent','on some furniture.<br><br>He then received a salary of','','had he','after spending','on the furniture','','spent'],
                      ['had',' at first','used','of it to buy books.<br><br>Later, he received a gift of','from his grandmother','had he','after spending','on the books','','used'],
                      ['had',' at first','gave','to his daughter and received','from his aunt','had he','after giving','to his daughter','','gave'],
                      ['had',' in his savings account','withdrew','from it and later deposited','in it','did he have in his savings account','in his savings account after withdrawing','from it',' in his savings account','withdrew'],
                      ['had',' with him','bought some goods for','and later received a bonus of','from his employer','had he','after spending','on the goods','','spent'],
                      ['won',' in a game','gave','of his winnings to his mother.<br><br>Later, he got a salary of','','had he','after giving','to his mother','','gave'],
                      ['sold his wares and earned','','used','of it to buy presents for his family.<br><br>Later, he won','in a lottery','had he','after spending','on presents','','used'],
                      ['had',' at first','donated','of it to a charity.<br><br>Later, he held a yard sale and earned','','had he','after donating','to the charity','','donated'],
                      ['had',' at first','used','of it to buy books for his school.<br><br>Later, he received a donation of','from his neighbours','had he','after using','to buy books','','used'],
                      ['had',' at first','spent','of it on air tickets.<br><br>He then received an income of','','had he','after spending','on the air tickets','','spent']]
   
        self.item = random.choice(self.items)
        
        self.name = random.choice(PersonName.UncleName)
        
        self.number1 = randint(1000,2000)
        self.number2 = randint(300,800)
        self.number3 = randint(2500,4000)
        
        self.problem = "%s %s $%d %s.<br><br>"%(self.name,self.item[0],self.number1,self.item[1])
        self.problem = self.problem + "He %s $%d %s $%d %s.<br><br>"%(self.item[2],self.number2,self.item[3],self.number3,self.item[4])
        self.problem = self.problem + "How much money %s in the end?"%(self.item[5])
        
        self.answer = self.number1-self.number2+self.number3

        self.unit = ""
        self.dollar_unit = "$"
          
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType8(self.problem,self.answer,self.number1,self.number2,self.number3,self.item[6],self.item[7],self.item[8],self.item[9],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType8",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,
                'unit':self.unit,'dollar_unit':self.dollar_unit}

    def ExplainType8(self,problem,answer,number1,number2,number3,item6,item7,item8,item9,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        self.colors = random.choice([['tomato','orange'],['blueviolet','violet'],['purple','plum'],['darkturquoise','dodgerblue'],['mediumorchid','mediumpurple'],['chocolate','burlywood'],['deeppink','lightpink']])
        self.color1 = self.colors[0]
        self.color2 = self.colors[1]
        
        #beginning of model 1
        if number1-number2>=number2:
            topBrace = 'large'
            firstCellWidth = 100
            secondCellWidth = 50
            thirdCellWidth = 150
            firstBrace = 'medium'
            secondBrace = 'small'
            upBrace = 'large1small1'
            bottomBrace = 'large1medium1small1'
        else:
            topBrace = 'large'
            firstCellWidth = 50
            secondCellWidth = 100
            thirdCellWidth = 150
            firstBrace = 'small'
            secondBrace = 'medium'
            upBrace = 'large1medium1'
            bottomBrace = 'large1medium1small1'
            
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td colspan=2>$%d</td></tr>"%(number1)
        self.solution_text = self.solution_text + "<tr><td colspan=2 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(topBrace)
        self.solution_text = self.solution_text + "<tr><td style='background-color:%s;height:25px;border:white solid 1px;width:%dpx;'>&nbsp;</td><td style='height:25px;border:white solid 1px;width:%dpx'><font style='font-size:0.75em'>%s</font></td></tr>"%(self.color1,firstCellWidth,secondCellWidth,item9)
        self.solution_text = self.solution_text + "<tr><td><img src='/images/explanation/P3_model_down_brace_%s.png' /></td><td><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(firstBrace,secondBrace)
        self.solution_text = self.solution_text + "<tr><td style='padding-bottom:10px'>? (a)</td><td style='padding-bottom:10px'>$%d</td></tr>"%(number2)
        self.solution_text = self.solution_text + "</table><br>"
        #end of model 1

        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "$%d &nbsp;&minus;&nbsp; $%d &nbsp;=&nbsp; $%d &nbsp;&nbsp; (a)<br>"%(number1,number2,number1-number2)
        self.solution_text = self.solution_text + "He had $%d left %s $%d %s.<br><br>"%(number1-number2,item6,number2,item7)
        self.solution_text = self.solution_text + "</font>"
        
        # beginning of model 2
        self.solution_text = self.solution_text + "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>$%d</td><td>$%d</td></tr>"%(number1-number2,number3)
        self.solution_text = self.solution_text + "<tr><td style='padding-bottom:2px'><img src='/images/explanation/P3_model_up_brace_%s.png' /><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(firstBrace,upBrace)
        self.solution_text = self.solution_text + "<tr><td style='background-color:%s;height:25px;border:white solid 1px;width:%dpx;'>&nbsp;</td><td style='background-color:%s;height:25px;border:white solid 1px;width:%dpx'>&nbsp;</td></tr>"%(self.color1,firstCellWidth,self.color2,secondCellWidth+thirdCellWidth)
        self.solution_text = self.solution_text + "<tr><td colspan=2><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(bottomBrace)
        self.solution_text = self.solution_text + "<tr><td colspan=2>?</td></tr>"
        self.solution_text = self.solution_text + "</table><br>"
        #end of model 2

        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "$%d &nbsp;+&nbsp; $%d &nbsp;=&nbsp; $%d<br>"%(number1-number2,number3,answer)
        self.solution_text = self.solution_text + "He had $%d%s in the end."%(answer,item8)
        self.solution_text = self.solution_text + "</font>" 

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType9(self):       
        '''e.g.:
        <There were> 4567 <spectators in the stadium> at first.
        <>2345 <of them left the stadium and> 3456 <more spectators came into the stadium>.
        How many <spectators are there in the stadium> now?'''

        self.complexity_level = "easy"
        self.HCScore = 3

        self.name = random.choice(PersonName.UncleName)
        
        self.items = [['There were','spectators in the stadium','','of them left the stadium and','more spectators came into the stadium','spectators were there in the stadium','After','spectators left the stadium, there were','spectators left in the stadium','There were','spectators in the stadium','spectators','left'],
                      ['There were','travellers at the airport','','of them left the airport and','more travellers came to the airport','travellers were there at the airport','After','travellers left the airport, there were','travellers left at the airport','There were','travellers at the airport','travellers','left'],
                      ['There were','passengers on the train','','of them got off the train and','more passengers boarded the train','passengers were there on the train','After','passengers got off the train, there were','passengers left on the train','There were','passengers on the train','passengers','got off'],
                      ['There were','children in the school hall','','of them left to see a basketball game and','more children came to the school hall','children were there in the school hall','After','children left to see the basketball game, there were','children left in the school hall','There were','children in the school hall','children','left'],
                      ['There were','workers in a factory','','of them left after completing their work and','more workers came to the factory','workers were there in the factory','After','workers left the factory, there were','workers left in the factory','There were','workers in the factory','workers','left'],
                      ['A fruiterer had','peaches','He sold ','of them and bought','more peaches from a supplier','peaches did he have','After selling','peaches, he had','peaches left','He had','peaches','peaches','sold'],
                      ['A baker baked','tarts','He sold ','of them and baked','more tarts','tarts did he have','After selling','tarts, he had','tarts left','He had','tarts','tarts','sold'],
                      ['A girl had','stamps','She gave away ','of them and bought','more stamps','stamps did she have','After giving away','stamps, she had','stamps left','She had','stamps','stamps','gave away'],
                      ['A boy had','marbles','He lost ','of them in a game and then bought','more marbles','marbles did he have','After losing','marbles, he had','marbles left','He had','marbles','marbles','lost'],
                      ['A bookstore had','magazines','It sold ','of them and then purchased','more magazines from a supplier','magazines did it have','After selling','magazines, it had','magazines left','It had','magazines','magazines','sold']]
   
        self.item = random.choice(self.items)
        
        self.number1 = randint(5000,6000)
        self.number2 = randint(3500,4500)
        self.number3 = randint(2000,3000)
        
        self.problem = "%s %d %s at first.<br><br>"%(self.item[0],self.number1,self.item[1])
        self.problem = self.problem + "%s%d %s %d %s.<br><br>"%(self.item[2],self.number2,self.item[3],self.number3,self.item[4])
        self.problem = self.problem + "How many %s in the end?"%(self.item[5])
        
        self.answer = self.number1-self.number2+self.number3

        self.unit = self.item[11]
        self.dollar_unit = ""
          
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType9(self.problem,self.answer,self.number1,self.number2,self.number3,self.item[6],self.item[7],self.item[8],self.item[9],self.item[10],self.item[12],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType9",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,
                'unit':self.unit,'dollar_unit':self.dollar_unit}

    def ExplainType9(self,problem,answer,number1,number2,number3,item6,item7,item8,item9,item10,item12,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        self.colors = random.choice([['tomato','orange'],['blueviolet','violet'],['purple','plum'],['darkturquoise','dodgerblue'],['mediumorchid','mediumpurple'],['chocolate','burlywood'],['deeppink','lightpink']])
        self.color1 = self.colors[0]
        self.color2 = self.colors[1]
        
        #beginning of model 1
        if number1-number2>=number3:
            topBrace = 'large1medium1'
            firstCellBrace = 'medium'
            firstCellWidth = 96
            secondCellWidth = 144
            thirdCellWidth = 48
            upBrace = 'small'
            bottomBrace = 'medium1small1'
        else:
            topBrace = 'large1small1'
            firstCellBrace = 'small'
            firstCellWidth = 48
            secondCellWidth = 144
            thirdCellWidth = 96
            upBrace = 'medium'
            bottomBrace = 'medium1small1'

        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td colspan=2>%d</td></tr>"%(number1)
        self.solution_text = self.solution_text + "<tr><td colspan=2 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(topBrace)
        self.solution_text = self.solution_text + "<tr><td style='background-color:%s;height:25px;border:white solid 1px;width:%dpx;'>&nbsp;</td><td style='height:25px;border:white solid 1px;width:%dpx'><font style='font-size:0.75em'>%s</font></td></tr>"%(self.color1,firstCellWidth,secondCellWidth,item12)
        self.solution_text = self.solution_text + "<tr><td><img src='/images/explanation/P3_model_down_brace_%s.png' /></td><td><img src='/images/explanation/P3_model_down_brace_large.png' /></td></tr>"%(firstCellBrace)
        self.solution_text = self.solution_text + "<tr><td>? (a)</td><td>%d</td></tr>"%(number2)
        self.solution_text = self.solution_text + "</table><br><br>"
        #end of model 1

        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "%d &nbsp;&minus;&nbsp; %d &nbsp;=&nbsp; %d &nbsp;&nbsp; (a)<br>"%(number1,number2,number1-number2)
        self.solution_text = self.solution_text + "%s %d %s %d %s.<br><br>"%(item6,number2,item7,number1-number2,item8)
        self.solution_text = self.solution_text + "</font>"

        #beginning of model 2
        self.solution_text = self.solution_text + "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>%d</td><td>%d</td></tr>"%(number1-number2,number3)
        self.solution_text = self.solution_text + "<tr><td style='padding-bottom:2px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(firstCellBrace,upBrace)
        self.solution_text = self.solution_text + "<tr><td style='background-color:%s;height:25px;border:white solid 1px;width:%dpx;'>&nbsp;</td><td style='background-color:%s;height:25px;border:white solid 1px;width:%dpx'>&nbsp;</td><td>&nbsp;</td></tr>"%(self.color1,firstCellWidth,self.color2,thirdCellWidth)
        self.solution_text = self.solution_text + "<tr><td colspan=2><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(bottomBrace)
        self.solution_text = self.solution_text + "<tr><td colspan=2>?</td></tr>"
        self.solution_text = self.solution_text + "</table><br>"
        #end of model 2
        
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "%d &nbsp;+&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number1-number2,number3,answer)
        self.solution_text = self.solution_text + "%s %d %s in the end."%(item9,answer,item10)
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType10(self):       
        '''e.g.:
        [Person.Boyname 1], [Person.Boyname 2] and [Person.Boyname 3] <have> 9456 <crayons> altogether.
        [Person.Boyname 1] <has> 5224 <crayons>.
        [Person.Boyname 2] <has> 2028 <crayons>.
        Find the number of <crayons> that [Person.Boyname 3] <has>.'''

        self.complexity_level = "easy"
        self.HCScore = 3

        self.name = random.choice(PersonName.UncleName)
        
        self.items = [['have','crayons','has'],['clicked','photos','clicked'],
                      ['collected','twigs','collected'],['collected','bird feathers','collected'],
                      ['have','popsicle sticks','has'],['bought','lollipops','bought'],
                      ['collected','pebbles','collected'],['have','postcards','has'],
                      ['collected','bottle caps','collected'],['picked','strawberries','picked'],
                      ['sold','glasses of lemonade','sold']]
   
        self.item = random.choice(self.items)
        
        self.names = random.sample(PersonName.BoyName,3)
        
        self.number1 = randint(1000,3000)
        self.number2 = randint(1000,3000)
        self.number3 = randint(1000,3000)
        
        self.total = self.number1 + self.number2 + self.number3
        
        self.problem = "%s, %s and %s %s %d %s altogether.<br><br>"%(self.names[0],self.names[1],self.names[2],self.item[0],self.total,self.item[1])
        self.problem = self.problem + "%s %s %d %s.<br><br>"%(self.names[0],self.item[2],self.number1,self.item[1])
        self.problem = self.problem + "%s %s %d %s.<br><br>"%(self.names[1],self.item[2],self.number2,self.item[1])
        self.problem = self.problem + "Find the number of %s that %s %s."%(self.item[1],self.names[2],self.item[2])
        
        self.answer = self.number3

        self.unit = self.item[1]
        self.dollar_unit = ""
          
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType10(self.problem,self.answer,self.names,self.number1,self.number2,self.item[0],self.item[1],self.item[2],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType10",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,
                'unit':self.unit,'dollar_unit':self.dollar_unit}

    def ExplainType10(self,problem,answer,names,number1,number2,item0,item1,item2,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        #beginning of model
        if number1==number2:
            firstBrace = 'medium'
            secondBrace = 'medium'
            if number1==answer:
                thirdBrace = 'medium'
                totalBrace = 'medium3'
            elif number1>answer:
                thirdBrace = 'small'
                totalBrace = 'medium2small1'
            else:
                thirdBrace = 'large'
                totalBrace = 'large1medium2'
        elif number1>number2:
            if answer<number2:
                firstBrace = 'large'
                secondBrace = 'medium'
                thirdBrace = 'small'
                totalBrace = 'large1medium1small1'
            elif answer<number1 and answer>number2:
                firstBrace = 'large'
                secondBrace = 'small'
                thirdBrace = 'medium'
                totalBrace = 'large1medium1small1'
            elif answer>number1:
                firstBrace = 'medium'
                secondBrace = 'small'
                thirdBrace = 'large'
                totalBrace = 'large1medium1small1'
            elif answer==number2:
                firstBrace = 'large'
                secondBrace = 'medium'
                thirdBrace = 'medium'
                totalBrace = 'large1medium2'
            elif answer==number1:
                firstBrace = 'medium'
                secondBrace = 'small'
                thirdBrace = 'medium'
                totalBrace = 'medium2small1'
        elif number1<number2:
            if answer>number2:
                firstBrace = 'small'
                secondBrace = 'medium'
                thirdBrace = 'large'
                totalBrace = 'large1medium1small1'
            elif answer<number2 and answer>number1:
                firstBrace = 'small'
                secondBrace = 'large'
                thirdBrace = 'medium'
                totalBrace = 'large1medium1small1'
            elif answer<number1:
                firstBrace = 'medium'
                secondBrace = 'large'
                thirdBrace = 'small'
                totalBrace = 'large1medium1small1'
            elif answer==number2:
                firstBrace = 'small'
                secondBrace = 'medium'
                thirdBrace = 'medium'
                totalBrace = 'medium2small1'
            elif answer==number1:
                firstBrace = 'medium'
                secondBrace = 'large'
                thirdBrace = 'medium'
                totalBrace = 'large1medium2'

        self.colors = random.choice([['tomato','orange','peru'],['blueviolet','violet','darkorchid'],['purple','plum','mediumvioletred'],['darkturquoise','dodgerblue','darkslateblue'],['mediumorchid','mediumpurple','palevioletred'],['chocolate','burlywood','brown'],['deeppink','lightpink','hotpink']])
        self.color1 = self.colors[0]
        self.color2 = self.colors[1]
        self.color3 = self.colors[2]
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0'>"
        self.solution_text = self.solution_text + "<tr><td colspan=3>%d</td></tr>"%(number1+number2+answer)
        self.solution_text = self.solution_text + "<tr><td colspan=3 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(totalBrace)
        self.solution_text = self.solution_text + "<tr><td style='background-color:%s;height:25px;border:white solid 1px;'><font style='font-size:0.75em;white-space:nowrap;'>%s</font></td><td style='background-color:%s;border:white solid 1px;white-space:nowrap;'><font style='font-size:0.75em'>%s</font></td><td style='background-color:%s;border:white solid 1px;white-space:nowrap;'><font style='font-size:0.75em'>%s</font></td></tr>"%(self.color1,names[0],self.color2,names[1],self.color3,names[2])
        self.solution_text = self.solution_text + "<tr><td><img src='/images/explanation/P3_model_down_brace_%s.png' /></td><td><img src='/images/explanation/P3_model_down_brace_%s.png' /></td><td><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(firstBrace,secondBrace,thirdBrace)
        self.solution_text = self.solution_text + "<tr><td>%d</td><td>%d</td><td>?</td></tr>"%(number1,number2)
        self.solution_text = self.solution_text + "</table><br><br>"
        #end of model

        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "%d &nbsp;+&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number1,number2,number1+number2)
        self.solution_text = self.solution_text + "%s and %s %s %d %s altogether.<br><br>"%(names[0],names[1],item0,number1+number2,item1)
        
        self.solution_text = self.solution_text + "%d &nbsp;&minus;&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number1+number2+answer,number1+number2,answer)
        self.solution_text = self.solution_text + "%s %s %d %s."%(names[2],item2,answer,item1)
        self.solution_text = self.solution_text + "</font>" 

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType11(self):       
        '''e.g.:
        <A vegetable grocer sold> 6904 <cabbages>, <tomatoes> and <carrots> altogether.
        If <he sold> 2045 <potatoes> and 1234 <tomatoes>, how many <onions> did <he sell>?'''

        self.complexity_level = "easy"
        self.HCScore = 3

        self.name = random.choice(PersonName.UncleName)
        
        self.items = [['A vegetable grocer sold','cucumbers','tomatoes','carrots','he sold','he sell','He sold'],
                      ['A fruit vendor had','peaches','kiwifruits','oranges','he had','he have','He had'],
                      ['A farmer had','hens','ducks','geese','he had','he have','He had'],
                      ['A convenience store sold','phone cards','lollipops','milk cartons','it sold','it sell','It sold'],
                      ['A post office sold','envelopes','stamps','postcards','it sold','it sell','It sold'],
                      ['A flower shop had','sunflowers','lilies','tulips','it had','it have','It had'],
                      ['An amusement park received','adults','girls','boys','it received','it receive','It received'],
                      ['A library carried','books','magazines','DVDs','it carried','it carry','It carried'],
                      ['A baker baked','pies','cakes','cookies','he baked','he bake','He baked'],
                      ['A fast food shop sold','sandwiches','salad bowls','burgers','it sold','it sell','It sold']]
   
        self.item = random.choice(self.items)
        
        self.number1 = randint(1000,3000)
        self.number2 = randint(1000,3000)
        self.number3 = randint(1000,3000)
        
        self.total = self.number1 + self.number2 + self.number3
        
        self.problem = "%s %d %s, %s and %s altogether.<br><br>"%(self.item[0],self.total,self.item[1],self.item[2],self.item[3])
        self.problem = self.problem + "If %s %d %s and %d %s, how many %s did %s?"%(self.item[4],self.number1,self.item[1],self.number2,self.item[2],self.item[3],self.item[5])
        
        self.answer = self.number3

        self.unit = self.item[3]
        self.dollar_unit = ""
          
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType11(self.problem,self.answer,self.number1,self.number2,self.item[1],self.item[2],self.item[3],self.item[6],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType11",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,
                'unit':self.unit,'dollar_unit':self.dollar_unit}

    def ExplainType11(self,problem,answer,number1,number2,item1,item2,item3,item6,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        #beginning of model
        if number1==number2:
            firstBrace = 'medium'
            secondBrace = 'medium'
            if number1==answer:
                thirdBrace = 'medium'
                totalBrace = 'medium3'
            elif number1>answer:
                thirdBrace = 'small'
                totalBrace = 'medium2small1'
            else:
                thirdBrace = 'large'
                totalBrace = 'large1medium2'
        elif number1>number2:
            if answer<number2:
                firstBrace = 'large'
                secondBrace = 'medium'
                thirdBrace = 'small'
                totalBrace = 'large1medium1small1'
            elif answer<number1 and answer>number2:
                firstBrace = 'large'
                secondBrace = 'small'
                thirdBrace = 'medium'
                totalBrace = 'large1medium1small1'
            elif answer>number1:
                firstBrace = 'medium'
                secondBrace = 'small'
                thirdBrace = 'large'
                totalBrace = 'large1medium1small1'
            elif answer==number2:
                firstBrace = 'large'
                secondBrace = 'medium'
                thirdBrace = 'medium'
                totalBrace = 'large1medium2'
            elif answer==number1:
                firstBrace = 'medium'
                secondBrace = 'small'
                thirdBrace = 'medium'
                totalBrace = 'medium2small1'
        elif number1<number2:
            if answer>number2:
                firstBrace = 'small'
                secondBrace = 'medium'
                thirdBrace = 'large'
                totalBrace = 'large1medium1small1'
            elif answer<number2 and answer>number1:
                firstBrace = 'small'
                secondBrace = 'large'
                thirdBrace = 'medium'
                totalBrace = 'large1medium1small1'
            elif answer<number1:
                firstBrace = 'medium'
                secondBrace = 'large'
                thirdBrace = 'small'
                totalBrace = 'large1medium1small1'
            elif answer==number2:
                firstBrace = 'small'
                secondBrace = 'medium'
                thirdBrace = 'medium'
                totalBrace = 'medium2small1'
            elif answer==number1:
                firstBrace = 'medium'
                secondBrace = 'large'
                thirdBrace = 'medium'
                totalBrace = 'large1medium2'

        self.colors = random.choice([['tomato','orange','peru'],['blueviolet','violet','darkorchid'],['purple','plum','mediumvioletred'],['darkturquoise','dodgerblue','darkslateblue'],['mediumorchid','mediumpurple','palevioletred'],['chocolate','burlywood','brown'],['deeppink','lightpink','hotpink']])
        self.color1 = self.colors[0]
        self.color2 = self.colors[1]
        self.color3 = self.colors[2]
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0'>"
        self.solution_text = self.solution_text + "<tr><td colspan=3>%d</td></tr>"%(number1+number2+answer)
        self.solution_text = self.solution_text + "<tr><td colspan=3 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(totalBrace)
        self.solution_text = self.solution_text + "<tr><td style='background-color:%s;height:25px;border:white solid 1px;'><font style='font-size:0.75em'>%s</font></td><td style='background-color:%s;border:white solid 1px;'><font style='font-size:0.75em'>%s</font></td><td style='background-color:%s;border:white solid 1px;'><font style='font-size:0.75em'>%s</font></td></tr>"%(self.color1,item1,self.color2,item2,self.color3,item3)
        self.solution_text = self.solution_text + "<tr><td><img src='/images/explanation/P3_model_down_brace_%s.png' /></td><td><img src='/images/explanation/P3_model_down_brace_%s.png' /></td><td><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(firstBrace,secondBrace,thirdBrace)
        self.solution_text = self.solution_text + "<tr><td>%d</td><td>%d</td><td>?</td></tr>"%(number1,number2)
        self.solution_text = self.solution_text + "</table><br><br>"
        #end of model

        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "%d &nbsp;+&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number1,number2,number1+number2)
        self.solution_text = self.solution_text + "%s %d %s and %s altogether.<br><br>"%(item6,number1+number2,item1,item2)
        
        self.solution_text = self.solution_text + "%d &nbsp;&minus;&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number1+number2+answer,number1+number2,answer)
        self.solution_text = self.solution_text + "%s %d %s."%(item6,answer,item3)
        self.solution_text = self.solution_text + "</font>" 

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType12(self):       
        '''e.g.:
        There are 6904 <onions and potatoes in a grocery store>.
        There are 3219 <onions>.
        The rest are either <white potatoes> or <red potatoes>.
        There are 1234 <white potatoes>.
        How many <red potatoes> are there?'''

        self.complexity_level = "easy"
        self.HCScore = 3

        self.name = random.choice(PersonName.UncleName)
        
        self.items = [['onions and potatoes in a grocery store','onions','white potatoes','red potatoes','potatoes','white','red'],
                      ['mandarins and watermelons in a fruit store','mandarins','red watermelons','yellow watermelons','watermelons','red','yellow'],
                      ['animals and birds on a farm','animals','chickens','ducks','birds','chickens','ducks'],
                      ['magazines and books in a bookshop','magazines','storybooks','course books','books','story','course'],
                      ['pens and pencils in a stationery shop','pens','mechanical pencils','colour pencils','pencils','mechanical','colour'],
                      ['postcards and envelopes in a post office','postcards','small envelopes','large envelopes','envelopes','small','large'],
                      ['sculptures and paintings in an art museum','sculptures','oil paintings','water paintings','paintings','oil','water'],
                      ['burgers and sandwiches in a canteen','burgers','vegetable sandwiches','tuna sandwiches','sandwiches','veg','tuna'],
                      ['pies and puffs in a bakery','pies','curry puffs','chicken puffs','puffs','curry','chicken'],
                      ['roses and orchids in a flower shop','roses','white orchids','pink orchids','orchids','white','pink']]
   
        self.item = random.choice(self.items)
        
        self.number1 = randint(1000,2000)
        self.number2 = randint(1000,2000)
        self.number3 = randint(2500,5000) #making number3 bigger than number1 and number2 just for ease of model-making
        
        self.total = self.number1 + self.number2 + self.number3
        
        self.problem = "There are %d %s.<br><br>"%(self.total,self.item[0])
        self.problem = self.problem + "There are %d %s. "%(self.number1,self.item[1])
        self.problem = self.problem + "The rest are either %s or %s.<br><br>"%(self.item[2],self.item[3])
        self.problem = self.problem + "There are %d %s. "%(self.number2,self.item[2])
        self.problem = self.problem + "Find the number of %s.<br>"%(self.item[3])

        self.answer = self.number3

        self.unit = self.item[3]
        self.dollar_unit = ""
          
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType12(self.problem,self.answer,self.number1,self.number2,self.item[1],self.item[3],self.item[4],self.item[5],self.item[6],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType12",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,
                'unit':self.unit,'dollar_unit':self.dollar_unit}

    def ExplainType12(self,problem,answer,number1,number2,item1,item3,item4,item5,item6,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        #beginning of model
        if number1<number2:
            firstCellBrace = 'small'
            secondCellBrace = 'medium'
            firstCellWidth = 48
            secondCellWidth = 48
            thirdCellWidth = 144
            firstCellColspan = 1
            secondCellColspan = 2
            answerCellColspan = 1
        elif number1>number2:
            firstCellBrace = 'medium'
            secondCellBrace = 'small'
            firstCellWidth = 48
            secondCellWidth = 48
            thirdCellWidth = 96
            firstCellColspan = 2
            secondCellColspan = 1
            answerCellColspan = 2
        else:
            firstCellBrace = 'medium'
            secondCellBrace = 'medium'
            firstCellWidth = 96
            secondCellWidth = 96
            thirdCellWidth = 144
            firstCellColspan = 1
            secondCellColspan = 1
            answerCellColspan = 1

        self.colors = random.choice([['tomato','orange','peru'],['blueviolet','violet','darkorchid'],['purple','plum','mediumvioletred'],['darkturquoise','dodgerblue','darkslateblue'],['mediumorchid','mediumpurple','palevioletred'],['chocolate','burlywood','brown'],['deeppink','lightpink','hotpink']])
        self.color1 = self.colors[0]
        self.color2 = self.colors[1]
        self.color3 = self.colors[2]
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d>%d</td></tr>"%(firstCellColspan,number1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(firstCellColspan,firstCellBrace)
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px;white-space:nowrap;'>%s</td><td colspan=%d style='background-color:%s;height:25px;border:white solid 1px;'>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td rowspan=3 style='padding:0;padding-top:3px;vertical-align:middle'><img src='/images/explanation/P3_model_right_brace_small.png' /></td><td rowspan=3 style='padding:0;vertical-align:middle'>&nbsp;%d</td></tr>"%(item1,firstCellColspan,self.color1,number1+number2+answer)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='width:%dpx;'>&nbsp;</td><td style='width:%dpx;'>&nbsp;</td><td style='width:%dpx;'>&nbsp;</td></tr>"%(firstCellWidth,secondCellWidth,thirdCellWidth)
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px;white-space:nowrap;'>%s</td><td colspan=%d style='background-color:%s;height:25px;border:white solid 1px;'><font style='font-size:0.75em'>%s</font></td><td colspan=%d style='background-color:%s;height:25px;border:white solid 1px;'><font style='font-size:0.75em'>%s</font></td></tr>"%(item4,secondCellColspan,self.color2,item5,answerCellColspan,self.color3,item6)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d><img src='/images/explanation/P3_model_down_brace_%s.png' /></td><td colspan=%d><img src='/images/explanation/P3_model_down_brace_large.png' /></td></tr>"%(secondCellColspan,secondCellBrace,answerCellColspan)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d>%d</td><td colspan=%d>?</td></tr>"%(secondCellColspan,number2,answerCellColspan)
        self.solution_text = self.solution_text + "</table><br><br>"
        #end of model

        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "%d &nbsp;&minus;&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number1+number2+answer,number1,number2+answer)
        self.solution_text = self.solution_text + "There are %d %s altogether.<br><br>"%(number2+answer,item4)
        
        self.solution_text = self.solution_text + "%d &nbsp;&minus;&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number2+answer,number2,answer)
        self.solution_text = self.solution_text + "There are %d %s."%(answer,item3)
        self.solution_text = self.solution_text + "</font>" 

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType13(self):       
        '''e.g.:
        [Person.Girlname1]'s <string> was 1452 cm long.
        [Person.Girlname2]'s <string> was 234 cm longer than [Person.Girlname1]'s <string>.
        [Person.Girlname2] used 675 cm of her <string>.
        How long was [Person.Girlname2]'s remaining <string>.'''

        self.complexity_level = "easy"
        self.HCScore = 3

        self.names = random.sample(PersonName.GirlName,2)
        
        self.items = ['string','lace','ribbon','rope','thread','wire','yarn','wool','twine','tape','fishing line']
           
        self.item = random.choice(self.items)
        
        self.number1 = randint(1000,2000)
        self.number2 = randint(200,600)
        self.number3 = randint(400,800)
        
        self.problem = "%s's %s was %d cm long.<br><br>"%(self.names[0],self.item,self.number1)
        self.problem = self.problem + "%s's %s was %d cm longer than %s's %s.<br><br>"%(self.names[1],self.item,self.number2,self.names[0],self.item)
        self.problem = self.problem + "%s used %d cm of her %s.<br><br>"%(self.names[1],self.number3,self.item)
        self.problem = self.problem + "What was the length of the remaining %s that %s had?"%(self.item,self.names[1])

        self.answer = self.number1 + self.number2 - self.number3

        self.unit = "cm"
        self.dollar_unit = ""
          
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType13(self.problem,self.answer,self.names,self.number1,self.number2,self.number3,self.item,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType13",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,
                'unit':self.unit,'dollar_unit':self.dollar_unit}

    def ExplainType13(self,problem,answer,names,number1,number2,number3,item,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        #beginning of model
        if number2>number3:
            number1Brace = 'large1small1'
            number2Brace = 'medium'
            usedBrace = 'small'
            leftBrace = 'large1medium1'
            usedWidth = 48
            leftWidth = 242
        elif number2==number3:
            number1Brace = 'large1medium1'
            number2Brace = 'medium'
            usedBrace = 'medium'
            leftBrace = 'large1medium1'
            usedWidth = 96
            leftWidth = 242
        else:
            number1Brace = 'large1medium1'
            number2Brace = 'small'
            usedBrace = 'medium'
            leftBrace = 'large1small1'
            usedWidth = 96
            leftWidth = 194

        self.colors = random.choice([['tomato','orange','peru'],['blueviolet','violet','darkorchid'],['purple','plum','mediumvioletred'],['darkturquoise','dodgerblue','darkslateblue'],['mediumorchid','mediumpurple','palevioletred'],['chocolate','burlywood','brown'],['deeppink','lightpink','hotpink']])
        self.color1 = self.colors[0]
        self.color2 = self.colors[1]
        self.color3 = self.colors[2]

        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2>%d cm</td><td>%d cm</td></tr>"%(number1,number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(number1Brace,number2Brace)
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td><td colspan=2 style='background-color:%s;height:25px;border:white solid 1px;'>&nbsp;</td><td>&nbsp;</td></tr>"%(names[0],self.color1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='width:%dpx;'>&nbsp;</td><td style='width:144px;'>&nbsp;</td><td style='width:%dpx;'>&nbsp;</td></tr>"%(usedWidth,leftWidth-144)
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;'><font style='font-size:0.8em;'>used</font></td><td colspan=2 style='background-color:%s;height:25px;border:white solid 1px;'><font style='font-size:0.8em;'>remaining</font></td></tr>"%(names[1],self.color2,self.color3)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td><img src='/images/explanation/P3_model_down_brace_%s.png' /></td><td colspan=2><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(usedBrace,leftBrace)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>%d cm</td><td colspan=2>?</td></tr>"%(number3)
        self.solution_text = self.solution_text + "</table><br><br>"
        #end of model
            
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "%d &nbsp;+&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number1,number2,number1+number2)
        self.solution_text = self.solution_text + "%s's %s was %d cm long at first.<br><br>"%(names[1],item,number1+number2)
        
        self.solution_text = self.solution_text + "%d &nbsp;&minus;&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number1+number2,number3,answer)
        self.solution_text = self.solution_text + "The length of %s's remaining %s was %d cm."%(names[1],item,answer)
        self.solution_text = self.solution_text + "</font>" 

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType14(self):       
        '''e.g.:
        [Person.Auntyname1] <has> $1234.
        [Person.Auntyname2] <has> $123 <less / more> than [Person.Auntyname1].
        How much will [Person.Auntyname2] have if she <spends> $234 <on some furniture>?'''

        self.complexity_level = "easy"
        self.HCScore = 3

        self.names = random.sample(PersonName.GirlName,2)
        
        self.items = [['has','spends','on some furniture','spends'],['has','buys some goods for','','spends'],
                      ['earns','gives away','to charity','gives'],['earns','pays','in bills','bills'],['wins','gives','to her son','gives'],
                      ['wins','donates','to charity','donates'],['receives','spends','on books','spends'],['receives','buys some jewellery for','','spends'],
                      ['saves','gives','to her mother','gives'],['saves','pays','for a dress','dress']]
           
        self.item = random.choice(self.items)
        
        self.names = random.sample(PersonName.AuntyName,2)
        
        self.number1 = randint(1000,2000)
        self.number2 = randint(200,500)
        self.number3 = randint(100,300)
        
        self.flag = randint(1,2)
        
        self.problem = "%s %s $%d.<br><br>"%(self.names[0],self.item[0],self.number1)
        if self.flag == 1:
            self.problem = self.problem + "%s %s $%d less than %s.<br><br>"%(self.names[1],self.item[0],self.number2,self.names[0])
            self.answer = self.number1 - self.number2 - self.number3
        else:
            self.problem = self.problem + "%s %s $%d more than %s.<br><br>"%(self.names[1],self.item[0],self.number2,self.names[0])
            self.answer = self.number1 + self.number2 - self.number3
        self.problem = self.problem + "How much money will %s have if she %s $%d %s?"%(self.names[1],self.item[1],self.number3,self.item[2])

        self.unit = ""
        self.dollar_unit = "$"
          
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType14(self.problem,self.answer,self.flag,self.names,self.number1,self.number2,self.number3,self.item[0],self.item[3],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType14",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,
                'unit':self.unit,'dollar_unit':self.dollar_unit}

    def ExplainType14(self,problem,answer,flag,names,number1,number2,number3,item0,item3,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        #beginning of model
        self.colors = random.choice([['tomato','orange','peru'],['blueviolet','violet','darkorchid'],['purple','plum','mediumvioletred'],['darkturquoise','dodgerblue','darkslateblue'],['mediumorchid','mediumpurple','palevioletred'],['chocolate','burlywood','brown'],['deeppink','lightpink','hotpink']])
        self.color1 = self.colors[0]
        self.color2 = self.colors[1]
        self.color3 = self.colors[2]

        if flag==1:
            if number2>number3:
                number1Brace = 'large1medium1small1'
                number2Brace = 'medium'
                usedBrace = 'small'
                leftBrace = 'large'
                number2Width = 96
                usedWidth = 48
                leftWidth = 144
            elif number2==number3:
                number1Brace = 'large1medium2'
                number2Brace = 'medium'
                usedBrace = 'medium'
                leftBrace = 'large'
                number2Width = 96
                usedWidth = 96
                leftWidth = 144
            else:
                number1Brace = 'large1medium1small1'
                number2Brace = 'small'
                usedBrace = 'medium'
                leftBrace = 'large'
                number2Width = 48
                usedWidth = 96
                leftWidth = 144
            self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=3>$%d</td></tr>"%(number1)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=3 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(number1Brace)
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td><td colspan=3 style='background-color:%s;height:25px;border:white solid 1px;'>&nbsp;</td></tr>"%(names[0],self.color1)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='width:%dpx;'>&nbsp;</td><td style='width:%dpx;'>&nbsp;</td><td style='width:%dpx;'>&nbsp;</td></tr>"%(leftWidth,usedWidth,number2Width)
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;'><font style='font-size:0.8em;'>left</font></td><td style='background-color:%s;height:25px;border:white solid 1px;'><font style='font-size:0.8em;'>%s</font></td><td>&nbsp;</td></tr>"%(names[1],self.color2,self.color3,item3)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td><img src='/images/explanation/P3_model_down_brace_%s.png' /></td><td><img src='/images/explanation/P3_model_down_brace_%s.png' /></td><td><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(leftBrace,usedBrace,number2Brace)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>?</td><td>$%d</td><td>$%d</td></tr>"%(number3,number2)
            self.solution_text = self.solution_text + "</table><br><br>"
        else:
            if number2>number3:
                number1Brace = 'large1small1'
                number2Brace = 'medium'
                usedBrace = 'small'
                leftBrace = 'large1medium1'
                usedWidth = 48
                leftWidth = 242
            elif number2==number3:
                number1Brace = 'large1medium1'
                number2Brace = 'medium'
                usedBrace = 'medium'
                leftBrace = 'large1medium1'
                usedWidth = 96
                leftWidth = 242
            else:
                number1Brace = 'large1medium1'
                number2Brace = 'small'
                usedBrace = 'medium'
                leftBrace = 'large1small1'
                usedWidth = 96
                leftWidth = 194
            self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2>$%d</td><td>$%d</td></tr>"%(number1,number2)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(number1Brace,number2Brace)
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td><td colspan=2 style='background-color:%s;height:25px;border:white solid 1px;'>&nbsp;</td><td>&nbsp;</td></tr>"%(names[0],self.color1)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='width:%dpx;'>&nbsp;</td><td style='width:144px;'>&nbsp;</td><td style='width:%dpx;'>&nbsp;</td></tr>"%(usedWidth,leftWidth-144)
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;'><font style='font-size:0.8em;'>%s</font></td><td colspan=2 style='background-color:%s;height:25px;border:white solid 1px;'><font style='font-size:0.8em;'>left</font></td></tr>"%(names[1],self.color2,item3,self.color3)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td><img src='/images/explanation/P3_model_down_brace_%s.png' /></td><td colspan=2><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(usedBrace,leftBrace)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$%d</td><td colspan=2>?</td></tr>"%(number3)
            self.solution_text = self.solution_text + "</table><br><br>"
            #end of model

        intermediateAnswer = 0
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        if flag==1:
            self.solution_text = self.solution_text + "$%d &nbsp;&minus;&nbsp; $%d &nbsp;=&nbsp; $%d<br>"%(number1,number2,number1-number2)
            self.solution_text = self.solution_text + "%s %s $%d.<br><br>"%(names[1],item0,number1-number2)
            intermediateAnswer = number1-number2
        else:
            self.solution_text = self.solution_text + "$%d &nbsp;+&nbsp; $%d &nbsp;=&nbsp; $%d<br>"%(number1,number2,number1+number2)
            self.solution_text = self.solution_text + "%s %s $%d.<br><br>"%(names[1],item0,number1+number2)
            intermediateAnswer = number1+number2
        self.solution_text = self.solution_text + "$%d &nbsp;&minus;&nbsp; $%d &nbsp;=&nbsp; $%d<br>"%(intermediateAnswer,number3,answer)
        self.solution_text = self.solution_text + "%s will have $%d."%(names[1],answer)
        self.solution_text = self.solution_text + "</font>" 

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType15(self):       
        '''e.g.:
        [Person.Unclename]'s <factory weaves> 5267 <mats>.
        His <factory weaves> 567 <more / fewer> <mats> than [Person.Auntyname]'s <factory>.
        If [Person.Auntyname] sells 2345 <mats>, how many <mats> does she have left?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.items = [['factory weaves','mats','factory'],['factory weaves','carpets','factory'],
                      ['factory makes','shirts','factory'],['factory makes','chairs','factory'],
                      ['factory makes','schoolbags','factory'],['farm has','turkeys','farm'],
                      ['farm has','goats','farm'],['egg farm has','eggs','egg farm'],
                      ['bird farm has','birds','bird farm'],['shop has','toys','shop'],
                      ['family makes','bags','family'],['family makes','flower vases','family'],
                      ['family makes','bracelets','family'],['family bakes','butter cookies','family'],
                      ['family bakes','brownies','family']]
           
        self.item = random.choice(self.items)
        
        self.names = [random.choice(PersonName.UncleName),random.choice(PersonName.AuntyName)]
        
        self.number1 = randint(4000,6000)
        self.number2 = randint(400,900)
        self.number3 = randint(1000,3000)
        
        self.flag = randint(1,2)
        
        self.problem = "%s's %s %d %s.<br><br>"%(self.names[0],self.item[0],self.number1,self.item[1])
        if self.flag == 1:
            self.problem = self.problem + "His %s %d fewer %s than %s's %s.<br><br>"%(self.item[0],self.number2,self.item[1],self.names[1],self.item[2])
            self.answer = self.number1 + self.number2 - self.number3
        else:
            self.problem = self.problem + "His %s %d more %s than %s's %s.<br><br>"%(self.item[0],self.number2,self.item[1],self.names[1],self.item[2])
            self.answer = self.number1 - self.number2 - self.number3
        self.problem = self.problem + "If %s sells %d %s, how many %s does she have left?"%(self.names[1],self.number3,self.item[1],self.item[1])

        self.unit = self.item[1]
        self.dollar_unit = ""
          
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType15(self.problem,self.answer,self.flag,self.names,self.number1,self.number2,self.number3,self.item[0],self.item[1],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType15",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,
                'unit':self.unit,'dollar_unit':self.dollar_unit}

    def ExplainType15(self,problem,answer,flag,names,number1,number2,number3,item0,item1,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        #beginning of model
        self.colors = random.choice([['tomato','orange','peru'],['blueviolet','violet','darkorchid'],['purple','plum','mediumvioletred'],['darkturquoise','dodgerblue','darkslateblue'],['mediumorchid','mediumpurple','palevioletred'],['chocolate','burlywood','brown'],['deeppink','lightpink','hotpink']])
        self.color1 = self.colors[0]
        self.color2 = self.colors[1]
        self.color3 = self.colors[2]

        if flag==1:
            if number2>number3:
                number1Brace = 'large1small1'
                number2Brace = 'medium'
                usedBrace = 'small'
                leftBrace = 'large1medium1'
                usedWidth = 48
                leftWidth = 242
            elif number2==number3:
                number1Brace = 'large1medium1'
                number2Brace = 'medium'
                usedBrace = 'medium'
                leftBrace = 'large1medium1'
                usedWidth = 96
                leftWidth = 242
            else:
                number1Brace = 'large1medium1'
                number2Brace = 'small'
                usedBrace = 'medium'
                leftBrace = 'large1small1'
                usedWidth = 96
                leftWidth = 194
            self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2>%d</td><td>%d</td></tr>"%(number1,number2)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(number1Brace,number2Brace)
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td><td colspan=2 style='background-color:%s;height:25px;border:white solid 1px;'>&nbsp;</td><td>&nbsp;</td></tr>"%(names[0],self.color1)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='width:%dpx;'>&nbsp;</td><td style='width:144px;'>&nbsp;</td><td style='width:%dpx;'>&nbsp;</td></tr>"%(usedWidth,leftWidth-144)
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;'><font style='font-size:0.8em;'>sells</font></td><td colspan=2 style='background-color:%s;height:25px;border:white solid 1px;'><font style='font-size:0.8em;'>left</font></td></tr>"%(names[1],self.color2,self.color3)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td><img src='/images/explanation/P3_model_down_brace_%s.png' /></td><td colspan=2><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(usedBrace,leftBrace)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>%d</td><td colspan=2>?</td></tr>"%(number3)
            self.solution_text = self.solution_text + "</table><br><br>"
        else:
            if number2>number3:
                number1Brace = 'large1medium1small1'
                number2Brace = 'medium'
                usedBrace = 'small'
                leftBrace = 'large'
                number2Width = 96
                usedWidth = 48
                leftWidth = 144
            elif number2==number3:
                number1Brace = 'large1medium2'
                number2Brace = 'medium'
                usedBrace = 'medium'
                leftBrace = 'large'
                number2Width = 96
                usedWidth = 96
                leftWidth = 144
            else:
                number1Brace = 'large1medium1small1'
                number2Brace = 'small'
                usedBrace = 'medium'
                leftBrace = 'large'
                number2Width = 48
                usedWidth = 96
                leftWidth = 144
            self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=3>%d</td></tr>"%(number1)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=3 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(number1Brace)
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td><td colspan=3 style='background-color:%s;height:25px;border:white solid 1px;'>&nbsp;</td></tr>"%(names[0],self.color1)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='width:%dpx;'>&nbsp;</td><td style='width:%dpx;'>&nbsp;</td><td style='width:%dpx;'>&nbsp;</td></tr>"%(leftWidth,usedWidth,number2Width)
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;'><font style='font-size:0.8em;'>left</font></td><td style='background-color:%s;height:25px;border:white solid 1px;'><font style='font-size:0.8em;'>sells</font></td><td>&nbsp;</td></tr>"%(names[1],self.color2,self.color3)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td><img src='/images/explanation/P3_model_down_brace_%s.png' /></td><td><img src='/images/explanation/P3_model_down_brace_%s.png' /></td><td><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(leftBrace,usedBrace,number2Brace)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>?</td><td>%d</td><td>%d</td></tr>"%(number3,number2)
            self.solution_text = self.solution_text + "</table><br><br>"
            #end of model

        intermediateAnswer = 0
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        if flag==1:
            self.solution_text = self.solution_text + "%d &nbsp;+&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number1,number2,number1+number2)
            self.solution_text = self.solution_text + "%s's %s %d %s.<br><br>"%(names[1],item0,number1+number2,item1)
            intermediateAnswer = number1+number2
        else:
            self.solution_text = self.solution_text + "%d &nbsp;&minus;&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number1,number2,number1-number2)
            self.solution_text = self.solution_text + "%s's %s %d %s.<br><br>"%(names[1],item0,number1-number2,item1)
            intermediateAnswer = number1-number2
        self.solution_text = self.solution_text + "%d &nbsp;&minus;&nbsp; %d &nbsp;=&nbsp; %d<br>"%(intermediateAnswer,number3,answer)
        self.solution_text = self.solution_text + "She has %d %s left."%(answer,item1)
        self.solution_text = self.solution_text + "</font>" 

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType16(self):       
        '''e.g.:
        [Person.Boyname1] <made> 150 litres of <sugar syrup>.    
        [Person.Boyname2] <made> 30 litres less <sugar syrup> than [Person.Boyname1].
        [Person.Boyname3] <made> 20 litres less <sugar syrup> than [Person.Boyname2].
        How much <sugar syrup> did [Person.Boyname3] <make>?'''

        self.complexity_level = "easy"
        self.HCScore = 3

        self.names = random.sample(PersonName.BoyName,3)
        
        self.items = [['made','sugar syrup','make'],['made','rose drink','make'],
                      ['made','lemonade','make'],['made','ice lemon tea','make'],
                      ['made','milk shake','make'],['sold','milk','sell'],['sold','water','sell'],
                      ['sold','fruit juice','sell'],['sold','water','sell'],['packed','chocolate milk','pack'],
                      ['packed','strawberry yogurt','pack'],['packed','mango drink','pack']]
           
        self.item = random.choice(self.items)
        
        self.number1 = randint(100,200)
        self.number2 = randint(20,40)
        self.number3 = randint(20,40)
        
        self.flag = randint(1,2)
        
        self.problem = "%s %s %d <font class='litreFont'>l</font>&nbsp; of %s.<br><br>"%(self.names[0],self.item[0],self.number1,self.item[1])
        if self.flag == 1:
            self.problem = self.problem + "%s %s %d <font class='litreFont'>l</font>&nbsp; less %s than %s.<br><br>"%(self.names[1],self.item[0],self.number2,self.item[1],self.names[0])
            self.problem = self.problem + "%s %s %d <font class='litreFont'>l</font>&nbsp; less %s than %s.<br><br>"%(self.names[2],self.item[0],self.number3,self.item[1],self.names[1])
            self.answer = self.number1 - self.number2 - self.number3
        else:
            self.problem = self.problem + "%s %s %d <font class='litreFont'>l</font>&nbsp; more %s than %s.<br><br>"%(self.names[1],self.item[0],self.number2,self.item[1],self.names[0])
            self.problem = self.problem + "%s %s %d <font class='litreFont'>l</font>&nbsp; more %s than %s.<br><br>"%(self.names[2],self.item[0],self.number3,self.item[1],self.names[1])
            self.answer = self.number1 + self.number2 + self.number3
        self.problem = self.problem + "How much %s did %s %s?"%(self.item[1],self.names[2],self.item[2])

        self.unit = "<font class='litreFont'>l</font>"
        self.dollar_unit = ""
          
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType16(self.problem,self.answer,self.flag,self.names,self.number1,self.number2,self.number3,self.item[0],self.item[1],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType16",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,
                'unit':self.unit,'dollar_unit':self.dollar_unit}

    def ExplainType16(self,problem,answer,flag,names,number1,number2,number3,item0,item1,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        #beginning of model
        self.colors = random.choice([['tomato','orange','peru'],['blueviolet','violet','darkorchid'],['purple','plum','mediumvioletred'],['darkturquoise','dodgerblue','darkslateblue'],['mediumorchid','mediumpurple','palevioletred'],['chocolate','burlywood','brown'],['deeppink','lightpink','hotpink']])
        self.color1 = self.colors[0]
        self.color2 = self.colors[1]
        self.color3 = self.colors[2]

        if number2>number3:
            number1Brace = 'large1medium1small1'
            number2Brace = 'medium'
            number3Brace = 'small'
        elif number2==number3:
            number1Brace = 'large1small2'
            number2Brace = 'small'
            number3Brace = 'small'
        else:
            number1Brace = 'large1medium1small1'
            number2Brace = 'small'
            number3Brace = 'medium'
        
        if flag==1:
            self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=3>%d <font class='litreFont'>l</font></td></tr>"%(number1)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=3 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(number1Brace)
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td><td colspan=2 style='background-color:%s;height:25px;border:white solid 1px;border-right:white dotted 1px;'>&nbsp;</td><td colspan=2 style='background-color:%s;height:25px;border:white solid 1px;border-left:white dotted 1px;'>&nbsp;</td></tr>"%(names[0],self.color1,self.color1)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(number2Brace)
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;border-right:white dotted 1px;'>&nbsp;</td><td style='background-color:%s;height:25px;border:white solid 1px;border-left:white dotted 1px;'>&nbsp;</td><td style='vertical-align:top;'>%d <font class='litreFont'>l</font></td></tr>"%(names[1],self.color2,self.color2,number2)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>&nbsp;</td><td><img src='/images/explanation/P3_model_down_brace_%s.png' /></td><td>&nbsp;</td></tr>"%(number3Brace)
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;'></td><td style='vertical-align:top;'>%d <font class='litreFont'>l</font></td></tr>"%(names[2],self.color3,number3)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td><img src='/images/explanation/P3_model_down_brace_large.png' /></td></tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>?</td></tr>"
            self.solution_text = self.solution_text + "</table><br><br>"
        else:
            self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>%d <font class='litreFont'>l</font></td><td>&nbsp;</td><td>&nbsp;</td></tr>"%(number1)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_large.png' /></td></tr>"
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;'>&nbsp;</td><td style='vertical-align:bottom;'>%d <font class='litreFont'>l</font></td><td>&nbsp;</td></tr>"%(names[0],self.color1,number2)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>&nbsp;</td><td><img src='/images/explanation/P3_model_up_brace_%s.png' /></td><td>&nbsp;</td></tr>"%(number2Brace)
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;border-right:white dotted 1px;'>&nbsp;</td><td style='background-color:%s;height:25px;border:white solid 1px;border-left:white dotted 1px;'>&nbsp;</td><td style='vertical-align:bottom;'>%d <font class='litreFont'>l</font></td></tr>"%(names[1],self.color2,self.color2,number3)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(number3Brace)
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td><td colspan=2 style='background-color:%s;height:25px;border:white solid 1px;border-right:white dotted 1px;'>&nbsp;</td><td style='background-color:%s;height:25px;border:white solid 1px;border-left:white dotted 1px;'>&nbsp;</td></tr>"%(names[2],self.color3,self.color3)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=3><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(number1Brace)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=3>?</td></tr>"
            self.solution_text = self.solution_text + "</table><br><br>"
            #end of model
                
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        if flag==1:
            self.solution_text = self.solution_text + "%d &nbsp;&minus;&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number1,number2,number1-number2)
            self.solution_text = self.solution_text + "%s %s %d <font class='litreFont'>l</font>&nbsp; of %s.<br><br>"%(names[1],item0,number1-number2,item1)
            self.solution_text = self.solution_text + "%d &nbsp;&minus;&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number1-number2,number3,answer)
            self.solution_text = self.solution_text + "%s %s %d <font class='litreFont'>l</font>&nbsp; of %s."%(names[2],item0,answer,item1)
        else:
            self.solution_text = self.solution_text + "%d &nbsp;+&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number1,number2,number1+number2)
            self.solution_text = self.solution_text + "%s %s %d <font class='litreFont'>l</font>&nbsp; of %s.<br><br>"%(names[1],item0,number1+number2,item1)
            self.solution_text = self.solution_text + "%d &nbsp;+&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number1+number2,number3,answer)
            self.solution_text = self.solution_text + "%s %s %d <font class='litreFont'>l</font>&nbsp; of %s."%(names[2],item0,answer,item1)
        self.solution_text = self.solution_text + "</font>" 

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType17(self):       
        '''e.g.:
        [Person.Girlname] made <a cake> using 1234 g of <all-purpose flour>, 1094 g of <whole wheat flour> and 456 g of <sugar>.
        How much more <flour> than <sugar> did she use for the <cake>?'''

        self.complexity_level = "easy"
        self.HCScore = 3

        self.name = random.choice(PersonName.GirlName)
        
        self.items = [['a cake','all-purpose flour','whole wheat flour','sugar','flour','cake','all-purpose','whole what'],
                      ['a fruit cocktail','green grapes','black grapes','pineapple','grapes','fruit cocktail','green','black'],
                      ['a fruit custard','green apples','red apples','bananas','apples','fruit custard','green','red'],
                      ['a pie','potatoes','peas','meat','vegetables','pie','potatoes','peas'],
                      ['a rice pudding','brown rice','white rice','sugar','rice','pudding','brown','white'],
                      ['pizzas','mozzarella cheese','parmesan cheese','tomatoes','cheese','pizzas','mozzarella','parmesan'],
                      ['biscuits','plain flour','corn flour','butter','flour','biscuits','plain','corn'],
                      ['a sand art','coarse sand','fine sand','pebbles','sand','sand art','coarse','fine'],
                      ['a mosaic','red tiles','yellow tiles','beads','tiles','mosaic','red','yellow'],
                      ['an art project','clam shells','snail shells','glass','shells','project','clam','snail']]
           
        self.item = random.choice(self.items)
        
        self.number1 = randint(1000,2000)
        self.number2 = randint(1000,2000)
        self.number3 = randint(400,800)
        
        self.problem = "%s made %s using %d g of %s, %d g of %s and %d g of %s.<br><br>"%(self.name,self.item[0],self.number1,self.item[1],
                                                                                          self.number2,self.item[2],self.number3,self.item[3])
        self.problem = self.problem + "How much more %s than %s did she use for the %s?"%(self.item[4],self.item[3],self.item[5])

        
        self.answer = (self.number1+self.number2) - self.number3
        
        self.unit = "g"
        self.dollar_unit = ""
          
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType17(self.problem,self.answer,self.number1,self.number2,self.number3,self.item[3],self.item[4],self.item[5],self.item[6],self.item[7],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType17",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,
                'unit':self.unit,'dollar_unit':self.dollar_unit}

    def ExplainType17(self,problem,answer,number1,number2,number3,item3,item4,item5,item6,item7,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        #beginning of model
        self.colors = random.choice([['tomato','orange','peru'],['blueviolet','violet','darkorchid'],['purple','plum','mediumvioletred'],['darkturquoise','dodgerblue','darkslateblue'],['mediumorchid','mediumpurple','palevioletred'],['chocolate','burlywood','brown'],['deeppink','lightpink','hotpink']])
        self.color1 = self.colors[0]
        self.color2 = self.colors[1]
        self.color3 = self.colors[2]

        if number1>number2:
            number1Brace = 'large'
            number2Brace = 'medium'
            moreBrace = 'medium2'
            number1Width = 144
            number2Width = 96
        elif number1==number2:
            number1Brace = 'medium'
            number2Brace = 'medium'
            moreBrace = 'medium1small1'
            number1Width = 96
            number2Width = 96
        else:
            number1Brace = 'medium'
            number2Brace = 'large'
            moreBrace = 'medium2'
            number1Width = 96
            number2Width = 144
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2>%d g</td><td>%d g</td></tr>"%(number1,number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(number1Brace,number2Brace)
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td><td colspan=2 style='background-color:%s;height:25px;border:white solid 1px;'><font style='font-size:0.8em;'>%s</font></td><td style='background-color:%s;height:25px;border:white solid 1px;'><font style='font-size:0.8em;'>%s</font></td></tr>"%(item4,self.color1,item6,self.color2,item7)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='width:48px;'>&nbsp;</td><td style='width:%dpx;'>&nbsp;</td><td style='width:%dpx;'>&nbsp;</td></tr>"%(number1Width-48,number2Width)
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;'>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>"%(item3,self.color3)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td><img src='/images/explanation/P3_model_down_brace_small.png' /></td><td colspan=2><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(moreBrace)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>%d g</td><td colspan=2>?</td></tr>"%(number3)
        self.solution_text = self.solution_text + "</table><br><br>"
        #end of model

        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "%d &nbsp;+&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number1,number2,number1+number2)
        self.solution_text = self.solution_text + "She used %d g of %s altogether.<br><br>"%(number1+number2,item4)
        self.solution_text = self.solution_text + "%d &nbsp;&minus;&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number1+number2,number3,answer)
        self.solution_text = self.solution_text + "She used %d g more %s than %s for the %s."%(answer,item4,item3,item5)
        self.solution_text = self.solution_text + "</font>" 

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType18(self):       
        '''e.g.:
        [Person.Name1] <packed> <twice / thrice> the <amount of milk> that [Person.Name2] <packed>.
        [Person.Name2] <packed> 273 <litres of milk>.
        How many <litres of milk> did they <pack> altogether?'''

        self.complexity_level = "easy"
        self.HCScore = 3

        self.names = random.sample(PersonName.PersonName,2)
               
        self.number = randint(200,500)
               
        self.items = [['packed','much milk',"<font class='litreFont'>l</font>&nbsp; of milk",'pack',"<font class='litreFont'>l</font>"],
                      ['sold','much rope','m of rope','sell','m'],
                      ['bought','much brown rice','g of brown rice','buy','g'],
                      ['had','many CDs','CDs','have','CDs'],
                      ['baked','many pizzas','pizzas','bake','pizzas'],
                      ['shared','many candies','candies','share','candies'],
                      ['collected','many candles','candles','collect','candles'],
                      ['counted','many bicycles','bicycles','count','bicycles'],
                      ['picked','many tomatoes','tomatoes','pick','tomatoes'],
                      ['read','many pages','pages','read','pages'],
                      ['solved','many maths problems','maths problems','solve','maths problems']]
        self.item = random.choice(self.items)

        self.times = random.choice([[2,"twice"],[3,"thrice"],[4,"4 times"]])
        
        self.problem = "%s %s %s as %s as %s.<br><br>"%(self.names[0],self.item[0],self.times[1],self.item[1],self.names[1])
        self.problem = self.problem + "%s %s %d %s.<br><br>"%(self.names[1],self.item[0],self.number,self.item[2])
        self.problem = self.problem + "How %s did they %s altogether?"%(self.item[1],self.item[3])               
        
        self.answer = self.times[0]*self.number + self.number
        
        self.unit = self.item[4]
        self.dollar_unit = ""
          
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType18(self.problem,self.answer,self.names,self.times[0],self.number,self.item[0],self.item[2],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType18",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,
                'unit':self.unit,'dollar_unit':self.dollar_unit}

    def ExplainType18(self,problem,answer,names,times,number,item0,item2,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        #beginning of model
        self.colors = random.choice([['tomato','orange'],['blueviolet','violet'],['purple','plum'],['darkturquoise','dodgerblue'],['mediumorchid','mediumpurple'],['chocolate','burlywood'],['deeppink','lightpink']])
        self.color1 = self.colors[0]
        self.color2 = self.colors[1]
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>%d</td></tr>"%(number)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_small.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;width:50px;'>&nbsp;</td><td colspan=%d>&nbsp;</td><td>&nbsp;&nbsp;</td><td rowspan=3 style='padding:0;padding-top:3px;vertical-align:middle'><img src='/images/explanation/P3_model_right_brace_small.png' /></td><td rowspan=3 style='padding:0;vertical-align:middle'>&nbsp;?</td></tr>"%(names[1],self.color1,times)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td>"%(names[0])
        for x in range(0, times):
            self.solution_text = self.solution_text + "<td style='background-color:%s;height:25px;border:white solid 1px;width:50px;'>&nbsp;</td>"%(self.color2)
        self.solution_text = self.solution_text + "</tr>"
        self.solution_text = self.solution_text + "</table><br><br><br>"
        #end of model

        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "Method 1:<blockquote>"
        self.solution_text = self.solution_text + "%d &nbsp;&times;&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number,times,number*times)
        self.solution_text = self.solution_text + "%s %s %d %s.<br><br>"%(names[0],item0,number*times,item2)
        self.solution_text = self.solution_text + "%d &nbsp;+&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number*times,number,answer)
        self.solution_text = self.solution_text + "They %s %d %s altogether.<br><br></blockquote>"%(item0,answer,item2)
        self.solution_text = self.solution_text + "Method 2:<blockquote>"
        self.solution_text = self.solution_text + "1 &nbsp;+&nbsp; %d &nbsp;=&nbsp; %d<br>"%(times,times+1)
        self.solution_text = self.solution_text + "There are %d units altogether.<br><br>"%(times+1)
        self.solution_text = self.solution_text + "%d &nbsp;&times;&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number,times+1,number*(times+1))
        self.solution_text = self.solution_text + "They %s %d %s altogether.</blockquote>"%(item0,answer,item2)
        self.solution_text = self.solution_text + "</font>" 

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType19(self):       
        '''e.g.:
        [Person.Unclename] <had> 8 <cartons of notebooks>.
        Each <carton> contained 156 <notebooks>.
        He <kept> 382 <notebooks for himself and sold the rest>.
        How many <notebooks did he sell>?'''

        self.complexity_level = "easy"
        self.HCScore = 3

        self.name = random.choice(PersonName.UncleName)
               
        self.items = [['had','cartons of notebooks','carton','notebooks','kept','notebooks for himself and sold the rest','notebooks did he sell','He sold','notebooks','sold'],
                      ['had','booklets of tickets to a dance show','booklet','tickets','kept','tickets for his friends and sold the remaining','tickets did he sell','He sold','tickets','sold'],
                      ['baked','trays of cookies','tray','cookies','threw away','burnt cookies and sold the remaining','cookies did he sell','He sold','cookies','sold'],
                      ['made','boxes of cheese rolls','box','cheese rolls','kept','for his family and sold the rest','cheese rolls did he sell','He sold','cheese rolls','sold'],
                      ['bought','boxes of markers for his class','box','markers','saved','markers for later and gave the rest to his pupils','markers did he give to his pupils','He gave','markers to his pupils','gave'],
                      ['bought','boxes of erasers to sell at his bookshop','box','erasers','kept','erasers for himself and sold the rest to his customers','erasers did he sell','He sold','erasers','sold'],
                      ['picked','boxes of guavas from his farm','box','guavas','threw away','rotten guavas and packed the rest into bags','guavas did he pack into bags','He packed','guavas into bags','packed'],
                      ['received','cartons of mangoes from his friend','carton','mangoes','kept','mangoes for his family and gave away the rest to his neighbours','mangoes did he give away to his neighbours','He gave away','mangoes to his neighbours','gave away'],
                      ['collected','books of stamps','book','stamps','gave away','stamps to a museum and sold the rest','stamps did he sell','He sold','stamps','sold'],
                      ['collected','books of coins','book','coins','divided','coins among his children and sold the rest','coins did he sell','He sold','coins','sold']]
        
        self.item = random.choice(self.items)
        
        self.number1 = randint(3,9)
        self.number2 = randint(100,200)
        self.number3 = randint(200,290)
                             
        self.problem = "%s %s %d %s.<br><br>"%(self.name,self.item[0],self.number1,self.item[1])
        self.problem = self.problem + "Each %s contained %d %s.<br><br>"%(self.item[2],self.number2,self.item[3])
        self.problem = self.problem + "He %s %d %s.<br><br>"%(self.item[4],self.number3,self.item[5])
        self.problem = self.problem + "How many %s?"%(self.item[6])
        
        self.answer = self.number1 * self.number2 - self.number3
        
        self.unit = self.item[3]
        self.dollar_unit = ""
          
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType19(self.problem,self.answer,self.item[0],self.item[3],self.item[7],self.item[8],self.item[9],self.number1,self.number2,self.number3,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType19",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,
                'unit':self.unit,'dollar_unit':self.dollar_unit}

    def ExplainType19(self,problem,answer,item0,item3,item7,item8,item9,number1,number2,number3,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        #beginning of model 1
        self.colors = random.choice([['tomato','orange','peru'],['blueviolet','violet','darkorchid'],['purple','plum','mediumvioletred'],['darkturquoise','dodgerblue','darkslateblue'],['mediumorchid','mediumpurple','palevioletred'],['chocolate','burlywood','brown'],['deeppink','lightpink','hotpink']])
        self.color1 = self.colors[0]
        self.color2 = self.colors[1]
        self.color3 = self.colors[2]

        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>%d</td></tr>"%(number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_small.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td>"%(item3)
        for x in range(0, number1):
            self.solution_text = self.solution_text + "<td style='background-color:%s;height:25px;border:white solid 1px;width:50px;'>&nbsp;</td>"%(self.color1)
        self.solution_text = self.solution_text + "</tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_small%d.png' /></td></tr>"%(number1,number1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d>? (a)</td></tr>"%(number1)
        self.solution_text = self.solution_text + "</table><br><br>"
        #end of model 1

        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "%d &nbsp;&times;&nbsp; %d &nbsp;=&nbsp; %d &nbsp;&nbsp;(a)<br>"%(number2,number1,number1*number2)
        self.solution_text = self.solution_text + "He %s %d %s.<br><br>"%(item0,number1*number2,item3)
        self.solution_text = self.solution_text + "</font>" 

        #beginning of model 2
        div = int(round(float(number3)/number2,0))
        if div==0:
            div = 1
        if div==number1:
            div = div-1
        self.solution_text = self.solution_text + "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2>%d</td></tr>"%(number1*number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_small%d.png' /></td></tr>"%(number1)
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;width:50px;'>&nbsp;</td><td style='background-color:%s;height:25px;border:white solid 1px;width:50px;'><font style='font-size:0.8em'>%s</font></td></tr>"%(item3,self.color2,self.color3,item9)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_small%d.png' /></td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_small%d.png' /></td></tr>"%(div,number1-div)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'>%d</td><td style='padding-bottom:3px;'>?</td></tr>"%(number3)
        self.solution_text = self.solution_text + "</table><br><br>"
        #end of model 2

        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "%d &nbsp;&minus;&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number1*number2,number3,answer)
        self.solution_text = self.solution_text + "%s %d %s."%(item7,answer,item8)
        self.solution_text = self.solution_text + "</font>" 

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType20(self):       
        '''e.g.:
        [Person.Girlname] had some <roses> and <daisies>.
        She <arranged> 5 <roses> and 6 <daisies> into each <vase>.
        She got a total of 7 <vases>.
        How many <flowers> were there altogether?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.GirlName)
        
        self.items = [['roses','daisies','arranged','vase','vases','flowers'],
                      ['pencils','erasers','put','pencil case','pencil cases','pencils and erasers'],
                      ['cupcakes','muffins','packed','box','boxes','cupcakes and muffins'],
                      ['coins','rings','put','purse','purses','coins and rings'],
                      ['gummies','biscuits','packed','packet','packets','gummies and biscuits'],
                      ['jellies','cookies','packed','container','containers','jellies and cookies'],
                      ['clips','rubberbands','put','pouch','pouches','clips and rubberbands'],
                      ['photos','cards','put','envelope','envelopes','photos and cards'],
                      ['notebooks','storybooks','put','bag','bags','notebooks and storybooks'],
                      ['plums','avocados','put','basket','baskets','fruits']]
        
        self.item = random.choice(self.items)
        
        self.number1 = randint(3,9)
        self.number2 = randint(3,9)
        self.number3 = randint(3,9)

        self.problem = "%s had some %s and %s.<br><br>"%(self.name,self.item[0],self.item[1])
        self.problem = self.problem + "She %s %d %s and %d %s into each %s.<br><br>"%(self.item[2],self.number1,self.item[0],self.number2,self.item[1],self.item[3])
        self.problem = self.problem + "She got a total of %d %s.<br><br>"%(self.number3,self.item[4])
        self.problem = self.problem + "How many %s were there altogether?"%(self.item[5])
        
        self.answer = (self.number1 + self.number2) * self.number3
        
        self.unit = self.item[5]
        self.dollar_unit = ""
          
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType20(self.problem,self.answer,self.number1,self.number2,self.number3,self.item[0],self.item[1],self.item[3],self.item[4],self.item[5],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType20",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,
                'unit':self.unit,'dollar_unit':self.dollar_unit}

    def ExplainType20(self,problem,answer,number1,number2,number3,item0,item1,item3,item4,item5,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        #beginning of model
        self.colors = random.choice([['tomato','orange'],['blueviolet','violet'],['purple','plum'],['darkturquoise','dodgerblue'],['mediumorchid','mediumpurple'],['chocolate','burlywood'],['deeppink','lightpink']])
        self.color1 = self.colors[0]
        self.color2 = self.colors[1]

        if number1==number2:
            firstBrace = 'medium'
            secondBrace = 'medium'
            totalBrace = 'medium2' 
        elif number1>number2:
            firstBrace = 'large'
            secondBrace = 'medium'
            totalBrace = 'large1medium1'
        else:
            firstBrace = 'medium'
            secondBrace = 'large'
            totalBrace = 'large1medium1'

        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>%d</td><td>%d</td></tr>"%(number1,number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(firstBrace,secondBrace)
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>1 %s</td><td style='background-color:%s;height:25px;border:white solid 1px;'><font style='font-size:0.8em;'>%s</font></td><td style='background-color:%s;height:25px;border:white solid 1px;'><font style='font-size:0.8em;'>%s</font></td></tr>"%(item3,self.color1,item0,self.color2,item1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(totalBrace)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2>? (a)</td></tr>"
        self.solution_text = self.solution_text + "</table><br><br>"
        #end of model
            
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "%d &nbsp;+&nbsp; %d &nbsp;=&nbsp; %d &nbsp;&nbsp; (a)<br>"%(number1,number2,number1+number2)
        self.solution_text = self.solution_text + "There were %d %s in each %s.<br><br>"%(number1+number2,item5,item3)
        self.solution_text = self.solution_text + "%d &nbsp;&times;&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number1+number2,number3,answer)
        self.solution_text = self.solution_text + "In %d %s, there were %d %s altogether."%(number3,item4,answer,item5)
        self.solution_text = self.solution_text + "</font>" 

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType21(self):       
        '''e.g.:
        [Person.Name1], [Person.Name2] and [Person.Name3] <saved some money>.
        [Person.Name1] <saved> 4 times as much as [Person.Name2].
        [Person.Name3] <saved> $12 more than [Person.Name1].
        [Person.Name2] <saved> $32.
        How much money did [Person.Name3] <save>?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.names = random.sample(PersonName.PersonName,3)
        
        self.items = [['saved some money','saved','save'],['earned some money','earned','earn'],
                      ['donated some money to a charity','donated','donate'],['went shopping','spent','spend'],
                      ['gave away some money to the needy','gave away','give away'],['received some pocket money','received','receive'],
                      ['had some money','had','have'],['counted the money in their wallets','counted','count'],
                      ['went to a bank to withdraw some money','withdrew','withdraw'],['deposited some money in their bank accounts','deposited','deposit']]
        
        self.item = random.choice(self.items)
        
        self.number1 = randint(2,9)
        self.number2 = randint(20,100)        
        self.number3 = randint(50,200)
                             
        self.problem = "%s, %s and %s %s.<br><br>"%(self.names[0],self.names[1],self.names[2],self.item[0])
        self.problem = self.problem + "%s %s %d times as much money as %s.<br><br>"%(self.names[0],self.item[1],self.number1,self.names[1])
        self.problem = self.problem + "%s %s $%d more than %s.<br><br>"%(self.names[2],self.item[1],self.number2,self.names[0])
        self.problem = self.problem + "%s %s $%d.<br><br>"%(self.names[1],self.item[1],self.number3)
        self.problem = self.problem + "How much money did %s %s?"%(self.names[2],self.item[2])
        
        self.answer = (self.number1 * self.number3) + self.number2
        
        self.unit = ""
        self.dollar_unit = "$"
          
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType21(self.problem,self.answer,self.names,self.number1,self.number2,self.number3,self.item[1],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType21",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,
                'unit':self.unit,'dollar_unit':self.dollar_unit}

    def ExplainType21(self,problem,answer,names,number1,number2,number3,item1,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        #beginning of model
        self.colors = random.choice([['tomato','orange','peru'],['blueviolet','violet','darkorchid'],['purple','plum','mediumvioletred'],['darkturquoise','dodgerblue','darkslateblue'],['mediumorchid','mediumpurple','palevioletred'],['chocolate','burlywood','brown'],['deeppink','lightpink','hotpink']])
        self.color1 = self.colors[0]
        self.color2 = self.colors[1]
        self.color3 = self.colors[2]

        if number2==number3:
            moreBrace = 'small'
            totalBrace = 'small%d'%(number1+1)
        elif number2>number3:
            moreBrace = 'medium'
            totalBrace = 'medium1small%d'%(number1)
        else:
            moreBrace = 'extrasmall'
            totalBrace = 'small%dextrasmall1'%(number1)

        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$%d</td></tr>"%(number3)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_small.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;width:50px;'>&nbsp;</td></tr>"%(names[1],self.color1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td>"%(names[0])
        for x in range(0, number1):
            self.solution_text = self.solution_text + "<td style='background-color:%s;height:25px;border:white solid 1px;width:52px;'>&nbsp;</td>"%(self.color2)
        self.solution_text = self.solution_text + "<td style='vertical-align:bottom;'>$%d</td></tr>"%(number2)
        self.solution_text = self.solution_text + "<tr><td colspan=%d>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(number1+1,moreBrace)
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td><td colspan=%d style='background-color:%s;height:25px;border:white solid 1px;border-right:white dotted 1px;'>&nbsp;</td><td style='background-color:%s;height:25px;border:white solid 1px;border-left:white dotted 1px;'>&nbsp;</td></tr>"%(names[2],number1,self.color3,self.color3)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(number1+1,totalBrace)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d>?</td></tr>"%(number1+1)
        self.solution_text = self.solution_text + "</table><br>"
        #end of model

        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "$%d &nbsp;&times;&nbsp; %d &nbsp;=&nbsp; $%d<br>"%(number3,number1,number3*number1)
        self.solution_text = self.solution_text + "%s %s $%d.<br><br>"%(names[0],item1,number3*number1)
        self.solution_text = self.solution_text + "$%d &nbsp;+&nbsp; $%d &nbsp;=&nbsp; $%d<br>"%(number3*number1,number2,answer)
        self.solution_text = self.solution_text + "%s %s $%d."%(names[2],item1,answer)
        self.solution_text = self.solution_text + "</font>" 

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType22(self):       
        '''e.g.:
        A <cushion cover> costs $5.
        [Person.Girlname] had $25 left after buying 8 <cushion covers>.
        Find the sum of money she had at first.'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.GirlName)
        
        self.items = [['cushion cover','cushion covers'],['plastic chair','plastic chairs'],
                      ['chessboard','chessboards'],['wooden easel','wooden easels'],['bandana','bandanas'],
                      ['box of water colour','boxes of water colours'],['packet of cheese','packets of cheese'],
                      ['container of fish food','containers of fish food'],['bag of cake mix','bags of cake mix'],
                      ['jar of pineapple tarts','jars of pineapple tarts']]
        
        self.item = random.choice(self.items)
        
        self.number1 = randint(5,20)
        self.number2 = randint(50,200)
        self.number3 = randint(3,9)
                             
        self.problem = "A %s costs $%d.<br><br>"%(self.item[0],self.number1)
        self.problem = self.problem + "%s had $%d left after buying %d %s.<br><br>"%(self.name,self.number2,self.number3,self.item[1])
        self.problem = self.problem + "Find the sum of money she had at first."
        
        self.answer = (self.number1 * self.number3) + self.number2
        
        self.unit = ""
        self.dollar_unit = "$"
          
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType22(self.problem,self.answer,self.number1,self.number2,self.number3,self.item[1],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType22",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,
                'unit':self.unit,'dollar_unit':self.dollar_unit}

    def ExplainType22(self,problem,answer,number1,number2,number3,item1,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        #beginning of model
        self.colors = random.choice([['tomato','orange','peru'],['blueviolet','violet','darkorchid'],['purple','plum','mediumvioletred'],['darkturquoise','dodgerblue','darkslateblue'],['mediumorchid','mediumpurple','palevioletred'],['chocolate','burlywood','brown'],['deeppink','lightpink','hotpink']])
        self.color1 = self.colors[0]
        self.color2 = self.colors[1]
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>$%d</td><td colspan=%d>&nbsp;</td><td>$%d</td></tr>"%(number1,number3-1,number2)
        self.solution_text = self.solution_text + "<tr><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_small.png' /></td><td colspan=%d>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_large.png' /></td></tr>"%(number3-1)
        self.solution_text = self.solution_text + "<tr>"
        for x in range(0, number3):
            self.solution_text = self.solution_text + "<td style='background-color:%s;height:25px;border:white solid 1px;width:48px;'>&nbsp;</td>"%(self.color1)
        self.solution_text = self.solution_text + "<td style='background-color:%s;height:25px;border:white solid 1px;'>left</td></tr>"%(self.color2)
        self.solution_text = self.solution_text + "<tr><td colspan=%d style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_large1small%d.png' /></td></tr>"%(number3+1,number3)
        self.solution_text = self.solution_text + "<tr><td colspan=%d>?</td></tr>"%(number3+1)
        self.solution_text = self.solution_text + "</table><br>"
        #end of model

        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "$%d &nbsp;&times;&nbsp; %d &nbsp;=&nbsp; $%d<br>"%(number1,number3,number1*number3)
        self.solution_text = self.solution_text + "The %d %s cost $%d altogether.<br><br>"%(number3,item1,number1*number3)
        self.solution_text = self.solution_text + "$%d &nbsp;+&nbsp; $%d &nbsp;=&nbsp; $%d<br>"%(number1*number3,number2,answer)
        self.solution_text = self.solution_text + "She had $%d at first."%(answer)
        self.solution_text = self.solution_text + "</font>" 

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType23(self):       
        '''e.g.:
        [Person.Gilrname] <makes> 8 <necklaces using beads>.
        She <uses> 270 <small beads> and 41 <big beads for each necklace>.
        How <many beads does she use> altogether?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.GirlName)
        
        self.items = [['makes','necklaces using beads','uses','small beads','big beads for each necklace','many beads does she use','beads','beads','for each necklace','necklace','small beads','big beads','necklaces'],
                      ['makes','mosaics using stones','uses','white stones','coloured stones for each mosaic','many stones does she use','stones','stones','for each mosaic','mosaic','white stones','coloured stones','mosaics'],
                      ['is making','model boats','uses','sticks','coins for each model boat','many sticks and coins does she use','sticks and coins','sticks and coins','for each model boat','model boat','sticks','coins','model boats'],
                      ['is decorating','similar flower pots with stickers','uses','small stickers','big stickers for each flower pot','many stickers does she use','stickers','stickers','for each flower pot','flower pot','small stickers','big stickers','flower pots'],
                      ['is packing','bags of balloons','packs','air balloons','water balloons in each bag','many balloons does she pack','ballons','ballons','in each bag','bag','air balloons','water balloons','bags'],
                      ['is packing','boxes with screws and bolts','packs','screws','bolts in each box','many screws and bolts does she pack','screws and bolts','screws and bolts','in each box','box','screws','bolts','boxes'],
                      ['is making','pizzas','uses','g flour','g cheese for one pizza','much flour and cheese does she use','g','g of flour and cheese','for one pizza','pizza','flour','cheese','pizzas'],
                      ['is making','loaves of bread','uses','g bread flour','g butter for one loaf','much flour and butter does she use','g','g of flour and butter','for one loaf','loaf','bread flour','butter','loaves'],
                      ['is potting plants in','pots','uses','g soil','g fertilizer for each pot','much soil and fertilizer does she use','g','g of soil and fertilizer','for each pot','pot','soil','fertilizer','pots'],
                      ['is making','pinatas for birthday parties','uses','g milk chocolate','g dark chocolate for each pinata','much chocolate does she use','g','g of chocolate','for each pinata','pinata','milk chocolate','dark chocolate','pinatas'],
                      ['is making','bottles of lemonade','uses','ml of water','ml of lemon juice for each bottle','much water and lemon juice does she use','ml','ml of water and lemon juice','for each bottle','bottle','water','lemon juice','bottles']]
        
        self.item = random.choice(self.items)
        
        self.number1 = randint(2,9)
        self.number2 = randint(120,300)        
        self.number3 = randint(20,70)
                             
        self.problem = "%s %s %d %s.<br><br>"%(self.name,self.item[0],self.number1,self.item[1])
        self.problem = self.problem + "She %s %d %s and %d %s.<br><br>"%(self.item[2],self.number2,self.item[3],self.number3,self.item[4])
        self.problem = self.problem + "How %s altogether?"%(self.item[5])
        
        self.answer = self.number1 * (self.number3 + self.number2)
        
        self.unit = self.item[6]
        self.dollar_unit = ""
          
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType23(self.problem,self.answer,self.number1,self.number2,self.number3,self.item[2],self.item[7],self.item[8],self.item[9],self.item[10],self.item[11],self.item[12],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType23",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,
                'unit':self.unit,'dollar_unit':self.dollar_unit}

    def ExplainType23(self,problem,answer,number1,number2,number3,item2,item7,item8,item9,item10,item11,item12,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        #beginning of model
        self.colors = random.choice([['tomato','orange'],['blueviolet','violet'],['purple','plum'],['darkturquoise','dodgerblue'],['mediumorchid','mediumpurple'],['chocolate','burlywood'],['deeppink','lightpink']])
        self.color1 = self.colors[0]
        self.color2 = self.colors[1]

        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>%d</td><td>%d</td></tr>"%(number2,number3)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_large.png' /></td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_medium.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>1 %s</td><td style='background-color:%s;height:25px;border:white solid 1px;'><font style='font-size:0.8em;'>%s</font></td><td style='background-color:%s;height:25px;border:white solid 1px;'><font style='font-size:0.8em;'>%s</font></td></tr>"%(item9,self.color1,item10,self.color2,item11)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_large1medium1.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2>? (a)</td></tr>"
        self.solution_text = self.solution_text + "</table><br><br>"
        #end of model
        
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "%d &nbsp;+&nbsp; %d &nbsp;=&nbsp; %d &nbsp;&nbsp; (a)<br>"%(number2,number3,number2+number3)
        self.solution_text = self.solution_text + "She %s %d %s %s.<br><br>"%(item2,number2+number3,item7,item8)
        self.solution_text = self.solution_text + "%d &nbsp;&times;&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number2+number3,number1,answer)
        self.solution_text = self.solution_text + "For %d %s, she %s %d %s altogether."%(number1,item12,item2,answer,item7)
        self.solution_text = self.solution_text + "</font>" 

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType24(self):       
        '''e.g.:
        [Person.Name] has three <bags of marbles>.
        <Bag A has> 14 <more marbles than Bag B>.
        <Bag B has> 3 times as <many marbles as Bag C>.
        <Bag C has> 13 <marbles>.
        <How many marbles are there in Bag A?>'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.PersonName)
        
        self.items = [['bags of marbles','Bag A has','more marbles than Bag B','Bag B has','many marbles as Bag C','Bag C has','marbles','How many marbles are there in Bag A?','marbles','There are','marbles in Bag A','','Bag A','Bag B','Bag C',''],
                      ['packets of bookmarks','Packet A has','more bookmarks than Packet B','Packet B has','many bookmarks as Packet C','Packet C has','bookmarks','Find the number of bookmarks in Packet A.','bookmarks','There are','bookmarks in Packet A','','Packet A','Packet B','Packet C',''],
                      ['packs of drawing sheets','Pack A has','more sheets than Pack B','Pack B has','many sheets as Pack C','Pack C has','sheets','How many sheets are there in Pack A?','sheets','There are','sheets in Pack A','','Pack A','Pack B','Pack C',''],
                      ['cartons of tiles','Carton A has','more tiles than Carton B','Carton B has','many tiles as Carton C','Carton C has','tiles','Find the number of tiles in Carton A.','tiles','There are','tiles in Carton A','','Carton A','Carton B','Carton C',''],
                      ['aquariums with fishes','Aquarium A has','more fishes than Aquarium B','Aquarium B has','many fishes as Aquarium C','Aquarium C has','fishes','How many fishes are there in Aquarium A?','fishes','There are','fishes in Aquarium A','','Aquarium A','Aquarium B','Aquarium C',''],
                      ['strings','The yellow string is','cm longer than the red string','The red string is','long as the blue string','The blue string is','cm long','What is the length of the yellow string?','cm','The yellow string is','cm long','','yellow','red','blue','cm'],
                      ['ropes','The longest rope is','cm longer than the medium-sized rope','The medium-sized rope is','long as the shortest rope','The shortest rope is','cm long','What is the length of the longest rope?','cm','The longest rope is','cm long','','longest','meduim','shortest','cm'],
                      ['envelopes','Envelope A has','g more mass than Envelope B','Envelope B has','much mass as Envelope C','Envelope C has a mass of','g','Find the mass of Envelope A.','g','The mass of Envelope A is','g','a mass of','Envelope A','Envelope B','Envelope C','g'],
                      ['tanks of water','Tank A contains',"<font class='litreFont'>l</font>&nbsp; more water than Tank B",'Tank B contains','much water as Tank C','Tank C contains',"<font class='litreFont'>l</font>&nbsp; of water",'How much water does Tank A contain?',"<font class='litreFont'>l</font>",'Tank A contains',"<font class='litreFont'>l</font>&nbsp; of water",'','Tank A','Tank B','Tank C',"<font class='litreFont'>l</font>"],
                      ['bottles of syrup','Bottle A has','ml more syrup than Bottle B','Bottle B has','much syrup as Bottle C','Bottle C has','ml of syrup','How much syrup does Bottle A have?','ml','Bottle A has','ml of syrup','','Bottle A','Bottle B','Bottle C','ml']]
        
        self.item = random.choice(self.items)
        
        self.number1 = randint(10,20)
        self.number2 = randint(2,8)        
        self.number3 = randint(10,20)
                             
        self.problem = "%s has three %s.<br><br>"%(self.name,self.item[0])
        self.problem = self.problem + "%s %d %s.<br><br>"%(self.item[1],self.number1,self.item[2])
        self.problem = self.problem + "%s %d times as %s.<br><br>"%(self.item[3],self.number2,self.item[4])
        self.problem = self.problem + "%s %d %s.<br><br>"%(self.item[5],self.number3,self.item[6])
        self.problem = self.problem + "%s"%(self.item[7])
        
        self.answer = (self.number2*self.number3)+self.number1
        
        self.unit = self.item[8]
        self.dollar_unit = ""
          
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType24(self.problem,self.answer,self.number1,self.number2,self.number3,self.item[3],self.item[6],self.item[9],self.item[10],self.item[11],self.item[12],self.item[13],self.item[14],self.item[15],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType24",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,
                'unit':self.unit,'dollar_unit':self.dollar_unit}

    def ExplainType24(self,problem,answer,number1,number2,number3,item3,item6,item9,item10,item11,item12,item13,item14,item15,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        #beginning of model
        self.colors = random.choice([['tomato','orange','peru'],['blueviolet','violet','darkorchid'],['purple','plum','mediumvioletred'],['darkturquoise','dodgerblue','darkslateblue'],['mediumorchid','mediumpurple','palevioletred'],['chocolate','burlywood','brown'],['deeppink','lightpink','hotpink']])
        self.color1 = self.colors[0]
        self.color2 = self.colors[1]
        self.color3 = self.colors[2]

        if number1==number3:
            moreBrace = 'small'
            totalBrace = 'small%d'%(number2+1)
        elif number1>number3:
            moreBrace = 'small1extrasmall1'
            totalBrace = 'small%dextrasmall1'%(number2+1)
        else:
            moreBrace = 'extrasmall'
            totalBrace = 'small%dextrasmall1'%(number2)

        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>%d %s</td></tr>"%(number3,item15)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_small.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;width:50px;'>&nbsp;</td></tr>"%(item14,self.color1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td>"%(item13)
        for x in range(0, number2):
            self.solution_text = self.solution_text + "<td style='background-color:%s;height:25px;border:white solid 1px;width:52px;'>&nbsp;</td>"%(self.color2)
        self.solution_text = self.solution_text + "<td style='vertical-align:bottom;'>%d %s</td></tr>"%(number1,item15)
        self.solution_text = self.solution_text + "<tr><td colspan=%d>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(number2+1,moreBrace)
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>%s</td><td colspan=%d style='background-color:%s;height:25px;border:white solid 1px;border-right:white dotted 1px;'>&nbsp;</td><td style='background-color:%s;height:25px;border:white solid 1px;border-left:white dotted 1px;'>&nbsp;</td></tr>"%(item12,number2,self.color3,self.color3)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(number2+1,totalBrace)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d>?</td></tr>"%(number2+1)
        self.solution_text = self.solution_text + "</table><br>"
        #end of model

        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "%d &nbsp;&times;&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number3,number2,number3*number2)
        self.solution_text = self.solution_text + "%s %s %d %s.<br><br>"%(item3,item11,number3*number2,item6)
        self.solution_text = self.solution_text + "%d &nbsp;+&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number3*number2,number1,answer)
        self.solution_text = self.solution_text + "%s %d %s."%(item9,answer,item10)
        self.solution_text = self.solution_text + "</font>" 

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType25(self):       
        '''e.g.:
        [Person.Unclename] had 795 <bananas>.
        He <separated> 45 <ripe bananas>.
        He <sold the remaining bananas equally to> 5 <fruit stalls>.
        How <many bananas did each fruit stall get>?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.UncleName)
        
        self.items = [['bananas','separated','ripe bananas','sold the remaining bananas equally to','fruit stalls','many bananas did each fruit stall get','bananas','sold','Each fruit stall got','bananas',''],
                      ['eggs','threw away','rotten ones','sold the remaining eggs equally to','grocery stores','many eggs did each grocery store get','eggs','sold','Each grocery store got','eggs',''],
                      ['packets of chalk','sold','packets of chalk to a bookshop','supplied the rest of the packets equally to','schools','many packets of chalk did each school receive','packets','supplied','Each school received','packets of chalk',''],
                      ['rolls of tape','kept','rolls of tape for himself','packed the remaining rolls of tape equally into','cartons','many rolls did he pack into each carton','rolls','packed','He packed','rolls in each carton',''],
                      ['pineapples','sold','pineapples to a bakery','distributed the remaining pineapples equally among','supermarkets','many pineapples did each supermarket receive','pineapples','distributed','Each supermarket received','pineapples',''],
                      ['toy cars','sold','toy cars to a toyshop','packed the remaining toy cars equally into','boxes','many toy cars did he pack in each box','toy cars','packed','He packed','toy cars in each box',''],
                      ['T-shirts','donated','T-shirts to a charity','sold the remaining T-shirts equally to','department stores','many T-shirts did each department store get','T-shirts','sold','Each department store got','T-shirts',''],
                      ["<font class='litreFont'>l</font>&nbsp; of milk",'kept',"<font class='litreFont'>l</font>&nbsp; of milk for himself",'sold the remaining milk equally to','ice cream shops','much milk did each ice cream shop get',"<font class='litreFont'>l</font>",'sold','Each ice cream shop got',"<font class='litreFont'>l</font>&nbsp; of milk","<font class='litreFont'>l</font>"],
                      ['kg of rice','gave away','kg of rice to his neighbours','sold the remaining rice equally to','hawkers at a food court','much rice did each hawker get','kg','sold','Each hawker got','kg of rice','kg'],
                      ['m of rope','gave','m of the rope to his brother','cut the remaining rope into','equal pieces','long was each piece','m','cut','Each piece was','m long','m']]
        
        self.item = random.choice(self.items)
        
        self.number1 = randint(5,8)
        self.answer = randint(50,100)        
        self.number2 = randint(50,100)
        self.number3 = self.number1*self.answer + self.number2
                             
        self.problem = "%s had %d %s.<br><br>"%(self.name,self.number3,self.item[0])
        self.problem = self.problem + "He %s %d %s.<br><br>"%(self.item[1],self.number2,self.item[2])
        self.problem = self.problem + "He %s %d %s.<br><br>"%(self.item[3],self.number1,self.item[4])
        self.problem = self.problem + "How %s?"%(self.item[5])
        
        self.unit = self.item[6]
        self.dollar_unit = ""
          
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType25(self.problem,self.answer,self.number1,self.number2,self.number3,self.item[0],self.item[7],self.item[8],self.item[9],self.item[10],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType25",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,
                'unit':self.unit,'dollar_unit':self.dollar_unit}

    def ExplainType25(self,problem,answer,number1,number2,number3,item0,item7,item8,item9,item10,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        #beginning of model
        self.colors = random.choice([['tomato','orange','peru'],['blueviolet','violet','darkorchid'],['purple','plum','mediumvioletred'],['darkturquoise','dodgerblue','darkslateblue'],['mediumorchid','mediumpurple','palevioletred'],['chocolate','burlywood','brown'],['deeppink','lightpink','hotpink']])
        self.color1 = self.colors[0]
        self.color2 = self.colors[1]

        if answer>=number2:
            answerBrace = 'small'
            number2Brace = 'extrasmall'
            totalBrace = 'small%dextrasmall1'%(number1)
        else:
            answerBrace = 'small'
            number2Brace = 'small1extrasmall1'
            totalBrace = 'small%dextrasmall1'%(number1+1)

        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td colspan=%d>%d %s</td></tr>"%(number1+1,number3,item10)
        self.solution_text = self.solution_text + "<tr><td colspan=%d style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(number1+1,totalBrace)
        self.solution_text = self.solution_text + "<tr><td style='background-color:%s;height:25px;border:white solid 1px;'>&nbsp;</td>"%(self.color2)
        for x in range(0, number1):
            self.solution_text = self.solution_text + "<td style='background-color:%s;height:25px;border:white solid 1px;width:52px;'>&nbsp;</td>"%(self.color1)
        self.solution_text = self.solution_text + "</tr>"
        self.solution_text = self.solution_text + "<tr><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_%s.png' /></td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(number2Brace,answerBrace)
        self.solution_text = self.solution_text + "<tr><td>%d %s</td><td>?</td></tr>"%(number2,item10)
        self.solution_text = self.solution_text + "</table><br><br>"
        #end of model

        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "%d &nbsp;&minus;&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number3,number2,number3-number2)
        self.solution_text = self.solution_text + "He %s %d %s altogether.<br><br>"%(item7,number3-number2,item0)
        self.solution_text = self.solution_text + "%d &nbsp;&divide;&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number3-number2,number1,answer)
        self.solution_text = self.solution_text + "%s %d %s."%(item8,answer,item9)
        self.solution_text = self.solution_text + "</font>" 

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType26(self):       
        '''e.g.:
        [Person.Auntyname] <bought> 3 <boxes of oil paint>.
        <There were> 40 <bottles of oil paint in each box>.
        <She divided the bottles> equally among 6 <pupils>.
        How many <bottles did each pupil receive>?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.AuntyName)
        
        self.items = [['bought','boxes of oil paint','There were','bottles of oil paint in each box','She divided the bottles','pupils','bottles did each pupil','bottles','pupil'],
                      ['bought','packets of glue sticks','Each packet had','glue sticks','The glue sticks were shared','sisters','glue sticks did each sister','glue sticks','sister'],
                      ['got','jars of tarts from a friend','There were','tarts in each jar','The tarts were divided','children','tarts did each child','tarts','child'],
                      ['had','packs of paintbrushes','There were','paintbrushes in each pack','She divided the paintbrushes','students','paintbrushes did each student','paintbrushes','student'],
                      ['had','bundles of sticks','There were','sticks in each bundle','The sticks were divided','cousins','sticks did each cousin','sticks','cousin'],
                      ['had','packets of bookmarks','Each packet had','bookmarks','The bookmarks were divided','of her nieces','bookmarks did each niece','bookmarks','niece'],
                      ['had','boxes of building blocks','Each box had','building blocks','The building blocks were shared','boys','building blocks did each boy','building blocks','boy'],
                      ['baked','trays of muffins','Each tray had','muffins','She divided the muffins','girls','muffins did each girl','muffins','girl'],
                      ['fried','bags of nuggets','Each bag had','nuggets','The nuggets were shared','brothers','nuggets did each brother','nuggets','brother'],
                      ['had','stack of colour sheets','Each stack had','colour sheets','The colour sheets were divided','kids','colour sheets did each kid','colour sheets','kid']]
        
        self.item = random.choice(self.items)
        
        self.number1 = randint(3,8)
        self.number3 = randint(4,9)
        
        while self.number1==self.number3:
            self.number3 = randint(4,9)
        
        self.number2 = random.randrange(self.number3*3,99,self.number3)      
                                     
        self.problem = "%s %s %d %s.<br><br>"%(self.name,self.item[0],self.number1,self.item[1])
        self.problem = self.problem + "%s %d %s.<br><br>"%(self.item[2],self.number2,self.item[3])
        self.problem = self.problem + "%s equally among %d %s.<br><br>"%(self.item[4],self.number3,self.item[5])
        self.problem = self.problem + "How many %s receive?"%(self.item[6])
        
        self.answer = (self.number1 * self.number2)/self.number3 
        
        self.unit = self.item[7]
        self.dollar_unit = ""
          
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType26(self.problem,self.answer,self.number1,self.number2,self.number3,self.item[7],self.item[8],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType26",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,
                'unit':self.unit,'dollar_unit':self.dollar_unit}

    def ExplainType26(self,problem,answer,number1,number2,number3,item7,item8,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        #beginning of model 1
        self.colors = random.choice([['tomato','orange','peru'],['blueviolet','violet','darkorchid'],['purple','plum','mediumvioletred'],['darkturquoise','dodgerblue','darkslateblue'],['mediumorchid','mediumpurple','palevioletred'],['chocolate','burlywood','brown'],['deeppink','lightpink','hotpink']])
        self.color1 = self.colors[0]

        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>%d</td></tr>"%(number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_small.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px;'>%s</td>"%(item7)
        for x in range(0, number1):
            self.solution_text = self.solution_text + "<td style='background-color:%s;height:25px;border:white solid 1px;width:52px;'>&nbsp;</td>"%(self.color1)
        self.solution_text = self.solution_text + "</tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_small%d.png' /></td></tr>"%(number1,number1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d>? (a)</td></tr>"%(number1)
        self.solution_text = self.solution_text + "</table><br>"
        #end of model 1

        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "%d &nbsp;&times;&nbsp; %d &nbsp;=&nbsp; %d &nbsp;&nbsp; (a)<br>"%(number2,number1,number2*number1)
        self.solution_text = self.solution_text + "There were %d %s altogether.<br><br>"%(number2*number1,item7)
        self.solution_text = self.solution_text + "</font>"
        
        #beginning of model 2
        cellWidth = (52*number1)/number3
        self.solution_text = self.solution_text + "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d>%d</td></tr>"%(number3,number1*number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_small%d.png' /></td></tr>"%(number3,number1)
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px;'>%s</td>"%(item7)
        for x in range(0, number3):
            self.solution_text = self.solution_text + "<td style='background-color:%s;height:25px;border:white solid 1px;width:%dpx'>&nbsp;</td>"%(self.color1,cellWidth)
        self.solution_text = self.solution_text + "</tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td><img src='/images/explanation/P3_model_down_brace_small%dto%d.png' /></td></tr>"%(number1,number3)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='vertical-align:top;padding-top:0px;'>?</td></tr>"
        self.solution_text = self.solution_text + "</table><br>"
        #end of model 2

        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "%d &nbsp;&divide;&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number2*number1,number3,answer)
        self.solution_text = self.solution_text + "Each %s received %d %s."%(item8,answer,item7)
        self.solution_text = self.solution_text + "</font>" 

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType27(self):       
        '''e.g.:
        [Person.Boyname] bought 6 <boxes> of <sharpeners>.
        Each <box> contained 36 <sharpeners>.
        He packed the <sharpeners> into <packets> of 8 <sharpeners> each.
        How many <packets> did he get?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.BoyName)
        
        self.items = [['boxes','sharpeners','box','packets','packet'],['boxes','shuttlecocks','box','cases','case'],
                      ['bags','balls','bag','packets','packet'],['bags','plums','bag','punnets','punnet'],['crates','soda bottles','crate','packs','pack'],
                      ['cartons','books','carton','packs','pack'],['trays','cupcakes','tray','bags','bag'],['baskets','eggs','basket','trays','tray'],
                      ['bunches','roses','bunch','bouquets','bouquet'],['jars','cookies','jar','bags','bag']]
        
        self.item = random.choice(self.items)
        
        self.number1 = randint(3,6)
        self.number3 = randint(self.number1+1,9)
        self.number2 = random.randrange(self.number3*3,99,self.number3)      
                                     
        self.problem = "%s bought %d %s of %s.<br><br>"%(self.name,self.number1,self.item[0],self.item[1])
        self.problem = self.problem + "Each %s contained %d %s.<br><br>"%(self.item[2],self.number2,self.item[1])
        self.problem = self.problem + "He packed the %s into %s of %d %s each.<br><br>"%(self.item[1],self.item[3],self.number3,self.item[1])
        self.problem = self.problem + "How many %s did he get?"%(self.item[3])
        
        self.answer = (self.number1 * self.number2)/self.number3 
        
        self.unit = self.item[3]
        self.dollar_unit = ""
          
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType27(self.problem,self.answer,self.number1,self.number2,self.number3,self.item[1],self.item[3],self.item[4],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType27",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,
                'unit':self.unit,'dollar_unit':self.dollar_unit}

    def ExplainType27(self,problem,answer,number1,number2,number3,item1,item3,item4,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        #beginning of model 1
        self.colors = random.choice([['tomato','orange','peru'],['blueviolet','violet','darkorchid'],['purple','plum','mediumvioletred'],['darkturquoise','dodgerblue','darkslateblue'],['mediumorchid','mediumpurple','palevioletred'],['chocolate','burlywood','brown'],['deeppink','lightpink','hotpink']])
        self.color1 = self.colors[0]

        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>%d</td></tr>"%(number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_medium.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px;'>%s</td>"%(item1)
        for x in range(0, number1):
            self.solution_text = self.solution_text + "<td style='background-color:%s;height:25px;border:white solid 1px;width:96px;'>&nbsp;</td>"%(self.color1)
        self.solution_text = self.solution_text + "</tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_medium%d.png' /></td></tr>"%(number1,number1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d>? (a)</td></tr>"%(number1)
        self.solution_text = self.solution_text + "</table><br>"
        #end of model 1

        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "%d &nbsp;&times;&nbsp; %d &nbsp;=&nbsp; %d &nbsp;&nbsp; (a)<br>"%(number2,number1,number2*number1)
        self.solution_text = self.solution_text + "There were %d %s altogether.<br><br>"%(number2*number1,item1)
        self.solution_text = self.solution_text + "</font>"
        
        #beginning of model 2
        self.solution_text = self.solution_text + "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0'>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=5>%d</td></tr>"%(number1*number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=5 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_medium%d.png' /></td></tr>"%(number1)
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px;'>%s</td><td style='background-color:%s;height:20px;border:white solid 1px;width:31px;padding-bottom:5px;'>%d</td><td style='background-color:%s;height:20px;border:white solid 1px;width:31px;padding-bottom:5px;'>%d</td><td colspan=2 style='height:20px;border:white solid 1px;padding-bottom:5px;'>. . . . .</td><td style='background-color:%s;height:20px;border:white solid 1px;width:31px;padding-bottom:5px'>%d</td></tr>"%(item1,self.color1,number3,self.color1,number3,self.color1,number3)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td><img src='/images/explanation/P3_model_down_brace_extrasmall.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=3 style='text-align:left;white-space:nowrap;'>1 %s</td></tr>"%(item4)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=5><img src='/images/explanation/P3_model_down_brace_medium%d.png' /></td></tr>"%(number1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=5>? %s</td></tr>"%(item3)
        self.solution_text = self.solution_text + "</table><br><br>"
        #end of model 2

        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "%d &nbsp;&divide;&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number2*number1,number3,answer)
        self.solution_text = self.solution_text + "He got %d %s."%(answer,item3)
        self.solution_text = self.solution_text + "</font>" 

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType28(self):       
        '''e.g.:
        A <farmer> <has> 220 <chickens>, <ducks> and <geese>..
        He <has> <twice> as many <chickens> as <ducks>.
        There are 40 <geese>.
        How many <ducks> are there?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.items = [['farmer','has','chickens','ducks','geese'],['florist','has','roses','orchids','lilies'],
                      ['fruit vendor','has','apples','oranges','watermelons'],['vegetable vendor','has','tomatoes','potatoes','pumpkins'],
                      ['teacher','has','pencils','sharpeners','markers'],['carpenter','has','nails','screws','bolts'],
                      ['tailor','has','spools of thread','needles','measuring tapes'],['baker','bakes','pies','bread rolls','mini cakes'],
                      ['boy','collects','stamps','stickers','coins'],['plumber','has','taps','showerheads','pipes']]
        
        self.item = random.choice(self.items)
        
        self.times = random.choice([[2,"twice"],[3,"thrice"],[4,"four times"]])
        
        self.number2 = randint(30,60)
        self.number1 = randint(30,60) * (self.times[0]+1) + self.number2   
                                     
        self.problem = "A %s %s a total of %d %s, %s and %s.<br><br>"%(self.item[0],self.item[1],self.number1,self.item[2],self.item[3],self.item[4])
        self.problem = self.problem + "He %s %s as many %s as %s.<br><br>"%(self.item[1],self.times[1],self.item[2],self.item[3])
        self.problem = self.problem + "There are %d %s.<br><br>"%(self.number2,self.item[4])
        self.problem = self.problem + "How many %s are there?"%(self.item[3])
        
        self.answer = (self.number1 - self.number2)/(self.times[0]+1)
        
        self.unit = self.item[3]
        self.dollar_unit = ""
          
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType28(self.problem,self.answer,self.number1,self.number2,self.times[0],self.item[2],self.item[3],self.item[4],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType28",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,
                'unit':self.unit,'dollar_unit':self.dollar_unit}

    def ExplainType28(self,problem,answer,number1,number2,times,item2,item3,item4,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        #beginning of model
        self.colors = random.choice([['tomato','orange','peru'],['blueviolet','violet','darkorchid'],['purple','plum','mediumvioletred'],['darkturquoise','dodgerblue','darkslateblue'],['mediumorchid','mediumpurple','palevioletred'],['chocolate','burlywood','brown'],['deeppink','lightpink','hotpink']])
        self.color1 = self.colors[0]
        self.color2 = self.colors[1]
        self.color3 = self.colors[2]

        if answer>=number2:
            answerBrace = 'small'
            number2Brace = 'extrasmall'
            number2Colspan = 1
        else:
            answerBrace = 'small'
            number2Brace = 'small1extrasmall1'
            number2Colspan = 3

        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2>?</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(answerBrace)
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px;'>%s</td><td colspan=2 style='background-color:%s;height:25px;border:white solid 1px;'>&nbsp;</td><td colspan=%d>&nbsp;</td><td>&nbsp;&nbsp;</td><td rowspan=5 style='padding:0;padding-top:3px;vertical-align:middle'><img src='/images/explanation/P3_model_right_brace_5row.png' /></td><td rowspan=5 style='padding:0;vertical-align:middle'>&nbsp;%d</td></tr>"%(item3,self.color1,times+1,number1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px;'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;border-right:0;width:28px;'>&nbsp;</td><td style='background-color:%s;height:25px;border:white solid 1px;border-left:0;width:28px;'>&nbsp;</td>"%(item2,self.color2,self.color2)
        self.solution_text = self.solution_text + "<td style='background-color:%s;height:25px;border:white solid 1px;border-right:0;width:28px;'>&nbsp;</td><td style='background-color:%s;height:25px;border:white solid 1px;border-left:0;width:28px;'>&nbsp;</td>"%(self.color2,self.color2)
        for x in range(2, times):
            self.solution_text = self.solution_text + "<td style='background-color:%s;height:25px;border:white solid 1px;width:52px;'>&nbsp;</td>"%(self.color2)
        self.solution_text = self.solution_text + "</tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px;'>%s</td><td colspan=%d style='background-color:%s;height:25px;border:white solid 1px;'>&nbsp;</td></tr>"%(item4,number2Colspan,self.color3)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(number2Colspan,number2Brace)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d>%d</td></tr>"%(number2Colspan,number2)
        self.solution_text = self.solution_text + "</table><br><br>"
        #end of model

        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "%d &nbsp;&minus;&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number1,number2,number1-number2)
        self.solution_text = self.solution_text + "There are %d %s and %s.<br><br>"%(number1-number2,item2,item3)
        self.solution_text = self.solution_text + "%d &nbsp;&divide;&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number1-number2,times+1,answer)
        self.solution_text = self.solution_text + "There are %d %s."%(answer,item3)
        self.solution_text = self.solution_text + "</font>" 

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType29(self):       
        '''e.g.:
        [Person.Boyname1] had 328 <bookmarks> and [Person.Boyname2] had 476 <bookmarks>.
        They divided the <bookmarks> equally between themselves.
        How many <bookmarks> did [Person.Boyname1] get?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.names = random.sample(PersonName.BoyName,2)
        
        self.items = ['bookmarks','sweets','icecream sticks','water chestnuts','pears','coins','cans','can tabs','ketchup sachets','forks','spoons','twigs','mints','plasters','cards']
        
        self.item = random.choice(self.items)
                
        self.number1 = random.randrange(200,400,2)
        self.number2 = random.randrange(200,400,2)
        
        while self.number1 == self.number2:
            self.number2 = random.randrange(200,400,2)
                                     
        self.problem = "%s had %d %s and %s had %d %s.<br><br>"%(self.names[0],self.number1,self.item,self.names[1],self.number2,self.item)
        self.problem = self.problem + "They divided the %s equally between themselves.<br><br>"%(self.item)
        self.problem = self.problem + "How many %s did each boy get?"%(self.item)
        
        self.answer = (self.number1 +  self.number2)/2
        
        self.unit = self.item
        self.dollar_unit = ""
          
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType29(self.problem,self.answer,self.names,self.number1,self.number2,self.item,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType29",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,
                'unit':self.unit,'dollar_unit':self.dollar_unit}

    def ExplainType29(self,problem,answer,names,number1,number2,item,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        #beginning of model 1
        self.colors = random.choice([['tomato','orange','peru'],['blueviolet','violet','darkorchid'],['purple','plum','mediumvioletred'],['darkturquoise','dodgerblue','darkslateblue'],['mediumorchid','mediumpurple','palevioletred'],['chocolate','burlywood','brown'],['deeppink','lightpink','hotpink']])
        self.color1 = self.colors[0]
        self.color2 = self.colors[1]
        self.color3 = self.colors[2]

        if number1>number2:
            number1Brace = 'large'
            number2Brace = 'medium'
        else:
            number1Brace = 'medium'
            number2Brace = 'large'

        self.solution_text = "<br><font class='ExplanationFont'><u>Before</u></font><br>"
        self.solution_text = self.solution_text + "<table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>%d</td><td>%d</td></tr>"%(number1,number2)
        self.solution_text = self.solution_text + "<tr><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(number1Brace,number2Brace)
        self.solution_text = self.solution_text + "<tr><td style='background-color:%s;height:25px;border:white solid 1px;'><font style='font-size:0.8em;'>%s</font></td><td style='background-color:%s;height:25px;border:white solid 1px;'><font style='font-size:0.8em;'>%s</font></td></tr>"%(self.color1,names[0],self.color2,names[1])
        self.solution_text = self.solution_text + "<tr><td colspan=2 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_large1medium1.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td colspan=2>? (a)</td></tr>"
        self.solution_text = self.solution_text + "</table><br><br>"
        #end of model 1

        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "%d &nbsp;+&nbsp; %d &nbsp;=&nbsp; %d &nbsp;&nbsp; (a)<br>"%(number1,number2,number1+number2)
        self.solution_text = self.solution_text + "They had %d %s altogether.<br><br><br>"%(number1+number2,item)
        self.solution_text = self.solution_text + "</font>"

        #beginning of model 2
        self.solution_text = self.solution_text + "<font class='ExplanationFont'><u>After</u></font><br>"
        self.solution_text = self.solution_text + "<table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td colspan=2>%d</td></tr>"%(number1+number2)
        self.solution_text = self.solution_text + "<tr><td colspan=2 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_large1medium1.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='background-color:%s;height:25px;border:white solid 1px;'><font style='font-size:0.8em;'>%s</font></td><td style='background-color:%s;height:25px;border:white solid 1px;width:130px;'><font style='font-size:0.8em;'>%s</font></td></tr>"%(self.color3,names[0],self.color3,names[1])
        self.solution_text = self.solution_text + "<tr><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_medium1extrasmall1.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td>?</td></tr>"
        self.solution_text = self.solution_text + "</table><br><br>"
        #end of model 2

        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "%d &nbsp;&divide;&nbsp; 2 &nbsp;=&nbsp; %d<br>"%(number1+number2,answer)
        self.solution_text = self.solution_text + "Each boy got %d %s."%(answer,item)
        self.solution_text = self.solution_text + "</font>" 

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType30(self):       
        '''e.g.:
        [Person.Boyname1], [Person.Boyname2] and [Person.Boyname3] <save> $360 altogether.
        [Person.Boyname1] <saves> 4 times as much money as [Person.Boyname3].
        [Person.Boyname2] <saves> $45.
        How much money does [Person.Boyname3] <save>?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.names = random.sample(PersonName.BoyName,3)
        
        self.items = [['save','saves'],['spend','spends'],['give away','gives away'],['earn','earns'],['get','gets'],
                      ['receive','receives'],['donate','donates'],['deposit','deposits'],['count','counts'],['win','wins']]
        
        self.item = random.choice(self.items)
                
        self.multiplier = randint(2,8)
        self.number3 = randint(20,90)
        self.number2 = randint(20,2*self.number3)
        self.number1 = self.multiplier * self.number3
        self.total = self.number1 + self.number2 + self.number3
                                     
        self.problem = "%s, %s and %s %s $%d altogether.<br><br>"%(self.names[0],self.names[1],self.names[2],self.item[0],self.total)
        self.problem = self.problem + "%s %s %d times as much money as %s.<br><br>"%(self.names[0],self.item[1],self.multiplier,self.names[2])
        self.problem = self.problem + "%s %s $%d.<br><br>"%(self.names[1],self.item[1],self.number2)
        self.problem = self.problem + "How much money does %s %s?"%(self.names[2],self.item[0])
        
        self.answer = self.number3
        
        self.unit = ""
        self.dollar_unit = "$"
          
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType30(self.problem,self.answer,self.names,self.total,self.multiplier,self.number2,self.item[0],self.item[1],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType30",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,
                'unit':self.unit,'dollar_unit':self.dollar_unit}

    def ExplainType30(self,problem,answer,names,total,multiplier,number2,item0,item1,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        #beginning of model
        self.colors = random.choice([['tomato','orange','peru'],['blueviolet','violet','darkorchid'],['purple','plum','mediumvioletred'],['darkturquoise','dodgerblue','darkslateblue'],['mediumorchid','mediumpurple','palevioletred'],['chocolate','burlywood','brown'],['deeppink','lightpink','hotpink']])
        self.color1 = self.colors[0]
        self.color2 = self.colors[1]
        self.color3 = self.colors[2]

        if answer>=number2:
            answerBrace = 'small'
            number2Brace = 'extrasmall'
            number2Colspan = 1
        else:
            answerBrace = 'small'
            number2Brace = 'small1extrasmall1'
            number2Colspan = 3

        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2>?</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(answerBrace)
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px;'>%s</td><td colspan=2 style='background-color:%s;height:25px;border:white solid 1px;'>&nbsp;</td><td colspan=%d>&nbsp;</td><td>&nbsp;&nbsp;</td><td rowspan=5 style='padding:0;padding-top:3px;vertical-align:middle'><img src='/images/explanation/P3_model_right_brace_5row.png' /></td><td rowspan=5 style='padding:0;vertical-align:middle'>&nbsp;$%d</td></tr>"%(names[2],self.color1,multiplier+1,total)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px;'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;border-right:0;width:28px;'>&nbsp;</td><td style='background-color:%s;height:25px;border:white solid 1px;border-left:0;width:28px;'>&nbsp;</td>"%(names[0],self.color2,self.color2)
        self.solution_text = self.solution_text + "<td style='background-color:%s;height:25px;border:white solid 1px;border-right:0;width:28px;'>&nbsp;</td><td style='background-color:%s;height:25px;border:white solid 1px;border-left:0;width:28px;'>&nbsp;</td>"%(self.color2,self.color2)
        for x in range(2,multiplier):
            self.solution_text = self.solution_text + "<td style='background-color:%s;height:25px;border:white solid 1px;width:52px;'>&nbsp;</td>"%(self.color2)
        self.solution_text = self.solution_text + "</tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px;'>%s</td><td colspan=%d style='background-color:%s;height:25px;border:white solid 1px;'>&nbsp;</td></tr>"%(names[1],number2Colspan,self.color3)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(number2Colspan,number2Brace)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d>$%d</td></tr>"%(number2Colspan,number2)
        self.solution_text = self.solution_text + "</table><br><br>"
        #end of model

        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "$%d &nbsp;&minus;&nbsp; $%d &nbsp;=&nbsp; $%d<br>"%(total,number2,total-number2)
        self.solution_text = self.solution_text + "%s and %s %s $%d altogether.<br><br>"%(names[0],names[2],item0,total-number2)
        self.solution_text = self.solution_text + "$%d &nbsp;&divide;&nbsp; %d &nbsp;=&nbsp; $%d<br>"%(total-number2,multiplier+1,answer)
        self.solution_text = self.solution_text + "%s %s $%d."%(names[2],item1,answer)
        self.solution_text = self.solution_text + "</font>" 

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType31(self):       
        '''e.g.:
        [Person.Name1], [Person.Name1] and [Person.Name3] have 150 <marbles> altogether.
        [Person.Name1] has 30 fewer <marbles> than [Person.Name2].
        [Person.Name3] has 3 times as many <marbles> as [Person.Name1].
        How many <marbles> does [Person.Name1] have?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.names = random.sample(PersonName.BoyName,3)
        
        self.items = ['marbles','bookmarks','drawing sheets','fishes','bows','breadsticks','darts','markers','envelopes','brushes']
        
        self.item = random.choice(self.items)
                
        self.multiplier = randint(2,7)
        self.number1 = randint(20,90)
        self.fewer = randint(10,self.number1-10)
        self.number2 = self.number1 + self.fewer
        self.number3 = self.multiplier * self.number1
        self.total = self.number1 + self.number2 + self.number3
                                     
        self.problem = "%s, %s and %s have %d %s altogether.<br><br>"%(self.names[0],self.names[1],self.names[2],self.total,self.item)
        self.problem = self.problem + "%s has %d fewer %s than %s.<br><br>"%(self.names[0],self.fewer,self.item,self.names[1])
        self.problem = self.problem + "%s has %d times as many %s as %s.<br><br>"%(self.names[2],self.multiplier,self.item,self.names[0])
        self.problem = self.problem + "How many %s does %s have?"%(self.item,self.names[0])
        
        self.answer = self.number1
        
        self.unit = self.item
        self.dollar_unit = ""
          
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType31(self.problem,self.answer,self.names,self.total,self.fewer,self.multiplier,self.item,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType31",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,
                'unit':self.unit,'dollar_unit':self.dollar_unit}

    def ExplainType31(self,problem,answer,names,total,fewer,multiplier,item,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        #beginning of model
        self.colors = random.choice([['tomato','orange','peru'],['blueviolet','violet','darkorchid'],['purple','plum','mediumvioletred'],['darkturquoise','dodgerblue','darkslateblue'],['mediumorchid','mediumpurple','palevioletred'],['chocolate','burlywood','brown'],['deeppink','lightpink','hotpink']])
        self.color1 = self.colors[0]
        self.color2 = self.colors[1]
        self.color3 = self.colors[2]

        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>&nbsp;</td><td>%d</td></tr>"%(fewer)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_extrasmall.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px;'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;border-right:white dotted 1px;'>&nbsp;</td><td style='background-color:%s;height:25px;border:white solid 1px;border-left:white dotted 1px;'>&nbsp;</td><td colspan=%d>&nbsp;</td><td>&nbsp;&nbsp;</td><td rowspan=5 style='padding:0;padding-top:3px;vertical-align:middle'><img src='/images/explanation/P3_model_right_brace_5row.png' /></td><td rowspan=5 style='padding:0;vertical-align:middle'>&nbsp;%d</td></tr>"%(names[1],self.color1,self.color1,multiplier,total)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px;'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;'>&nbsp;</td></tr>"%(names[0],self.color3)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px;'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;'>&nbsp;</td><td style='background-color:%s;height:25px;border:white solid 1px;border-right:0;width:28px;'>&nbsp;</td><td style='background-color:%s;height:25px;border:white solid 1px;border-left:0;width:28px;'>&nbsp;</td>"%(names[2],self.color2,self.color2,self.color2)
        for x in range(2,multiplier):
            self.solution_text = self.solution_text + "<td style='background-color:%s;height:25px;border:white solid 1px;width:56px;'>&nbsp;</td>"%(self.color2)
        self.solution_text = self.solution_text + "</tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_small.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>?</td></tr>"
        self.solution_text = self.solution_text + "</table><br><br>"
        #end of model

        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;"
        self.solution_text = self.solution_text + "%d &nbsp;&minus;&nbsp; %d &nbsp;=&nbsp; %d<br><br>"%(total,fewer,total-fewer)
        self.solution_text = self.solution_text + "</font>"

        self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>%d units</td><td style='padding-left:0px; padding-right:0px; padding-top:3px'><img src='/images/explanation/right_arrow_2.png' /></td><td style='text-align:left'>%d</td></tr>"%(multiplier+2,total-fewer)
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>1 unit</td><td style='padding-left:0px; padding-right:0px; padding-top:3px'><img src='/images/explanation/right_arrow_2.png' /></td><td style='text-align:left'>%d &nbsp;&divide;&nbsp; %d</td></tr>"%(total-fewer,multiplier+2)
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px;text-align:right'>=</td><td style='text-align:left'>%d</td></tr>"%(answer)
        self.solution_text = self.solution_text + "</table><br>"
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;"
        self.solution_text = self.solution_text + "%s has %d %s."%(names[0],answer,item)
        self.solution_text = self.solution_text + "</font>"
        self.solution_text = self.solution_text + "<br><br><br>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType32(self):       
        '''e.g.:
        <There are >16 <men> and 25 <women in a hall>.
        Each of them <has> 8 <files>.
        How many <files> do they <have> altogether?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.names = random.sample(PersonName.BoyName,3)
        
        self.items = [['There are ','men','women in a hall','has','files','have','There are','men and women in the hall','men','women'],
                      ['There are ','boys','girls at a party','receives','chocolate bars','receive','There are','children at the party','boys','girls'],
                      ['There are ','women','men at an office','has','reference books','have','There are','women and men at the office','women','men'],
                      ['','children','adults go to a library','borrows','books','borrow','','people go to the library','children','adults'],
                      ['','women','men go to a sale','buys','T-shirts','buy','','women and men go to the sale','women','men'],
                      ['','adults','children go to a bakery','buys','pastries','buy','','people go to the bakery','adults','children'],
                      ['','girls','boys attend an art class','receives','sheets of craft paper','receive','','children attend the art class','girls','boys'],
                      ['','children','adults participate in a race','receives','goodies','receive','','people participate in the race','children','adults'],
                      ['','boys','girls take part in a tree planting event','plants','trees','plant','','children take part in the event','boys','girls'],
                      ['','adults','children take part in a kite flying festival','has','kites','have','','people take part in the festival','adults','children']]
        
        self.item = random.choice(self.items)
                
        self.number1 = randint(20,70)
        self.number2 = randint(20,70)
        self.number3 = randint(5,9)
                                     
        self.problem = "%s%d %s and %d %s.<br><br>"%(self.item[0],self.number1,self.item[1],self.number2,self.item[2])
        self.problem = self.problem + "Each of them %s %d %s.<br><br>"%(self.item[3],self.number3,self.item[4])
        self.problem = self.problem + "How many %s do they %s altogether?"%(self.item[4],self.item[5])
        
        self.answer = (self.number1+self.number2)*self.number3
        
        self.unit = self.item[4]
        self.dollar_unit = ""
          
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType32(self.problem,self.answer,self.number1,self.number2,self.number3,self.item[4],self.item[5],self.item[6],self.item[7],self.item[8],self.item[9],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType32",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,
                'unit':self.unit,'dollar_unit':self.dollar_unit}

    def ExplainType32(self,problem,answer,number1,number2,number3,item4,item5,item6,item7,item8,item9,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        #beginning of model
        self.colors = random.choice([['tomato','orange'],['blueviolet','violet'],['purple','plum'],['darkturquoise','dodgerblue'],['mediumorchid','mediumpurple'],['chocolate','burlywood'],['deeppink','lightpink']])
        self.color1 = self.colors[0]
        self.color2 = self.colors[1]
        
        if number1>number2:
            firstBrace = 'large'
            secondBrace = 'medium'
            totalBrace = 'large1medium1'
        elif number1==number2:
            firstBrace = 'medium'
            secondBrace = 'medium'
            totalBrace = 'medium2'
        else:
            firstBrace = 'medium'
            secondBrace = 'large'
            totalBrace = 'large1medium1'

        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>%d</td><td>%d</td></tr>"%(number1,number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(firstBrace,secondBrace)
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;white-space:nowrap;padding-right:7px'>&nbsp;</td><td style='background-color:%s;height:25px;border:white solid 1px;'><font style='font-size:0.8em;'>%s</font></td><td style='background-color:%s;height:25px;border:white solid 1px;'><font style='font-size:0.8em;'>%s</font></td></tr>"%(self.color1,item8,self.color2,item9)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(totalBrace)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2>? (a)</td></tr>"
        self.solution_text = self.solution_text + "</table><br><br>"
        #end of model

        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "%d &nbsp;+&nbsp; %d &nbsp;=&nbsp; %d &nbsp;&nbsp; (a)<br>"%(number1,number2,number1+number2)
        self.solution_text = self.solution_text + "%s %d %s.<br><br>"%(item6,number1+number2,item7)
        self.solution_text = self.solution_text + "%d &nbsp;&times;&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number1+number2,number3,answer)
        self.solution_text = self.solution_text + "They %s %d %s altogether."%(item5,answer,item4)
        self.solution_text = self.solution_text + "</font>" 

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType33(self):       
        '''e.g.:
        <A farmer> <harvested> 487 <mangoes>.
        He <harvested> 4 times as many <oranges as mangoes>.
        How many more <oranges than mangoes did he harvest>?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.items = [['A farmer','harvested','mangoes','oranges as mangoes','oranges than mangoes did he harvest','oranges than mangoes','oranges'],
                      ['A carpenter','made','tables','tables as chairs','chairs than tables did he make','chairs than tables','chairs'],
                      ['A plumber','repaired','pipes','taps as pipes','taps than pipes did he repair','taps than pipes','taps'],
                      ['An electrician','fix','fans','lights as fans','lights than fans did he fix','lights than fans','lights'],
                      ['A painter','painted','doors','windows as doors','windows than doors did he paint','windows than doors','windows'],
                      ['A baker','baked','cakes','cookies as cakes','cookies than cakes did he bake','cookies than cakes','cookies'],
                      ['A doctor','examined','children','adults as children','adults than children did he examine','adults than children','adults'],
                      ['A fisherman','caught','groupers','pomfrets as groupers','pomfrets than groupers did he catch','pomfrets than groupers','pomfrets'],
                      ['A boy','collected','seashells','marbles as seashells','marbles than seashells did he collect','marbles than seashells','marbles'],
                      ['A vegetable vendor','sold','carrots','tomatoes as carrots','potatoes than carrots did he sell','potatoes than carrots','tomatoes']]

        self.item = random.choice(self.items)
                
        self.number1 = randint(200,900)
        self.number2 = randint(3,9)
                                     
        self.problem = "%s %s %d %s.<br><br>"%(self.item[0],self.item[1],self.number1,self.item[2])
        self.problem = self.problem + "He %s %d times as many %s.<br><br>"%(self.item[1],self.number2,self.item[3])
        self.problem = self.problem + "How many more %s?"%(self.item[4])
        
        self.answer = (self.number1*self.number2)-self.number1
        
        self.unit = ""
        self.dollar_unit = ""
          
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType33(self.problem,self.answer,self.number1,self.number2,self.item[1],self.item[2],self.item[5],self.item[6],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType33",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,
                'unit':self.unit,'dollar_unit':self.dollar_unit}

    def ExplainType33(self,problem,answer,number1,number2,item1,item2,item5,item6,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        #beginning of model
        self.colors = random.choice([['tomato','orange','peru'],['blueviolet','violet','darkorchid'],['purple','plum','mediumvioletred'],['darkturquoise','dodgerblue','darkslateblue'],['mediumorchid','mediumpurple','palevioletred'],['chocolate','burlywood','brown'],['deeppink','lightpink','hotpink']])
        self.color1 = self.colors[0]
        self.color2 = self.colors[1]

        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>%d</td><td colspan=%d>?</td></tr>"%(number1,number2-1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_small.png' /></td><td colspan=%d style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_small%d.png' /></td></tr>"%(number2-1,number2-1)
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px;'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;'>&nbsp;</td></tr>"%(item2,self.color1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px;'>%s</td>"%(item6)
        for x in range(0, number2):
            self.solution_text = self.solution_text + "<td style='background-color:%s;height:25px;border:white solid 1px;width:52px;'>&nbsp;</td>"%(self.color2)
        self.solution_text = self.solution_text + "</tr>"
        self.solution_text = self.solution_text + "</table><br><br>"
        #end of model

        self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>1 unit</td><td style='padding-left:0px; padding-right:0px; padding-top:3px'><img src='/images/explanation/right_arrow_2.png' /></td><td style='text-align:left'>%d</td></tr>"%(number1)
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>%d units</td><td style='padding-left:0px; padding-right:0px; padding-top:3px'><img src='/images/explanation/right_arrow_2.png' /></td><td style='text-align:left'>%d &nbsp;&times;&nbsp; %d</td></tr>"%(number2-1,number1,number2-1)
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px;text-align:right'>=</td><td style='text-align:left'>%d</td></tr>"%(answer)
        self.solution_text = self.solution_text + "</table><br>"
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;"
        self.solution_text = self.solution_text + "He %s %d more %s."%(item1,answer,item5)
        self.solution_text = self.solution_text + "</font>"
        self.solution_text = self.solution_text + "<br><br><br>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType34(self):       
        '''e.g.:
        [Person.Unclename] bought a <wallet>, a <bag> and a <suit>.
        The <wallet> cost $75.
        The <bag> cost $103 more than the <wallet>.
        The <suit> cost twice as much as the <bag>.
        Find the cost of the <suit>.'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.UncleName)
        
        self.items = [['wallet','bag','suit'],['speaker','camera','laptop'],['chair','table','sofa'],
                      ['headset','printer','cell phone'],['toy scooter','bicycle','mountain bike'],
                      ['sleeping bag','tent','waterbed'],['CD player','DVD player','TV'],['bottle of perfume','watch','bracelet'],
                      ['bedsheet','comforter','bed'],['cutlery set','crockery set','dining table set']]

        
        self.item = random.choice(self.items)
                
        self.number1 = randint(40,99)
        self.number2 = randint(150,200)
        self.times = random.choice([[2,"twice"],[3,"thrice"],[4,"4 times"]])
                                     
        self.problem = "%s bought a %s, a %s and a %s.<br><br>"%(self.name,self.item[0],self.item[1],self.item[2])
        self.problem = self.problem + "The %s cost $%d.<br><br>"%(self.item[0],self.number1)
        self.problem = self.problem + "The %s cost $%d more than the %s.<br><br>"%(self.item[1],self.number2,self.item[0])
        self.problem = self.problem + "The %s cost %s as much as the %s.<br><br>"%(self.item[2],self.times[1],self.item[1])
        self.problem = self.problem + "Find the cost of the %s."%(self.item[2])
        
        self.answer = (self.number1+self.number2)*self.times[0]
        
        self.unit = ""
        self.dollar_unit = "$"
          
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType34(self.problem,self.answer,self.number1,self.number2,self.times[0],self.item[0],self.item[1],self.item[2],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType34",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,
                'unit':self.unit,'dollar_unit':self.dollar_unit}

    def ExplainType34(self,problem,answer,number1,number2,times,item0,item1,item2,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        #beginning of model
        self.colors = random.choice([['tomato','orange','peru'],['blueviolet','violet','darkorchid'],['purple','plum','mediumvioletred'],['darkturquoise','dodgerblue','darkslateblue'],['mediumorchid','mediumpurple','palevioletred'],['chocolate','burlywood','brown'],['deeppink','lightpink','hotpink']])
        self.color1 = self.colors[0]
        self.color2 = self.colors[1]
        self.color3 = self.colors[2]

        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$%d</td><td>$%d</td></tr>"%(number1,number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_extrasmall.png' /></td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_small.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px;'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;'>&nbsp;</td></tr>"%(item0,self.color1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px;'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;border-right:white dotted 1px;'>&nbsp;</td><td style='background-color:%s;height:25px;border:white solid 1px;border-left:white dotted 1px;'>&nbsp;</td></tr>"%(item1,self.color2,self.color2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px;'>%s</td><td colspan=2 style='background-color:%s;height:25px;border:white solid 1px;'>&nbsp;</td>"%(item2,self.color3)
        for x in range(1, times):
            self.solution_text = self.solution_text + "<td style='background-color:%s;height:25px;border:white solid 1px;width:85px;'>&nbsp;</td>"%(self.color3)
        self.solution_text = self.solution_text + "</tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_small%dextrasmall%d.png' /></td></tr>"%(times+1,times,times)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d>?</td></tr>"%(times+1)
        self.solution_text = self.solution_text + "</table><br><br>"
        #end of model

        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "$%d &nbsp;+&nbsp; $%d &nbsp;=&nbsp; $%d<br>"%(number1,number2,number1+number2)
        self.solution_text = self.solution_text + "The %s cost $%d.<br><br>"%(item1,number1+number2)
        self.solution_text = self.solution_text + "$%d &nbsp;&times;&nbsp; %d &nbsp;=&nbsp; $%d<br>"%(number1+number2,times,answer)
        self.solution_text = self.solution_text + "The %s cost $%d.<br><br>"%(item2,answer)
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType35(self):       
        '''e.g.:
        [Person.Auntyname] had $450.
        She bought a <camera> and had $275 left.
        [Person.Unclename] wants to buy 4 such <cameras>.
        How much money would he need?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.names = [random.choice(PersonName.AuntyName),random.choice(PersonName.UncleName)]
        
        self.items = [['camera','cameras','camera'],['air cooler','air coolers','cooler'],['ceiling fan','ceiling fans','fan'],
                      ['printer','printers','printer'],['leather chair','leather chairs','chair'],['bag','bags','bag'],
                      ['DVD player','DVD players','player'],['watch','watches','watch'],['microwave oven','microwave ovens','oven'],['vacuum cleaner','vacuum cleaners','vacuum']]
        
        self.item = random.choice(self.items)
                
        self.number1 = random.randrange(500,1500,10)
        self.price = random.randrange(100,400,50)
        self.left = self.number1 - self.price
        self.number2 = randint(3,9)
                                     
        self.problem = "%s had $%d.<br><br>"%(self.names[0],self.number1)
        self.problem = self.problem + "She bought a %s and had $%d left.<br><br>"%(self.item[0],self.left)
        self.problem = self.problem + "%s wants to buy %d such %s.<br><br>"%(self.names[1],self.number2,self.item[1])
        self.problem = self.problem + "How much money would he need?"
        
        self.answer = self.price * self.number2
        
        self.unit = ""
        self.dollar_unit = "$"
          
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType35(self.problem,self.answer,self.names,self.number1,self.left,self.number2,self.item[0],self.item[2],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType35",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,
                'unit':self.unit,'dollar_unit':self.dollar_unit}

    def ExplainType35(self,problem,answer,names,number1,left,number2,item0,item2,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        #beginning of model 1
        self.colors = random.choice([['tomato','orange','peru'],['blueviolet','violet','darkorchid'],['purple','plum','mediumvioletred'],['darkturquoise','dodgerblue','darkslateblue'],['mediumorchid','mediumpurple','palevioletred'],['chocolate','burlywood','brown'],['deeppink','lightpink','hotpink']])
        self.color1 = self.colors[0]
        self.color2 = self.colors[1]
        
        if number1-left>=left:
            topBrace = 'small1extrasmall1'
            secondBrace = 'extrasmall'
        else:
            topBrace = 'medium1small1'
            secondBrace = 'medium'

        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2>$%d</td></tr>"%(number1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(topBrace)
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px;'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;'><font style='font-size:0.8em'>%s</font></td><td style='background-color:%s;height:25px;border:white solid 1px;'><font style='font-size:0.8em'>left</font></td></tr>"%(names[0],self.color1,item2,self.color2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_small.png' /></td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(secondBrace)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'>? (a)</td><td style='padding-bottom:3px;'>$%d</td></tr>"%(left)
        self.solution_text = self.solution_text + "</table><br><br>"
        #end of model 1

        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "$%d &nbsp;&minus;&nbsp; $%d &nbsp;=&nbsp; $%d &nbsp;&nbsp; (a)<br>"%(number1,left,number1-left)
        self.solution_text = self.solution_text + "The cost of one %s is $%d.<br><br><br>"%(item0,number1-left)
        self.solution_text = self.solution_text + "</font>"
        
        #beginning of model 2
        self.solution_text = self.solution_text + "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$%d</td></tr>"%(number1-left)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_small.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px;'>%s</td>"%(names[1])
        for x in range(0, number2):
            self.solution_text = self.solution_text + "<td style='background-color:%s;height:25px;border:white solid 1px;width:52px;'>&nbsp;</td>"%(self.color1)
        self.solution_text = self.solution_text + "</tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_small%d.png' /></td></tr>"%(number2,number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d>?</td></tr>"%(number2)
        self.solution_text = self.solution_text + "</table><br>"
        #end of model 2

        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "$%d &nbsp;&times;&nbsp; %d &nbsp;=&nbsp; $%d<br>"%(number1-left,number2,answer)
        self.solution_text = self.solution_text + "%s would need $%d.<br><br>"%(names[1],answer)
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType36(self):       
        '''e.g.:
        [Person.Unclename] had 5 <packets of sweets>.
        Each <packet> contained 120 <sweets>.
        He <kept> 174 <sweets for himself and sold the rest>.
        How many <sweets did he sell>?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.UncleName)
        
        self.items = [['packets of sweets','packet','sweets','kept','sweets for himself and sold the rest','sweets did he sell','sold','sweets'],
                      ['packets of postcards','packet','postcards','gave','postcards to his children and sold the rest','postcards did he sell','sold','postcards'],
                      ['boxes of kiwi fruits','box','kiwi fruits','threw away','kiwi fruits that were spoilt and sold the rest','kiwi fruits did he sell','sold','kiwi fruits'],
                      ['boxes of staplers','box','staplers','saved','staplers for later and sold the rest','staplers did he sell','sold','staplers'],
                      ['cartons of caps','carton','caps','gave away','caps to charity','caps had he left','had','caps left'],
                      ['cartons of tennis balls','carton','tennis balls','supplied','tennis balls to a tennis school','tennis balls had he left','had','tennis balls left'],
                      ['packs of posters','pack','posters','sold','posters','posters had he left','had','posters left'],
                      ['packs of picture frames','pack','picture frames','separated','picture frames that were damaged and put the rest on sale','picture frames were put on sale','put','picture frames on sale'],
                      ['packs of magnetic stickers','pack','magnetic stickers','sold','magnetic stickers','magnetic stickers had he left','had','magnetic stickers left'],
                      ['tanks of fishes','tank','fishes','sold','fishes','fishes had he left','had','fishes left']]
        
        self.item = random.choice(self.items)
                
        self.number1 = randint(3,9)
        self.number2 = random.randrange(120,400,10)
        self.number3 = randint(50,200)
        
        while self.number3==self.number2:
            self.number3 = randint(50,200)
                                     
        self.problem = "%s had %d %s.<br><br>"%(self.name,self.number1,self.item[0])
        self.problem = self.problem + "Each %s contained %d %s.<br><br>"%(self.item[1],self.number2,self.item[2])
        self.problem = self.problem + "He %s %d %s.<br><br>"%(self.item[3],self.number3,self.item[4])
        self.problem = self.problem + "How many %s?"%(self.item[5])
        
        self.answer = self.number1 * self.number2 - self.number3
        
        self.unit = self.item[2]
        self.dollar_unit = ""
          
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType36(self.problem,self.answer,self.number1,self.number2,self.number3,self.item[2],self.item[6],self.item[7],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType36",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,
                'unit':self.unit,'dollar_unit':self.dollar_unit}

    def ExplainType36(self,problem,answer,number1,number2,number3,item2,item6,item7,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        #beginning of model 1
        self.colors = random.choice([['tomato','orange','peru'],['blueviolet','violet','darkorchid'],['purple','plum','mediumvioletred'],['darkturquoise','dodgerblue','darkslateblue'],['mediumorchid','mediumpurple','palevioletred'],['chocolate','burlywood','brown'],['deeppink','lightpink','hotpink']])
        self.color1 = self.colors[0]
        self.color2 = self.colors[1]

        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>%d</td></tr>"%(number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_small.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px;'>%s</td>"%(item2)
        for x in range(0, number1):
            self.solution_text = self.solution_text + "<td style='background-color:%s;height:25px;border:white solid 1px;width:52px;'>&nbsp;</td>"%(self.color1)
        self.solution_text = self.solution_text + "</tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_small%d.png' /></td></tr>"%(number1,number1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d>? (a)</td></tr>"%(number1)
        self.solution_text = self.solution_text + "</table><br>"
        #end of model 1

        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "%d &nbsp;&times;&nbsp; %d &nbsp;=&nbsp; %d &nbsp;&nbsp; (a)<br>"%(number2,number1,number2*number1)
        self.solution_text = self.solution_text + "He had %d %s at first.<br><br>"%(number2*number1,item2)
        self.solution_text = self.solution_text + "</font>"
        
        #beginning of model 2
        if number3>number2:
            firstBrace = 'small1extrasmall1'
            answerBrace = 'small%dextrasmall1'%(number1-2)
        else:
            firstBrace = 'extrasmall'
            answerBrace = 'small%dextrasmall1'%(number1-1)

        self.solution_text = self.solution_text + "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2>%d</td></tr>"%(number2*number1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_small%d.png' /></td></tr>"%(number1)
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px;'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;'>&nbsp;</td><td style='background-color:%s;height:25px;border:white solid 1px;'>&nbsp;</td></tr>"%(item2,self.color2,self.color3)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_%s.png' /></td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(firstBrace,answerBrace)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'>%d</td><td style='padding-bottom:3px;'>?</td></tr>"%(number3)
        self.solution_text = self.solution_text + "</table><br>"
        #end of model 2

        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "%d &nbsp;&minus;&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number2*number1,number3,answer)
        self.solution_text = self.solution_text + "He %s %d %s.<br><br>"%(item6,answer,item7)
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType37(self):       
        '''e.g.:
        [Person.Girlname1] <had> 5 times as much money as [Person.Girlname2].
        [Person.Girlname3] <had> $30 <less / more> than [Person.Girlname1].
        [Person.Girlname2] <had> $25.
        How much money did [Person.Girlname3] <have>?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.names = random.sample(PersonName.GirlName,3)
        
        self.items = [['had','have'],['received','receive'],['borrowed','borrow'],
                      ['donated','donate'],['deposited','deposit'],['saved','save'],
                      ['counted','count'],['earned','earn'],['paid','pay'],['gave away','give away']]
        
        self.item = random.choice(self.items)
                
        self.number1 = randint(3,8)
        self.number2 = randint(150,300)
        self.number3 = randint(50,100)
        
        self.flag = randint(1,2)
        
        self.problem = "%s %s %d times as much money as %s.<br><br>"%(self.names[0],self.item[0],self.number1,self.names[1])
        if self.flag == 1:
            self.problem = self.problem + "%s %s $%d less than %s.<br><br>"%(self.names[2],self.item[0],self.number3,self.names[0])
            self.answer = self.number1*self.number2 - self.number3
        else:
            self.problem = self.problem + "%s %s $%d more than %s.<br><br>"%(self.names[2],self.item[0],self.number3,self.names[0])
            self.answer = self.number1*self.number2 + self.number3
        self.problem = self.problem + "%s %s $%d.<br><br>"%(self.names[1],self.item[0],self.number2)
        self.problem = self.problem + "How much money did %s %s?"%(self.names[2],self.item[1])
        
        self.unit = ""
        self.dollar_unit = "$"
          
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType37(self.problem,self.answer,self.flag,self.names,self.number1,self.number2,self.number3,self.item[0],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType37",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,
                'unit':self.unit,'dollar_unit':self.dollar_unit}

    def ExplainType37(self,problem,answer,flag,names,number1,number2,number3,item0,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        #beginning of model
        self.colors = random.choice([['tomato','orange','peru'],['blueviolet','violet','darkorchid'],['purple','plum','mediumvioletred'],['darkturquoise','dodgerblue','darkslateblue'],['mediumorchid','mediumpurple','palevioletred'],['chocolate','burlywood','brown'],['deeppink','lightpink','hotpink']])
        self.color1 = self.colors[0]
        self.color2 = self.colors[1]
        self.color3 = self.colors[2]

        if flag==1:
            self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$%d</td></tr>"%(number2)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_small.png' /></td></tr>"
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px;'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;'>&nbsp;</td></tr>"%(names[1],self.color1)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td></tr>"
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px;'>%s</td>"%(names[0])
            for x in range(0,number1-1):
                self.solution_text = self.solution_text + "<td style='background-color:%s;height:25px;border:white solid 1px;width:53px;'>&nbsp;</td>"%(self.color2)
            self.solution_text = self.solution_text + "<td style='background-color:%s;height:25px;border:white solid 1px;border-right:0;width:25px;'>&nbsp;</td><td style='background-color:%s;height:25px;border:white solid 1px;border-left:0;width:25px;'>&nbsp;</td>"%(self.color2,self.color2)
            self.solution_text = self.solution_text + "</tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td></tr>"
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px;'>%s</td><td colspan=%d style='background-color:%s;height:25px;border:white solid 1px;'>&nbsp;</td></tr>"%(names[2],number1,self.color3)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_small%dextrasmall1.png' /></td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_extrasmall.png' /></td></tr>"%(number1,number1-1)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d style='padding-bottom:3px;'>?</td><td>$%d</td></tr>"%(number1,number3)
            self.solution_text = self.solution_text + "</table><br><br>"
        else:
            self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>$%d</td></tr>"%(number2)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_small.png' /></td></tr>"
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px;'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;'>&nbsp;</td></tr>"%(names[1],self.color1)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td></tr>"
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px;'>%s</td>"%(names[0])
            for x in range(0,number1):
                self.solution_text = self.solution_text + "<td style='background-color:%s;height:25px;border:white solid 1px;width:52px;'>&nbsp;</td>"%(self.color2)
            self.solution_text = self.solution_text + "<td style='vertical-align:bottom'>$%d</td></tr>"%(number3)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_extrasmall.png' /></td></tr>"%(number1)
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px;'>%s</td><td colspan=%d style='background-color:%s;height:25px;border:white solid 1px;border-right:white dotted 1px;'>&nbsp;</td><td style='background-color:%s;height:25px;border:white solid 1px;border-left:white dotted 1px;'>&nbsp;</td></tr>"%(names[2],number1,self.color3,self.color3)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_small%dextrasmall1.png' /></td></tr>"%(number1+1,number1)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d style='padding-bottom:3px;'>?</td></tr>"%(number1+1)
            self.solution_text = self.solution_text + "</table><br><br>"
        #end of model

        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "$%d &nbsp;&times;&nbsp; %d &nbsp;=&nbsp; $%d<br>"%(number2,number1,number2*number1)
        self.solution_text = self.solution_text + "%s %s $%d.<br><br>"%(names[0],item0,number2*number1)
        if flag==1:
            self.solution_text = self.solution_text + "$%d &nbsp;&minus;&nbsp; $%d &nbsp;=&nbsp; $%d<br>"%(number2*number1,number3,answer)
        else:
            self.solution_text = self.solution_text + "$%d &nbsp;+&nbsp; $%d &nbsp;=&nbsp; $%d<br>"%(number2*number1,number3,answer)
        self.solution_text = self.solution_text + "%s %s $%d.<br><br>"%(names[2],item0,answer)
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType38(self):       
        '''e.g.:
        [Person.Name1] <had> 15 <fewer / more> <paper roses> than [Person.Name2].
        [Person.Name2] <had> 4 times as many <paper roses> as [Person.Name3].
        [Person.Name3] <had> 28 <paper roses>.
        Find the number of <paper roses> that [Person.Name1] <had>.'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.names = random.sample(PersonName.PersonName,3)
        
        self.items = [['had','paper roses'],['had','guppies'],['collected','picture postcards'],
                      ['collected','foreign stamps'],['bought','marbles'],['bought','buttons'],
                      ['painted','cards'],['painted','icecream sticks'],['won','animal cards'],
                      ['sold','concert tickets']]
        
        self.item = random.choice(self.items)
                
        self.number3 = randint(50,99)
        self.multiplier = randint(3,8)
        self.number2 = self.multiplier*self.number3
        self.diff = randint(20,45)
        
        self.flag = randint(1,2)
        
        if self.flag == 1:
            self.problem = "%s %s %d fewer %s than %s.<br><br>"%(self.names[0],self.item[0],self.diff,self.item[1],self.names[1])
            self.answer = self.number3*self.multiplier - self.diff
        else:
            self.problem = "%s %s %d more %s than %s.<br><br>"%(self.names[0],self.item[0],self.diff,self.item[1],self.names[1])
            self.answer = self.number3*self.multiplier + self.diff

        self.problem = self.problem + "%s %s %d times as many %s as %s.<br><br>"%(self.names[1],self.item[0],self.multiplier,self.item[1],self.names[2])
        self.problem = self.problem + "%s %s %d %s.<br><br>"%(self.names[2],self.item[0],self.number3,self.item[1])
        self.problem = self.problem + "Find the number of %s that %s %s."%(self.item[1],self.names[0],self.item[0])
        
        self.unit = self.item[1]
        self.dollar_unit = ""
          
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType38(self.problem,self.answer,self.flag,self.names,self.diff,self.multiplier,self.number3,self.item[0],self.item[1],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType38",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,
                'unit':self.unit,'dollar_unit':self.dollar_unit}

    def ExplainType38(self,problem,answer,flag,names,diff,multiplier,number3,item0,item1,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        #beginning of model
        self.colors = random.choice([['tomato','orange','peru'],['blueviolet','violet','darkorchid'],['purple','plum','mediumvioletred'],['darkturquoise','dodgerblue','darkslateblue'],['mediumorchid','mediumpurple','palevioletred'],['chocolate','burlywood','brown'],['deeppink','lightpink','hotpink']])
        self.color1 = self.colors[0]
        self.color2 = self.colors[1]
        self.color3 = self.colors[2]

        if flag==1:
            self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>%d</td></tr>"%(number3)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_small.png' /></td></tr>"
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px;'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;'>&nbsp;</td></tr>"%(names[2],self.color1)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td></tr>"
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px;'>%s</td>"%(names[1])
            for x in range(0,multiplier-1):
                self.solution_text = self.solution_text + "<td style='background-color:%s;height:25px;border:white solid 1px;width:53px;'>&nbsp;</td>"%(self.color2)
            self.solution_text = self.solution_text + "<td style='background-color:%s;height:25px;border:white solid 1px;border-right:0;width:25px;'>&nbsp;</td><td style='background-color:%s;height:25px;border:white solid 1px;border-left:0;'>&nbsp;</td>"%(self.color2,self.color2)
            self.solution_text = self.solution_text + "</tr>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td></tr>"
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px;'>%s</td><td colspan=%d style='background-color:%s;height:25px;border:white solid 1px;'>&nbsp;</td></tr>"%(names[0],multiplier,self.color3)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_small%dextrasmall1.png' /></td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_extrasmall.png' /></td></tr>"%(multiplier,multiplier-1)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d style='padding-bottom:3px;'>?</td><td>%d</td></tr>"%(multiplier,diff)
            self.solution_text = self.solution_text + "</table><br><br>"
        else:
            self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>%d</td></tr>"%(number3)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_small.png' /></td></tr>"
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px;'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;'>&nbsp;</td></tr>"%(names[2],self.color1)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td></tr>"
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px;'>%s</td>"%(names[1])
            for x in range(0,multiplier):
                self.solution_text = self.solution_text + "<td style='background-color:%s;height:25px;border:white solid 1px;width:52px;'>&nbsp;</td>"%(self.color2)
            self.solution_text = self.solution_text + "<td style='vertical-align:bottom'>%d</td></tr>"%(diff)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_extrasmall.png' /></td></tr>"%(multiplier)
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px;'>%s</td><td colspan=%d style='background-color:%s;height:25px;border:white solid 1px;border-right:white dotted 1px;'>&nbsp;</td><td style='background-color:%s;height:25px;border:white solid 1px;border-left:white dotted 1px;'>&nbsp;</td></tr>"%(names[0],multiplier,self.color3,self.color3)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_small%dextrasmall1.png' /></td></tr>"%(multiplier+1,multiplier)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d style='padding-bottom:3px;'>?</td></tr>"%(multiplier+1)
            self.solution_text = self.solution_text + "</table><br><br>"
        #end of model

        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "%d &nbsp;&times;&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number3,multiplier,number3*multiplier)
        self.solution_text = self.solution_text + "%s %s %d %s.<br><br>"%(names[1],item0,number3*multiplier,item1)
        if flag==1:
            self.solution_text = self.solution_text + "%d &nbsp;&minus;&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number3*multiplier,diff,answer)
        else:
            self.solution_text = self.solution_text + "%d &nbsp;+&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number3*multiplier,diff,answer)
        self.solution_text = self.solution_text + "%s %s %d %s.<br><br>"%(names[0],item0,answer,item1)
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType39(self):       
        '''e.g.:
        [Person.Auntyname] packed 844 <cream cookies> into <bags> of 4.
        She sold all the <cream cookies> at $2 a <bag>.
        Find the sum of money she received.'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.AuntyName)
        
        self.items = [['cream cookies','bags','bag'],['eggplants','bags','bag'],
                      ['comic books','packs','pack'],['fridge magnets','packs','pack'],
                      ['ribbon bows','packets','packet'],['keychains','packets','packet'],
                      ['pies','boxes','box'],['strawberries','boxes','box'],['clips','pouches','pouch'],
                      ['daffodils','baskets','basket']]
        
        self.item = random.choice(self.items)
                
        self.numbers = random.choice([[3,randint(100,300)],
                                      [4,randint(100,220)],
                                      [5,randint(50,180)],
                                      [6,randint(40,150)],
                                      [7,randint(40,120)]
                                      ])
        
        self.number2 = self.numbers[0]
        self.multiplier = self.numbers[1]
        self.number1 = self.multiplier * self.number2
        self.number3 = randint(2,5)

        self.problem = "%s packed %d %s into %s of %d.<br><br>"%(self.name,self.number1,self.item[0],self.item[1],self.number2)
        self.problem = self.problem + "She sold all the %s at $%d a %s.<br><br>"%(self.item[0],self.number3,self.item[2])
        self.problem = self.problem + "Find the sum of money she received."
        
        self.answer = self.number1/self.number2 * self.number3
        
        self.unit = ""
        self.dollar_unit = "$"
          
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType39(self.problem,self.answer,self.number1,self.number2,self.number3,self.item[0],self.item[1],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType39",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,
                'unit':self.unit,'dollar_unit':self.dollar_unit}

    def ExplainType39(self,problem,answer,number1,number2,number3,item0,item1,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        #beginning of model
        self.color1 = random.choice(['brown','chocolate','coral','darkorange','orange','salmon','darksalmon','deeppink','firebrick','indianred'])
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td colspan=5>%d</td></tr>"%(number1)
        self.solution_text = self.solution_text + "<tr><td colspan=5 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_small5.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='background-color:%s;height:20px;border:white solid 1px;width:50px;padding-bottom:5px;'>$%d</td><td style='background-color:%s;height:20px;border:white solid 1px;width:54px;padding-bottom:5px;'>$%d</td><td colspan=2 style='height:20px;border:white solid 1px;width:50px;padding-bottom:5px;'>. . . . .</td><td style='background-color:%s;height:20px;border:white solid 1px;width:54px;padding-bottom:5px'>$%d</td></tr>"%(self.color1,number3,self.color1,number3,self.color1,number3)
        self.solution_text = self.solution_text + "<tr><td><img src='/images/explanation/P3_model_down_brace_small.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td colspan=5 style='text-align:left;'>%d %s</td></tr>"%(number2,item0)
        self.solution_text = self.solution_text + "<tr><td colspan=5><img src='/images/explanation/P3_model_down_brace_small5.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td colspan=5>$ ?</td></tr>"
        self.solution_text = self.solution_text + "</table><br><br>"
        #end of model

        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "%d &nbsp;&divide;&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number1,number2,number1/number2)
        self.solution_text = self.solution_text + "She got %d %s.<br><br>"%(number1/number2,item1)
        self.solution_text = self.solution_text + "%d &nbsp;&times;&nbsp; $%d &nbsp;=&nbsp; $%d<br>"%(number1/number2,number3,answer)
        self.solution_text = self.solution_text + "She received $%d.<br><br>"%(answer)
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType40(self):       
        '''e.g.:
        [Person.Unclename] had 126 <cans of wood paint> and 4 times as many <cans of wall paint>.
        He sold the <cans of wall paint> equally to 7 <contractors>.
        How many <cans of wall paint> did each <contractor> buy?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.UncleName)
        
        self.items = [['cans of wood paint','cans of wall paint','contractors','contractor'],
                      ['curtain rods','curtain ties','stores','store'],['leafy plants','flowering plants','plant nurseries','plant nursery'],
                      ['guavas','apples','fruit stalls','fruit stall'],['red bell peppers','green bell peppers','vegetable vendors','vegetable vendor'],
                      ['storybooks','jotter books','bookshops','bookshop'],['laser printers','inkjet printers','IT stores','IT store'],
                      ['jackets','shirts','department stores','department store'],['guppies','clown fishes','pet shops','pet shop']]
        
        self.item = random.choice(self.items)

        self.number2 = randint(3,8)
        self.number3 = randint(4,9)

        while self.number2==self.number3:
            self.number3 = randint(4,9)

        self.number1 = randint(5,15) * self.number3
        
        self.problem = "%s had %d %s and %d times as many %s.<br><br>"%(self.name,self.number1,self.item[0],self.number2,self.item[1])
        self.problem = self.problem + "He sold the %s equally to %d %s.<br><br>"%(self.item[1],self.number3,self.item[2])
        self.problem = self.problem + "How many %s did each %s buy?"%(self.item[1],self.item[3])     
        
        self.answer = (self.number1*self.number2)/self.number3
        
        self.unit = self.item[1]
        self.dollar_unit = ""
          
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType40(self.problem,self.answer,self.number1,self.number2,self.number3,self.item[0],self.item[1],self.item[3],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType40",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,
                'unit':self.unit,'dollar_unit':self.dollar_unit}

    def ExplainType40(self,problem,answer,number1,number2,number3,item0,item1,item3,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        #beginning of model 1
        self.colors = random.choice([['tomato','orange','peru'],['blueviolet','violet','darkorchid'],['purple','plum','mediumvioletred'],['darkturquoise','dodgerblue','darkslateblue'],['mediumorchid','mediumpurple','palevioletred'],['chocolate','burlywood','brown'],['deeppink','lightpink','hotpink']])
        self.color1 = self.colors[0]
        self.color2 = self.colors[1]

        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>%d</td></tr>"%(number1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_small.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px;'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;width:52px;'>&nbsp;</td></tr>"%(item0,self.color1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px;'>%s</td>"%(item1)
        for x in range(0, number2):
            self.solution_text = self.solution_text + "<td style='background-color:%s;height:25px;border:white solid 1px;width:52px;'>&nbsp;</td>"%(self.color2)
        self.solution_text = self.solution_text + "</tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_small%d.png' /></td></tr>"%(number2,number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d>? (a)</td></tr>"%(number2)
        self.solution_text = self.solution_text + "</table><br>"
        #end of model 1

        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "%d &nbsp;&times;&nbsp; %d &nbsp;=&nbsp; %d &nbsp;&nbsp; (a)<br>"%(number1,number2,number1*number2)
        self.solution_text = self.solution_text + "He had %d %s.<br><br>"%(number1*number2,item1)
        self.solution_text = self.solution_text + "</font>"

        #beginning of model 2
        cellWidth = (52*number2)/number3
        self.solution_text = self.solution_text + "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d>%d</td></tr>"%(number3,number1*number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_small%d.png' /></td></tr>"%(number3,number2)
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px;'>%s</td>"%(item1)
        for x in range(0, number3):
            self.solution_text = self.solution_text + "<td style='background-color:%s;height:25px;border:white solid 1px;width:%dpx'>&nbsp;</td>"%(self.color2,cellWidth)
        self.solution_text = self.solution_text + "</tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td><img src='/images/explanation/P3_model_down_brace_small%dto%d.png' /></td></tr>"%(number2,number3)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='vertical-align:top;padding-top:0px;'>?</td></tr>"
        self.solution_text = self.solution_text + "</table><br>"
        #end of model 2

        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "%d &nbsp;&divide;&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number1*number2,number3,answer)
        self.solution_text = self.solution_text + "Each %s bought %d %s.<br><br>"%(item3,answer,item1)
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType41(self):       
        '''e.g.:
        [Person.Boyname1], [Person.Boyname2] and [Person.Boyname3] <have some paper clips>.
        [Person.Boyname1] <has> 900 <paper clips>.
        He <has> 5 times as many <paper clips> as [Person.Boyname2].
        [Person.Boyname3] <has> 375 <paper clips>.
        How many more <paper clips> <does> [Person.Boyname3] <have> than [Person.Boyname2]?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.names = random.sample(PersonName.BoyName,3)
        
        self.items = [['have some paper clips','has','paper clips','does','have'],
                      ['like to collect superhero stickers','has','stickers','does','have'],
                      ['shared some marbles among themselves','received','marbles','did','receive'],
                      ['are coaster collectors','has','coasters','does','have'],
                      ['each has a set of building blocks','has','blocks','does','have'],
                      ['baked cupcakes for a food festival','baked','cupcakes','did','bake'],
                      ['clicked photos of a sport event','clicked','photos','did','click'],
                      ['each had a carton of binding rings','had','binding rings','did','have'],
                      ['went apple picking on a farm','picked','apples','did','pick'],
                      ['like to collect sea glass','has','pieces of sea glass','does','have']]
        
        self.item = random.choice(self.items)
                
        self.numbers = random.choice([[4,randint(100,220)],
                                      [5,randint(60,180)],
                                      [6,randint(50,150)],
                                      [7,randint(50,120)],
                                      [8,randint(40,100)],
                                      [9,randint(40,100)]
                                      ])
        
        self.number2 = self.numbers[0]
        self.multiplier = self.numbers[1]
        self.number1 = self.multiplier * self.number2
        self.number3 = randint(330,700)
        while self.number1==self.number3:
            self.number3 = randint(330,700) #to make sure that number1 is not equal to number 3, for model's sake

        self.problem = "%s, %s and %s %s.<br><br>"%(self.names[0],self.names[1],self.names[2],self.item[0])
        self.problem = self.problem + "%s %s %d %s.<br><br>"%(self.names[0],self.item[1],self.number1,self.item[2])
        self.problem = self.problem + "He %s %d times as many %s as %s.<br><br>"%(self.item[1],self.number2,self.item[2],self.names[1])
        self.problem = self.problem + "%s %s %d %s.<br><br>"%(self.names[2],self.item[1],self.number3,self.item[2])
        self.problem = self.problem + "How many more %s %s %s %s than %s?"%(self.item[2],self.item[3],self.names[2],self.item[4],self.names[1])
        
        self.answer = self.number3 - self.number1/self.number2
        
        self.unit = self.item[2]
        self.dollar_unit = ""
          
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType41(self.problem,self.answer,self.names,self.number1,self.number2,self.number3,self.item[1],self.item[2],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType41",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,
                'unit':self.unit,'dollar_unit':self.dollar_unit}

    def ExplainType41(self,problem,answer,names,number1,number2,number3,item1,item2,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        #beginning of model
        self.colors = random.choice([['tomato','orange','peru'],['blueviolet','violet','darkorchid'],['purple','plum','mediumvioletred'],['darkturquoise','dodgerblue','darkslateblue'],['mediumorchid','mediumpurple','palevioletred'],['chocolate','burlywood','brown'],['deeppink','lightpink','hotpink']])
        self.color1 = self.colors[0]
        self.color2 = self.colors[1]
        self.color3 = self.colors[2]

        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d>%d</td></tr>"%(number2,number1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_extrasmall%d.png' /></td></tr>"%(number2,number2)
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px;'>%s</td>"%(names[0])
        for x in range(0, number2):
            self.solution_text = self.solution_text + "<td style='background-color:%s;height:25px;border:white solid 1px;width:30px;'>&nbsp;</td>"%(self.color1)
        self.solution_text = self.solution_text + "</tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td></tr>"
        #self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px;'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;width:31px;'>&nbsp;</td></tr>"%(names[1],self.color2)
        #self.solution_text = self.solution_text + "<tr><td>&nbsp;</td></tr>"
        if number3>number1:
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px;'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;width:31px;'>&nbsp;</td><td colspan=%d style='vertical-align:bottom;'>?</td></tr>"%(names[1],self.color2,number2)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>&nbsp;</td><td colspan=%d style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_medium1extrasmall%d.png' /></td></tr>"%(number2,number2-1)
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px;'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;border-right:white dotted 1px;'>&nbsp;</td><td colspan=%d style='background-color:%s;height:25px;border:white solid 1px;border-left:white dotted 1px;border-right:0;'>&nbsp;</td><td style='background-color:%s;height:25px;border:white solid 1px;border-left:0;'>&nbsp;</td></tr>"%(names[2],self.color3,number2-1,self.color3,self.color3)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_medium1extrasmall%d.png' /></td></tr>"%(number2+1,number2)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d>%d</td></tr>"%(number2+1,number3)
        else:
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px;'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;width:31px;'>&nbsp;</td><td colspan=%d style='vertical-align:bottom;'>?</td></tr>"%(names[1],self.color2,number2-2)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>&nbsp;</td><td colspan=%d style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_extrasmall%d.png' /></td></tr>"%(number2-2,number2-2)
            self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px;'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;border-right:white dotted 1px;'>&nbsp;</td><td colspan=%d style='background-color:%s;height:25px;border:white solid 1px;border-left:white dotted 1px;'>&nbsp;</td></tr>"%(names[2],self.color3,number2-2,self.color3)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d style='padding-bottom:3px;'><img src='/images/explanation/P3_model_down_brace_extrasmall%d.png' /></td></tr>"%(number2-1,number2-1)
            self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d>%d</td></tr>"%(number2-1,number3)
        self.solution_text = self.solution_text + "</table><br><br>"
        #end of model

        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "%d &nbsp;&divide;&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number1,number2,number1/number2)
        self.solution_text = self.solution_text + "%s %s %d %s.<br><br>"%(names[1],item1,number1/number2,item2)
        self.solution_text = self.solution_text + "%d &nbsp;&minus;&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number3,number1/number2,answer)
        self.solution_text = self.solution_text + "%s %s %d more %s than %s.<br><br>"%(names[2],item1,answer,item2,names[1])
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType42(self):       
        '''e.g.:
        [Person.Girlname1], [Person.Girlname2] and [Person.Boyname] <sold tickets to a charity concert>.
        [Person.Girlname1] <collected> $459.
        She <collected> $286 less than [Person.Girlname2].
        [Person.Girlname2] <collected> 5 times as much money as [Person.Boyname] .
        How much money <did> [Person.Boyname] <collect>?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.names = random.sample(PersonName.GirlName,2)+[random.choice(PersonName.BoyName)]
        
        self.items = [['collected some money by selling concert tickets','collected','did','collect'],
                      ['have different part-time jobs','earns','does','earn'],
                      ['donated some money to a charity','donated','did','donate'],
                      ['counted the money in their piggy banks','had','did','have'],
                      ['saved some money','saved','did','save'],
                      ['shared some money among themselves','received','did','receive'],
                      ['went shopping','spent','did','spend'],
                      ['went to a bank to deposit some money','deposited','did','deposit'],
                      ['went to a bank to withdraw some money','withdrew','did','withdraw'],
                      ['won some prize money in a competition','won','did','win']]
        
        self.item = random.choice(self.items)
                
        self.numbers = random.choice([[3,randint(100,300)],
                                      [4,randint(100,220)],
                                      [5,randint(60,180)],
                                      [6,randint(50,150)],
                                      [7,randint(50,120)],
                                      [8,randint(40,100)],
                                      [9,randint(40,100)]
                                      ])
        
        self.number3 = self.numbers[0]
        self.total = self.numbers[1]*self.number3
        #self.number1 = randint(140,self.total/2)
        self.number1 = randint(self.numbers[1],self.total/2-5) #to not be smaller than 1 unit for the ease of model drawing and also to make sure that number1!=number2
        self.number2 = self.total - self.number1

        self.problem = "%s, %s and %s %s.<br><br>"%(self.names[0],self.names[1],self.names[2],self.item[0])
        self.problem = self.problem + "%s %s $%d.<br><br>"%(self.names[0],self.item[1],self.number1)
        self.problem = self.problem + "She %s $%d less than %s.<br><br>"%(self.item[1],self.number2,self.names[1])
        self.problem = self.problem + "%s %s %d times as much money as %s.<br><br>"%(self.names[1],self.item[1],self.number3,self.names[2])
        self.problem = self.problem + "How much money %s %s %s?"%(self.item[2],self.names[2],self.item[3])
        
        self.answer = (self.number1+self.number2)/self.number3
        
        self.unit = ""
        self.dollar_unit = "$"
          
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType42(self.problem,self.answer,self.names,self.number1,self.number2,self.number3,self.item[1],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType42",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,
                'unit':self.unit,'dollar_unit':self.dollar_unit}

    def ExplainType42(self,problem,answer,names,number1,number2,number3,item1,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        div,mod = divmod(number1,answer)

        #beginning of model
        self.colors = random.choice([['tomato','orange','peru'],['blueviolet','violet','darkorchid'],['purple','plum','mediumvioletred'],['darkturquoise','dodgerblue','darkslateblue'],['mediumorchid','mediumpurple','palevioletred'],['chocolate','burlywood','brown'],['deeppink','lightpink','hotpink']])
        self.color1 = self.colors[0]
        self.color2 = self.colors[1]
        self.color3 = self.colors[2]

        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d>$%d</td><td colspan=%d>$%d</td></tr>"%(div+1,number1,number3-div,number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=%d style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_small%dextrasmall1.png' /></td><td colspan=%d style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_small%dextrasmall1.png' /></td></tr>"%(div+1,div,number3-div,number3-div-1)
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px;'>%s</td><td colspan=%d style='background-color:%s;height:25px;border:white solid 1px;'>&nbsp;</td></tr>"%(names[0],div+1,self.color3)
        
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td></tr>"

        self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px;'>%s</td>"%(names[1])
        for x in range(0, div):
            self.solution_text = self.solution_text + "<td style='background-color:%s;height:25px;border:white solid 1px;width:52px;'>&nbsp;</td>"%(self.color1)
        self.solution_text = self.solution_text + "<td style='background-color:%s;height:25px;border:white solid 1px;border-right:0;width:26px;'>&nbsp;</td>"%(self.color1)
        self.solution_text = self.solution_text + "<td style='background-color:%s;height:25px;border:white solid 1px;border-left:0;width:26px;'>&nbsp;</td>"%(self.color1)
        for x in range(div+1,number3):
            self.solution_text = self.solution_text + "<td style='background-color:%s;height:25px;border:white solid 1px;width:52px;'>&nbsp;</td>"%(self.color1)
        self.solution_text = self.solution_text + "</tr>"

        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td></tr>"

        self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px;'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;'>&nbsp;</td></tr>"%(names[2],self.color2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td><img src='/images/explanation/P3_model_down_brace_small.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>?</td></tr>"
        self.solution_text = self.solution_text + "</table><br>"
        #end of model

        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "$%d &nbsp;+&nbsp; $%d &nbsp;=&nbsp; $%d<br>"%(number1,number2,number1+number2)
        self.solution_text = self.solution_text + "%s %s $%d.<br><br>"%(names[1],item1,number1+number2)
        self.solution_text = self.solution_text + "$%d &nbsp;&divide;&nbsp; %d &nbsp;=&nbsp; $%d<br>"%(number1+number2,number3,answer)
        self.solution_text = self.solution_text + "%s %s $%d.<br><br>"%(names[2],item1,answer)
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType43(self):       
        '''e.g.:
        [Person.Auntyname] <made> 328 <donuts> <in the morning>.
        She <made> another 64 <donuts> <in the afternoon>.
        She packed all the <donuts> into <boxes> of 8 <donuts> each.
        How many <boxes> did she get?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.AuntyName)
        
        self.items = [['made','donuts','in the morning','in the afternoon','boxes','box'],
                      ['made','jamrolls','in the first batch','in the second batch','containers','container'],
                      ['made','paper flowers','last week','this week','packets','packet'],
                      ['baked','scones','yesterday','today','bags','bag'],
                      ['baked','mini-pizzas','in the afternoon','in the evening','boxes','box'],
                      ['baked','bagels','on Monday','on Tuesday','containers','container'],
                      ['received','mousepads','in the first shipment','in the second shipment','packs','pack'],
                      ['received','scarves','in the first batch','in the second batch','packs','pack'],
                      ['sewed','cushion covers','in July','in August','bundles','bundle'],
                      ['painted','mugs','in September','in October','boxes','box']]
        
        self.item = random.choice(self.items)
                
        self.numbers = random.choice([[3,randint(100,300)],
                                      [4,randint(100,220)],
                                      [5,randint(60,180)],
                                      [6,randint(50,150)],
                                      [7,randint(50,120)],
                                      [8,randint(40,100)],
                                      [9,randint(40,100)]
                                      ])
        
        self.number3 = self.numbers[0]
        self.total = self.numbers[1]*self.number3
        self.number1 = randint(self.total/2+20,self.total*2/3) #added +20 for the sake of model
        self.number2 = self.total - self.number1

        self.problem = "%s %s %d %s %s.<br><br>"%(self.name,self.item[0],self.number1,self.item[1],self.item[2])
        self.problem = self.problem + "She %s another %d %s %s.<br><br>"%(self.item[0],self.number2,self.item[1],self.item[3])
        self.problem = self.problem + "She packed all the %s into %s of %d %s each.<br><br>"%(self.item[1],self.item[4],self.number3,self.item[1])
        self.problem = self.problem + "How many %s did she get?"%(self.item[4])
        
        self.answer = (self.number1+self.number2)/self.number3
        
        self.unit = self.item[4]
        self.dollar_unit = ""
          
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType43(self.problem,self.answer,self.number1,self.number2,self.number3,self.item[0],self.item[1],self.item[4],self.item[5],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType43",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,
                'unit':self.unit,'dollar_unit':self.dollar_unit}

    def ExplainType43(self,problem,answer,number1,number2,number3,item0,item1,item4,item5,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        #beginning of model 1
        self.colors = random.choice([['tomato','orange','peru'],['blueviolet','violet','darkorchid'],['purple','plum','mediumvioletred'],['darkturquoise','dodgerblue','darkslateblue'],['mediumorchid','mediumpurple','palevioletred'],['chocolate','burlywood','brown'],['deeppink','lightpink','hotpink']])
        self.color1 = self.colors[0]
        self.color2 = self.colors[1]
        self.color3 = self.colors[2]
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>%d</td><td>%d</td></tr>"%(number1,number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_large.png' /></td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_medium.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px;white-space:nowrap;'>%s</td><td style='background-color:%s;height:20px;border:white solid 1px;padding-bottom:5px;'>&nbsp;</td><td style='background-color:%s;height:20px;border:white solid 1px;padding-bottom:5px;'>&nbsp;</td></tr>"%(item1,self.color1,self.color2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2><img src='/images/explanation/P3_model_down_brace_large1medium1.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2>? (a)</td></tr>"
        self.solution_text = self.solution_text + "</table><br><br>"
        #end of model 1

        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "%d &nbsp;+&nbsp; %d &nbsp;=&nbsp; %d &nbsp;&nbsp; (a)<br>"%(number1,number2,number1+number2)
        self.solution_text = self.solution_text + "She %s %d %s altogether.<br><br>"%(item0,number1+number2,item1)
        self.solution_text = self.solution_text + "</font>"

        #beginning of model 2
        self.solution_text = self.solution_text + "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=5>%d</td></tr>"%(number1+number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=5 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_large1medium1.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px;white-space:nowrap;'>%s</td><td style='background-color:%s;height:20px;border:white solid 1px;width:50px;padding-bottom:5px;'>%d</td><td style='background-color:%s;height:20px;border:white solid 1px;width:50px;padding-bottom:5px;'>%d</td><td colspan=2 style='height:20px;border:white solid 1px;width:30px;padding-bottom:5px;'>. . . . .</td><td style='background-color:%s;height:20px;border:white solid 1px;width:50px;padding-bottom:5px'>%d</td></tr>"%(item1,self.color3,number3,self.color3,number3,self.color3,number3)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td><img src='/images/explanation/P3_model_down_brace_small.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2 style='text-align:left;white-space:nowrap;'>1 %s</td></tr>"%(item5)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=5><img src='/images/explanation/P3_model_down_brace_large1medium1.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=5>? %s</td></tr>"%(item4)
        self.solution_text = self.solution_text + "</table><br><br>"
        #end of model 2

        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "%d &nbsp;&divide;&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number1+number2,number3,answer)
        self.solution_text = self.solution_text + "She got %d %s.<br><br>"%(answer,item4)
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType44(self):       
        '''e.g.:
        <Factory A> <manufactured> 760 <phones> every <week>.
        <Factory B> <manufactured> 490 fewer <phones> than <Factory A> every <week>.
        How many <phones> had <Factory B> <manufactured> after 8 <weeks>?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.items = [['Factory A','manufactured','phones','week','Factory B','weeks'],
                      ['Factory A','manufactured','garments','day','Factory B','days'],
                      ['Fruit Stall A','sold','fruit platters','day','Fruit Stall B','days'],
                      ['Poultry Farm A','sold','chickens','week','Poultry Farm B','weeks'],
                      ['Grocery Store A','sold','juice cartons','week','Grocery Store B','weeks'],
                      ['Park A','received','visitors','month','Park B','months'],
                      ['Library A','received','new books','month','Library B','months'],
                      ['Boating Company A','served','tourists','month','Boating Company B','months'],
                      ['Restaurant A','served','customers','weekend','Restaurant B','weekends'],
                      ['Shop A','served','customers','day','Shop B','days']]
        
        self.item = random.choice(self.items)
                       
        self.number1 = randint(600,900)
        self.number2 = randint(300,self.number1-100)
        self.diff = self.number1 - self.number2
        self.number3 = randint(3,9)

        self.problem = "%s %s %d %s every %s.<br><br>"%(self.item[0],self.item[1],self.number1,self.item[2],self.item[3])
        self.problem = self.problem + "%s %s %d fewer %s than %s every %s.<br><br>"%(self.item[4],self.item[1],self.diff,self.item[2],self.item[0],self.item[3])
        self.problem = self.problem + "How many %s had %s %s after %d %s?"%(self.item[2],self.item[4],self.item[1],self.number3,self.item[5])
        
        self.answer = (self.number2)*self.number3
        
        self.unit = self.item[2]
        self.dollar_unit = ""
          
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType44(self.problem,self.answer,self.number1,self.diff,self.number3,self.item,self.item[0],self.item[4],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType44",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,
                'unit':self.unit,'dollar_unit':self.dollar_unit}

    def ExplainType44(self,problem,answer,number1,diff,number3,item,item0,item4,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        #beginning of model 1
        self.colors = random.choice([['tomato','orange','peru'],['blueviolet','violet','darkorchid'],['purple','plum','mediumvioletred'],['darkturquoise','dodgerblue','darkslateblue'],['mediumorchid','mediumpurple','palevioletred'],['chocolate','burlywood','brown'],['deeppink','lightpink','hotpink']])
        self.color1 = self.colors[0]
        self.color2 = self.colors[1]
        
        if number1-diff>diff:
            firstCellBrace = 'medium'
            secondCellBrace = 'small'
            topCellBrace = 'medium1small1'
            firstCellWidth = 96
        elif number1-diff==diff:
            firstCellBrace = 'medium'
            secondCellBrace = 'medium'
            topCellBrace = 'medium2'
            firstCellWidth = 96
        else:
            firstCellBrace = 'small'
            secondCellBrace = 'medium'
            topCellBrace = 'medium1small1'
            firstCellWidth = 48
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2>%d</td></tr>"%(number1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td colspan=2 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(topCellBrace)
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px;white-space:nowrap;'>%s</td><td colspan=2 style='background-color:%s;height:20px;border:white solid 1px;padding-bottom:5px;'>&nbsp;</td></tr>"%(item0,self.color1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px;white-space:nowrap;'>%s</td><td style='background-color:%s;height:20px;border:white solid 1px;padding-bottom:5px;'>&nbsp;</td></tr>"%(item4,self.color2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td><img src='/images/explanation/P3_model_down_brace_%s.png' /></td><td><img src='/images/explanation/P3_model_down_brace_%s.png' /></td></tr>"%(firstCellBrace,secondCellBrace)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>? (a)</td><td>%d</td></tr>"%(diff)
        self.solution_text = self.solution_text + "</table><br><br>"
        #end of model 1

        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "%d &nbsp;&minus;&nbsp; %d &nbsp;=&nbsp; %d &nbsp;&nbsp; (a)<br>"%(number1,diff,number1-diff)
        self.solution_text = self.solution_text + "%s %s %d %s every %s.<br><br>"%(item[4],item[1],number1-diff,item[2],item[3])
        self.solution_text = self.solution_text + "</font>"
        
        #beginning of model 2
        self.solution_text = self.solution_text + "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>%d</td></tr>"%(number1-diff)
        self.solution_text = self.solution_text + "<tr><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(firstCellBrace)
        self.solution_text = self.solution_text + "<tr>"
        for x in range(0, number3):
            self.solution_text = self.solution_text + "<td style='background-color:%s;height:25px;border:white solid 1px;width:%dpx;'>&nbsp;</td>"%(self.color2,firstCellWidth)
        self.solution_text = self.solution_text + "</tr>"
        self.solution_text = self.solution_text + "<tr><td colspan=%d><img src='/images/explanation/P3_model_down_brace_%s%d.png' /></td></tr>"%(number3,firstCellBrace,number3)
        self.solution_text = self.solution_text + "<tr><td colspan=%d>?</td></tr>"%(number3)
        self.solution_text = self.solution_text + "</table><br>"
        #end of model 2
        
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "%d &nbsp;&times;&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number1-diff,number3,answer)
        self.solution_text = self.solution_text + "%s had %s %d %s after %d %s.<br><br>"%(item[4],item[1],answer,item[2],number3,item[5])
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType45(self):       
        '''e.g.:
        [Person.Boyname] had 24 <pencils> and <pens> altogether.
        After he exchanged 5 <pencils> for 5 <pens>, he had the same number of <pencils> as <pens>.
        How many <pens> did he have at first?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.BoyName)
        
        self.items = [['pencils','pens'],['sharpeners','erasers'],['spoons','forks'],['apples','oranges'],['roses','lilies'],['red marbles','black marbles'],['stickers','stamps'],['bowls','cups'],['candles','candle holders'],['mugs','glasses']]
        
        self.item = random.choice(self.items)
                       
        self.number1 = random.randrange(30,200,2)
        self.number2 = randint(4,self.number1/2-10)
        
        self.problem = "%s had %d %s and %s altogether.<br><br>"%(self.name,self.number1,self.item[0],self.item[1])
        self.problem = self.problem + "After he exchanged %d %s for %d %s, he had the same number of %s as %s.<br><br>"%(self.number2,self.item[0],self.number2,
                                                                                                                         self.item[1],self.item[0],self.item[1]
                                                                                                                         )
        self.problem = self.problem + "How many %s did he have at first?"%(self.item[1])
        
        self.answer = (self.number1 / 2) - self.number2
        
        self.unit = self.item[1]
        self.dollar_unit = ""
          
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType45(self.problem,self.answer,self.number1,self.number2,self.item[0],self.item[1],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType45",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,
                'unit':self.unit,'dollar_unit':self.dollar_unit}

    def ExplainType45(self,problem,answer,number1,number2,item0,item1,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        #beginning of model
        self.colors = random.choice([['tomato','orange','peru'],['blueviolet','violet','darkorchid'],['purple','plum','mediumvioletred'],['darkturquoise','dodgerblue','darkslateblue'],['mediumorchid','mediumpurple','palevioletred'],['chocolate','burlywood','brown'],['deeppink','lightpink','hotpink']])
        self.color1 = self.colors[0]
        self.color2 = self.colors[1]
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td><u>Before</u></td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:right;padding-right:7px;white-space:nowrap;'>%s</td><td colspan=3 style='background-color:%s;height:20px;border:white solid 1px;padding-bottom:5px;'>&nbsp;</td><td>&nbsp;</td><td>&nbsp;&nbsp;</td><td rowspan=3 style='padding:0;padding-top:3px;vertical-align:middle'><img src='/images/explanation/P3_model_right_brace_small.png' /></td><td rowspan=3 style='padding:0;vertical-align:middle'>&nbsp;%d</td></tr>"%(item0,self.color1,number1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>&nbsp;</td><td style='width:100px;'>&nbsp;</td><td style='width:50px;'>&nbsp;</td><td style='width:50px;'>&nbsp;</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:right;padding-right:7px;white-space:nowrap;'>%s</td><td style='background-color:%s;height:20px;border:white solid 1px;'>&nbsp;</td></tr>"%(item1,self.color2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>&nbsp;</td><td><img src='/images/explanation/P3_model_down_brace_medium.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>&nbsp;</td><td>?</td></tr>"
        self.solution_text = self.solution_text + "</table>"
        
        self.solution_text = self.solution_text + "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td><u>After</u></td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>&nbsp;</td><td colspan=2>? (a)</td><td>%d</td></tr>"%(number2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>&nbsp;</td><td colspan=2 style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_medium1small1.png' /></td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_small.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:right;padding-right:7px;white-space:nowrap;'>%s</td><td colspan=2 style='background-color:%s;height:20px;border:white solid 1px;padding-bottom:5px;'>&nbsp;</td><td style='height:20px;border:white dotted 1px;padding-bottom:5px;'>&nbsp;</td><td>&nbsp;</td><td>&nbsp;&nbsp;</td><td rowspan=3 style='padding:0;padding-top:3px;vertical-align:middle'><img src='/images/explanation/P3_model_right_brace_small.png' /></td><td rowspan=3 style='padding:0;vertical-align:middle'>&nbsp;%d</td></tr>"%(item0,self.color1,number1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>&nbsp;</td><td style='width:100px;'>&nbsp;</td><td style='width:50px;'>&nbsp;</td><td style='width:50px;'>&nbsp;</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td style='text-align:right;padding-right:7px;white-space:nowrap;'>%s</td><td style='background-color:%s;height:20px;border:white solid 1px;'>&nbsp;</td><td style='background-color:%s;height:20px;border:white dotted 1px;'>&nbsp;</td></tr>"%(item1,self.color2,self.color2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>&nbsp;</td><td><img src='/images/explanation/P3_model_down_brace_medium.png' /></td><td><img src='/images/explanation/P3_model_down_brace_small.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>&nbsp;</td><td>?</td><td>%d</td></tr>"%(number2)
        self.solution_text = self.solution_text + "</table><br><br>"
        #end of model
        
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "%d &nbsp;&divide;&nbsp; 2 &nbsp;=&nbsp; %d &nbsp;&nbsp; (a)<br>"%(number1,number1/2)
        self.solution_text = self.solution_text + "He had %d %s and %d %s in the end.<br><br>"%(number1/2,item0,number1/2,item1)
        self.solution_text = self.solution_text + "%d &nbsp;&minus;&nbsp; %d &nbsp;=&nbsp; %d<br>"%(number1/2,number2,answer)
        self.solution_text = self.solution_text + "He had %d %s at first.<br><br>"%(answer,item1)
        self.solution_text = self.solution_text + "</font>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType46(self):       
        '''e.g.:
        There were 8 <goats and hens on a farm>.
        [Person.Boyname] counted 20 <legs> altogether.
        How many <goats were there on the farm>?
        <(Hint: A goat has 4 legs. A hen has 2 legs.)>'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.BoyName)
        
        self.items = [['goats and hens on a farm','legs','goats were there on the farm','(Hint: A goat has 4 legs. A hen has 2 legs.)',4,2,'goats','Start by putting 2 legs to each creature &minus; hen as well as goat.','creatures','legs'],
                      ['monkeys and flamingos in a zoo','legs','monkeys were there in the zoo','(Hint: A monkey has 4 legs. A flamingo has 2 legs.)',4,2,'monkeys','Start by putting 2 legs to each creature &minus; flamingo as well as monkey.','creatures','legs'],
                      ['cars and motorbikes in a carpark','wheels','cars were there in the carpark','(Hint: A car has 4 wheels. A motorbike has 2 wheels.)',4,2,'cars','Start by putting 2 wheels to each vehicle &minus; motorbike as well as car.','vehicles','wheels'],
                      ['toy buses and tricycles in a toys shop','wheels','toy buses were there in the toys shop','(Hint: A toy bus has 4 wheels. A tricycle has 3 wheels.)',4,3,'toy buses','Start by putting 3 wheels to each vehicle &minus; tricycle as well as toy bus.','vehicles','wheel'],
                      ['dogs and men in a park','legs','dogs were there in the park','(Hint: A dog has 4 legs. A man has 2 legs.)',4,2,'dogs','Start by putting 2 legs to each creature &minus; man as well as dog.','creatures','legs'],
                      ['lobsters and octopuses in an aquarium','legs and arms','lobsters were there in the aquarium','(Hint: A lobster has 10 legs. An octopus has 8 arms.)',10,8,'lobsters','Start by putting 8 arms or legs to each sea creature &minus; octopus as well as lobster.','sea creatures','legs'],
                      ['bluebells and forget-me-nots in a vase','petals','bluebells were there in the vase','(Hint: A bluebell has 6 petals. A forget-me-not has 5 petals.)',6,5,'bluebells','Start by putting 5 petals to each flower.','flowers','petal'],
                      ['chairs and tripod tables in a furniture shop','legs','chairs were there in the furniture shop','(Hint: A chair has 4 legs. A tripod table has 3 legs.)',4,3,'chairs','Start by putting 3 legs to each piece of furniture &minus; tripod table as well as chair.','pieces of furniture','leg'],
                      ['fans in an electrical appliances shop.<br><br>Some of the fans had 3 blades while others had 5 blades','blades','fans with 5 blades were there','',5,3,'fans with 5 blades','Start by putting 3 blades to each fan.','fans','blades'],
                      ['electrical adapters in a shop.<br><br>Some of the adapters had 3 pins while others had 2 pins','pins','adapters with 3 pins were there','',3,2,'adapters with 3 pins','Start by putting 2 pins to each adapter.','adapters','pin']]
        
        self.item = random.choice(self.items)
                       
        self.number1 = self.item[4]
        self.number2 = self.item[5]
        self.number3 = randint(6,10)
        self.number4 = randint(6,10)
        self.total = self.number3 + self.number4
        self.legs = self.number3*self.number1 + self.number4*self.number2
        
        self.problem = "There were %d %s.<br><br>"%(self.total,self.item[0])
        self.problem = self.problem + "%s counted %d %s altogether.<br><br>"%(self.name,self.legs,self.item[1])
        self.problem = self.problem + "How many %s?<br><br>"%(self.item[2])
        self.problem = self.problem + "%s"%(self.item[3])
        
        self.answer = self.number3
        self.unit = self.item[6]
        self.dollar_unit = ""
          
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType46(self.problem,self.answer,self.total,self.number2,self.legs,self.item[1],self.item[4],self.item[5],self.item[6],self.item[7],self.item[8],self.item[9],self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType46",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,
                'unit':self.unit,'dollar_unit':self.dollar_unit}

    def ExplainType46(self,problem,answer,total,number2,legs,item1,item4,item5,item6,item7,item8,item9,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        self.solution_text = "<br><table class='ExplanationTable' border=0>"
        self.solution_text = self.solution_text + "<tr><td>%s</td></tr>"%(item7)
        self.solution_text = self.solution_text + "</table><br>"
        
        self.solution_text = self.solution_text + "<table class='ExplanationTable' border=0>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:left;white-space:nowrap;vertical-align:top;'>%d &nbsp;&times;&nbsp; %d &nbsp;=&nbsp; %d<br>So far, we have used up only %d %s.</td></tr>"%(total,number2,total*number2,total*number2,item1)
        self.solution_text = self.solution_text + "</table><br>"

        self.solution_text = self.solution_text + "<table class='ExplanationTable' border=0>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:left;white-space:nowrap;vertical-align:top;'>%d &nbsp;&minus;&nbsp; %d &nbsp;=&nbsp; %d<br>There are %d remaining %s.</td><td style='text-align:left;'><div class='side'>%d &nbsp;&minus;&nbsp; %d &nbsp;=&nbsp; %d<br>The %s need %d more %s each.</div></td></tr>"%(legs,total*number2,legs-total*number2,legs-total*number2,item1,item4,item5,item4-item5,item6,item4-item5,item9)
        self.solution_text = self.solution_text + "</table>"

        self.solution_text = self.solution_text + "<table class='ExplanationTable' border=0>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:left;white-space:nowrap;vertical-align:top;'>%d &nbsp;&divide;&nbsp; %d &nbsp;=&nbsp; %d<br>There were %d %s.</td><td style='text-align:left;'><div class='side'>The remaining %s could be put on up to %d %s.</div></td></tr>"%(legs-total*number2,item4-item5,answer,answer,item6,item1,answer,item8)
        self.solution_text = self.solution_text + "</table>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType47(self):       
        '''e.g.:
        [Person.Name1], [Person.Name2] and [Person.Name3] have 19 <postage stamps> altogether.
        [Person.Name2] has 3 more <postage stamps> than [Person.Name1].
        [Person.Name3] has 2 fewer <postage stamps> than [Person.Name1].
        How many <postage stamps> has [Person.Name3]?'''

        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.names = random.sample(PersonName.BoyName,3)
        
        self.items = ['postage stamps','butterfly stickers','paper flowers','water chestnuts','seashells','paper discs','balls','clown fishes','building blocks','glue sticks','postcards']
        
        self.item = random.choice(self.items)

        self.number1 = randint(40,400)
        self.more = randint(5,30)
        self.fewer = randint(5,30)
        
        self.number2 = self.number1+self.more
        self.number3 = self.number1-self.fewer
        
        self.total = self.number1 + self.number2 + self.number3
        
        self.problem = "%s, %s and %s have %d %s altogether.<br><br>"%(self.names[0],self.names[1],self.names[2],self.total,self.item)
        self.problem = self.problem + "%s has %d more %s than %s.<br><br>"%(self.names[1],self.more,self.item,self.names[0])
        self.problem = self.problem + "%s has %d fewer %s than %s.<br><br>"%(self.names[2],self.fewer,self.item,self.names[0])
        self.problem = self.problem + "How many %s has %s?"%(self.item,self.names[2])
        
        self.answer = self.number3
        
        self.unit = self.item
        self.dollar_unit = ""
          
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType47(self.problem,self.answer,self.names,self.total,self.more,self.fewer,self.item,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType47",
                'grade':3,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1,
                'unit':self.unit,'dollar_unit':self.dollar_unit}

    def ExplainType47(self,problem,answer,names,total,more,fewer,item,unit,dollar_unit):
        self.answer_text = "<br>The correct answer is:<br>%s%s %s"%(dollar_unit,str(answer),unit)

        #beginning of model
        self.colors = random.choice([['tomato','orange','peru'],['blueviolet','violet','darkorchid'],['purple','plum','mediumvioletred'],['darkturquoise','dodgerblue','darkslateblue'],['mediumorchid','mediumpurple','palevioletred'],['chocolate','burlywood','brown'],['deeppink','lightpink','hotpink']])
        self.color1 = self.colors[0]
        self.color2 = self.colors[1]
        self.color3 = self.colors[2]
        
        if fewer<more:
            fewerCellBrace = 'extrasmall'
            moreCellBrace = 'small'
        elif fewer==more:
            fewerCellBrace = 'small'
            moreCellBrace = 'small'
        else:
            fewerCellBrace = 'small'
            moreCellBrace = 'extrasmall'
        
        self.solution_text = "<br><table class='ExplanationModelTable' cellspacing='0' cellpadding='0' border=0>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>&nbsp;</td><td>%d</td><td>%d</td></tr>"%(fewer,more)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>&nbsp;</td><td style='padding-bottom:2px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td><td style='padding-bottom:3px;'><img src='/images/explanation/P3_model_up_brace_%s.png' /></td></tr>"%(fewerCellBrace,moreCellBrace)
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px;'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;border-right:white dotted 1px;'>&nbsp;</td><td style='background-color:%s;height:25px;border:white solid 1px;border-right:white dotted 1px;border-left:white dotted 1px;'>&nbsp;</td><td style='background-color:%s;height:25px;border:white solid 1px;border-left:white dotted 1px;'>&nbsp;</td><td>&nbsp;&nbsp;</td><td rowspan=5 style='padding:0;padding-top:3px;vertical-align:middle'><img src='/images/explanation/P3_model_right_brace_5row.png' /></td><td rowspan=5 style='padding:0;vertical-align:middle'>&nbsp;%d</td></tr>"%(names[1],self.color3,self.color3,self.color3,total)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px;'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;border-right:white dotted 1px;'>&nbsp;</td><td style='background-color:%s;height:25px;border:white solid 1px;border-left:white dotted 1px;'>&nbsp;</td></tr>"%(names[0],self.color2,self.color2)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>&nbsp;</td></tr>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:right;padding-right:7px;'>%s</td><td style='background-color:%s;height:25px;border:white solid 1px;'>&nbsp;</td></tr>"%(names[2],self.color1)
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td><img src='/images/explanation/P3_model_down_brace_large.png' /></td></tr>"
        self.solution_text = self.solution_text + "<tr><td>&nbsp;</td><td>?</td></tr>"
        self.solution_text = self.solution_text + "</table><br><br>"
        #end of model

        self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>%d + %d + %d</td><td style='padding-left:0px;padding-right:0px'>=</td><td style='text-align:left'>%d</td></tr>"%(fewer,fewer,more,more+fewer+fewer)
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>%d &nbsp;&minus;&nbsp; %d</td><td style='padding-left:0px;padding-right:0px'>=</td><td style='text-align:left'>%d</td></tr>"%(total,more+fewer+fewer,total-(more+fewer+fewer))
        self.solution_text = self.solution_text + "</table><br>"

        self.solution_text = self.solution_text + "<table class='ExplanationTable'>"
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>3 units</td><td style='padding-left:0px; padding-right:0px; padding-top:3px'><img src='/images/explanation/right_arrow_2.png' /></td><td style='text-align:left'>%d</td></tr>"%(total-(more+fewer+fewer))
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>1 unit</td><td style='padding-left:0px; padding-right:0px; padding-top:3px'><img src='/images/explanation/right_arrow_2.png' /></td><td style='text-align:left'>%d &nbsp;&divide;&nbsp; 3</td></tr>"%(total-(more+fewer+fewer))
        self.solution_text = self.solution_text + "<tr><td style='text-align:left'>&nbsp;</td><td style='padding-left:0px; padding-right:0px;text-align:right'>=</td><td style='text-align:left'>%d</td></tr>"%(answer)
        self.solution_text = self.solution_text + "</table><br>"
        self.solution_text = self.solution_text + "<font class='ExplanationFont'>"
        self.solution_text = self.solution_text + "&nbsp;&nbsp;&nbsp;"
        self.solution_text = self.solution_text + "%s has %d %s."%(names[2],answer,item)
        self.solution_text = self.solution_text + "</font>"
        self.solution_text = self.solution_text + "<br><br><br>"

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
                return str(answer)==str(InputAnswer).lower()
            except ValueError:
                return False            