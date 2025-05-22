'''
Created on Jan 26, 2011

Module: WordProblems
Generates "Word Problems" problems for Primary 5

Version: 1.0

Author:
   Farhat Pachisa (farhat.pachisa@homecampus.com.sg)
   
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
        ProblemList = [[self.GenerateProblemType1(),self.GenerateProblemType2(),self.GenerateProblemType3(),self.GenerateProblemType4(),self.GenerateProblemType5()],
                          [self.GenerateProblemType6(),self.GenerateProblemType7(),self.GenerateProblemType8(),self.GenerateProblemType9()],
                          [self.GenerateProblemType10(),self.GenerateProblemType11(),self.GenerateProblemType12()],
                          [self.GenerateProblemType13(),self.GenerateProblemType14(),self.GenerateProblemType15()],
                          [self.GenerateProblemType16(),self.GenerateProblemType17(),self.GenerateProblemType18(),self.GenerateProblemType19(),self.GenerateProblemType20(),self.GenerateProblemType21(),self.GenerateProblemType22()],
                          [self.GenerateProblemType23(),self.GenerateProblemType24(),self.GenerateProblemType25(),self.GenerateProblemType26()],
                          [self.GenerateProblemType27(),self.GenerateProblemType28(),self.GenerateProblemType29(),self.GenerateProblemType30()],
                          [self.GenerateProblemType31(),self.GenerateProblemType32()],
                          [self.GenerateProblemType33(),self.GenerateProblemType34()],
                          [self.GenerateProblemType35(),self.GenerateProblemType36(),self.GenerateProblemType37()],
                          [self.GenerateProblemType38(),self.GenerateProblemType39()],
                          [self.GenerateProblemType40(),self.GenerateProblemType41(),self.GenerateProblemType42()],
                          [self.GenerateProblemType43()],
                          [self.GenerateProblemType44()],
                          [self.GenerateProblemType45(),self.GenerateProblemType46()],
                          [self.GenerateProblemType47()],
                          [self.GenerateProblemType48()],
                          [self.GenerateProblemType49()],
                          [self.GenerateProblemType50(),self.GenerateProblemType51()],
                          [self.GenerateProblemType52(),self.GenerateProblemType53(),self.GenerateProblemType54(),self.GenerateProblemType55()],
                          [self.GenerateProblemType56(),self.GenerateProblemType57(),self.GenerateProblemType58(),self.GenerateProblemType59()],
                          [self.GenerateProblemType60(),self.GenerateProblemType61(),self.GenerateProblemType62()],
                          [self.GenerateProblemType63()],
                          [self.GenerateProblemType64()],
                          [self.GenerateProblemType65(),self.GenerateProblemType66()],
                          [self.GenerateProblemType67(),self.GenerateProblemType68(),self.GenerateProblemType69()],
                          [self.GenerateProblemType70()],
                          [self.GenerateProblemType71(),self.GenerateProblemType72()],
                          [self.GenerateProblemType73(),self.GenerateProblemType74(),self.GenerateProblemType75()],
                          [self.GenerateProblemType76()],
                          [self.GenerateProblemType77(),self.GenerateProblemType78()],
                          [self.GenerateProblemType79(),self.GenerateProblemType80()],
                          [self.GenerateProblemType82(),self.GenerateProblemType83()],
                          [self.GenerateProblemType84(),self.GenerateProblemType85(),self.GenerateProblemType86()],
                          [self.GenerateProblemType87(),self.GenerateProblemType88(),self.GenerateProblemType89(),self.GenerateProblemType90()],
                          [self.GenerateProblemType91()],
                          [self.GenerateProblemType92()],
                          [self.GenerateProblemType93(),self.GenerateProblemType94(),self.GenerateProblemType95(),self.GenerateProblemType96(),self.GenerateProblemType97(),self.GenerateProblemType98()],
                          [self.GenerateProblemType99(),self.GenerateProblemType100()],
                          [self.GenerateProblemType101(),self.GenerateProblemType102(),self.GenerateProblemType103()],
                          [self.GenerateProblemType104()],
                          [self.GenerateProblemType105(),self.GenerateProblemType106()],
                          [self.GenerateProblemType107(),self.GenerateProblemType108()],
                          [self.GenerateProblemType109()],
                          [self.GenerateProblemType110(),self.GenerateProblemType111(),self.GenerateProblemType112(),self.GenerateProblemType113(),self.GenerateProblemType114()],
                          [self.GenerateProblemType115(),self.GenerateProblemType116()],
                          [self.GenerateProblemType117(),self.GenerateProblemType118()],
                          [self.GenerateProblemType119(),self.GenerateProblemType120(),self.GenerateProblemType121()],
                          [self.GenerateProblemType122(),self.GenerateProblemType123()]
                          ]
        return random.choice(random.choice(ProblemList))
        #return self.GenerateProblemType116()
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:['ProblemType1','ProblemType2','ProblemType3','ProblemType4','ProblemType5',],
                            2:['ProblemType6','ProblemType7','ProblemType8','ProblemType9',],
                            3:['ProblemType10','ProblemType11','ProblemType12',],
                            4:['ProblemType13','ProblemType14','ProblemType15',],
                            5:['ProblemType16','ProblemType17','ProblemType18','ProblemType19','ProblemType20','ProblemType21','ProblemType22',],
                            6:['ProblemType23','ProblemType24','ProblemType25','ProblemType26',],
                            7:['ProblemType27','ProblemType28','ProblemType29','ProblemType30',],
                            8:['ProblemType31','ProblemType32',],
                            9:['ProblemType33','ProblemType34',],
                            10:['ProblemType35','ProblemType36','ProblemType37',],
                            11:['ProblemType38','ProblemType39',],
                            12:['ProblemType40','ProblemType41','ProblemType42',],
                            13:['ProblemType43',],
                            14:['ProblemType44',],
                            15:['ProblemType45','ProblemType46',],
                            16:['ProblemType47',],
                            17:['ProblemType48',],
                            18:['ProblemType49',],
                            19:['ProblemType50','ProblemType51',],
                            20:['ProblemType52','ProblemType53','ProblemType54','ProblemType55',],
                            21:['ProblemType56','ProblemType57','ProblemType58','ProblemType59',],
                            22:['ProblemType60','ProblemType61','ProblemType62',],
                            23:['ProblemType63',],
                            24:['ProblemType64',],
                            25:['ProblemType65','ProblemType66',],
                            26:['ProblemType67','ProblemType68','ProblemType69',],
                            27:['ProblemType70',],
                            28:['ProblemType71','ProblemType72',],
                            29:['ProblemType73','ProblemType74','ProblemType75',],
                            30:['ProblemType76',],
                            31:['ProblemType77','ProblemType78',],
                            32:['ProblemType79','ProblemType80',],
                            33:['ProblemType82','ProblemType83',],
                            34:['ProblemType84','ProblemType85','ProblemType86',],
                            35:['ProblemType87','ProblemType88','ProblemType89','ProblemType90',],
                            36:['ProblemType91',],
                            37:['ProblemType92',],
                            38:['ProblemType93','ProblemType94','ProblemType95','ProblemType96','ProblemType97','ProblemType98',],
                            39:['ProblemType99','ProblemType100',],
                            40:['ProblemType101','ProblemType102','ProblemType103',],
                            41:['ProblemType104',],
                            42:['ProblemType105','ProblemType106',],
                            43:['ProblemType107','ProblemType108',],
                            44:['ProblemType109',],
                            45:['ProblemType110','ProblemType111','ProblemType112','ProblemType113','ProblemType114',],
                            46:['ProblemType115','ProblemType116',],
                            47:['ProblemType117','ProblemType118',],
                            48:['ProblemType119','ProblemType120','ProblemType121',],
                            49:['ProblemType122','ProblemType123',],
                            }

        self.GenerateProblemType = {1:[self.GenerateProblemType1(),self.GenerateProblemType2(),self.GenerateProblemType3(),self.GenerateProblemType4(),self.GenerateProblemType5(),],
                                    2:[self.GenerateProblemType6(),self.GenerateProblemType7(),self.GenerateProblemType8(),self.GenerateProblemType9(),],
                                    3:[self.GenerateProblemType10(),self.GenerateProblemType11(),self.GenerateProblemType12(),],
                                    4:[self.GenerateProblemType13(),self.GenerateProblemType14(),self.GenerateProblemType15(),],
                                    5:[self.GenerateProblemType16(),self.GenerateProblemType17(),self.GenerateProblemType18(),self.GenerateProblemType19(),self.GenerateProblemType20(),self.GenerateProblemType21(),self.GenerateProblemType22(),],
                                    6:[self.GenerateProblemType23(),self.GenerateProblemType24(),self.GenerateProblemType25(),self.GenerateProblemType26(),],
                                    7:[self.GenerateProblemType27(),self.GenerateProblemType28(),self.GenerateProblemType29(),self.GenerateProblemType30(),],
                                    8:[self.GenerateProblemType31(),self.GenerateProblemType32(),],
                                    9:[self.GenerateProblemType33(),self.GenerateProblemType34()],
                                    10:[self.GenerateProblemType35(),self.GenerateProblemType36(),self.GenerateProblemType37()],
                                    11:[self.GenerateProblemType38(),self.GenerateProblemType39()],
                                    12:[self.GenerateProblemType40(),self.GenerateProblemType41(),self.GenerateProblemType42()],
                                    13:[self.GenerateProblemType43()],
                                    14:[self.GenerateProblemType44()],
                                    15:[self.GenerateProblemType45(),self.GenerateProblemType46()],
                                    16:[self.GenerateProblemType47()],
                                    17:[self.GenerateProblemType48()],
                                    18:[self.GenerateProblemType49()],
                                    19:[self.GenerateProblemType50(),self.GenerateProblemType51()],
                                    20:[self.GenerateProblemType52(),self.GenerateProblemType53(),self.GenerateProblemType54(),self.GenerateProblemType55()],
                                    21:[self.GenerateProblemType56(),self.GenerateProblemType57(),self.GenerateProblemType58(),self.GenerateProblemType59()],
                                    22:[self.GenerateProblemType60(),self.GenerateProblemType61(),self.GenerateProblemType62()],
                                    23:[self.GenerateProblemType63()],
                                    24:[self.GenerateProblemType64()],
                                    25:[self.GenerateProblemType65(),self.GenerateProblemType66()],
                                    26:[self.GenerateProblemType67(),self.GenerateProblemType68(),self.GenerateProblemType69()],
                                    27:[self.GenerateProblemType70()],
                                    28:[self.GenerateProblemType71(),self.GenerateProblemType72()],
                                    29:[self.GenerateProblemType73(),self.GenerateProblemType74(),self.GenerateProblemType75()],
                                    30:[self.GenerateProblemType76()],
                                    31:[self.GenerateProblemType77(),self.GenerateProblemType78()],
                                    32:[self.GenerateProblemType79(),self.GenerateProblemType80()],
                                    33:[self.GenerateProblemType82(),self.GenerateProblemType83()],
                                    34:[self.GenerateProblemType84(),self.GenerateProblemType85(),self.GenerateProblemType86()],
                                    35:[self.GenerateProblemType87(),self.GenerateProblemType88(),self.GenerateProblemType89(),self.GenerateProblemType90()],
                                    36:[self.GenerateProblemType91()],
                                    37:[self.GenerateProblemType92()],
                                    38:[self.GenerateProblemType93(),self.GenerateProblemType94(),self.GenerateProblemType95(),self.GenerateProblemType96(),self.GenerateProblemType97(),self.GenerateProblemType98()],
                                    39:[self.GenerateProblemType99(),self.GenerateProblemType100()],
                                    40:[self.GenerateProblemType101(),self.GenerateProblemType102(),self.GenerateProblemType103()],
                                    41:[self.GenerateProblemType104()],
                                    42:[self.GenerateProblemType105(),self.GenerateProblemType106()],
                                    43:[self.GenerateProblemType107(),self.GenerateProblemType108()],
                                    44:[self.GenerateProblemType109()],
                                    45:[self.GenerateProblemType110(),self.GenerateProblemType111(),self.GenerateProblemType112(),self.GenerateProblemType113(),self.GenerateProblemType114()],
                                    46:[self.GenerateProblemType115(),self.GenerateProblemType116()],
                                    47:[self.GenerateProblemType117(),self.GenerateProblemType118()],
                                    48:[self.GenerateProblemType119(),self.GenerateProblemType120(),self.GenerateProblemType121()],
                                    49:[self.GenerateProblemType122(),self.GenerateProblemType123()]
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
                            "ProblemType23":self.GenerateProblemType23(),
                            "ProblemType24":self.GenerateProblemType24(),
                            "ProblemType25":self.GenerateProblemType25(),
                            "ProblemType26":self.GenerateProblemType26(),
                            "ProblemType27":self.GenerateProblemType27(),
                            "ProblemType28":self.GenerateProblemType28(),
                            "ProblemType29":self.GenerateProblemType29(),
                            "ProblemType30":self.GenerateProblemType30(),
                            "ProblemType31":self.GenerateProblemType31(),
                            "ProblemType32":self.GenerateProblemType32(),
                            "ProblemType33":self.GenerateProblemType33(),
                            "ProblemType34":self.GenerateProblemType34(),
                            "ProblemType35":self.GenerateProblemType35(),
                            "ProblemType36":self.GenerateProblemType36(),
                            "ProblemType37":self.GenerateProblemType37(),
                            "ProblemType38":self.GenerateProblemType38(),
                            "ProblemType39":self.GenerateProblemType39(),
                            "ProblemType40":self.GenerateProblemType40(),
                            "ProblemType41":self.GenerateProblemType41(),
                            "ProblemType42":self.GenerateProblemType42(),
                            "ProblemType43":self.GenerateProblemType43(),
                            "ProblemType44":self.GenerateProblemType44(),
                            "ProblemType45":self.GenerateProblemType45(),
                            "ProblemType46":self.GenerateProblemType46(),
                            "ProblemType47":self.GenerateProblemType47(),
                            "ProblemType48":self.GenerateProblemType48(),
                            "ProblemType49":self.GenerateProblemType49(),
                            "ProblemType50":self.GenerateProblemType50(),
                            "ProblemType51":self.GenerateProblemType51(),
                            "ProblemType52":self.GenerateProblemType52(),
                            "ProblemType53":self.GenerateProblemType53(),
                            "ProblemType54":self.GenerateProblemType54(),
                            "ProblemType55":self.GenerateProblemType55(),
                            "ProblemType56":self.GenerateProblemType56(),
                            "ProblemType57":self.GenerateProblemType57(),
                            "ProblemType58":self.GenerateProblemType58(),
                            "ProblemType59":self.GenerateProblemType59(),
                            "ProblemType60":self.GenerateProblemType60(),
                            "ProblemType61":self.GenerateProblemType61(),
                            "ProblemType62":self.GenerateProblemType62(),
                            "ProblemType63":self.GenerateProblemType63(),
                            "ProblemType64":self.GenerateProblemType64(),
                            "ProblemType65":self.GenerateProblemType65(),
                            "ProblemType66":self.GenerateProblemType66(),
                            "ProblemType67":self.GenerateProblemType67(),
                            "ProblemType68":self.GenerateProblemType68(),
                            "ProblemType69":self.GenerateProblemType69(),
                            "ProblemType70":self.GenerateProblemType70(),
                            "ProblemType71":self.GenerateProblemType71(),
                            "ProblemType72":self.GenerateProblemType72(),
                            "ProblemType73":self.GenerateProblemType73(),
                            "ProblemType74":self.GenerateProblemType74(),
                            "ProblemType75":self.GenerateProblemType75(),
                            "ProblemType76":self.GenerateProblemType76(),
                            "ProblemType77":self.GenerateProblemType77(),
                            "ProblemType78":self.GenerateProblemType78(),
                            "ProblemType79":self.GenerateProblemType79(),
                            "ProblemType80":self.GenerateProblemType80(),
                            "ProblemType82":self.GenerateProblemType82(),
                            "ProblemType83":self.GenerateProblemType83(),
                            "ProblemType84":self.GenerateProblemType84(),
                            "ProblemType85":self.GenerateProblemType85(),
                            "ProblemType86":self.GenerateProblemType86(),
                            "ProblemType87":self.GenerateProblemType87(),
                            "ProblemType88":self.GenerateProblemType88(),
                            "ProblemType89":self.GenerateProblemType89(),
                            "ProblemType90":self.GenerateProblemType90(),
                            "ProblemType91":self.GenerateProblemType91(),
                            "ProblemType92":self.GenerateProblemType92(),
                            "ProblemType93":self.GenerateProblemType93(),
                            "ProblemType94":self.GenerateProblemType94(),
                            "ProblemType95":self.GenerateProblemType95(),
                            "ProblemType96":self.GenerateProblemType96(),
                            "ProblemType97":self.GenerateProblemType97(),
                            "ProblemType98":self.GenerateProblemType98(),
                            "ProblemType99":self.GenerateProblemType99(),
                            "ProblemType100":self.GenerateProblemType100(),
                            "ProblemType101":self.GenerateProblemType101(),
                            "ProblemType102":self.GenerateProblemType102(),
                            "ProblemType103":self.GenerateProblemType103(),
                            "ProblemType104":self.GenerateProblemType104(),
                            "ProblemType105":self.GenerateProblemType105(),
                            "ProblemType106":self.GenerateProblemType106(),
                            "ProblemType107":self.GenerateProblemType107(),
                            "ProblemType108":self.GenerateProblemType108(),
                            "ProblemType109":self.GenerateProblemType109(),
                            "ProblemType110":self.GenerateProblemType110(),
                            "ProblemType111":self.GenerateProblemType111(),
                            "ProblemType112":self.GenerateProblemType112(),
                            "ProblemType113":self.GenerateProblemType113(),
                            "ProblemType114":self.GenerateProblemType114(),
                            "ProblemType115":self.GenerateProblemType115(),
                            "ProblemType116":self.GenerateProblemType116(),
                            "ProblemType117":self.GenerateProblemType117(),
                            "ProblemType118":self.GenerateProblemType118(),
                            "ProblemType119":self.GenerateProblemType119(),
                            "ProblemType120":self.GenerateProblemType120(),
                            "ProblemType121":self.GenerateProblemType121(),
                            "ProblemType122":self.GenerateProblemType122(),
                            "ProblemType123":self.GenerateProblemType123(),
                            }
        return self.ProblemType[problem_type]
        
    def GenerateProblemType1(self):
        '''e.g.:Annie spent $23 on a frock and 5 times as much on a coat. 
        	If she had $200 at first, how much money had she left?'''
           
        self.GirlName = random.choice(PersonName.GirlName)
        self.ItemPool = {"frock-coat":randint(15,25),"printer-laptop":randint(200,250),
                      "thumb drive-camera":randint(50,70),"notebook-magazine":randint(2,3),
                      "handbag-dress":randint(20,30),"bag of potato chips-box of chocolates":randint(2,4),
                      "toaster-coffee maker":randint(20,70),"movie dvd-dvd player":randint(15,25),
                      "bunch of bananas-box of berries":randint(1,3),"pair of swimming goggles-swimsuit":randint(9,13),
                      "smart phone-TV":randint(250,350),"jersey-pair of shoes":randint(10,15),
                      "pencil-box of colours":randint(1,2),"can of soft drink-burger":randint(1,1),
                      "book-toy":randint(3,10),"table lamp-study table":randint(15,20),
                      "bottle of soft drink-pizza":randint(1,2),"carpet-sofa":randint(50,100),
                      "flower vase-bouquet of flowers":randint(6,9)}
        
        self.item = self.ItemPool.keys()[randint(0,len(self.ItemPool)-1)]
        self.item1 = self.item.partition("-")[0]
        self.item2 = self.item.partition("-")[2]
        self.amount = self.ItemPool[self.item]
        self.multiplier = randint(3,8)
        '''money left is between half the price of item1 and twice the price of item1'''
        self.MoneyLeft  = randint(int(self.amount*0.5),self.amount*2)
        self.InitialMoney = self.amount+self.multiplier*self.amount+self.MoneyLeft
        
        self.answer = self.MoneyLeft
        self.problem1 = "%s spent $%d on a %s and %d times as much on a %s. If she had $%d at first, how much money had she left?"%(self.GirlName,self.amount,self.item1,self.multiplier,self.item2,self.InitialMoney)
        self.problem2 = "%s paid $%d for a %s and %d times as much for a %s. If she had $%d at first, how much money did she have left?"%(self.GirlName,self.amount,self.item1,self.multiplier,self.item2,self.InitialMoney)
        self.problem3 = "%s had $%d. How much money had she left after paying $%d for a %s and %d times as much for a %s?"%(self.GirlName,self.InitialMoney,self.amount,self.item1,self.multiplier,self.item2)
        self.problem4 = "%s had $%d. She spent $%d on a %s and %d times as much on a %s. How much money had she left?"%(self.GirlName,self.InitialMoney,self.amount,self.item1,self.multiplier,self.item2)
        self.problem5 = "%s had $%d. She paid $%d for a %s and %d times as much for a %s. How much money did she have left?"%(self.GirlName,self.InitialMoney,self.amount,self.item1,self.multiplier,self.item2)
        self.problem6 = "%s bought a %s and a %s. The %s cost $%d and the %s cost %d times as much. If she had $%d at first, how much money had she left after the purchases?"%(self.GirlName,self.item1,self.item2,self.item1,self.amount,self.item2,self.multiplier,self.InitialMoney)
        self.problem = random.choice([self.problem1,self.problem2,self.problem3,self.problem4,self.problem5,self.problem6])
        
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.GirlName,self.problem,self.answer,self.multiplier,self.item1,self.item2,self.amount,self.InitialMoney)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'dollar_unit':"$",'template':self.template,'explain':self.explain,'problem_type':"ProblemType1"}

    def ExplainType1(self,GirlName,problem,answer,multiplier,item1,item2,amount,InitialMoney):
        self.answer_text = "The correct answer is: <b>$"+str(answer)
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'>"
        self.table_text = self.table_text + "<tr><td></td><td align='center'>$"+str(amount)+"<br><img src='/images/explanation/up_curly_braces_pt7cm.png'/></td></tr>"
        self.table_text = self.table_text + "<tr><td style='width:100px'>"+item1+"</td><td><img src='/images/explanation/pink_block_pt7cm.png'/></td></tr>"
        self.table_text = self.table_text + "<tr><td>"+item2+"</td>"
        for _i in range(multiplier):
            self.table_text = self.table_text+"<td><img src='/images/explanation/green_block_pt7cm.png'/></td>"
        self.table_text = self.table_text + "</tr></table><br>"
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(multiplier)+" units x $"+str(amount)+" = "+str(multiplier*amount)+"</div>"
        self.solution_text = self.solution_text + "<div>The "+item2+" cost $"+str(multiplier*amount)+".</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(amount)+" + $"+str(multiplier*amount)+" = $"+str(amount+multiplier*amount)+"</div>"
        self.solution_text = self.solution_text + "<div>"+GirlName+" spent $"+str(amount+multiplier*amount)+" altogether.</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(InitialMoney)+" - $"+str(amount+multiplier*amount)+" = $"+str(InitialMoney-(amount+multiplier*amount))+"</div>"
        self.solution_text = self.solution_text + "<div>"+GirlName+" had $"+str(InitialMoney-(amount+multiplier*amount))+" left.</div><br>"       

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    def GenerateProblemType2(self):
        '''e.g.: Annie wants a frock that costs $23 and a coat that costs 5 times as much. 
        	If she has only $120 with her, how much more will she need to buy the two items?'''
 
        self.GirlName = random.choice(PersonName.GirlName)
        self.ItemPool = {"frock-coat":randint(15,25),"printer-laptop":randint(200,250),
                      "thumb drive-camera":randint(50,70),"notebook-magazine":randint(2,3),
                      "handbag-dress":randint(20,30),"bag of potato chips-box of chocolates":randint(2,4),
                      "toaster-coffee maker":randint(20,70),"movie dvd-dvd player":randint(15,25),
                      "bunch of bananas-box of berries":randint(1,3),"pair of swimming goggles-swimsuit":randint(9,13),
                      "smart phone-TV":randint(250,350),"jersey-pair of shoes":randint(10,15),
                      "pencil-box of colours":randint(1,2),"can of soft drink-burger":randint(1,1),
                      "book-toy":randint(3,10),"table lamp-study table":randint(15,20),
                      "bottle of soft drink-pizza":randint(1,2),"carpet-sofa":randint(50,100),
                      "flower vase-bouquet of flowers":randint(6,9)}
        
        self.item = self.ItemPool.keys()[randint(0,len(self.ItemPool)-1)]
        self.item1 = self.item.partition("-")[0]
        self.item2 = self.item.partition("-")[2]
        self.amount = self.ItemPool[self.item]
        self.multiplier = randint(3,8)
        '''The initial money should be less than the self.amount+self.amount*multiplier value so that there is no negative numbers
        So min initial money is half the amount she needs to buy item 2 and max is exact money required to buy both items '''
        self.InitialMoney = randint(int(0.5*self.amount*self.multiplier),self.amount*self.multiplier+self.amount)
        self.MoneyRequired = self.amount+self.amount*self.multiplier-self.InitialMoney
        
        self.answer = self.MoneyRequired
               
        self.problem1 = "%s wants a %s that costs $%d and a %s that costs %d times as much. If she has only $%d with her, how much more will she need to buy the two items?"%(self.GirlName,self.item1,self.amount,self.item2,self.multiplier,self.InitialMoney)
        self.problem2 = "%s has $%d. She wants a %s that costs $%d and a %s that costs %d times as much. How much more money will she need?"%(self.GirlName,self.InitialMoney,self.item1,self.amount,self.item2,self.multiplier)
        self.problem3 = "%s has $%d. How much more money will she need to buy a %s that costs $%d and a %s that costs %d times as much?"%(self.GirlName,self.InitialMoney,self.item1,self.amount,self.item2,self.multiplier)
        
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])
        
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.GirlName,self.problem,self.answer,self.multiplier,self.item1,self.item2,self.amount,self.InitialMoney)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"$",'problem_type':"ProblemType2"}

    def ExplainType2(self,GirlName,problem,answer,multiplier,item1,item2,amount,InitialMoney):
        self.answer_text = "The correct answer is: <b>$"+str(answer)
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'>"
        self.table_text = self.table_text + "<tr><td></td><td align='center'>$"+str(amount)+"<br><img src='/images/explanation/up_curly_braces_pt7cm.png'/></td></tr>"
        self.table_text = self.table_text + "<tr><td style='width:100px'>"+item1+"</td><td><img src='/images/explanation/pink_block_pt7cm.png'/></td></tr>"
        self.table_text = self.table_text + "<tr><td>"+item2+"</td>"
        for _i in range(multiplier):
            self.table_text = self.table_text+"<td><img src='/images/explanation/green_block_pt7cm.png'/></td>"
        self.table_text = self.table_text + "</tr></table><br>"
        self.solution_text = """<div>Solution:</div><br>
                        <div>"""+str(multiplier)+" x $"+str(amount)+" = "+str(multiplier*amount)+"</div>"
        self.solution_text = self.solution_text + "<div>The "+item2+" costs $"+str(multiplier*amount)+".</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(amount)+" + $"+str(multiplier*amount)+" = $"+str(amount+multiplier*amount)+"</div>"
        self.solution_text = self.solution_text + "<div>"+GirlName+" needs $"+str(amount+multiplier*amount)+" altogether.</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(amount+multiplier*amount)+" - $"+str(InitialMoney)+" = $"+str(amount+multiplier*amount-InitialMoney)+"</div>"
        self.solution_text = self.solution_text + "<div>"+GirlName+" needs $"+str(amount+multiplier*amount-InitialMoney)+" more to buy the two items.</div>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain
        
    def GenerateProblemType3(self):
        '''e.g.: After paying for a frock and a coat, Annie had $62 left. If the frock cost $23 
        	and the coat cost 5 times as much as the frock, how much money had Annie at first?'''
          
        self.GirlName = random.choice(PersonName.GirlName)
        self.ItemPool = {"frock-coat":randint(15,25),"printer-laptop":randint(200,250),
                      "thumb drive-camera":randint(50,70),"notebook-magazine":randint(2,3),
                      "handbag-dress":randint(20,30),"bag of potato chips-box of chocolates":randint(2,4),
                      "toaster-coffee maker":randint(20,70),"movie dvd-dvd player":randint(15,25),
                      "bunch of bananas-box of berries":randint(1,3),"pair of swimming goggles-swimsuit":randint(9,13),
                      "smart phone-TV":randint(250,350),"jersey-pair of shoes":randint(10,15),
                      "pencil-box of colours":randint(1,2),"can of soft drink-burger":randint(1,1),
                      "book-toy":randint(3,10),"table lamp-study table":randint(15,20),
                      "bottle of soft drink-pizza":randint(1,2),"carpet-sofa":randint(50,100),
                      "flower vase-bouquet of flowers":randint(6,9)}
        
        self.item = self.ItemPool.keys()[randint(0,len(self.ItemPool)-1)]
        self.item1 = self.item.partition("-")[0]
        self.item2 = self.item.partition("-")[2]
        self.amount = self.ItemPool[self.item]
        self.multiplier = randint(3,8)
        '''money left is between half the price of item1 and twice the price of item1 and making sure its not zero'''
        self.MoneyLeft  = randint(int(self.amount*0.5),self.amount*2) + 1
        self.InitialMoney = self.MoneyLeft + self.amount + self.multiplier*self.amount
        
        self.answer = self.InitialMoney
             
        self.problem1 = "After paying for a %s and a %s, %s had $%d left. If the %s cost $%d and the %s cost %d times as much as the %s, how much money had %s at first?"%(self.item1,self.item2,self.GirlName,self.MoneyLeft,self.item1,self.amount,self.item2,self.multiplier,self.item1,self.GirlName)
        self.problem2 = "A %s costs $%d and a %s costs %d times as much. If %s is left with $%d after paying for the %s and the %s, how much money had she at first?"%(self.item1,self.amount,self.item2,self.multiplier,self.GirlName,self.MoneyLeft,self.item1,self.item2)
        self.problem3 = "%s had $%d left after paying for a %s and a %s. If the %s cost $%d and the %s cost %d times as much, how much money had %s at first?"%(self.GirlName,self.MoneyLeft,self.item1,self.item2,self.item1,self.amount,self.item2,self.multiplier,self.GirlName)
        self.problem4 = "%s bought a %s and a %s. The %s cost %d times as much as the %s. If she paid $%d for the %s and had $%d left after the purchases, how much money did she have at first?"%(self.GirlName,self.item1,self.item2,self.item2,self.multiplier,self.item1,self.amount,self.item1,self.MoneyLeft)
        
        self.problem = random.choice([self.problem1,self.problem2,self.problem3,self.problem4])
        
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.GirlName,self.problem,self.answer,self.multiplier,self.item1,self.item2,self.amount,self.MoneyLeft)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"$",'problem_type':"ProblemType3"}

    def ExplainType3(self,GirlName,problem,answer,multiplier,item1,item2,amount,MoneyLeft):
        self.answer_text = "The correct answer is: <b>$"+str(answer)
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'>"
        self.table_text = self.table_text + "<tr><td></td><td align='center'>$"+str(amount)+"<br><img src='/images/explanation/up_curly_braces_pt7cm.png'/></td></tr>"
        self.table_text = self.table_text + "<tr><td style='width:100px'>"+item1+"</td><td><img src='/images/explanation/pink_block_pt7cm.png'/></td></tr>"
        self.table_text = self.table_text + "<tr><td>"+item2+"</td>"
        for _i in range(multiplier):
            self.table_text = self.table_text+"<td><img src='/images/explanation/green_block_pt7cm.png'/></td>"
        self.table_text = self.table_text + "</tr></table><br>"
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(multiplier)+" x $"+str(amount)+" = $"+str(multiplier*amount)+"</div>"
        self.solution_text = self.solution_text + "<div>The "+item2+" costs $"+str(multiplier*amount)+".</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(amount)+" + $"+str(multiplier*amount)+" = $"+str(amount+multiplier*amount)+"</div>"
        self.solution_text = self.solution_text + "<div>"+GirlName+" needs $"+str(amount+multiplier*amount)+" altogether.</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(amount+multiplier*amount)+" + $"+str(MoneyLeft)+" = $"+str(amount+multiplier*amount+MoneyLeft)+"</div>"
        self.solution_text = self.solution_text + "<div>"+GirlName+" had $"+str(amount+multiplier*amount+MoneyLeft)+" at first.</div>"
        self.solution_text = self.solution_text + "<br><div> Watch below video for explanation of similar problem<br>"
        VideoLink = '<object><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "YFCaivv2DgA";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain
        
    def GenerateProblemType4(self):
        '''e.g.:Annie had $200. After paying for a frock and a coat, Annie had $62 left. 
        	If the coat cost 5 times as much as the frock, what was the cost of the frock?'''
         
        self.GirlName = random.choice(PersonName.GirlName)
        self.ItemPool = {"frock-coat":randint(15,25),"printer-laptop":randint(200,250),
                      "thumb drive-camera":randint(50,70),"notebook-magazine":randint(2,3),
                      "handbag-dress":randint(20,30),"bag of potato chips-box of chocolates":randint(2,4),
                      "toaster-coffee maker":randint(20,70),"movie dvd-dvd player":randint(15,25),
                      "bunch of bananas-box of berries":randint(1,3),"pair of swimming goggles-swimsuit":randint(9,13),
                      "smart phone-TV":randint(250,350),"jersey-pair of shoes":randint(10,15),
                      "pencil-box of colours":randint(1,2),"can of soft drink-burger":randint(1,1),
                      "book-toy":randint(3,10),"table lamp-study table":randint(15,20),
                      "bottle of soft drink-pizza":randint(1,2),"carpet-sofa":randint(50,100),
                      "flower vase-bouquet of flowers":randint(6,9)}
        
        self.item = self.ItemPool.keys()[randint(0,len(self.ItemPool)-1)]
        self.item1 = self.item.partition("-")[0]
        self.item2 = self.item.partition("-")[2]
        self.amount = self.ItemPool[self.item]
        self.multiplier = randint(3,8)
        '''money left is between half the price of item1 and twice the price of item1'''
        self.MoneyLeft  = randint(int(self.amount*0.5),self.amount*2)
        self.InitialMoney = self.MoneyLeft + self.amount + self.multiplier*self.amount
        
        self.answer = self.amount
             
        self.problem1 = "%s had $%d. After paying for a %s and a %s, %s had $%d left. If the %s cost %d times as much as the %s, what was the cost of the %s?"%(self.GirlName,self.InitialMoney,self.item1,self.item2,self.GirlName,self.MoneyLeft,self.item2,self.multiplier,self.item1,self.item1)
        self.problem2 = "After paying for a %s and a %s, %s had $%d left. The %s cost %d times as much as the %s. If she had $%d at first, find the cost of the %s."%(self.item1,self.item2,self.GirlName,self.MoneyLeft,self.item2,self.multiplier,self.item1,self.InitialMoney,self.item1)
        
        self.problem = random.choice([self.problem1,self.problem2])
        
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.GirlName,self.problem,self.answer,self.multiplier,self.item1,self.amount,self.item2,self.InitialMoney,self.MoneyLeft)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"$",'problem_type':"ProblemType4"}

    def ExplainType4(self,GirlName,problem,answer,multiplier,item1,amount,item2,InitialMoney,MoneyLeft):
        self.answer_text = "The correct answer is: <b>$"+str(answer)
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'>"
        self.table_text = self.table_text + "<tr><td></td><td align='center'>?<br><img src='/images/explanation/up_curly_braces_pt7cm.png'/></td></tr>"
        self.table_text = self.table_text + "<tr><td style='width:100px'>"+item1+"</td><td><img src='/images/explanation/pink_block_pt7cm.png'/></td>"
        for _i in range(multiplier-1):
            self.table_text = self.table_text+"<td></td>"        
        self.table_text = self.table_text + "<td rowspan=2><img src='/images/explanation/right_curly_braces_pt7cm.png'></td>"
        self.table_text = self.table_text + "<td rowspan=2 valign='center'>$"+str(InitialMoney)+"-$"+str(MoneyLeft)+"</td></tr>"
        self.table_text = self.table_text + "<tr><td>"+item2+"</td>"
        for _i in range(multiplier):
            self.table_text = self.table_text+"<td><img src='/images/explanation/green_block_pt7cm.png'/></td>"
        self.table_text = self.table_text + "</tr></table><br>"
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(InitialMoney)+" - $"+str(MoneyLeft)+" = $"+str(InitialMoney-MoneyLeft)+"</div>"
        self.solution_text = self.solution_text + "<div>"+GirlName+" spent $"+str(InitialMoney-MoneyLeft)+" altogether.</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(multiplier+1)+" units = $"+str(InitialMoney-MoneyLeft)+"</div>"
        self.solution_text = self.solution_text + "<div> 1 unit = $"+str(InitialMoney-MoneyLeft)+" &divide; "+str(multiplier+1)+"</div>"
        self.solution_text = self.solution_text + "<div>"+"        = $"+str(amount)+"</div><br>"
        self.solution_text = self.solution_text + "<div> The cost of the "+item1+" is $"+str(amount)+".</div>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain
        
    def GenerateProblemType5(self):
        '''e.g.:Annie had $200. After buying a frock and a coat she had $62 left. If the frock cost $23, 
    		how many times	as expensive as the frock was the coat?'''
           
        self.GirlName = random.choice(PersonName.GirlName)
        self.ItemPool = {"frock-coat":randint(15,25),"printer-laptop":randint(200,250),
                      "thumb drive-camera":randint(50,70),"notebook-magazine":randint(2,3),
                      "handbag-dress":randint(20,30),"bag of potato chips-box of chocolates":randint(2,4),
                      "toaster-coffee maker":randint(20,70),"movie dvd-dvd player":randint(15,25),
                      "bunch of bananas-box of berries":randint(1,3),"pair of swimming goggles-swimsuit":randint(9,13),
                      "smart phone-TV":randint(250,350),"jersey-pair of shoes":randint(10,15),
                      "pencil-box of colours":randint(1,2),"can of soft drink-burger":randint(1,1),
                      "book-toy":randint(3,10),"table lamp-study table":randint(15,20),
                      "bottle of soft drink-pizza":randint(1,2),"carpet-sofa":randint(50,100),
                      "flower vase-bouquet of flowers":randint(6,9)}
        
        self.item = self.ItemPool.keys()[randint(0,len(self.ItemPool)-1)]
        self.item1 = self.item.partition("-")[0]
        self.item2 = self.item.partition("-")[2]
        self.amount = self.ItemPool[self.item]
        self.multiplier = randint(3,8)
        '''money left is between half the price of item1 and twice the price of item1'''
        self.MoneyLeft  = randint(int(self.amount*0.5),self.amount*2)
        self.InitialMoney = self.MoneyLeft + self.amount + self.multiplier*self.amount
        
        self.answer = self.multiplier
             
        self.problem1 = "%s had $%d. After buying a %s and a %s she had $%d left. If the %s cost $%d, how many times as expensive as the %s was the %s?"%(self.GirlName,self.InitialMoney,self.item1,self.item2,self.MoneyLeft,self.item1,self.amount,self.item1,self.item2)   
        self.problem2 = "After buying a %s and a %s, %s had $%d of her $%d left. If the %s cost $%d, how many times as expensive as the %s was the %s?"%(self.item1,self.item2,self.GirlName,self.MoneyLeft,self.InitialMoney,self.item1,self.amount,self.item1,self.item2)
        self.problem3 = "%s had $%d of her $%d left after buying a %s and a %s. If the %s cost $%d, how many times as expensive as the %s was the %s?"%(self.GirlName,self.MoneyLeft,self.InitialMoney,self.item1,self.item2,self.item1,self.amount,self.item1,self.item2)
        
        self.problem = random.choice([self.problem1,self.problem2])
        
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5(self.GirlName,self.problem,self.answer,self.multiplier,self.amount,self.item1,self.item2,self.InitialMoney,self.MoneyLeft)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"",'unit':"times",'problem_type':"ProblemType5"}

    def ExplainType5(self,GirlName,problem,answer,multiplier,amount,item1,item2,InitialMoney,MoneyLeft):
        self.answer_text = "The correct answer is: <b>"+str(answer)+"</b> times"
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'>"
        self.table_text = self.table_text + "<tr><td></td><td align='center'>$"+str(amount)+"<br><img src='/images/explanation/up_curly_braces_pt7cm.png'/></td></tr>"
        self.table_text = self.table_text + "<tr><td style='width:100px'>"+item1+"</td><td><img src='/images/explanation/pink_block_pt7cm.png'/></td></tr>"
        self.table_text = self.table_text + "<tr><td>"+item2+"</td>"
        '''putting the third block as broken'''
        for _i in range(2):
            self.table_text = self.table_text+"<td><img src='/images/explanation/green_block_pt7cm.png'/></td>"
        self.table_text = self.table_text +  "<td><img src='/images/explanation/broken_green_block_pt7cm.png'/></td>"
        for _i in range(multiplier-3):
            self.table_text = self.table_text+"<td><img src='/images/explanation/green_block_pt7cm.png'/></td>"
        self.table_text = self.table_text + "</tr></table><br>"
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(InitialMoney)+" - $"+str(MoneyLeft)+" = "+str(InitialMoney-MoneyLeft)+"</div>"
        self.solution_text = self.solution_text + "<div>"+GirlName+" spent $"+str(InitialMoney-MoneyLeft)+" altogether.</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(InitialMoney-MoneyLeft)+" - $"+str(amount)+ " = $"+str(InitialMoney-MoneyLeft-amount)+"</div>"
        self.solution_text = self.solution_text + "<div> The "+ item2+" cost $"+str(InitialMoney-MoneyLeft-amount)+".</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(InitialMoney-MoneyLeft-amount)+" &divide; $"+str(amount)+" = "+str((InitialMoney-MoneyLeft-amount)/amount)+"</div>"
        self.solution_text = self.solution_text + "<div> The "+item2+" was "+str((InitialMoney-MoneyLeft-amount)/amount)+" times as expensive as the "+item1+".</div>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    '''Problem Type 2 starts here as defined in the problem ppt'''
    def GenerateProblemType6(self):
        '''e.g.:Bala had $15. He bought 3 bars of chocolate for $2 each and 6 cans of soda for $1 each. 
    		How much money had he left?'''
           
        self.BoyName = random.choice(PersonName.BoyName)
        self.ItemPool = {"ties-scarves":randint(15,25),"bowls-spoons":randint(2,4),
                      "notebooks-pens":randint(2,3),"plates-trays":randint(3,4),
                      "bags of potato chips-boxes of chocolates":randint(2,4),
                      "mugs-glasses":randint(2,5),"photo frames-movie dvds":randint(10,20),
                      "buns-cakes":randint(2,4),"shirts-pants":randint(15,40),
                      "rubber bands-marbles":randint(1,2),"jerseys-pairs of shoes":randint(10,50),
                      "toy cars-toy robots":randint(5,20),"cookies-burgers":randint(2,4),
                      "books-toys":randint(3,10),"chairs-tables":randint(20,40),
                      "flower pots-plants":randint(5,15),"pillows-blankets":randint(15,40),
                      "pails-tumblers":randint(3,9)}
        
        self.item = self.ItemPool.keys()[randint(0,len(self.ItemPool)-1)]
        self.item1 = self.item.partition("-")[0]
        self.item2 = self.item.partition("-")[2]
        '''number of items the boy will buy'''
        self.number1 = randint(3,6)
        self.number2 = randint(3,6)
        '''the amount he will pay for which item'''
        self.amount1 = self.ItemPool[self.item]
        self.amount2 = randint(int(self.amount1*1.25),int(self.amount1*2))

        '''money left is between half the value of (amount1*number1) and twice the value of (amount1*number1)'''
        self.MoneyLeft  = randint(int(self.amount1*self.number1*0.5),self.amount1*self.number1*2)
        self.InitialMoney = self.MoneyLeft + self.amount1*self.number1 + self.amount2*self.number2
        
        self.answer = self.MoneyLeft
        
        self.problem1 = "%s had $%d. He bought %d %s for $%d each and %d %s for $%d each. How much money had he left?"%(self.BoyName,self.InitialMoney,self.number1,self.item1,self.amount1,self.number2,self.item2,self.amount2)   
        self.problem2 = "%s had $%d. How much money had he left after paying $%d for each of %d %s and $%d for each of %d %s?"%(self.BoyName,self.InitialMoney,self.amount1,self.number1,self.item1,self.amount2,self.number2,self.item2)
        self.problem3 = "%s bought %d %s for $%d each and %d %s for $%d each. If he had $%d at first, how much money did he have left?"%(self.BoyName,self.number1,self.item1,self.amount1,self.number2,self.item2,self.amount2,self.InitialMoney)
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])
        
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6(self.BoyName,self.problem,self.answer,self.number1,self.amount1,self.item1,self.number2,self.amount2,self.item2,self.InitialMoney,self.MoneyLeft)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"$",'problem_type':"ProblemType6"}

    def ExplainType6(self,BoyName,problem,answer,number1,amount1,item1,number2,amount2,item2,InitialMoney,MoneyLeft):
        self.answer_text = "The correct answer is: <b>$"+str(answer)+"</b>"
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'>"
        self.table_text = self.table_text + "<tr><td align='center'>$"+str(amount2)+"<br><img src='/images/explanation/up_curly_braces_pt7cm.png'/></td>"
        for _i in range(number2-1):
            self.table_text = self.table_text + "<td>"
        self.table_text = self.table_text + "<td align='center'>$"+str(amount1)+"<br><img src='/images/explanation/up_curly_braces_pt5cm.png'/></td></tr>"
        self.table_text = self.table_text + "<tr>"
        for _i in range(number2):
            self.table_text = self.table_text + "<td><img src='/images/explanation/pink_block_pt7cm.png'/></td>"
        for _i in range(number1):
            self.table_text = self.table_text + "<td><img src='/images/explanation/green_block_pt5cm.png'/></td>"
        self.table_text = self.table_text +  "</tr>"
        '''adjusting the down curly braces to span all the columns'''
        self.table_text = self.table_text + "<tr><td align='center' colspan="+str(number1+number2)+"><img src='/images/explanation/down_curly_braces_3cm.png' width="+str((number1*34+number2*46))+" height=23/></td>"
        self.table_text = self.table_text + "<tr><td align='center' colspan="+str(number1+number2)+">?</td>"
        self.table_text = self.table_text + "</tr></table><br>"

        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(number1)+" x $"+str(amount1)+" = $"+str(number1*amount1)+"</div>"
        self.solution_text = self.solution_text + "<div>Total cost of "+item1+" is $"+str(number1*amount1)+".</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(number2)+" x $"+str(amount2)+" = $"+str(number2*amount2)+"</div>"
        self.solution_text = self.solution_text + "<div>Total cost of "+item2+" is $"+str(number2*amount2)+".</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(number1*amount1)+" + $"+str(number2*amount2)+ " = $"+str(number1*amount1+number2*amount2)+"</div>"
        self.solution_text = self.solution_text + "<div>"+BoyName+" spent a total of $"+str(number1*amount1+number2*amount2)+".</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(InitialMoney)+" - $"+str(number1*amount1+number2*amount2)+" = $"+str(InitialMoney-(number1*amount1+number2*amount2))+"</div>"
        self.solution_text = self.solution_text + "<div>"+BoyName+" had $"+str(InitialMoney-(number1*amount1+number2*amount2))+" left.</div>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    def GenerateProblemType7(self):
        '''e.g.:Bala had $15. After paying for 3 bars of chocolate and 6 cans of soda, he had $3 left. 
    		If each bar of chocolate cost $2, find the cost of each can of soda.'''
           
        self.BoyName = random.choice(PersonName.BoyName)
        self.ItemPool = {"ties-scarves":randint(15,25),"bowls-spoons":randint(2,4),
                      "notebooks-pens":randint(2,3),"plates-trays":randint(3,4),
                      "bags of potato chips-boxes of chocolates":randint(2,4),
                      "mugs-glasses":randint(2,5),"photo frames-movie dvds":randint(10,20),
                      "buns-cakes":randint(2,4),"shirts-pairs of pants":randint(15,40),
                      "rubber bands-marbles":randint(1,3),"jerseys-pairs of shoes":randint(10,50),
                      "toy cars-toy robots":randint(5,20),"cookies-burgers":randint(2,4),
                      "books-toys":randint(3,10),"chairs-tables":randint(20,40),
                      "flower pots-plants":randint(5,15),"pillows-blankets":randint(15,40),
                      "pails-tumblers":randint(3,9)}
        
        '''To make grammatically correct statement we need singular form of the items above'''
        self.SingleItem = {"ties":"tie","scarves":"scarf","bowls":"bowl","spoons":"spoon",
                      "notebooks":"notebook","pens":"pen","plates":"plate","trays":"tray",
                      "bags of potato chips":"bag of potato chips","boxes of chocolates":"box of chocolates",
                      "mugs":"mug","glasses":"glass","photo frames":"photo frame","movie dvds":"movie dvd",
                      "buns":"bun","cakes":"cake","shirts":"shirt","pairs of pants":"pair of pants",
                      "rubber bands":"rubber band","marbles":"marble","jerseys":"jersey","pairs of shoes":"pair of shoes",
                      "toy cars":"toy car","toy robots":"toy robot","cookies":"cookie","burgers":"burger",
                      "books":"book","toys":"toy","chairs":"chair","tables":"table",
                      "flower pots":"flower pot","plants":"plant","pillows":"pillow","blankets":"blanket",
                      "pails":"pail","tumblers":"tumbler"}        
        
        self.item = self.ItemPool.keys()[randint(0,len(self.ItemPool)-1)]
        self.item1 = self.item.partition("-")[0]
        self.item2 = self.item.partition("-")[2]
        self.SingleItem1 = self.SingleItem[self.item1]
        self.SingleItem2 = self.SingleItem[self.item2]
        '''number of items the boy will buy'''
        self.number1 = randint(3,6)
        self.number2 = randint(3,6)
        '''the amount he will pay for which item'''
        self.amount1 = self.ItemPool[self.item]
        self.amount2 = randint(int(self.amount1*1.25),int(self.amount1*2))

        '''money left is between half the value of (amount1*number1) and twice the value of (amount1*number1)'''
        self.MoneyLeft  = randint(int(self.amount1*self.number1*0.5),self.amount1*self.number1*2)
        self.InitialMoney = self.MoneyLeft + self.amount1*self.number1 + self.amount2*self.number2
        
        self.answer = self.amount2      
        
        self.problem1 = "%s had $%d. After paying for %d %s and %d %s, he had $%d left. If each %s cost $%d, find the cost of each %s."%(self.BoyName,self.InitialMoney,self.number1,self.item1,self.number2,self.item2,self.MoneyLeft,self.SingleItem1,self.amount1,self.SingleItem2)
        self.problem2 = "%s had $%d. He bought %d %s for $%d each. He also bought %d %s and had $%d left. What was the cost of each %s?"%(self.BoyName,self.InitialMoney,self.number1,self.item1,self.amount1,self.number2,self.item2,self.MoneyLeft,self.SingleItem2)
        self.problem3 = "After paying for %d %s and %d %s, %s had $%d left. If he had $%d at first and each %s cost $%d, find the cost of each %s."%(self.number1,self.item1,self.number2,self.item2,self.BoyName,self.MoneyLeft,self.InitialMoney,self.SingleItem1,self.amount1,self.SingleItem2)
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])
        
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7(self.BoyName,self.problem,self.answer,self.number1,self.amount1,self.item1,self.SingleItem1,self.number2,self.amount2,self.item2,self.SingleItem2,self.InitialMoney,self.MoneyLeft)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"$",'problem_type':"ProblemType7"}

    def ExplainType7(self,BoyName,problem,answer,number1,amount1,item1,SingleItem1,number2,amount2,item2,SingleItem2,InitialMoney,MoneyLeft):
        self.answer_text = "The correct answer is: <b>$"+str(answer)+"</b>"
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'>"
        self.table_text = self.table_text + "<tr><td align='center'>?<br><img src='/images/explanation/up_curly_braces_pt7cm.png'/></td>"
        for _i in range(number2-1):
            self.table_text = self.table_text + "<td>"
        self.table_text = self.table_text + "<td align='center'>$"+str(amount1)+"<br><img src='/images/explanation/up_curly_braces_pt5cm.png'/></td></tr>"
        self.table_text = self.table_text + "<tr>"
        for _i in range(number2):
            self.table_text = self.table_text + "<td><img src='/images/explanation/pink_block_pt7cm.png'/></td>"
        for _i in range(number1):
            self.table_text = self.table_text + "<td><img src='/images/explanation/green_block_pt5cm.png'/></td>"
        self.table_text = self.table_text +  "</tr>"
        '''adjusting the down curly braces to span all the columns'''
        self.table_text = self.table_text + "<tr><td align='center' colspan="+str(number1+number2)+"><img src='/images/explanation/down_curly_braces_3cm.png' width="+str((number1*34+number2*46))+" height=23/></td>"
        self.table_text = self.table_text + "<tr><td align='center' colspan="+str(number1+number2)+">$"+str(InitialMoney)+" - $"+str(MoneyLeft)+"</td>"
        self.table_text = self.table_text + "</tr></table><br>"

        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(InitialMoney)+" - $"+str(MoneyLeft)+" = $"+str(InitialMoney-MoneyLeft)+"</div>"
        self.solution_text = self.solution_text + "<div>"+BoyName+" spent $"+str(InitialMoney-MoneyLeft)+" altogether.</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(number1)+" "+item1+" x $"+str(amount1)+" = $"+str(number1*amount1)+"</div>"
        self.solution_text = self.solution_text + "<div>Total cost of "+item1+" is $"+str(number1*amount1)+".</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(InitialMoney-MoneyLeft)+" - $"+str(number1*amount1)+ " = $"+str((InitialMoney-MoneyLeft)-number1*amount1)+"</div>"
        self.solution_text = self.solution_text + "<div>Total cost of "+item2+" is $"+str((InitialMoney-MoneyLeft)-number1*amount1)+".</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str((InitialMoney-MoneyLeft)-number1*amount1)+" &divide; "+str(number2)+" "+item2+" = $"+str(((InitialMoney-MoneyLeft)-number1*amount1)/number2)+"</div>"
        self.solution_text = self.solution_text + "<div> The cost of each "+SingleItem2+" is $"+str(((InitialMoney-MoneyLeft)-number1*amount1)/number2)+".</div>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    def GenerateProblemType8(self):
        '''e.g.:Bala had $15. After paying for 3 bars of chocolate and some cans of soda, he had $3 left. If each bar
		of chocolate cost $2 and each can of soda cost $1, find the number of cans of soda he bought.'''
            
        self.BoyName = random.choice(PersonName.BoyName)
        self.ItemPool = {"ties-scarves":randint(15,25),"bowls-spoons":randint(2,4),
                      "notebooks-pens":randint(2,3),"plates-trays":randint(3,4),
                      "bags of potato chips-boxes of chocolates":randint(2,4),
                      "mugs-glasses":randint(2,5),"photo frames-movie dvds":randint(10,20),
                      "buns-cakes":randint(2,4),"shirts-pairs of pants":randint(15,40),
                      "rubber bands-marbles":randint(1,2),"jerseys-pairs of shoes":randint(10,50),
                      "toy cars-toy robots":randint(5,20),"cookies-burgers":randint(2,4),
                      "books-toys":randint(3,10),"chairs-tables":randint(20,40),
                      "flower pots-plants":randint(5,15),"pillows-blankets":randint(15,40),
                      "pails-tumblers":randint(3,9)}

        '''To make grammatically correct statement we need singular form of the items above'''
        self.SingleItem = {"ties":"tie","scarves":"scarf","bowls":"bowl","spoons":"spoon",
                      "notebooks":"notebook","pens":"pen","plates":"plate","trays":"tray",
                      "bags of potato chips":"bag of potato chips","boxes of chocolates":"box of chocolates",
                      "mugs":"mug","glasses":"glass","photo frames":"photo frame","movie dvds":"movie dvd",
                      "buns":"bun","cakes":"cake","shirts":"shirt","pairs of pants":"pair of pants",
                      "rubber bands":"rubber band","marbles":"marble","jerseys":"jersey","pairs of shoes":"pair of shoes",
                      "toy cars":"toy car","toy robots":"toy robot","cookies":"cookie","burgers":"burger",
                      "books":"book","toys":"toy","chairs":"chair","tables":"table",
                      "flower pots":"flower pot","plants":"plant","pillows":"pillow","blankets":"blanket",
                      "pails":"pail","tumblers":"tumbler"}        
        
        self.item = self.ItemPool.keys()[randint(0,len(self.ItemPool)-1)]
        self.item1 = self.item.partition("-")[0]
        self.item2 = self.item.partition("-")[2]
        self.SingleItem1 = self.SingleItem[self.item1]
        self.SingleItem2 = self.SingleItem[self.item2]
        '''number of items the boy will buy'''
        self.number1 = randint(3,7)
        self.number2 = randint(3,7)
        '''the amount he will pay for which item'''
        self.amount1 = self.ItemPool[self.item]
        self.amount2 = randint(int(self.amount1*1.25),int(self.amount1*2))

        '''money left is between half the value of (amount1*number1) and twice the value of (amount1*number1)'''
        self.MoneyLeft  = randint(int(self.amount1*self.number1*0.5),self.amount1*self.number1*2)
        self.InitialMoney = self.MoneyLeft + self.amount1*self.number1 + self.amount2*self.number2
        
        self.answer = self.number2      
           
        self.problem1 = "%s had $%d. After paying for %d %s and some %s, he had $%d left. If each %s cost $%d and each %s cost $%d, find the number of %s he bought."%(self.BoyName,self.InitialMoney,self.number1,self.item1,self.item2,self.MoneyLeft,self.SingleItem1,self.amount1,self.SingleItem2,self.amount2,self.item2)
        self.problem2 = "%s had $%d. He bought %d %s for $%d each. He also bought some %s for $%d each and had $%d left. How many %s did he buy?"%(self.BoyName,self.InitialMoney,self.number1,self.item1,self.amount1,self.item2,self.amount2,self.MoneyLeft,self.item2)
        self.problem3 = "After paying for %d %s and some %s, %s had $%d left. He had $%d at first. Each %s cost $%d and each %s cost $%d. Find the number of %s he bought."%(self.number1,self.item1,self.item2,self.BoyName,self.MoneyLeft,self.InitialMoney,self.SingleItem1,self.amount1,self.SingleItem2,self.amount2,self.item2)
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])
        
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType8(self.BoyName,self.problem,self.answer,self.number1,self.amount1,self.item1,self.SingleItem1,self.number2,self.amount2,self.item2,self.SingleItem2,self.InitialMoney,self.MoneyLeft)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"",'unit':self.item2,'problem_type':"ProblemType8"}

    def ExplainType8(self,BoyName,problem,answer,number1,amount1,item1,SingleItem1,number2,amount2,item2,SingleItem2,InitialMoney,MoneyLeft):
        self.answer_text = "The correct answer is: <b>"+str(answer)+" "+item2
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'>"
        self.table_text = self.table_text + "<tr><td align='center'>$"+str(amount2)+"<br><img src='/images/explanation/up_curly_braces_pt7cm.png'/></td>"
        for _i in range(number2-1):
            self.table_text = self.table_text + "<td>"
        self.table_text = self.table_text + "<td align='center'>$"+str(amount1)+"<br><img src='/images/explanation/up_curly_braces_pt5cm.png'/></td></tr>"
        self.table_text = self.table_text + "<tr>"
        '''creating pink blocks for item2 and inserting a broken block at 3rd position'''
        for _i in range(2):
            self.table_text = self.table_text + "<td><img src='/images/explanation/pink_block_pt7cm.png'/></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/broken_pink_block_pt7cm.png'/></td>"
        for _i in range(number2-3):
            self.table_text = self.table_text + "<td><img src='/images/explanation/pink_block_pt7cm.png'/></td>"        
        for _i in range(number1):
            self.table_text = self.table_text + "<td><img src='/images/explanation/green_block_pt5cm.png'/></td>"
        self.table_text = self.table_text +  "</tr>"
        '''adjusting the down curly braces to span all the columns'''
        self.table_text = self.table_text + "<tr><td align='center' colspan="+str(number2)+"><img src='/images/explanation/down_curly_braces_3cm.png' width="+str(number2*46)+" height=23/></td>"
        self.table_text = self.table_text + "<tr><td align='center' colspan="+str(number2)+">?</td>"
        self.table_text = self.table_text + "</tr></table><br>"

        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(InitialMoney)+" - $"+str(MoneyLeft)+" = $"+str(InitialMoney-MoneyLeft)+"</div>"
        self.solution_text = self.solution_text + "<div>"+BoyName+" spent $"+str(InitialMoney-MoneyLeft)+" altogether.</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(number1)+" "+item1+" x $"+str(amount1)+" = $"+str(number1*amount1)+"</div>"
        self.solution_text = self.solution_text + "<div>Total cost of "+item1+" is $"+str(number1*amount1)+".</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(InitialMoney-MoneyLeft)+" - $"+str(number1*amount1)+ " = $"+str((InitialMoney-MoneyLeft)-number1*amount1)+"</div>"
        self.solution_text = self.solution_text + "<div>Total cost of "+item2+" is $"+str((InitialMoney-MoneyLeft)-number1*amount1)+".</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str((InitialMoney-MoneyLeft)-number1*amount1)+" &divide;$ "+str(amount2)+" = "+str(((InitialMoney-MoneyLeft)-number1*amount1)/amount2)+" "+item2+"</div>"
        self.solution_text = self.solution_text + "<div>"+BoyName+" bought "+str(((InitialMoney-MoneyLeft)-number1*amount1)/amount2)+" "+item2+".</div>"
        self.solution_text = self.solution_text + "<br><div> Watch below video for explanation of similar problem<br>"
        VideoLink = '<object><param name="movie" value="https://www.youtube.com/v/u1zgFlCw8Aw?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded"><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "8pXRGKpOA4E";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    def GenerateProblemType9(self):
        '''e.g.:After paying for 3 bars of chocolate and 6 cans of soda, Bala had $3 left. If each bar of chocolate cost $2
		and each can of soda cost $1, how much money had Bala at first?'''
            
        self.BoyName = random.choice(PersonName.BoyName)
        self.ItemPool = {"ties-scarves":randint(15,25),"bowls-spoons":randint(2,4),
                      "notebooks-pens":randint(2,3),"plates-trays":randint(3,4),
                      "bags of potato chips-boxes of chocolates":randint(2,4),
                      "mugs-glasses":randint(2,5),"photo frames-movie dvds":randint(10,20),
                      "buns-cakes":randint(2,4),"shirts-pairs of pants":randint(15,40),
                      "rubber bands-marbles":randint(1,2),"jerseys-pairs of shoes":randint(10,50),
                      "toy cars-toy robots":randint(5,20),"cookies-burgers":randint(2,4),
                      "books-toys":randint(3,10),"chairs-tables":randint(20,40),
                      "flower pots-plants":randint(5,15),"pillows-blankets":randint(15,40),
                      "pails-tumblers":randint(3,9)}

        '''To make grammatically correct statement we need singular form of the items above'''
        self.SingleItem = {"ties":"tie","scarves":"scarf","bowls":"bowl","spoons":"spoon",
                      "notebooks":"notebook","pens":"pen","plates":"plate","trays":"tray",
                      "bags of potato chips":"bag of potato chips","boxes of chocolates":"box of chocolates",
                      "mugs":"mug","glasses":"glass","photo frames":"photo frame","movie dvds":"movie dvd",
                      "buns":"bun","cakes":"cake","shirts":"shirt","pairs of pants":"pair of pants",
                      "rubber bands":"rubber band","marbles":"marble","jerseys":"jersey","pairs of shoes":"pair of shoes",
                      "toy cars":"toy car","toy robots":"toy robot","cookies":"cookie","burgers":"burger",
                      "books":"book","toys":"toy","chairs":"chair","tables":"table",
                      "flower pots":"flower pot","plants":"plant","pillows":"pillow","blankets":"blanket",
                      "pails":"pail","tumblers":"tumbler"}        
        
        self.item = self.ItemPool.keys()[randint(0,len(self.ItemPool)-1)]
        self.item1 = self.item.partition("-")[0]
        self.item2 = self.item.partition("-")[2]
        self.SingleItem1 = self.SingleItem[self.item1]
        self.SingleItem2 = self.SingleItem[self.item2]
        '''number of items the boy will buy'''
        self.number1 = randint(3,7)
        self.number2 = randint(3,6)
        '''the amount he will pay for which item'''
        self.amount1 = self.ItemPool[self.item]
        self.amount2 = randint(int(self.amount1*1.25),int(self.amount1*2))

        '''money left is between half the value of (amount1*number1) and twice the value of (amount1*number1)'''
        self.MoneyLeft  = randint(int(self.amount1*self.number1*0.5),self.amount1*self.number1*2)
        self.InitialMoney = self.MoneyLeft + self.amount1*self.number1 + self.amount2*self.number2
        
        self.answer = self.InitialMoney
        
        self.problem1 = "After paying for %d %s and %d %s, %s had $%d left. If each %s cost $%d and each %s cost $%d, how much money had %s at first?"%(self.number1,self.item1,self.number2,self.item2,self.BoyName,self.MoneyLeft,self.SingleItem1,self.amount1,self.SingleItem2,self.amount2,self.BoyName)
        self.problem2 = "%s bought %d %s for $%d each and %d %s for $%d each. If he had $%d left, how much money did he have at first?"%(self.BoyName,self.number1,self.item1,self.amount1,self.number2,self.item2,self.amount2,self.MoneyLeft)
        self.problem3 = "%s had $%d left after paying $%d for each of %d %s and $%d for each of %d %s? How much money had he at first?"%(self.BoyName,self.MoneyLeft,self.amount1,self.number1,self.item1,self.amount2,self.number2,self.item2)
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])
        
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType9(self.BoyName,self.problem,self.answer,self.number1,self.amount1,self.item1,self.SingleItem1,self.number2,self.amount2,self.item2,self.SingleItem2,self.InitialMoney,self.MoneyLeft)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"$",'problem_type':"ProblemType9"}

    def ExplainType9(self,BoyName,problem,answer,number1,amount1,item1,SingleItem1,number2,amount2,item2,SingleItem2,InitialMoney,MoneyLeft):
        self.answer_text = "The correct answer is: <b>$"+str(answer)+"</b>"
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'>"
        self.table_text = self.table_text + "<tr><td align='center'>$"+str(amount2)+"<br><img src='/images/explanation/up_curly_braces_pt7cm.png'/></td>"
        for _i in range(number2-1):
            self.table_text = self.table_text + "<td>"
        self.table_text = self.table_text + "<td align='center'>$"+str(amount1)+"<br><img src='/images/explanation/up_curly_braces_pt5cm.png'/></td></tr>"
        self.table_text = self.table_text + "<tr>"
        for _i in range(number2):
            self.table_text = self.table_text + "<td><img src='/images/explanation/pink_block_pt7cm.png'/></td>"
        for _i in range(number1):
            self.table_text = self.table_text + "<td><img src='/images/explanation/green_block_pt5cm.png'/></td>"
        self.table_text = self.table_text +  "</tr>"
        '''adjusting the down curly braces to span all the columns'''
        self.table_text = self.table_text + "<tr><td align='center' colspan="+str(number1+number2)+"><img src='/images/explanation/down_curly_braces_3cm.png' width="+str((number1*34+number2*46))+" height=23/></td>"
        self.table_text = self.table_text + "<tr><td align='center' colspan="+str(number1+number2)+">?</td>"
        self.table_text = self.table_text + "</tr></table><br>"
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(number1)+" x $"+str(amount1)+" = $"+str(number1*amount1)+"</div>"
        self.solution_text = self.solution_text + "<div>Total cost of "+item1+" is $"+str(number1*amount1)+".</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(number2)+" x $"+str(amount2)+" = $"+str(number2*amount2)+"</div>"
        self.solution_text = self.solution_text + "<div>Total cost of "+item2+" is $"+str(number2*amount2)+".</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(number1*amount1)+" + $"+str(number2*amount2)+ " = $"+str(number1*amount1+number2*amount2)+"</div>"
        self.solution_text = self.solution_text + "<div>"+BoyName+" spent a total of $"+str(number1*amount1+number2*amount2)+".</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(number1*amount1+number2*amount2)+" + $"+str(MoneyLeft)+" = $"+str(number1*amount1+number2*amount2+MoneyLeft)+"</div>"
        self.solution_text = self.solution_text + "<div>"+BoyName+" had $"+str(number1*amount1+number2*amount2+MoneyLeft)+" at first.</div>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain
        
        '''Problem Type 3 starts here as defined in the problem ppt'''
    def GenerateProblemType10(self):
        '''e.g.:Annie bought 2 similar frocks and a coat. The coat cost $92 more than each frock. If the cost of the coat
		was 5 times as much as the cost of each frock, how much money did Annie spend altogether?'''
            
        self.GirlName = random.choice(PersonName.GirlName)
        self.ItemPool = {"ties-jacket":randint(15,50),"bowls-microwave":randint(15,30),
                      "notebooks-toy":randint(4,10),"boxes of chocolates-christmas tree":randint(5,15),
                      "plates-cooking pot":randint(4,10),"mugs-coffee maker":randint(5,15),
                      "pastries-cake":randint(1,5),"shirts-pair of pants":randint(15,20),"marbles-board game":randint(1,5),
                      "toy cars-toy house":randint(2,10),"jerseys-pair of soccer boots":randint(10,30),
                      "chickens-lamb":randint(5,10),"cans of soft drink-burger":randint(1,3),
                      "thumb drives-printer":randint(15,30),"chairs-table":randint(10,30),
                      "flower pots-water hose":randint(5,10),"pillows-mattress":randint(10,25),
                      "rings-necklace":randint(5,50)}

        '''To make grammatically correct statement we need singular form of the items above'''
        self.SingleItem = {"ties":"tie","bowls":"bowl","notebooks":"notebook","plates":"plate","mugs":"mug",
                      "boxes of chocolates":"box of chocolates",
                      "pastries":"pastry","shirts":"shirt","marbles":"marble","toy cars":"toy car",
                      "jerseys":"jersey","chickens":"chicken","cans of soft drink":"can of soft drink",
                      "thumb drives":"thumb drive","chairs":"chair","flower pots":"flower pot",
                      "pillows":"pillow","rings":"ring"}        
        
        self.item = self.ItemPool.keys()[randint(0,len(self.ItemPool)-1)]
        self.item1 = self.item.partition("-")[0]
        self.item2 = self.item.partition("-")[2]
        self.SingleItem1 = self.SingleItem[self.item1]
        '''number of items the boy will buy'''
        self.number1 = randint(3,7)
        '''the amount he will pay for each item'''
        self.amount1 = self.ItemPool[self.item]
        self.multiplier = randint(3,7)
        self.amount2 = self.multiplier * self.amount1
        self.diff = self.amount2 - self.amount1
        self.MoneySpent = self.number1*self.amount1 + self.amount2
        
        self.answer = self.MoneySpent
        
        self.problem1 = "%s bought %d similar %s and a %s. The %s cost $%d more than each %s. If the cost of the %s was %d times as much as the cost of each %s, how much money did %s spend altogether?"%(self.GirlName,self.number1,self.item1,self.item2,self.item2,self.diff,self.SingleItem1,self.item2,self.multiplier,self.SingleItem1,self.GirlName)
        self.problem2 = "A %s costs %d times as much as a %s. The %s costs $%d more than each %s. If %s bought %d similar %s and a %s, how much did she spend altogether?"%(self.item2,self.multiplier,self.SingleItem1,self.item2,self.diff,self.SingleItem1,self.GirlName,self.number1,self.item1,self.item2)
        self.problem3 = "A %s costs %d times as much as a %s. Each %s costs $%d less than the %s. If %s bought %d similar %s and a %s, how much did she spend altogether?"%(self.item2,self.multiplier,self.SingleItem1,self.SingleItem1,self.diff,self.item2,self.GirlName,self.number1,self.item1,self.item2)
        self.problem4 = "%s bought %d similar %s and a %s. Each %s cost $%d less than the %s. If the cost of the %s was %d times as much as the cost of each %s, how much money did %s spend altogether?"%(self.GirlName,self.number1,self.item1,self.item2,self.SingleItem1,self.diff,self.item2,self.item2,self.multiplier,self.SingleItem1,self.GirlName)
        self.problem = random.choice([self.problem1,self.problem2,self.problem3,self.problem4])
        
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType10(self.GirlName,self.problem,self.answer,self.number1,self.amount1,self.item1,self.SingleItem1,self.amount2,self.item2,self.diff,self.multiplier)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"$",'problem_type':"ProblemType10"}

    def ExplainType10(self,GirlName,problem,answer,number1,amount1,item1,SingleItem1,amount2,item2,diff,multiplier):
        self.answer_text = "The correct answer is: <b>$"+str(answer)+"</b>"
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'><tr><td>"+item1+"</td><td><img src='/images/explanation/green_block_pt7cm.png'></td>"
        '''generating the table span for right curly braces'''
        for _i in range(multiplier-1):
            self.table_text = self.table_text + "<td></td>"
        self.table_text = self.table_text + "<td rowspan="+str(number1+1)+"><img src='/images/explanation/right_curly_braces_3cm.png'></td>"
        self.table_text = self.table_text + "<td rowspan="+str(number1+1)+">?</td></tr>"
        for _i in range(number1-1):
            self.table_text = self.table_text + "<tr><td>"+item1+"</td><td><img src='/images/explanation/green_block_pt7cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td>"+str(item2)+"</td>"
        for _i in range(multiplier):
            self.table_text = self.table_text + "<td><img src='/images/explanation/pink_block_pt7cm.png'></td>"
        self.table_text = self.table_text + "</tr><tr><td></td><td></td>"
        '''generating columng for down curly brace'''
        self.table_text = self.table_text + "<td colspan="+str(multiplier-1)+"><img src='/images/explanation/down_curly_braces_3cm.png' width="+str(46*(multiplier-1))+"></td></tr>"
        self.table_text = self.table_text + "<tr><td></td><td></td><td align='center' colspan="+str(multiplier-1)+">$"+str(diff)+"</td></tr>"
        self.table_text = self.table_text + "</table><br>"
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(multiplier-1)+" units = $"+str(diff)+"</div>"
        self.solution_text = self.solution_text + "<div>1 unit  = $"+str(diff)+" &divide; "+str(multiplier-1)+" = $"+str(diff/(multiplier-1))+"</div>"
        self.solution_text = self.solution_text + "<div>"+str(multiplier+number1)+" units = "+str(multiplier+number1)+" x $"+str(diff/(multiplier-1))+" = $"+str((multiplier+number1)*diff/(multiplier-1))+"</div><br>"
        self.solution_text = self.solution_text + "<div>"+GirlName+" spent a total of $"+str((multiplier+number1)*diff/(multiplier-1))+".</div><br>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    def GenerateProblemType11(self):
        '''e.g.:Annie bought 2 similar frocks and a coat for $161 altogether. If the cost of the coat was 5 times as
		much as the cost of each frock, how much more than each frock did the coat cost?'''
            
        self.GirlName = random.choice(PersonName.GirlName)
        self.ItemPool = {"ties-jacket":randint(15,50),"bowls-microwave":randint(15,30),
                      "notebooks-toy":randint(4,10),"boxes of chocolates-christmas tree":randint(5,15),
                      "plates-cooking pot":randint(4,10),"mugs-coffee maker":randint(5,15),
                      "pastries-cake":randint(1,5),"shirts-pair of pants":randint(15,20),"marbles-board game":randint(1,5),
                      "toy cars-toy house":randint(2,10),"jerseys-pair of soccer boots":randint(10,30),
                      "chickens-lamb":randint(5,10),"cans of soft drink-burger":randint(1,3),
                      "thumb drives-printer":randint(15,30),"chairs-table":randint(10,30),
                      "flower pots-water hose":randint(5,10),"pillows-mattress":randint(10,25),
                      "rings-necklace":randint(5,50)}

        '''To make grammatically correct statement we need singular form of the items above'''
        self.SingleItem = {"ties":"tie","bowls":"bowl","notebooks":"notebook","plates":"plate","mugs":"mug",
                      "boxes of chocolates":"box of chocolates",
                      "pastries":"pastry","shirts":"shirt","marbles":"marble","toy cars":"toy car",
                      "jerseys":"jersey","chickens":"chicken","cans of soft drink":"can of soft drink",
                      "thumb drives":"thumb drive","chairs":"chair","flower pots":"flower pot",
                      "pillows":"pillow","rings":"ring"}        
        
        self.item = self.ItemPool.keys()[randint(0,len(self.ItemPool)-1)]
        self.item1 = self.item.partition("-")[0]
        self.item2 = self.item.partition("-")[2]
        self.SingleItem1 = self.SingleItem[self.item1]
        '''number of items the boy will buy'''
        self.number1 = randint(2,10)
        '''the amount he will pay for each item'''
        self.amount1 = self.ItemPool[self.item]
        self.multiplier = randint(3,7)
        self.amount2 = self.multiplier * self.amount1
        self.diff = self.amount2 - self.amount1
        self.MoneySpent = self.number1*self.amount1 + self.amount2
        
        self.answer = self.diff
        
        self.problem1 = "%s bought %d similar %s and a %s for $%d altogether. If the cost of the %s was %d times as much as the cost of each %s, how much more than each %s did the %s cost?"%(self.GirlName,self.number1,self.item1,self.item2,self.MoneySpent,self.item2,self.multiplier,self.SingleItem1,self.SingleItem1,self.item2)
        self.problem2 = "%s paid $%d for %d similar %s and a %s. The %s cost %d times as much as each %s. How much more than each %s did the %s cost?"%(self.GirlName,self.MoneySpent,self.number1,self.item1,self.item2,self.item2,self.multiplier,self.SingleItem1,self.SingleItem1,self.item2)
        self.problem3 = "A %s costs %d times as much as a %s. %s bought %d %s and a %s. If she spent $%d altogether, how much more than each %s did the %s cost?"%(self.item2,self.multiplier,self.SingleItem1,self.GirlName,self.number1,self.item1,self.item2,self.MoneySpent,self.SingleItem1,self.item2)
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])
        
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType11(self.GirlName,self.problem,self.answer,self.number1,self.amount1,self.item1,self.SingleItem1,self.amount2,self.item2,self.diff,self.multiplier,self.MoneySpent)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"$",'problem_type':"ProblemType11"}

    def ExplainType11(self,GirlName,problem,answer,number1,amount1,item1,SingleItem1,amount2,item2,diff,multiplier,MoneySpent):
        self.answer_text = "The correct answer is: <b>$"+str(answer)+"</b>"
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'><tr><td>"+item1+"</td><td><img src='/images/explanation/green_block_pt7cm.png'></td>"
        '''generating the table span for right curly braces'''
        for _i in range(multiplier-1):
            self.table_text = self.table_text + "<td></td>"
        self.table_text = self.table_text + "<td rowspan="+str(number1+1)+"><img src='/images/explanation/right_curly_braces_3cm.png'></td>"
        self.table_text = self.table_text + "<td valign='center' rowspan="+str(number1+1)+">$"+str(MoneySpent)+"</td></tr>"
        for _i in range(number1-1):
            self.table_text = self.table_text + "<tr><td>"+item1+"</td><td><img src='/images/explanation/green_block_pt7cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td>"+str(item2)+"</td>"
        for _i in range(multiplier):
            self.table_text = self.table_text + "<td><img src='/images/explanation/pink_block_pt7cm.png'></td>"
        self.table_text = self.table_text + "</tr><tr><td></td><td></td>"
        '''generating columng for down curly brace'''
        self.table_text = self.table_text + "<td colspan="+str(multiplier-1)+"><img src='/images/explanation/down_curly_braces_3cm.png' width="+str(46*(multiplier-1))+"></td></tr>"
        self.table_text = self.table_text + "<tr><td></td><td></td><td align='center' colspan="+str(multiplier-1)+">?</td></tr>"
        self.table_text = self.table_text + "</table><br>"
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(multiplier+number1)+" units = $"+str(MoneySpent)+"</div>"
        self.solution_text = self.solution_text + "<div>1 unit  = $"+str(MoneySpent)+" &divide; "+str(multiplier+number1)+" = $"+str(MoneySpent/(multiplier+number1))+"</div>"
        self.solution_text = self.solution_text + "<div>"+str(multiplier-1)+" units = "+str(multiplier-1)+" x $"+str(MoneySpent/(multiplier+number1))+" = $"+str((multiplier-1)*MoneySpent/(multiplier+number1))+"</div><br>"
        self.solution_text = self.solution_text + "<div> The "+item2+" cost $"+str((multiplier-1)*MoneySpent/(multiplier+number1))+" more than each "+SingleItem1+".</div><br>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    def GenerateProblemType12(self):
        '''e.g.:Annie bought 2 similar frocks and a coat. Each frock cost $92 less than the coat. If Annie spent $161 altogether, 
		how many times as expensive as each frock was the coat?'''
            
        self.GirlName = random.choice(PersonName.GirlName)
        self.ItemPool = {"ties-jacket":randint(15,50),"bowls-microwave":randint(15,30),
                      "notebooks-toy":randint(4,10),"boxes of chocolates-christmas tree":randint(5,15),
                      "plates-cooking pot":randint(4,10),"mugs-coffee maker":randint(5,15),
                      "pastries-cake":randint(1,5),"shirts-pair of pants":randint(15,20),"marbles-board game":randint(1,5),
                      "toy cars-toy house":randint(2,10),"jerseys-pair of soccer boots":randint(10,30),
                      "cans of soft drink-burger":randint(1,3),
                      "thumb drives-printer":randint(15,30),"chairs-table":randint(10,30),
                      "flower pots-water hose":randint(5,10),"pillows-mattress":randint(10,25),
                      "rings-necklace":randint(5,50)}

        '''To make grammatically correct statement we need singular form of the items above'''
        self.SingleItem = {"ties":"tie","bowls":"bowl","notebooks":"notebook","plates":"plate","mugs":"mug",
                      "boxes of chocolates":"box of chocolates",
                      "pastries":"pastry","shirts":"shirt","marbles":"marble","toy cars":"toy car",
                      "jerseys":"jersey","cans of soft drink":"can of soft drink",
                      "thumb drives":"thumb drive","chairs":"chair","flower pots":"flower pot",
                      "pillows":"pillow","rings":"ring"}        
        
        self.item = self.ItemPool.keys()[randint(0,len(self.ItemPool)-1)]
        self.item1 = self.item.partition("-")[0]
        self.item2 = self.item.partition("-")[2]
        self.SingleItem1 = self.SingleItem[self.item1]
        '''number of items the boy will buy'''
        self.number1 = randint(3,7)
        '''the amount he will pay for each item'''
        self.amount1 = self.ItemPool[self.item]
        self.multiplier = randint(3,7)
        self.amount2 = self.multiplier * self.amount1
        self.diff = self.amount2 - self.amount1
        self.MoneySpent = self.number1*self.amount1 + self.amount2
        
        self.answer = self.multiplier
        
        self.problem1 = "%s bought %d similar %s and a %s. Each %s cost $%d less than the %s. If %s spent $%d altogether, how many times as expensive as each %s was the %s?"%(self.GirlName,self.number1,self.item1,self.item2,self.SingleItem1,self.diff,self.item2,self.GirlName,self.MoneySpent,self.SingleItem1,self.item2)
        self.problem2 = "%s bought %d similar %s and a %s. The %s cost $%d more than each %s. If %s spent $%d altogether, how many times as expensive as each %s was the %s?"%(self.GirlName,self.number1,self.item1,self.item2,self.item2,self.diff,self.SingleItem1,self.GirlName,self.MoneySpent,self.SingleItem1,self.item2)
        self.problem3 = "%s paid $%d for %d similar %s and a %s. If each %s cost $%d less than the %s, how many times as expensive as each %s was the %s?"%(self.GirlName,self.MoneySpent,self.number1,self.item1,self.item2,self.SingleItem1,self.diff,self.item2,self.SingleItem1,self.item2)
        self.problem4 = "%s paid $%d for %d similar %s and a %s. If the %s cost $%d more than each %s, how many times as expensive as each %s was the %s?"%(self.GirlName,self.MoneySpent,self.number1,self.item1,self.item2,self.item2,self.diff,self.SingleItem1,self.SingleItem1,self.item2)
        self.problem5 = "%s bought %d similar %s and a %s for $%d. If each %s cost $%d less than the %s, how many times as expensive as each %s was the %s?"%(self.GirlName,self.number1,self.item1,self.item2,self.MoneySpent,self.SingleItem1,self.diff,self.item2,self.SingleItem1,self.item2)
        self.problem6 = "%s bought %d similar %s and a %s for $%d. If the %s cost $%d more than each %s, how many times as expensive as each %s was the %s?"%(self.GirlName,self.number1,self.item1,self.item2,self.MoneySpent,self.item2,self.diff,self.SingleItem1,self.SingleItem1,self.item2)
        self.problem = random.choice([self.problem1,self.problem2,self.problem3,self.problem4,self.problem5,self.problem6])
        
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType12(self.GirlName,self.problem,self.answer,self.number1,self.amount1,self.item1,self.SingleItem1,self.amount2,self.item2,self.diff,self.multiplier,self.MoneySpent)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"",'unit':"times",'problem_type':"ProblemType12"}

    def ExplainType12(self,GirlName,problem,answer,number1,amount1,item1,SingleItem1,amount2,item2,diff,multiplier,MoneySpent):
        self.answer_text = "The correct answer is: <b>"+str(answer)+" times</b>"
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'><tr><td height=21>"+item1+"</td><td><img src='/images/explanation/green_block_pt7cm.png'></td>"
        '''generating the table span for right curly braces'''
        for _i in range(multiplier-1):
            self.table_text = self.table_text + "<td></td>"
        self.table_text = self.table_text + "<td rowspan="+str(number1+1)+"><img src='/images/explanation/right_curly_braces_3cm.png'></td>"
        self.table_text = self.table_text + "<td valign='center' rowspan="+str(number1+1)+">$"+str(MoneySpent)+"</td></tr>"
        for _i in range(number1-3):
            self.table_text = self.table_text + "<tr><td height=21>"+item1+"</td><td><img src='/images/explanation/green_block_pt7cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td height=21>"+item1+"</td><td><img src='/images/explanation/green_block_pt7cm.png'></td>"
        '''Generating the $ text above the up curly braces'''
        self.table_text = self.table_text + "<td align='center' colspan="+str(multiplier-1)+">$"+str(diff)+"</td></tr>"
        self.table_text = self.table_text + "<tr><td>"+item1+"</td><td><img src='/images/explanation/green_block_pt7cm.png'></td>"
        '''Generating the up curly brace'''
        self.table_text = self.table_text + "<td colspan="+str(multiplier-1)+"><img src='/images/explanation/up_curly_braces_3cm.png' height=21 width="+str(45*(multiplier-1))+"></td></tr>"
        self.table_text = self.table_text + "<tr><td>"+str(item2)+"</td>"
        for _i in range(2):
            self.table_text = self.table_text + "<td><img src='/images/explanation/pink_block_pt7cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/broken_pink_block_pt7cm.png'></td>"
        for _i in range(multiplier-3):
            self.table_text = self.table_text + "<td><img src='/images/explanation/pink_block_pt7cm.png'></td>"
        self.table_text = self.table_text + "</tr><tr><td></td>"
        '''generating columng for down curly brace'''
        self.table_text = self.table_text + "<td colspan="+str(multiplier)+"><img src='/images/explanation/down_curly_braces_3cm.png' width="+str(46*(multiplier))+"></td></tr>"
        self.table_text = self.table_text + "<tr><td></td><td align='center' colspan="+str(multiplier)+">?</td></tr>"
        self.table_text = self.table_text + "</table><br>"
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(MoneySpent)+" - $"+str(diff)+" = $"+str(MoneySpent-diff)+"</div>"
        self.solution_text = self.solution_text + "<div>$"+str(MoneySpent-diff)+" &divide; "+str(number1+1)+" units = $"+str((MoneySpent-diff)/(number1+1))+"</div>"
        self.solution_text = self.solution_text + "<div> Cost of each "+SingleItem1+" is $"+str((MoneySpent-diff)/(number1+1))+"</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(number1)+" units x $"+str((MoneySpent-diff)/(number1+1))+" = $"+str(number1*(MoneySpent-diff)/(number1+1))+"</div>"
        self.solution_text = self.solution_text + "<div> Total cost of the "+item1+" is $"+str(number1*(MoneySpent-diff)/(number1+1))+".</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(MoneySpent)+" - $"+str(number1*(MoneySpent-diff)/(number1+1))+" = $"+str(MoneySpent-number1*(MoneySpent-diff)/(number1+1))+"</div>"
        self.solution_text = self.solution_text + "<div>Cost of the "+item2+" is $"+str(MoneySpent-number1*(MoneySpent-diff)/(number1+1))+".</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(MoneySpent-number1*(MoneySpent-diff)/(number1+1))+" &divide; $"+str((MoneySpent-diff)/(number1+1))+" = $"+str((MoneySpent-number1*(MoneySpent-diff)/(number1+1))/((MoneySpent-diff)/(number1+1)))+"</div>"
        self.solution_text = self.solution_text + "<div> The "+item2+" was "+str((MoneySpent-number1*(MoneySpent-diff)/(number1+1))/((MoneySpent-diff)/(number1+1)))+" times as expensive as each "+SingleItem1+".</div>"
      
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain
        
        '''Problem Type 4 as defined in the ppt starts from here'''
    def GenerateProblemType13(self):
        '''e.g.:Annie bought 2 similar frocks and a coat. The coat cost 5 times as much as each frock. If the coat cost $69 more
		than the 2 frocks combined, how much money did Annie spend altogether?'''
            
        self.GirlName = random.choice(PersonName.GirlName)
        self.ItemPool = {"ties-jacket":randint(15,50),"bowls-microwave":randint(15,30),
                      "notebooks-toy":randint(4,10),"boxes of chocolates-christmas tree":randint(5,15),
                      "plates-cooking pot":randint(4,10),"mugs-coffee maker":randint(5,15),
                      "pastries-cake":randint(1,5),"blouses-suit":randint(15,20),"dolls-board game":randint(1,5),
                      "toy cars-toy house":randint(2,10),"jerseys-pair of soccer boots":randint(10,30),
                      "cans of soft drink-burger":randint(1,3),"frocks-coat":randint(5,20),
                      "thumb drives-printer":randint(15,30),"chairs-table":randint(10,30),
                      "flower pots-water hose":randint(5,10),"pillows-mattress":randint(10,25),
                      "rings-necklace":randint(5,50)}

        '''To make grammatically correct statement we need singular form of the items above'''
        self.SingleItem = {"ties":"tie","bowls":"bowl","notebooks":"notebook","plates":"plate","mugs":"mug",
                      "boxes of chocolates":"box of chocolates","frocks":"frock",
                      "pastries":"pastry","blouses":"blouse","dolls":"doll","toy cars":"toy car",
                      "jerseys":"jersey","cans of soft drink":"can of soft drink",
                      "thumb drives":"thumb drive","chairs":"chair","flower pots":"flower pot",
                      "pillows":"pillow","rings":"ring"}        
        
        self.item = self.ItemPool.keys()[randint(0,len(self.ItemPool)-1)]
        self.item1 = self.item.partition("-")[0]
        self.item2 = self.item.partition("-")[2]
        self.SingleItem1 = self.SingleItem[self.item1]
        '''number of items the girl will buy'''
        self.number1 = randint(2,4)
        '''the amount she will pay for each item'''
        self.amount1 = self.ItemPool[self.item]
        self.multiplier = randint(5,7)
        self.amount2 = self.multiplier * self.amount1
        self.diff = self.amount2 - self.amount1*self.number1
        self.MoneySpent = self.number1*self.amount1 + self.amount2
        
        self.answer = self.MoneySpent
        
        self.problem1 = "%s bought %d similar %s and a %s. The %s cost %d times as much as each %s. If the %s cost $%d more than the %d %s combined, how much money did %s spend altogether?"%(self.GirlName,self.number1,self.item1,self.item2,self.item2,self.multiplier,self.SingleItem1,self.item2,self.diff,self.number1,self.item1,self.GirlName)
        self.problem2 = "A %s costs %d times as much as a %s. If %s bought %d %s and a %s and she spent $%d more on the %s than on the %d %s combined, how much money did she spend altogether?"%(self.item2,self.multiplier,self.SingleItem1,self.GirlName,self.number1,self.item1,self.item2,self.diff,self.item2,self.number1,self.item1)
        self.problem3 = "%s purchased %d %s and a %s. She paid $%d more for the %s than for the %d %s combined. If the %s cost %d times as much as each %s, how much money did %s spend altogether?"%(self.GirlName,self.number1,self.item1,self.item2,self.diff,self.item2,self.number1,self.item1,self.item2,self.multiplier,self.SingleItem1,self.GirlName)
        self.problem4 = "%s purchased %d %s and a %s. If the %s cost %d times as much as each %s and she paid $%d more for the %s than the %d %s combined, find how much money she spent altogether."%(self.GirlName,self.number1,self.item1,self.item2,self.item2,self.multiplier,self.SingleItem1,self.diff,self.item2,self.number1,self.item1)
        self.problem = random.choice([self.problem1,self.problem2,self.problem3,self.problem4])
        
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType13(self.GirlName,self.problem,self.answer,self.number1,self.amount1,self.item1,self.SingleItem1,self.amount2,self.item2,self.diff,self.multiplier,self.MoneySpent)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"$",'problem_type':"ProblemType13"}

    def ExplainType13(self,GirlName,problem,answer,number1,amount1,item1,SingleItem1,amount2,item2,diff,multiplier,MoneySpent):
        self.answer_text = "The correct answer is: <b>$"+str(answer)+"</b>"
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'><tr><td height=24>"+item1+"</td>"
        for _i in range(number1):
            self.table_text = self.table_text + "<td><img src='/images/explanation/green_block_pt7cm.png'></td>"
        for _i in range(multiplier-number1):
            self.table_text = self.table_text + "<td></td>"
        self.table_text = self.table_text + "<td rowspan=2><img src='/images/explanation/right_curly_braces_2cm.png'></td>"
        self.table_text = self.table_text + "<td rowspan=2>?</td></tr>"
        self.table_text = self.table_text + "<tr><td height=24>"+item2+"</td>"
        for _1 in range(multiplier):
            self.table_text = self.table_text + "<td><img src='/images/explanation/pink_block_pt7cm.png'></td>"
        self.table_text = self.table_text + "</tr><tr>"
        for _1 in range(number1+1):
            self.table_text = self.table_text + "<td></td>"
        self.table_text = self.table_text + "<td colspan="+str(multiplier-number1)+"><img src='/images/explanation/down_curly_braces_2cm.png' width="+str(45*(multiplier-number1))+"></td></tr><tr>"
        self.table_text = self.table_text + "</tr><tr>"
        for _1 in range(number1+1):
            self.table_text = self.table_text + "<td></td>"
        self.table_text = self.table_text + "<td align='center' colspan="+str(multiplier-number1)+">$"+str(diff)+"</td></tr>"
        self.table_text = self.table_text + "</table><br>"
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(multiplier-number1)+" units = $"+str(diff)+"</div>"
        self.solution_text = self.solution_text + "<div>1 unit = $"+str(diff)+" &divide; "+str(multiplier-number1)+" = $"+str(diff/(multiplier-number1))+"</div>"
        self.solution_text = self.solution_text + "<div>"+str(multiplier+number1)+" units = "+str(multiplier+number1)+" x $"+str(diff/(multiplier-number1))+" = $"+str((multiplier+number1)*(diff/(multiplier-number1)))+"</div><br>"
        self.solution_text = self.solution_text + "<div>"+GirlName+" spent $"+str((multiplier+number1)*(diff/(multiplier-number1)))+" altogether.</div>"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain        

    def GenerateProblemType14(self):
        '''e.g.:Annie bought 2 similar frocks and a coat for $161 altogether. If the cost of the coat was 5 times as much as the cost of
		each frock, how much more did the coat cost than the 2 frocks combined?'''
            
        self.GirlName = random.choice(PersonName.GirlName)
        self.ItemPool = {"ties-jacket":randint(15,50),"bowls-microwave":randint(15,30),
                      "notebooks-toy":randint(4,10),"boxes of chocolates-christmas tree":randint(5,15),
                      "plates-cooking pot":randint(4,10),"mugs-coffee maker":randint(5,15),
                      "pastries-cake":randint(1,5),"blouses-suit":randint(15,20),"dolls-board game":randint(1,5),
                      "toy cars-toy house":randint(2,10),"jerseys-pair of soccer boots":randint(10,30),
                      "cans of soft drink-burger":randint(1,3),"frocks-coat":randint(5,20),
                      "thumb drives-printer":randint(15,30),"chairs-table":randint(10,30),
                      "flower pots-water hose":randint(5,10),"pillows-mattress":randint(10,25),
                      "rings-necklace":randint(5,50)}

        '''To make grammatically correct statement we need singular form of the items above'''
        self.SingleItem = {"ties":"tie","bowls":"bowl","notebooks":"notebook","plates":"plate","mugs":"mug",
                      "boxes of chocolates":"box of chocolates","frocks":"frock",
                      "pastries":"pastry","blouses":"blouse","dolls":"doll","toy cars":"toy car",
                      "jerseys":"jersey","cans of soft drink":"can of soft drink",
                      "thumb drives":"thumb drive","chairs":"chair","flower pots":"flower pot",
                      "pillows":"pillow","rings":"ring"}        
        
        self.item = self.ItemPool.keys()[randint(0,len(self.ItemPool)-1)]
        self.item1 = self.item.partition("-")[0]
        self.item2 = self.item.partition("-")[2]
        self.SingleItem1 = self.SingleItem[self.item1]
        '''number of items the girl will buy'''
        self.number1 = randint(2,4)
        '''the amount she will pay for each item'''
        self.amount1 = self.ItemPool[self.item]
        self.multiplier = randint(6,8)
        self.amount2 = self.multiplier * self.amount1
        self.diff = self.amount2 - self.amount1*self.number1
        self.MoneySpent = self.number1*self.amount1 + self.amount2
        
        self.answer = self.diff
        
        self.problem1 = "%s bought %d similar %s and a %s for $%d altogether. If the cost of the %s was %d times as much as the cost of each %s, how much more did the %s cost than the %d %s combined?"%(self.GirlName,self.number1,self.item1,self.item2,self.MoneySpent,self.item2,self.multiplier,self.SingleItem1,self.item2,self.number1,self.item1)
        self.problem2 = "%s paid $%d for %d similar %s and a %s. The %s cost %d times as much as each %s. How much more did the %s cost than the %d %s combined?"%(self.GirlName,self.MoneySpent,self.number1,self.item1,self.item2,self.item2,self.multiplier,self.SingleItem1,self.item2,self.number1,self.item1)
        self.problem3 = "A %s costs %d times as much as a %s. %s bought %d %s and a %s. If she spent $%d altogether, how much more did the %s cost than the %d %s combined?"%(self.item2,self.multiplier,self.SingleItem1,self.GirlName,self.number1,self.item1,self.item2,self.MoneySpent,self.item2,self.number1,self.item1)
        self.problem4 = "%s purchased %d %s and a %s. If she paid $%d altogether and the %s cost %d times as much as each %s, find how much more the %s cost than the %d %s combined."%(self.GirlName,self.number1,self.item1,self.item2,self.MoneySpent,self.item2,self.multiplier,self.SingleItem1,self.item2,self.number1,self.item1)
        self.problem = random.choice([self.problem1,self.problem2,self.problem3,self.problem4])
        
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType14(self.GirlName,self.problem,self.answer,self.number1,self.amount1,self.item1,self.SingleItem1,self.amount2,self.item2,self.diff,self.multiplier,self.MoneySpent)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"$",'problem_type':"ProblemType14"}

    def ExplainType14(self,GirlName,problem,answer,number1,amount1,item1,SingleItem1,amount2,item2,diff,multiplier,MoneySpent):
        self.answer_text = "The correct answer is: <b>$"+str(answer)+"</b>"
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'><tr><td height=24>"+item1+"</td>"
        for _i in range(number1):
            self.table_text = self.table_text + "<td><img src='/images/explanation/green_block_pt7cm.png'></td>"
        for _i in range(multiplier-number1):
            self.table_text = self.table_text + "<td></td>"
        self.table_text = self.table_text + "<td rowspan=2><img src='/images/explanation/right_curly_braces_2cm.png'></td>"
        self.table_text = self.table_text + "<td rowspan=2>$"+str(MoneySpent)+"</td></tr>"
        self.table_text = self.table_text + "<tr><td height=24>"+item2+"</td>"
        for _1 in range(multiplier):
            self.table_text = self.table_text + "<td><img src='/images/explanation/pink_block_pt7cm.png'></td>"
        self.table_text = self.table_text + "</tr><tr>"
        for _1 in range(number1+1):
            self.table_text = self.table_text + "<td></td>"
        self.table_text = self.table_text + "<td align='center' colspan="+str(multiplier-number1)+"><img src='/images/explanation/down_curly_braces_2cm.png' height=24 width="+str(45*(multiplier-number1))+"></td></tr><tr>"
        self.table_text = self.table_text + "</tr><tr>"
        for _1 in range(number1+1):
            self.table_text = self.table_text + "<td></td>"
        self.table_text = self.table_text + "<td align='center' colspan="+str(multiplier-number1)+">?</td></tr>"
        self.table_text = self.table_text + "</table><br>"
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(multiplier+number1)+" units = $"+str(MoneySpent)+"</div>"
        self.solution_text = self.solution_text + "<div>1 unit = $"+str(MoneySpent)+" &divide; "+str(multiplier+number1)+" = $"+str(MoneySpent/(multiplier+number1))+"</div>"
        self.solution_text = self.solution_text + "<div>"+str(multiplier-number1)+" units = "+str(multiplier-number1)+" x $"+str(MoneySpent/(multiplier+number1))+" = $"+str((multiplier-number1)*(MoneySpent/(multiplier+number1)))+"</div><br>"
        self.solution_text = self.solution_text + "<div The >"+item2+" cost $"+str((multiplier-number1)*(MoneySpent/(multiplier+number1)))+" more than the "+str(number1)+" "+item1+" combined.</div>"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain        

    def GenerateProblemType15(self):
        '''e.g.:Annie bought 2 similar frocks and a coat. The frocks cost $69 less than the coat. 
		If Annie spent $161 altogether, how many times as expensive as each frock was the coat?'''
            
        self.GirlName = random.choice(PersonName.GirlName)
        self.ItemPool = {"ties-jacket":randint(15,50),"bowls-microwave":randint(15,30),
                      "notebooks-toy":randint(4,10),"boxes of chocolates-christmas tree":randint(5,15),
                      "plates-cooking pot":randint(4,10),"mugs-coffee maker":randint(5,15),
                      "pastries-cake":randint(1,5),"blouses-suit":randint(15,20),"dolls-board game":randint(1,5),
                      "toy cars-toy house":randint(2,10),"jerseys-pair of soccer boots":randint(10,30),
                      "cans of soft drink-burger":randint(1,3),"frocks-coat":randint(5,20),
                      "thumb drives-printer":randint(15,30),"chairs-table":randint(10,30),
                      "flower pots-water hose":randint(5,10),"pillows-mattress":randint(10,25),
                      "rings-necklace":randint(5,50)}

        '''To make grammatically correct statement we need singular form of the items above'''
        self.SingleItem = {"ties":"tie","bowls":"bowl","notebooks":"notebook","plates":"plate","mugs":"mug",
                      "boxes of chocolates":"box of chocolates","frocks":"frock",
                      "pastries":"pastry","blouses":"blouse","dolls":"doll","toy cars":"toy car",
                      "jerseys":"jersey","cans of soft drink":"can of soft drink",
                      "thumb drives":"thumb drive","chairs":"chair","flower pots":"flower pot",
                      "pillows":"pillow","rings":"ring"}        
        
        self.item = self.ItemPool.keys()[randint(0,len(self.ItemPool)-1)]
        self.item1 = self.item.partition("-")[0]
        self.item2 = self.item.partition("-")[2]
        self.SingleItem1 = self.SingleItem[self.item1]
        '''number of items the girl will buy'''
        self.number1 = randint(2,4)
        '''the amount she will pay for each item'''
        self.amount1 = self.ItemPool[self.item]
        self.multiplier = randint(5,7)
        self.amount2 = self.multiplier * self.amount1
        self.diff = self.amount2 - self.amount1*self.number1
        self.MoneySpent = self.number1*self.amount1 + self.amount2
        
        self.answer = self.multiplier
        
        self.problem1 = "%s bought %d similar %s and a %s. The %s cost $%d less than the %s. If %s spent $%d altogether, how many times as expensive as each %s was the %s?"%(self.GirlName,self.number1,self.item1,self.item2,self.item1,self.diff,self.item2,self.GirlName,self.MoneySpent,self.SingleItem1,self.item2)
        self.problem2 = "%s bought %d similar %s and a %s. The %s cost $%d more than the %s. If %s spent $%d altogether, how many times as expensive as each %s was the %s?"%(self.GirlName,self.number1,self.item1,self.item2,self.item2,self.diff,self.item1,self.GirlName,self.MoneySpent,self.SingleItem1,self.item2)
        self.problem3 = "%s paid $%d for %d similar %s and a %s. If the %s cost $%d less than the %s, how many times as expensive as each %s was the %s?"%(self.GirlName,self.MoneySpent,self.number1,self.item1,self.item2,self.item1,self.diff,self.item2,self.SingleItem1,self.item2)
        self.problem4 = "%s paid $%d for %d similar %s and a %s. If the %s cost $%d more than the %s, how many times as expensive as each %s was the %s?"%(self.GirlName,self.MoneySpent,self.number1,self.item1,self.item2,self.item2,self.diff,self.item1,self.SingleItem1,self.item2)
        self.problem5 = "%s bought %d similar %s and a %s for $%d. If the %s cost $%d less than the %s, how many times as expensive as each %s was the %s?"%(self.GirlName,self.number1,self.item1,self.item2,self.MoneySpent,self.item1,self.diff,self.item2,self.SingleItem1,self.item2)
        self.problem6 = "%s bought %d similar %s and a %s for $%d. If the %s cost $%d more than the %s, how many times as expensive as each %s was the %s?"%(self.GirlName,self.number1,self.item1,self.item2,self.MoneySpent,self.item2,self.diff,self.item1,self.SingleItem1,self.item2)
        self.problem = random.choice([self.problem1,self.problem2,self.problem3,self.problem4,self.problem5,self.problem6])
        
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType15(self.GirlName,self.problem,self.answer,self.number1,self.amount1,self.item1,self.SingleItem1,self.amount2,self.item2,self.diff,self.multiplier,self.MoneySpent)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"",'unit':"times",'problem_type':"ProblemType15"}

    def ExplainType15(self,GirlName,problem,answer,number1,amount1,item1,SingleItem1,amount2,item2,diff,multiplier,MoneySpent):
        self.answer_text = "The correct answer is: <b>"+str(answer)+" times</b>"
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'><tr><td height=24>"+item1+"</td>"
        for _i in range(number1):
            self.table_text = self.table_text + "<td><img src='/images/explanation/green_block_pt7cm.png'></td>"
        self.table_text = self.table_text + "<td align='center' colspan="+str(multiplier-number1)+">$"+str(diff)
        self.table_text = self.table_text + "<br><img src='/images/explanation/up_curly_braces_2cm.png' height=24 width="+str(45*(multiplier-number1))+"></td>"
        self.table_text = self.table_text + "<td rowspan=2><img src='/images/explanation/right_curly_braces_2cm.png'></td>"
        self.table_text = self.table_text + "<td rowspan=2>$"+str(MoneySpent)+"</td></tr>"
        self.table_text = self.table_text + "<tr><td height=24>"+item2+"</td>"
        for _1 in range(2):
            self.table_text = self.table_text + "<td><img src='/images/explanation/pink_block_pt7cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/broken_pink_block_pt7cm.png'></td>"
        for _1 in range(multiplier-3):
            self.table_text = self.table_text + "<td><img src='/images/explanation/pink_block_pt7cm.png'></td>"
        self.table_text = self.table_text + "</tr><tr><td></td>"
        self.table_text = self.table_text + "<td align = 'center' colspan="+str(multiplier)+"><img src='/images/explanation/down_curly_braces_3cm.png' height=24 width="+str(45*(multiplier))+">"
        self.table_text = self.table_text + "<br>?</td></tr>"
        self.table_text = self.table_text + "</table><br>"
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(MoneySpent)+" - $"+str(diff)+" = $"+str(MoneySpent-diff)+"</div>"
        self.solution_text = self.solution_text + "<div>$"+str(MoneySpent-diff)+" &divide; "+str(2*number1)+" units = $"+str((MoneySpent-diff)/(2*number1))+"</div>"
        self.solution_text = self.solution_text + "<div>Cost of each "+SingleItem1+" is $"+str((MoneySpent-diff)/(2*number1))+".</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(number1)+" units x $"+str((MoneySpent-diff)/(2*number1))+" = $"+str(number1*(MoneySpent-diff)/(2*number1))+"</div>"
        self.solution_text = self.solution_text + "<div>Total cost of the "+item1+" is $"+str(number1*(MoneySpent-diff)/(2*number1))+".</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(MoneySpent)+" - $"+str(number1*(MoneySpent-diff)/(2*number1))+" = $"+str(MoneySpent-number1*(MoneySpent-diff)/(2*number1))+"</div>"
        self.solution_text = self.solution_text + "<div>Cost of the "+item2+" is $"+str(MoneySpent-number1*(MoneySpent-diff)/(2*number1))+".</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(MoneySpent-number1*(MoneySpent-diff)/(2*number1))+" &divide; $"+str((MoneySpent-diff)/(2*number1))+" = "+str((MoneySpent-number1*(MoneySpent-diff)/(2*number1))/((MoneySpent-diff)/(2*number1)))+"</div>"
        self.solution_text = self.solution_text + "<div>The "+item2+" was "+str((MoneySpent-number1*(MoneySpent-diff)/(2*number1))/((MoneySpent-diff)/(2*number1)))+" times as expensive as each "+SingleItem1+".</div>"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain         

    '''Problem type 5 starts here'''
    def GenerateProblemType16(self):
        '''e.g.:Before a $150 discount on a laptop, it cost 5 times as much as a printer. Annie paid $1050 altogether for
		the printer and the discounted laptop. What was the original price of the laptop?'''
            
        self.BoyName = random.choice(PersonName.BoyName)
        self.ItemPool = {"shirt-coat":randint(25,50),"Phone-TV":randint(150,300),
                      "printer-laptop":randint(150,300),"jersey-pair of shoes":randint(15,30),
                      "book-toy":randint(5,15),"mug-toaster":randint(5,15),
                      "bicycle accessory-bicycle":randint(15,40),"table lamp-study table":randint(10,25),
                      "movie dvd-dvd player":randint(10,20),"carpet-sofa":randint(25,100)}      
        
        self.item = self.ItemPool.keys()[randint(0,len(self.ItemPool)-1)]
        self.item1 = self.item.partition("-")[0]
        self.item2 = self.item.partition("-")[2]
        '''the amount she will pay for each item'''
        self.amount1 = self.ItemPool[self.item]
        self.multiplier = randint(5,7)
        self.OrigPrice = self.multiplier * self.amount1
        '''10-30% discount on the item'''
        self.discount = self.OrigPrice * randint(1,3)/10
        self.MoneySpent = self.amount1 + self.OrigPrice - self.discount
        
        self.answer = self.OrigPrice
        
        self.problem1 = "Before a $%d discount on a %s, it cost %d times as much as a %s. %s paid $%d altogether for the %s and the discounted %s. What was the original price of the %s?"%(self.discount,self.item2,self.multiplier,self.item1,self.BoyName,self.MoneySpent,self.item1,self.item2,self.item2)
        self.problem2 = "%s received a $%d discount on the purchase of a %s. He also bought a %s and paid $%d altogether. If the %s cost %d times as much as the %s before discount, find the original price of the %s."%(self.BoyName,self.discount,self.item2,self.item1,self.MoneySpent,self.item2,self.multiplier,self.item1,self.item2)
        self.problem3 = "%s bought a %s at $%d off. He also bought a %s and paid $%d altogether. What was the original price of the %s if, before discount, it cost %d times as much as the %s?"%(self.BoyName,self.item2,self.discount,self.item1,self.MoneySpent,self.item2,self.multiplier,self.item1)
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])
        
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType16(self.BoyName,self.problem,self.answer,self.amount1,self.item1,self.OrigPrice,self.discount,self.item2,self.multiplier,self.MoneySpent)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"$",'problem_type':"ProblemType16"}

    def ExplainType16(self,BoyName,problem,answer,amount1,item1,OrigPrice,discount,item2,multiplier,MoneySpent):
        self.answer_text = "The correct answer is: <b>$"+str(answer)+"</b>"
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'><tr><td height=24>"+item1+"</td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/green_block_pt7cm.png'></td>"
        for _i in range(multiplier-1):
            self.table_text = self.table_text + "<td></td>"
        self.table_text = self.table_text + "<td height=24 align='center'>$"+str(discount)+"<br><img src='/images/explanation/up_curly_braces_1cm.png' width=28></td>"
        self.table_text = self.table_text + "<td height=24 rowspan=2><img src='/images/explanation/right_curly_braces_1cm.png'></td>"
        self.table_text = self.table_text + "<td rowspan=2>$"+str(MoneySpent)+"-$"+str(discount)+"</td></tr>"
        self.table_text = self.table_text + "<tr><td height=24>"+item2+"</td>"
        for _1 in range(multiplier-1):
            self.table_text = self.table_text + "<td><img src='/images/explanation/pink_block_pt7cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/pink_block_pt3cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/yellow_block_pt4cm.png'></td>"
        self.table_text = self.table_text + "</tr><tr><td></td>"
        self.table_text = self.table_text + "<td align = 'center' colspan="+str(multiplier+1)+"><img src='/images/explanation/down_curly_braces_3cm.png' height=24 width="+str(45*(multiplier+1))+">"
        self.table_text = self.table_text + "<br>?</td></tr>"
        self.table_text = self.table_text + "</table><br>"
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(MoneySpent)+" + $"+str(discount)+" = $"+str(MoneySpent+discount)+"</div>"
        self.solution_text = self.solution_text + "<div>Before discount, the "+item2+" and the "+item1+" cost $"+str(MoneySpent+discount)+" altogether.</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(multiplier+1)+" units =$"+str(MoneySpent+discount)+"</div>"
        self.solution_text = self.solution_text + "<div>1 unit = $"+str(MoneySpent+discount)+" &divide; "+str(multiplier+1)+" = $"+str((MoneySpent+discount)/(multiplier+1))+"</div>"
        self.solution_text = self.solution_text + "<div>"+str(multiplier)+" units ="+str(multiplier)+" x $"+str((MoneySpent+discount)/(multiplier+1))+" = $"+str(multiplier*(MoneySpent+discount)/(multiplier+1))+"</div>"
        self.solution_text = self.solution_text + "<div>The original price of the "+item2+" was $"+str(multiplier*(MoneySpent+discount)/(multiplier+1))+".</div>"
        self.solution_text = self.solution_text + "<br><div> Watch below video for explanation of similar problem<br>"
        VideoLink = '<object><param name="movie" value="https://www.youtube.com/v/u1zgFlCw8Aw?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded"><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "kXt8MDLM8Iw";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain
        
    def GenerateProblemType17(self):
        '''e.g.:Before discount, a laptop cost 5 times as much as a printer. Annie paid $1050 altogether for the printer and the
		discounted laptop. If the printer cost $200, how much discount did Annie get on the laptop?'''
            
        self.BoyName = random.choice(PersonName.BoyName)
        self.ItemPool = {"shirt-coat":randint(25,50),"Phone-TV":randint(150,300),
                      "printer-laptop":randint(150,300),"jersey-pair of shoes":randint(15,30),
                      "book-toy":randint(5,15),"mug-toaster":randint(5,15),
                      "bicycle accessory-bicycle":randint(15,40),"table lamp-study table":randint(10,25),
                      "movie dvd-dvd player":randint(10,20),"carpet-sofa":randint(25,100)}      
        
        self.item = self.ItemPool.keys()[randint(0,len(self.ItemPool)-1)]
        self.item1 = self.item.partition("-")[0]
        self.item2 = self.item.partition("-")[2]
        '''the amount she will pay for each item'''
        self.amount1 = self.ItemPool[self.item]
        self.multiplier = randint(5,7)
        self.OrigPrice = self.multiplier * self.amount1
        '''10-30% discount on the item'''
        self.discount = self.OrigPrice * randint(1,3)/10
        self.MoneySpent = self.amount1 + self.OrigPrice - self.discount
        
        self.answer = self.discount
        
        self.problem1 = "Before discount, a %s cost %d times as much as a %s. %s paid $%d altogether for the %s and the discounted %s. If the %s cost $%d, how much discount did %s get on the %s?"%(self.item2,self.multiplier,self.item1,self.BoyName,self.MoneySpent,self.item1,self.item2,self.item1,self.amount1,self.BoyName,self.item2)
        self.problem2 = "%s paid $%d altogether for a %s and a %s. He paid $%d for the %s and received a discount on the %s. Before discount, if the %s cost %d times as much as the %s, how much discount did %s get on the %s?"%(self.BoyName,self.MoneySpent,self.item2,self.item1,self.amount1,self.item1,self.item2,self.item2,self.multiplier,self.item1,self.BoyName,self.item2)
        self.problem3 = "%s received a discount on the purchase of a %s. He also bought a %s and paid $%d altogether. If the %s cost %d times as much as the %s before discount, find the amount of discount that %s got on the %s."%(self.BoyName,self.item2,self.item1,self.MoneySpent,self.item2,self.multiplier,self.item1,self.BoyName,self.item2)
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])
        
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType17(self.BoyName,self.problem,self.answer,self.amount1,self.item1,self.OrigPrice,self.discount,self.item2,self.multiplier,self.MoneySpent)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"$",'problem_type':"ProblemType17"}

    def ExplainType17(self,BoyName,problem,answer,amount1,item1,OrigPrice,discount,item2,multiplier,MoneySpent):
        self.answer_text = "The correct answer is: <b>$"+str(answer)+"</b>"
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'><tr><td></td><td height=24>$"+str(amount1)+"<br><img src='images/explanation/up_curly_braces_pt7cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td height=24>"+item1+"</td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/green_block_pt7cm.png'></td>"
        for _i in range(multiplier-1):
            self.table_text = self.table_text + "<td></td>"
        self.table_text = self.table_text + "<td height=24 align='center'>?<br><img src='/images/explanation/up_curly_braces_1cm.png' width=28></td></tr>"
        self.table_text = self.table_text + "<tr><td height=24>"+item2+"</td>"
        for _1 in range(multiplier-1):
            self.table_text = self.table_text + "<td><img src='/images/explanation/pink_block_pt7cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/pink_block_pt3cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/yellow_block_pt4cm.png'></td>"
        self.table_text = self.table_text + "</tr><tr><td></td>"
        self.table_text = self.table_text + "<td align = 'center' colspan="+str(multiplier)+"><img src='/images/explanation/down_curly_braces_3cm.png' height=24 width="+str(45*(multiplier))+">"
        self.table_text = self.table_text + "<br>$"+str(MoneySpent)+"-$"+str(amount1)+"</td></tr>"
        self.table_text = self.table_text + "</table><br>"
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(multiplier)+" units x $"+str(amount1)+" = $"+str(multiplier*amount1)+"</div>"
        self.solution_text = self.solution_text + "<div>Before discount, the "+item2+" cost $"+str(multiplier*amount1)+".</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(MoneySpent)+" - $"+str(amount1)+" = $"+str(MoneySpent-amount1)+"</div>"
        self.solution_text = self.solution_text + "<div>After discount, the "+item2+" cost $"+str(MoneySpent-amount1)+".</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(multiplier*amount1)+" - $"+str(MoneySpent-amount1)+" = $"+str(multiplier*amount1-(MoneySpent-amount1))+"</div>"
        self.solution_text = self.solution_text + "<div>"+BoyName+" got a discount of $"+str(multiplier*amount1-(MoneySpent-amount1))+" on the "+item2+".</div>"

        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain 

    def GenerateProblemType18(self):
        '''e.g.:Before a $150 discount on a laptop, it cost 5 times as much as a printer. If Annie paid $1050 altogether
		for the printer and the discounted laptop, how much did she pay for the printer?'''
            
        self.BoyName = random.choice(PersonName.BoyName)
        self.ItemPool = {"shirt-coat":randint(25,50),"Phone-TV":randint(150,300),
                      "printer-laptop":randint(150,300),"jersey-pair of shoes":randint(15,30),
                      "book-toy":randint(5,15),"mug-toaster":randint(5,15),
                      "bicycle accessory-bicycle":randint(15,40),"table lamp-study table":randint(10,25),
                      "movie dvd-dvd player":randint(10,20),"carpet-sofa":randint(25,100)}      
        
        self.item = self.ItemPool.keys()[randint(0,len(self.ItemPool)-1)]
        self.item1 = self.item.partition("-")[0]
        self.item2 = self.item.partition("-")[2]
        '''the amount she will pay for each item'''
        self.amount1 = self.ItemPool[self.item]
        self.multiplier = randint(3,7)
        self.OrigPrice = self.multiplier * self.amount1
        '''10-30% discount on the item'''
        self.discount = self.OrigPrice * randint(1,3)/10
        self.MoneySpent = self.amount1 + self.OrigPrice - self.discount
        
        self.answer = self.amount1
        
        self.problem1 = "Before a $%d discount on a %s, it cost %d times as much as a %s. If %s paid $%d altogether for the %s and the discounted %s, how much did he pay for the %s?"%(self.discount,self.item2,self.multiplier,self.item1,self.BoyName,self.MoneySpent,self.item1,self.item2,self.item1)
        self.problem2 = "%s received a $%d discount on the purchase of a %s. He also bought a %s and paid $%d altogether. If the %s cost %d times as much as the %s before discount, find the amount of money that %s paid for the %s."%(self.BoyName,self.discount,self.item2,self.item1,self.MoneySpent,self.item2,self.multiplier,self.item1,self.BoyName,self.item1)
        self.problem3 = "%s bought a %s at $%d off. He also bought a %s and paid $%d altogether. If, before discount, the %s cost %d times as much as the %s, how much money did %s pay for the %s?"%(self.BoyName,self.item2,self.discount,self.item1,self.MoneySpent,self.item2,self.multiplier,self.item1,self.BoyName,self.item1)
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])
        
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType18(self.BoyName,self.problem,self.answer,self.amount1,self.item1,self.OrigPrice,self.discount,self.item2,self.multiplier,self.MoneySpent)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"$",'problem_type':"ProblemType18"}

    def ExplainType18(self,BoyName,problem,answer,amount1,item1,OrigPrice,discount,item2,multiplier,MoneySpent):
        self.answer_text = "The correct answer is: <b>$"+str(answer)+"</b>"
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'><tr><td></td><td align='center' height=24>?<br><img src='images/explanation/up_curly_braces_pt7cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td height=24>"+item1+"</td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/green_block_pt7cm.png'></td>"
        for _i in range(multiplier-1):
            self.table_text = self.table_text + "<td></td>"
        self.table_text = self.table_text + "<td height=24 align='center'>$"+str(discount)+"<br><img src='/images/explanation/up_curly_braces_pt4cm.png'></td>"
        self.table_text = self.table_text + "<td rowspan=2><img src='/images/explanation/right_curly_braces_1cm.png' height=48></td>"
        self.table_text = self.table_text + "<td rowspan=2>$"+str(MoneySpent)+"+$"+str(discount)+"</td>"
        self.table_text = self.table_text + "<tr><td height=24>"+item2+"</td>"
        for _1 in range(multiplier-1):
            self.table_text = self.table_text + "<td><img src='/images/explanation/pink_block_pt7cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/pink_block_pt3cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/yellow_block_pt4cm.png'></td>"
        self.table_text = self.table_text + "</tr></table><br>"
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(MoneySpent)+" + $"+str(discount)+" = $"+str(MoneySpent+discount)+"</div>"
        self.solution_text = self.solution_text + "<div>Before discount, the "+item2+" and the "+item1+" cost $"+str(MoneySpent+discount)+" altogether.</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(multiplier+1)+" units = $"+str(MoneySpent+discount)+"</div>"
        self.solution_text = self.solution_text + "<div>1 unit = $"+str(MoneySpent+discount)+" &divide; "+str(multiplier+1)+" = $"+str((MoneySpent+discount)/(multiplier+1))+"</div>"
        self.solution_text = self.solution_text + "<div>"+BoyName+" paid $"+str((MoneySpent+discount)/(multiplier+1))+" for the "+item1+".</div>"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain
        
    def GenerateProblemType19(self):
        '''e.g.:After a discount of $150 on a laptop, it cost 4 times as much as a printer. If the printer and the laptop
		were priced at $1150 altogether before discount, what was the cost of the printer?'''
            
        self.BoyName = random.choice(PersonName.BoyName)
        self.ItemPool = {"shirt-coat":randint(25,50),"Phone-TV":randint(150,300),
                      "printer-laptop":randint(150,300),"jersey-pair of shoes":randint(15,30),
                      "book-toy":randint(5,15),"mug-toaster":randint(5,15),
                      "bicycle accessory-bicycle":randint(15,40),"table lamp-study table":randint(10,25),
                      "movie dvd-dvd player":randint(10,20),"carpet-sofa":randint(25,100)}      
        
        self.item = self.ItemPool.keys()[randint(0,len(self.ItemPool)-1)]
        self.item1 = self.item.partition("-")[0]
        self.item2 = self.item.partition("-")[2]
        '''the amount she will pay for each item'''
        self.amount1 = self.ItemPool[self.item]
        self.multiplier = randint(3,7)
        '''10-30% discount on the item'''
        self.discount = self.multiplier * self.amount1 * randint(1,3)/10        
        self.OrigPrice = self.multiplier * self.amount1 + self.discount
        self.BeforeDisc = self.amount1 + self.OrigPrice
        
        self.answer = self.amount1
        
        self.problem1 = "After a discount of $%d on a %s, it cost %d times as much as a %s. If the %s and the %s were priced at $%d altogether before discount, what was the cost of the %s?"%(self.discount,self.item2,self.multiplier,self.item1,self.item1,self.item2,self.BeforeDisc,self.item1)
        self.problem2 = "%s purchased a %s and a %s. After a discount of $%d on the %s, it cost %d times as much as the %s. If the %s and the %s were priced at $%d altogether before discount, what was the cost of the %s?"%(self.BoyName,self.item1,self.item2,self.discount,self.item2,self.multiplier,self.item1,self.item2,self.item1,self.BeforeDisc,self.item1)
        self.problem3 = "A %s cost %d times as much as a %s after a discount of $%d. If before discount, the items were priced at $%d altogether, find the cost of the %s."%(self.item2,self.multiplier,self.item1,self.discount,self.BeforeDisc,self.item1)
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])
        
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType19(self.BoyName,self.problem,self.answer,self.amount1,self.item1,self.OrigPrice,self.discount,self.item2,self.multiplier,self.BeforeDisc)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"$",'problem_type':"ProblemType19"}

    def ExplainType19(self,BoyName,problem,answer,amount1,item1,OrigPrice,discount,item2,multiplier,BeforeDisc):
        self.answer_text = "The correct answer is: <b>$"+str(answer)+"</b>"
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'><tr><td></td><td align='center' height=24>?<br><img src='images/explanation/up_curly_braces_pt7cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td height=24>"+item1+"</td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/green_block_pt7cm.png'></td>"
        for _i in range(multiplier-1):
            self.table_text = self.table_text + "<td></td>"
        self.table_text = self.table_text + "<td height=24 align='center'>$"+str(discount)+"<br><img src='/images/explanation/up_curly_braces_pt4cm.png'></td>"
        self.table_text = self.table_text + "<td rowspan=2><img src='/images/explanation/right_curly_braces_1cm.png' height=48></td>"
        self.table_text = self.table_text + "<td rowspan=2>$"+str(BeforeDisc)+"</td>"
        self.table_text = self.table_text + "<tr><td height=24>"+item2+"</td>"
        for _1 in range(multiplier):
            self.table_text = self.table_text + "<td><img src='/images/explanation/pink_block_pt7cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/yellow_block_pt4cm.png'></td>"
        self.table_text = self.table_text + "</tr></table><br>"
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(BeforeDisc)+" - $"+str(discount)+" = $"+str(BeforeDisc-discount)+"</div>"
        self.solution_text = self.solution_text + "<div>After discount, the "+item2+" and "+item1+" cost $"+str(BeforeDisc-discount)+" altogether.</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(multiplier+1)+" units = $"+str(BeforeDisc-discount)+"</div>"
        self.solution_text = self.solution_text + "<div>1 unit = $"+str(BeforeDisc-discount)+" &divide; "+str(multiplier+1)+" = $"+str((BeforeDisc-discount)/(multiplier+1))+"</div>"
        self.solution_text = self.solution_text + "<div>The cost of the "+item1+" was $"+str((BeforeDisc-discount)/(multiplier+1))+".</div>"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain  

    def GenerateProblemType20(self):
        '''e.g.:After discount on a laptop, it cost 4 times as much as a printer. If the items were priced at $1150 altogether before
		discount and the laptop cost $800 after discount, how much discount was given on the laptop?'''
            
        self.BoyName = random.choice(PersonName.BoyName)
        self.ItemPool = {"shirt-coat":randint(25,50),"Phone-TV":randint(150,300),
                      "printer-laptop":randint(150,300),"jersey-pair of shoes":randint(15,30),
                      "book-toy":randint(5,15),"mug-toaster":randint(5,15),
                      "bicycle accessory-bicycle":randint(15,40),"table lamp-study table":randint(10,25),
                      "movie dvd-dvd player":randint(10,20),"carpet-sofa":randint(25,100)}      
        
        self.item = self.ItemPool.keys()[randint(0,len(self.ItemPool)-1)]
        self.item1 = self.item.partition("-")[0]
        self.item2 = self.item.partition("-")[2]
        '''the amount she will pay for each item'''
        self.amount1 = self.ItemPool[self.item]
        self.multiplier = randint(3,7)
        '''10-30% discount on the item'''
        self.discount = self.multiplier * self.amount1 * randint(1,3)/10        
        self.OrigPrice = self.multiplier * self.amount1 + self.discount
        self.DiscPrice = self.multiplier * self.amount1
        self.BeforeDisc = self.amount1 + self.OrigPrice
        
        self.answer = self.discount
        
        self.problem1 = "After discount on a %s, it cost %d times as much as a %s. If the items were priced at $%d altogether before discount and the %s cost $%d after discount, how much discount was given on the %s?"%(self.item2,self.multiplier,self.item1,self.BeforeDisc,self.item2,self.DiscPrice,self.item2)
        self.problem2 = "After discount, a %s cost $%d. After discount, the %s cost %d times as much as a %s. If the %s and the %s were priced at $%d altogether before discount, how much discount was given on the %s?"%(self.item2,self.DiscPrice,self.item2,self.multiplier,self.item1,self.item2,self.item1,self.BeforeDisc,self.item2)
        self.problem3 = "After receiving a discount on the purchase of a %s %s paid $%d for it. He also bought a %s. After discount, the %s cost %d times as much as the %s. If the items were priced at $%d altogether before discount, find the amount of discount given on the %s."%(self.item2,self.BoyName,self.DiscPrice,self.item1,self.item2,self.multiplier,self.item1,self.BeforeDisc,self.item2)
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])
        
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType20(self.BoyName,self.problem,self.answer,self.amount1,self.item1,self.OrigPrice,self.DiscPrice,self.discount,self.item2,self.multiplier,self.BeforeDisc)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"$",'problem_type':"ProblemType20"}

    def ExplainType20(self,BoyName,problem,answer,amount1,item1,OrigPrice,DiscPrice,discount,item2,multiplier,BeforeDisc):
        self.answer_text = "The correct answer is: <b>$"+str(answer)+"</b>"
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'>"
        self.table_text = self.table_text + "<tr><td height=24>"+item1+"</td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/green_block_pt7cm.png'></td>"
        for _i in range(multiplier-1):
            self.table_text = self.table_text + "<td></td>"
        self.table_text = self.table_text + "<td height=24 align='center'>?<br><img src='/images/explanation/up_curly_braces_pt4cm.png'></td>"
        self.table_text = self.table_text + "<td rowspan=2><img src='/images/explanation/right_curly_braces_1cm.png' height=48></td>"
        self.table_text = self.table_text + "<td rowspan=2>$"+str(BeforeDisc)+"</td>"
        self.table_text = self.table_text + "<tr><td height=24>"+item2+"</td>"
        for _1 in range(multiplier):
            self.table_text = self.table_text + "<td><img src='/images/explanation/pink_block_pt7cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/yellow_block_pt4cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td></td><td align=center colspan="+str(multiplier)+"><img src='/images/explanation/down_curly_braces_3cm.png' width="+str(multiplier*45)+">"
        self.table_text = self.table_text + "<br>$"+str(DiscPrice)+"</td>"
        self.table_text = self.table_text + "</tr></table><br>"
        
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(multiplier)+" units = $"+str(DiscPrice)+"</div>"
        self.solution_text = self.solution_text + "<div>1 unit = $"+str(DiscPrice)+" &divide; "+str(multiplier)+" = $"+str(DiscPrice/multiplier)+"</div>"
        self.solution_text = self.solution_text + "<div>"+str(multiplier+1)+" units = "+str(multiplier+1)+" x $"+str(DiscPrice/multiplier)+" = $"+str((multiplier+1)*(DiscPrice/multiplier))+"</div>"
        self.solution_text = self.solution_text + "<div>After discount, the items cost $"+str((multiplier+1)*(DiscPrice/multiplier))+" altogether.</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(BeforeDisc)+" - $"+str((multiplier+1)*(DiscPrice/multiplier))+" = $"+str(BeforeDisc-((multiplier+1)*(DiscPrice/multiplier)))+"</div>"
        self.solution_text = self.solution_text + "<div>The discount given on the "+item2+" was $"+str(BeforeDisc-((multiplier+1)*(DiscPrice/multiplier)))+".</div>"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    def GenerateProblemType21(self):
        '''e.g.:After a $150 discount on a laptop, it cost 4 times as much as a printer. If the printer cost $200, what was
		the usual price of the laptop?'''
            
        self.BoyName = random.choice(PersonName.BoyName)
        self.ItemPool = {"shirt-coat":randint(25,50),"Phone-TV":randint(150,300),
                      "printer-laptop":randint(150,300),"jersey-pair of shoes":randint(15,30),
                      "book-toy":randint(5,15),"mug-toaster":randint(5,15),
                      "bicycle accessory-bicycle":randint(15,40),"table lamp-study table":randint(10,25),
                      "movie dvd-dvd player":randint(10,20),"carpet-sofa":randint(25,100)}      
        
        self.item = self.ItemPool.keys()[randint(0,len(self.ItemPool)-1)]
        self.item1 = self.item.partition("-")[0]
        self.item2 = self.item.partition("-")[2]
        '''the amount she will pay for each item'''
        self.amount1 = self.ItemPool[self.item]
        self.multiplier = randint(3,7)
        '''10-30% discount on the item'''
        self.discount = self.multiplier * self.amount1 * randint(1,3)/10        
        self.OrigPrice = self.multiplier * self.amount1 + self.discount
        self.DiscPrice = self.multiplier * self.amount1
        self.BeforeDisc = self.amount1 + self.OrigPrice
        
        self.answer = self.OrigPrice
        
        self.problem1 = "After a $%d discount on a %s, it cost %d times as much as a %s. If the %s cost $%d, what was the usual price of the %s?"%(self.discount,self.item2,self.multiplier,self.item1,self.item1,self.amount1,self.item2)        
        self.problem2 = "%s purchased a %s and a %s. After a discount of $%d on the %s, it cost %d times as much as the %s. If the %s cost $%d, what was the usual price of the %s?"%(self.BoyName,self.item1,self.item2,self.discount,self.item2,self.multiplier,self.item1,self.item1,self.amount1,self.item2)
        self.problem3 = "After discount, a %s cost %d times as much as a %s. If %s paid $%d for the %s and received a discount of $%d on the %s, what was the usual price of the %s?"%(self.item2,self.multiplier,self.item1,self.BoyName,self.amount1,self.item1,self.discount,self.item2,self.item2)
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])
        
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType21(self.BoyName,self.problem,self.answer,self.amount1,self.item1,self.OrigPrice,self.DiscPrice,self.discount,self.item2,self.multiplier,self.BeforeDisc)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"$",'problem_type':"ProblemType21"}

    def ExplainType21(self,BoyName,problem,answer,amount1,item1,OrigPrice,DiscPrice,discount,item2,multiplier,BeforeDisc):
        self.answer_text = "The correct answer is: <b>$"+str(answer)+"</b>"
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'><tr><td></td><td align='center' height=24>$"+str(amount1)+"<br><img src='images/explanation/up_curly_braces_pt7cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td height=24>"+item1+"</td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/green_block_pt7cm.png'></td>"
        for _i in range(multiplier-1):
            self.table_text = self.table_text + "<td></td>"
        self.table_text = self.table_text + "<td height=24 align='center'>$"+str(discount)+"<br><img src='/images/explanation/up_curly_braces_pt4cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td height=24>"+item2+"</td>"
        for _1 in range(multiplier):
            self.table_text = self.table_text + "<td><img src='/images/explanation/pink_block_pt7cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/yellow_block_pt4cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td></td><td align='center' colspan="+str(multiplier+1)+"><img src='/images/explanation/down_curly_braces_2cm.png' height=24 width="+str(45*(multiplier+1))+">"
        self.table_text = self.table_text + "<br>?</td>"
        self.table_text = self.table_text + "</tr></table><br>"
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(multiplier)+" units x $"+str(amount1)+" = $"+str(multiplier*amount1)+"</div>"
        self.solution_text = self.solution_text + "<div>After discount, the "+item2+" cost $"+str(multiplier*amount1)+".</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(multiplier*amount1)+" + $"+str(discount)+" = $"+str(multiplier*amount1+discount)+"</div>"
        self.solution_text = self.solution_text + "<div>The usual price of the "+item1+" was $"+str(multiplier*amount1+discount)+".</div>"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    def GenerateProblemType22(self):
        '''e.g.:After a $150 discount on a laptop, it cost 4 times as much as a printer. 
                If the laptop and the printer were priced at $1150 altogether before discount, 
                what was the usual price of the laptop?'''
            
        self.BoyName = random.choice(PersonName.BoyName)
        self.ItemPool = {"shirt-coat":randint(25,50),"Phone-TV":randint(150,300),
                      "printer-laptop":randint(150,300),"jersey-pair of shoes":randint(15,30),
                      "book-toy":randint(5,15),"mug-toaster":randint(5,15),
                      "bicycle accessory-bicycle":randint(15,40),"table lamp-study table":randint(10,25),
                      "movie dvd-dvd player":randint(10,20),"carpet-sofa":randint(25,100)}      
        
        self.item = self.ItemPool.keys()[randint(0,len(self.ItemPool)-1)]
        self.item1 = self.item.partition("-")[0]
        self.item2 = self.item.partition("-")[2]
        '''the amount she will pay for each item'''
        self.amount1 = self.ItemPool[self.item]
        self.multiplier = randint(3,7)
        '''10-30% discount on the item'''
        self.discount = self.multiplier * self.amount1 * randint(1,3)/10        
        self.OrigPrice = self.multiplier * self.amount1 + self.discount
        self.DiscPrice = self.multiplier * self.amount1
        self.BeforeDisc = self.amount1 + self.OrigPrice
        
        self.answer = self.OrigPrice
        
        self.problem1 = "After a $%d discount on a %s, it cost %d times as much as a %s. If the %s and the %s were priced at $%d altogether before discount, what was the usual price of the %s?"%(self.discount,self.item2,self.multiplier,self.item1,self.item2,self.item1,self.BeforeDisc,self.item2)
        self.problem2 = "%s purchased a %s and a %s. After a discount of $%d on the %s, it cost %d times as much as the %s. If the %s and the %s were priced at $%d altogether before discount, what was the usual price of the %s?"%(self.BoyName,self.item1,self.item2,self.discount,self.item2,self.multiplier,self.item1,self.item2,self.item1,self.BeforeDisc,self.item2) 
        self.problem3 = "A %s cost %d times as much as a %s after a discount of $%d. If, before discount, the items were priced at $%d altogether, what was the usual price of the %s?"%(self.item2,self.multiplier,self.item1,self.discount,self.BeforeDisc,self.item2)
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])
        
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType22(self.BoyName,self.problem,self.answer,self.amount1,self.item1,self.OrigPrice,self.DiscPrice,self.discount,self.item2,self.multiplier,self.BeforeDisc)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"$",'problem_type':"ProblemType22"}

    def ExplainType22(self,BoyName,problem,answer,amount1,item1,OrigPrice,DiscPrice,discount,item2,multiplier,BeforeDisc):
        self.answer_text = "The correct answer is: <b>$"+str(answer)+"</b>"
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'>"
        self.table_text = self.table_text + "<tr><td height=24>"+item1+"</td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/green_block_pt7cm.png'></td>"
        for _i in range(multiplier-1):
            self.table_text = self.table_text + "<td></td>"
        self.table_text = self.table_text + "<td height=24 align='center'>$"+str(discount)+"<br><img src='/images/explanation/up_curly_braces_pt4cm.png'></td>"
        self.table_text = self.table_text + "<td rowspan=2 align='center'><img src='/images/explanation/right_curly_braces_1cm.png'></td>"
        self.table_text = self.table_text + "<td rowspan=2 align='center'>$"+str(BeforeDisc)+"</td></tr>"
        self.table_text = self.table_text + "<tr><td height=24>"+item2+"</td>"
        for _1 in range(multiplier):
            self.table_text = self.table_text + "<td><img src='/images/explanation/pink_block_pt7cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/yellow_block_pt4cm.png'></td></tr>"
        self.table_text = self.table_text + "</table><br>"
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(BeforeDisc)+" - $"+str(discount)+" = $"+str(BeforeDisc-discount)+"</div>"
        self.solution_text = self.solution_text + "<div>After discount, the "+item2+" and "+item1+" cost $"+str(BeforeDisc-discount)+" altogether.</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(multiplier+1)+" units = $"+str(BeforeDisc-discount)+"</div>"
        self.solution_text = self.solution_text + "<div>1 unit = $"+str(BeforeDisc-discount)+" &divide; "+str(multiplier+1)+" = $"+str((BeforeDisc-discount)/(multiplier+1))+"</div>"
        self.solution_text = self.solution_text + "<div>"+str(multiplier)+" units = "+str(multiplier)+" x $"+str((BeforeDisc-discount)/(multiplier+1))+" = $"+str(multiplier*(BeforeDisc-discount)/(multiplier+1))+"</div><br>"
        self.solution_text = self.solution_text + "<div>After discount, the "+item2+" cost $"+str(multiplier*(BeforeDisc-discount)/(multiplier+1))+"</div>"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    '''Problem Type 7 starts here'''
    def GenerateProblemType23(self):
        '''e.g.:Annie has 10 notebooks. Betty has 4 times as many notebooks as Annie. How many notebooks have
                Annie and Betty altogether?'''
            
        self.PersonNames = random.sample(PersonName.PersonName,2)
        self.ItemPool = ["flags","stamps","pencils","pens","marbles","fishes","flowers","toy cars","CDs","kites","cans","books",
                         "red flags","blue flags","paper boats","rings","key chains","cup cakes","buns"]      
        
        self.person1 = self.PersonNames[0]
        self.person2 = self.PersonNames[1]
        self.item = random.choice(self.ItemPool)
        self.quantity1 = randint(3,8)
        self.multiplier = randint(3,8)
        self.quantity2 = self.quantity1 * self.multiplier
        self.total = self.quantity1 + self.quantity2
        
        self.answer = self.total
        
        self.problem1 = "%s has %d %s. %s has %d times as many %s as %s. How many %s have %s and %s altogether?"%(self.person1,self.quantity1,self.item,self.person2,self.multiplier,self.item,self.person1,self.item,self.person1,self.person2)                                                                                                                
        self.problem2 = "%s has %d times as many %s as %s. If %s has %d %s, how many %s do %s and %s have altogether?"%(self.person2,self.multiplier,self.item,self.person1,self.person1,self.quantity1,self.item,self.item,self.person1,self.person2)                                                                                                                                                                                                    
        self.problem3 = "How many %s have %s and %s altogether, if %s has %d %s and %s has %d times as many?"%(self.item,self.person1,self.person2,self.person1,self.quantity1,self.item,self.person2,self.multiplier)
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])
        
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType23(self.problem,self.answer,self.person1,self.person2,self.item,self.quantity1,self.quantity2,self.multiplier)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"",'unit':self.item,'problem_type':"ProblemType23"}

    def ExplainType23(self,problem,answer,person1,person2,item,quantity1,quantity2,multiplier):
        self.answer_text = "The correct answer is: <b>"+str(answer)+" "+item
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'><tr><td></td><td align='center' width=45>"+str(quantity1)+" "+item+"<br>"
        self.table_text = self.table_text + "<img src='/images/explanation/up_curly_braces_pt7cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td>"+person1+"</td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/pink_block_pt7cm.png'></td>"
        for _i in range (multiplier-1):
            self.table_text = self.table_text + "<td></td>"
        self.table_text = self.table_text + "<td rowspan=2 align='center'><img src='/images/explanation/right_curly_braces_1cm.png'></td>"
        self.table_text = self.table_text + "<td rowspan=2 align='center'>?</td></tr>"
        self.table_text = self.table_text + "<tr><td>"+person2+"</td>"
        for _i in range (multiplier):
            self.table_text = self.table_text + "<td><img src='/images/explanation/green_block_pt7cm.png'></td>"
        self.table_text = self.table_text + "</tr></table><br>"
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>1 unit = "+str(quantity1)+" "+item+"</div>"
        self.solution_text = self.solution_text + "<div>"+str(multiplier)+" units = "+str(multiplier)+" x "+str(quantity1)+" "+item+" = "+str(multiplier*quantity1)+" "+item+"</div>"
        self.solution_text = self.solution_text + "<div>"+person2+" has "+str(multiplier*quantity1)+" "+item+".</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(quantity1)+" "+item+" + "+str(multiplier*quantity1)+" "+item+" = "+str(quantity1+multiplier*quantity1)+" "+item+"</div>"
        self.solution_text = self.solution_text + "<div>"+person1+" and "+person2+" have "+str(quantity1+multiplier*quantity1)+" "+item+" altogether.</div>"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain    

    def GenerateProblemType24(self):
        '''e.g.:Betty has 4 times as many notebooks as Annie. If they have a 50 notebooks, how many more notebooks than Annie has Betty?'''
            
        self.PersonNames = random.sample(PersonName.PersonName,2)
        self.ItemPool = ["flags","stamps","pencils","pens","marbles","fishes","flowers","toy cars","CDs","kites","cans","books",
                         "red flags","blue flags","paper boats","rings","key chains","cup cakes","buns"]      
        
        self.person1 = self.PersonNames[0]
        self.person2 = self.PersonNames[1]
        self.item = random.choice(self.ItemPool)
        self.quantity1 = randint(3,8)
        self.multiplier = randint(3,8)
        self.quantity2 = self.quantity1 * self.multiplier
        self.total = self.quantity1 + self.quantity2
        self.diff = self.quantity2 - self.quantity1        
        self.answer = self.diff
        
        self.problem1 = "%s has %d times as many %s as %s. If they have %d %s, how many more %s than %s has %s?"%(self.person2,self.multiplier,self.item,self.person1,self.total,self.item,self.item,self.person1,self.person2)        														
        self.problem2 = "%s and %s have %d %s. If %s has %d times as many %s as %s, how many more %s than %s has %s?"%(self.person1,self.person2,self.total,self.item,self.person2,self.multiplier,self.item,self.person1,self.item,self.person1,self.person2)        													
        self.problem3 = "%s has %d times as many %s as %s. How many more %s than %s has %s, if they have %d %s altogether?"%(self.person2,self.multiplier,self.item,self.person1,self.item,self.person1,self.person2,self.total,self.item)        																
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])
        
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType24(self.problem,self.answer,self.person1,self.person2,self.item,self.quantity1,self.quantity2,self.multiplier,self.total,self.diff)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"",'unit':self.item,'problem_type':"ProblemType24"}

    def ExplainType24(self,problem,answer,person1,person2,item,quantity1,quantity2,multiplier,total,diff):
        self.answer_text = "The correct answer is: <b>"+str(answer)+" "+item
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'>"
        self.table_text = self.table_text + "<tr><td>"+person1+"</td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/pink_block_pt7cm.png'></td>"
        for _i in range (multiplier-1):
            self.table_text = self.table_text + "<td></td>"
        self.table_text = self.table_text + "<td rowspan=2 align='center'><img src='/images/explanation/right_curly_braces_1cm.png'></td>"
        self.table_text = self.table_text + "<td rowspan=2 align='center'>"+str(total)+" "+item+"</td></tr>"
        self.table_text = self.table_text + "<tr><td>"+person2+"</td>"
        for _i in range (multiplier):
            self.table_text = self.table_text + "<td><img src='/images/explanation/green_block_pt7cm.png'></td>"
        self.table_text = self.table_text + "</tr><tr><td></td><td></td>"
        self.table_text = self.table_text + "<td align='center' height=24 colspan="+str(multiplier-1)+"><img src='/images/explanation/down_curly_braces_3cm.png' width="+str(45*(multiplier-1))+"><br>"
        self.table_text = self.table_text + "?</td>"
        self.table_text = self.table_text + "</tr></table><br>"
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(multiplier+1)+" units = "+str(total)+" "+item+"</div>"
        self.solution_text = self.solution_text + "<div>1 unit = "+str(total)+" "+item+" &divide; "+str(multiplier+1)+" = "+str(total/(multiplier+1))+" "+item+"</div>"
        self.solution_text = self.solution_text + "<div>"+str(multiplier-1)+" units = "+str(multiplier-1)+" x "+str(total/(multiplier+1))+" "+item+" = "+str((multiplier-1)*(total/(multiplier+1)))+" "+item+"</div><br>"
        self.solution_text = self.solution_text + "<div>"+person2+" has "+str((multiplier-1)*(total/(multiplier+1)))+" more "+item+" than "+person1+"</div>"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    def GenerateProblemType25(self):
        '''e.g.:: Annie and Betty have 50 notebooks. If Betty has 4 times as many notebooks as Annie, find the difference in the number of notebooks that they have.'''
            
        self.PersonNames = random.sample(PersonName.PersonName,2)
        self.ItemPool = ["flags","stamps","pencils","pens","marbles","fishes","flowers","toy cars","CDs","kites","cans","books",
                         "red flags","blue flags","paper boats","rings","key chains","cup cakes","buns"]      
        
        self.person1 = self.PersonNames[0]
        self.person2 = self.PersonNames[1]
        self.item = random.choice(self.ItemPool)
        self.quantity1 = randint(3,8)
        self.multiplier = randint(3,8)
        self.quantity2 = self.quantity1 * self.multiplier
        self.total = self.quantity1 + self.quantity2
        self.diff = self.quantity2 - self.quantity1        
        self.answer = self.diff
        
        self.problem1 = "%s has %d times as many %s as %s. If they have %d %s, find the difference in the number of %s that they have."%(self.person2,self.multiplier,self.item,self.person1,self.total,self.item,self.item)        																	
        self.problem2 = "%s and %s have %d %s. If %s has %d times as many %s as %s, find the difference in the number of %s that they have."%(self.person1,self.person2,self.total,self.item,self.person2,self.multiplier,self.item,self.person1,self.item)        																	
        self.problem3 = "%s has %d times as many %s as %s. Find the difference in the number of %s that they have, if they have %d %s altogether?"%(self.person2,self.multiplier,self.item,self.person1,self.item,self.total,self.item)
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])
        
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType25(self.problem,self.answer,self.person1,self.person2,self.item,self.quantity1,self.quantity2,self.multiplier,self.total,self.diff)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"",'unit':self.item,'problem_type':"ProblemType25"}

    def ExplainType25(self,problem,answer,person1,person2,item,quantity1,quantity2,multiplier,total,diff):
        self.answer_text = "The correct answer is: <b>"+str(answer)+" "+item
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'>"
        self.table_text = self.table_text + "<tr><td>"+person1+"</td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/pink_block_pt7cm.png'></td>"
        for _i in range (multiplier-1):
            self.table_text = self.table_text + "<td></td>"
        self.table_text = self.table_text + "<td rowspan=2 align='center'><img src='/images/explanation/right_curly_braces_1cm.png'></td>"
        self.table_text = self.table_text + "<td rowspan=2 align='center'>"+str(total)+" "+item+"</td></tr>"
        self.table_text = self.table_text + "<tr><td>"+person2+"</td>"
        for _i in range (multiplier):
            self.table_text = self.table_text + "<td><img src='/images/explanation/green_block_pt7cm.png'></td>"
        self.table_text = self.table_text + "</tr><tr><td></td><td></td>"
        self.table_text = self.table_text + "<td align='center' colspan="+str(multiplier-1)+"><img src='/images/explanation/down_curly_braces_3cm.png' width="+str(45*(multiplier-1))+"><br>"
        self.table_text = self.table_text + "?</td>"
        self.table_text = self.table_text + "</tr></table><br>"
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(multiplier+1)+" units = "+str(total)+" "+item+"</div>"
        self.solution_text = self.solution_text + "<div>1 unit = "+str(total)+" "+item+" &divide; "+str(multiplier+1)+" = "+str(total/(multiplier+1))+" "+item+"</div>"
        self.solution_text = self.solution_text + "<div>"+str(multiplier-1)+" units = "+str(multiplier-1)+" x "+str(total/(multiplier+1))+" "+item+" = "+str((multiplier-1)*(total/(multiplier+1)))+" "+item+"</div><br>"
        self.solution_text = self.solution_text + "<div>The difference in the numbers of "+item+" that they have is "+str((multiplier-1)*(total/(multiplier+1)))+".</div>"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    def GenerateProblemType26(self):
        '''e.g.:: Betty has 4 times as many notebooks as Annie. If they have a 50 notebooks, how many fewer notebooks than Betty has Annie? '''
            
        self.PersonNames = random.sample(PersonName.PersonName,2)
        self.ItemPool = ["flags","stamps","pencils","pens","marbles","fishes","flowers","toy cars","CDs","kites","cans","books",
                         "red flags","blue flags","paper boats","rings","key chains","cup cakes","buns"]      
        
        self.person1 = self.PersonNames[0]
        self.person2 = self.PersonNames[1]
        self.item = random.choice(self.ItemPool)
        self.quantity1 = randint(3,8)
        self.multiplier = randint(3,8)
        self.quantity2 = self.quantity1 * self.multiplier
        self.total = self.quantity1 + self.quantity2
        self.diff = self.quantity2 - self.quantity1        
        self.answer = self.diff

        self.problem1 = "%s has %d times as many %s as %s. If they have a %d %s, how many fewer %s than %s has %s?"%(self.person2,self.multiplier,self.item,self.person1,self.total,self.item,self.item,self.person2,self.person1)         													
        self.problem2 = "%s and %s have %d %s. If %s has %d times as many %s as %s, how many fewer %s than %s has %s?"%(self.person1,self.person2,self.total,self.item,self.person2,self.multiplier,self.item,self.person1,self.item,self.person2,self.person1)        														
        self.problem3 = "%s has %d times as many %s as %s. How many fewer %s than %s has %s, if they have %d %s altogether?"%(self.person2,self.multiplier,self.item,self.person1,self.item,self.person2,self.person1,self.total,self.item)
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])

        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType26(self.problem,self.answer,self.person1,self.person2,self.item,self.quantity1,self.quantity2,self.multiplier,self.total,self.diff)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"",'unit':self.item,'problem_type':"ProblemType26"}

    def ExplainType26(self,problem,answer,person1,person2,item,quantity1,quantity2,multiplier,total,diff):
        self.answer_text = "The correct answer is: <b>"+str(answer)+" "+item
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'>"
        self.table_text = self.table_text + "<tr><td>"+person1+"</td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/pink_block_pt7cm.png'></td>"
        for _i in range (multiplier-1):
            self.table_text = self.table_text + "<td></td>"
        self.table_text = self.table_text + "<td rowspan=2 align='center'><img src='/images/explanation/right_curly_braces_1cm.png'></td>"
        self.table_text = self.table_text + "<td rowspan=2 align='center'>"+str(total)+" "+item+"</td></tr>"
        self.table_text = self.table_text + "<tr><td>"+person2+"</td>"
        for _i in range (multiplier):
            self.table_text = self.table_text + "<td><img src='/images/explanation/green_block_pt7cm.png'></td>"
        self.table_text = self.table_text + "</tr><tr><td></td><td></td>"
        self.table_text = self.table_text + "<td align='center' colspan="+str(multiplier-1)+"><img src='/images/explanation/down_curly_braces_3cm.png' width="+str(45*(multiplier-1))+"><br>"
        self.table_text = self.table_text + "?</td>"
        self.table_text = self.table_text + "</tr></table><br>"
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(multiplier+1)+" units = "+str(total)+" "+item+"</div>"
        self.solution_text = self.solution_text + "<div>1 unit = "+str(total)+" "+item+" &divide; "+str(multiplier+1)+" = "+str(total/(multiplier+1))+" "+item+"</div>"
        self.solution_text = self.solution_text + "<div>"+str(multiplier-1)+" units = "+str(multiplier-1)+" x "+str(total/(multiplier+1))+" "+item+" = "+str((multiplier-1)*(total/(multiplier+1)))+" "+item+"</div><br>"
        self.solution_text = self.solution_text + "<div>"+person1+" has "+str((multiplier-1)*(total/(multiplier+1)))+ " fewer "+item+" than "+person2+".</div>"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    '''Problem type 8 starts here'''
    def GenerateProblemType27(self):
        '''e.g.:Annie bought 27 notebooks and paid a total of $81. Betty bought 37 such notebooks. How much did Betty pay for all her notebooks?'''
            
        self.PersonNames = random.sample(PersonName.GirlName,2)
        self.ItemPool = ["flags","stamps","pencils","pens","marbles","fishes","flowers","toy cars","CDs","kites","cans","books",
                         "red flags","blue flags","paper boats","rings","key chains","cup cakes","buns"]      
        
        self.person1 = self.PersonNames[0]
        self.person2 = self.PersonNames[1]
        self.item = random.choice(self.ItemPool)
        self.quantity1 = randint(3,13)
        self.quantity2 = randint(14,25)
        self.price = randint(3,6)
        self.amount1 = self.price * self.quantity1
        self.amount2 = self.price * self.quantity2
        self.TotalAmount = self.amount1 + self.amount2
        self.total = self.quantity1 + self.quantity2
                
        self.answer = self.amount2

        self.problem1 = "%s bought %d %s and paid a total of $%d. %s bought %d such %s. How much did %s pay for all her %s?"%(self.person1,self.quantity1,self.item,self.amount1,self.person2,self.quantity2,self.item,self.person2,self.item)        														
        self.problem2 = "%s bought %d %s while %s bought %d %s. If %s paid $%d for the %s, how much did %s pay for all her %s?"%(self.person1,self.quantity1,self.item,self.person2,self.quantity2,self.item,self.person1,self.amount1,self.item,self.person2,self.item)        												
        self.problem3 = "%s bought %d %s for $%d. If %s bought %d such %s, find how much %s paid for all her %s."%(self.person1,self.quantity1,self.item,self.amount1,self.person2,self.quantity2,self.item,self.person2,self.item)
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])
        
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType27(self.problem,self.answer,self.person1,self.person2,self.item,self.quantity1,self.quantity2,self.price,self.amount1,self.amount2,self.TotalAmount,self.total)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"$",'problem_type':"ProblemType27"}

    def ExplainType27(self,problem,answer,person1,person2,item,quantity1,quantity2,price,amount1,amount2,TotalAmount,total):
        self.answer_text = "The correct answer is: <b>$"+str(answer)+"</b>"
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'><tr><td></td><td height=24>$"+str(amount1)+" for "+str(quantity1)+" "+item+"<br>"
        self.table_text = self.table_text + "<img src='/images/explanation/up_curly_braces_2cm.png'></td><td></td></tr>"
        self.table_text = self.table_text + "<tr><td>"+person1+"</td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/pink_block_2cm.png'></td><td></td></tr>"
        self.table_text = self.table_text + "<tr><td>"+person2+"</td>"
        self.table_text = self.table_text + "<td colspan=2><img src='/images/explanation/green_block_3cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td></td>"
        self.table_text = self.table_text + "<td align='center' colspan=2><img src='/images/explanation/down_curly_braces_3cm.png'><br>"
        self.table_text = self.table_text + "?</td>"
        self.table_text = self.table_text + "</tr></table><br>"
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(quantity1)+" units =$"+str(amount1)+"</div>"
        self.solution_text = self.solution_text + "<div>1 unit = $"+str(amount1)+" &divide; "+str(quantity1)+" = $"+str(amount1/quantity1)+"</div>"
        self.solution_text = self.solution_text + "<div>"+str(quantity2)+" units = "+str(quantity2)+" x $"+str(amount1/quantity1)+" = $"+str(quantity2*amount1/quantity1)+"</div><br>"
        self.solution_text = self.solution_text + "<div>"+person2+" paid $"+str(quantity2*amount1/quantity1)+" for all her "+item+".</div>"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    def GenerateProblemType28(self):
        '''e.g.:Annie bought 27 notebooks and paid a total of $81. Betty bought 37 similar notebooks as Annie. How much did they pay altogether?'''
            
        self.PersonNames = random.sample(PersonName.GirlName,2)
        self.ItemPool = ["flags","stamps","pencils","pens","marbles","fishes","flowers","toy cars","CDs","kites","cans","books",
                         "red flags","blue flags","paper boats","rings","key chains","cup cakes","buns"]      
        
        self.person1 = self.PersonNames[0]
        self.person2 = self.PersonNames[1]
        self.item = random.choice(self.ItemPool)
        self.quantity1 = randint(3,13)
        self.quantity2 = randint(14,25)
        self.price = randint(3,6)
        self.amount1 = self.price * self.quantity1
        self.amount2 = self.price * self.quantity2
        self.TotalAmount = self.amount1 + self.amount2
        self.total = self.quantity1 + self.quantity2
                
        self.answer = self.TotalAmount

        self.problem1 = "%s bought %d %s and paid a total of $%d. %s bought %d similar %s as %s. How much did they pay altogether?"%(self.person1,self.quantity1,self.item,self.amount1,self.person2,self.quantity2,self.item,self.person1)        														
        self.problem2 = "%s bought %d %s while %s bought %d %s. If %s paid $%d for the %s, how much did they pay altogether?"%(self.person1,self.quantity1,self.item,self.person2,self.quantity2,self.item,self.person1,self.amount1,self.item)        														
        self.problem3 = "%s bought %d %s for $%d. If %s bought %d similar %s as %s, find how much they paid altogether."%(self.person1,self.quantity1,self.item,self.amount1,self.person2,self.quantity2,self.item,self.person1)
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])
        
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType28(self.problem,self.answer,self.person1,self.person2,self.item,self.quantity1,self.quantity2,self.price,self.amount1,self.amount2,self.TotalAmount,self.total)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"$",'problem_type':"ProblemType28"}

    def ExplainType28(self,problem,answer,person1,person2,item,quantity1,quantity2,price,amount1,amount2,TotalAmount,total):
        self.answer_text = "The correct answer is: <b>$"+str(answer)+"</b>"
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'><tr><td></td><td height=24>$"+str(amount1)+" for "+str(quantity1)+" "+item+"<br>"
        self.table_text = self.table_text + "<img src='/images/explanation/up_curly_braces_2cm.png'></td><td></td></tr>"
        self.table_text = self.table_text + "<tr><td>"+person1+"</td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/pink_block_2cm.png'></td><td></td>"
        self.table_text = self.table_text + "<td rowspan=2><img src='/images/explanation/right_curly_braces_2cm.png'></td>"
        self.table_text = self.table_text + "<td rowspan=2>?</td>"
        self.table_text = self.table_text + "<tr><td>"+person2+"</td>"
        self.table_text = self.table_text + "<td colspan=2><img src='/images/explanation/green_block_3cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td></td>"
        self.table_text = self.table_text + "<td align='center' colspan=2><img src='/images/explanation/down_curly_braces_3cm.png'><br>"
        self.table_text = self.table_text + "?</td>"
        self.table_text = self.table_text + "</tr></table><br>"
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(quantity1)+" units = $"+str(amount1)+"</div>"
        self.solution_text = self.solution_text + "<div>1 unit = $"+str(amount1)+" &divide; "+str(quantity1)+" = $"+str(amount1/quantity1)+"</div>"
        self.solution_text = self.solution_text + "<div>"+str(quantity2)+" units = "+str(quantity2)+" x $"+str(amount1/quantity1)+" = $"+str(quantity2*amount1/quantity1)+"</div>"
        self.solution_text = self.solution_text + "<div>"+person2+" paid $"+str(quantity2*amount1/quantity1)+" for all her "+item+".</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(amount1)+" + $"+str(quantity2*amount1/quantity1)+" = $"+str(TotalAmount)+"</div>"
        self.solution_text = self.solution_text + "<div>"+person1+" and "+person2+" paid $"+str(TotalAmount)+" altogether.</div>"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    def GenerateProblemType29(self):
        '''e.g.:Annie bought 27 notebooks and paid a total of $81. If Annie and Betty paid $192 altogether, how many notebooks did Betty buy?'''
            
        self.PersonNames = random.sample(PersonName.GirlName,2)
        self.ItemPool = ["flags","stamps","pencils","pens","marbles","fishes","flowers","toy cars","CDs","kites","cans","books",
                         "red flags","blue flags","paper boats","rings","key chains","cup cakes","buns"]      
        
        self.person1 = self.PersonNames[0]
        self.person2 = self.PersonNames[1]
        self.item = random.choice(self.ItemPool)
        self.quantity1 = randint(3,13)
        self.quantity2 = randint(14,25)
        self.price = randint(3,6)
        self.amount1 = self.price * self.quantity1
        self.amount2 = self.price * self.quantity2
        self.TotalAmount = self.amount1 + self.amount2
        self.total = self.quantity1 + self.quantity2
                
        self.answer = self.quantity2

        self.problem1 = "%s bought %d %s and paid a total of $%d. If %s and %s paid $%d altogether, how many %s did %s buy?"%(self.person1,self.quantity1,self.item,self.amount1,self.person1,self.person2,self.TotalAmount,self.item,self.person2)																
        self.problem2 = "%s and %s paid $%d altogether for similar %s. If %s bought %d %s and paid $%d, how many %s did %s buy?"%(self.person1,self.person2,self.TotalAmount,self.item,self.person1,self.quantity1,self.item,self.amount1,self.item,self.person2)																	
        self.problem3 = "%s and %s bought some %s and paid $%d altogether. If %s bought %d %s and paid $%d, find the number of %s that %s bought."%(self.person1,self.person2,self.item,self.TotalAmount,self.person1,self.quantity1,self.item,self.amount1,self.item,self.person2)
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])
        
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType29(self.problem,self.answer,self.person1,self.person2,self.item,self.quantity1,self.quantity2,self.price,self.amount1,self.amount2,self.TotalAmount,self.total)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"",'unit':self.item,'problem_type':"ProblemType29"}

    def ExplainType29(self,problem,answer,person1,person2,item,quantity1,quantity2,price,amount1,amount2,TotalAmount,total):
        self.answer_text = "The correct answer is: <b>"+str(answer)+" "+item
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'><tr><td></td><td height=24>$"+str(amount1)+" for "+str(quantity1)+" "+item+"<br>"
        self.table_text = self.table_text + "<img src='/images/explanation/up_curly_braces_2cm.png'></td><td></td></tr>"
        self.table_text = self.table_text + "<tr><td>"+person1+"</td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/pink_block_2cm.png'></td><td></td>"
        self.table_text = self.table_text + "<td rowspan=2><img src='/images/explanation/right_curly_braces_2cm.png'></td>"
        self.table_text = self.table_text + "<td rowspan=2>$"+str(TotalAmount)+"</td>"
        self.table_text = self.table_text + "<tr><td>"+person2+"</td>"
        self.table_text = self.table_text + "<td colspan=2><img src='/images/explanation/green_block_3cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td></td>"
        self.table_text = self.table_text + "<td align='center' colspan=2><img src='/images/explanation/down_curly_braces_3cm.png'><br>"
        self.table_text = self.table_text + "?</td>"
        self.table_text = self.table_text + "</tr></table><br>"
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(TotalAmount)+" - $"+str(amount1)+" = $"+str(TotalAmount-amount1)+"</div>"
        self.solution_text = self.solution_text + "<div>"+person2+" paid $"+str(TotalAmount-amount1)+" for her "+item+".</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(amount1)+" &divide; "+str(quantity1)+" units = $"+str(amount1/quantity1)+"</div>"
        self.solution_text = self.solution_text + "<div>Each "+item+" cost $"+str(amount1/quantity1)+"</div>"
        self.solution_text = self.solution_text + "<div>$"+str(TotalAmount-amount1)+" &divide; $"+str(amount1/quantity1)+" = "+str((TotalAmount-amount1)/(amount1/quantity1))+" units</div>"
        self.solution_text = self.solution_text + "<div>"+person2+" bought "+str((TotalAmount-amount1)/(amount1/quantity1))+" "+item+".</div>"
        self.solution_text = self.solution_text + "<br><div> Watch below video for explanation of similar problem<br>"
        VideoLink = '<object><param name="movie" value="https://www.youtube.com/v/u1zgFlCw8Aw?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded"><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "HTAX7pfRTZ8";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    def GenerateProblemType30(self):
        '''e.g.:Annie and Betty bought some notebooks and paid $192 altogether. If Betty bought 10 more notebooks than Annie and paid $30 more than Annie, 
		find the number of notebooks that Annie bought?'''
            
        self.PersonNames = random.sample(PersonName.GirlName,2)
        self.ItemPool = ["flags","stamps","pencils","pens","marbles","fishes","flowers","toy cars","CDs","kites","cans","books",
                         "red flags","blue flags","paper boats","rings","key chains","cup cakes","buns"]      
        
        self.person1 = self.PersonNames[0]
        self.person2 = self.PersonNames[1]
        self.item = random.choice(self.ItemPool)
        self.quantity1 = randint(3,13)
        self.quantity2 = randint(14,25)
        self.price = randint(3,6)
        self.amount1 = self.price * self.quantity1
        self.amount2 = self.price * self.quantity2
        self.TotalAmount = self.amount1 + self.amount2
        self.total = self.quantity1 + self.quantity2
        self.QuantDiff = self.quantity2 - self.quantity1
        self.AmountDiff = self.amount2 - self.amount1
                
        self.answer = self.quantity1

        self.problem1 = "%s and %s bought some %s and paid $%d altogether. If %s bought %d more %s than %s and paid $%d more than %s, find the number of %s that %s bought?"%(self.person1,self.person2,self.item,self.TotalAmount,self.person2,self.QuantDiff,self.item,self.person1,self.AmountDiff,self.person1,self.item,self.person1)																				
        self.problem2 = "%s and %s paid $%d altogether for similar %s. If %s bought %d fewer %s than %s and paid $%d less than %s, how many %s did %s buy?"%(self.person1,self.person2,self.TotalAmount,self.item,self.person1,self.QuantDiff,self.item,self.person2,self.AmountDiff,self.person2,self.item,self.person1)        																			
        self.problem3 = "%s bought %d more %s than %s and paid $%d more than her. If %s and %s paid $%d altogether for their %s, find the number of %s that %s bought."%(self.person2,self.QuantDiff,self.item,self.person1,self.AmountDiff,self.person1,self.person2,self.TotalAmount,self.item,self.item,self.person1)
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])
        
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType30(self.problem,self.answer,self.person1,self.person2,self.item,self.quantity1,self.quantity2,self.TotalAmount,self.QuantDiff,self.AmountDiff)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"",'unit':self.item,'problem_type':"ProblemType30"}

    def ExplainType30(self,problem,answer,person1,person2,item,quantity1,quantity2,TotalAmount,QuantDiff,AmountDiff):
        self.answer_text = "The correct answer is: <b>"+str(answer)+" "+item
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'><tr><td></td><td align='center' height=24>?<br>"
        self.table_text = self.table_text + "<img src='/images/explanation/up_curly_braces_2cm.png'></td>"
        self.table_text = self.table_text + "<td height=24>$"+str(AmountDiff)+" for "+str(QuantDiff)+" "+item+"<br>"
        self.table_text = self.table_text + "<img src='/images/explanation/up_curly_braces_1cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td>"+person1+"</td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/pink_block_2cm.png'></td><td></td>"
        self.table_text = self.table_text + "<td rowspan=2><img src='/images/explanation/right_curly_braces_2cm.png'></td>"
        self.table_text = self.table_text + "<td rowspan=2>$"+str(TotalAmount)+"</td>"
        self.table_text = self.table_text + "<tr><td>"+person2+"</td>"
        self.table_text = self.table_text + "<td colspan=2><img src='/images/explanation/green_block_3cm.png'></td></tr>"
        self.table_text = self.table_text + "</table><br>"
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(TotalAmount)+" - $"+str(AmountDiff)+" = $"+str(TotalAmount-AmountDiff)+"</div>"
        self.solution_text = self.solution_text + "<div>$"+str(TotalAmount-AmountDiff)+" &divide; 2 units = $"+str((TotalAmount-AmountDiff)/2)+"</div>"
        self.solution_text = self.solution_text + "<div>"+person1+" paid $"+str((TotalAmount-AmountDiff)/2)+" for her " +item+".</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(QuantDiff)+" units = $"+str(AmountDiff)+"</div>"
        self.solution_text = self.solution_text + "<div>1 unit =$"+str(AmountDiff)+" &divide; "+str(QuantDiff)+" = $"+str(AmountDiff/QuantDiff)+"</div>"
        self.solution_text = self.solution_text + "<div>Each "+item+" cost $"+str(AmountDiff/QuantDiff)+".</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str((TotalAmount-AmountDiff)/2)+" &divide; $"+str(AmountDiff/QuantDiff)+" = "+str(((TotalAmount-AmountDiff)/2)/(AmountDiff/QuantDiff))+"</div>"
        self.solution_text = self.solution_text + "<div>"+person1+" bought "+str(((TotalAmount-AmountDiff)/2)/(AmountDiff/QuantDiff))+" "+item+".</div>"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    '''Problem Type 9 starts here'''
    def GenerateProblemType31(self):
        '''e.g.:A jersey costs $25 and a coat costs 3 times as much. If Bala bought a jersey and a coat for herself, 
		and another jersey and a coat for John, how much did she pay in total?'''
            
        self.PersonNames = random.sample(PersonName.BoyName,2)
        self.ItemPool = {"soft drink-pizza":randint(2,4),"sticker-craft book":randint(2,4),"pencil-notebook":randint(2,3),
                         "pen-letter pad":randint(2,4),"marble-board game":randint(2,5),"plant-flower pot":randint(3,6),
                         "toy car-board game":randint(3,7),"shirt-pair of pants":randint(10,20),"kite-spool":randint(2,4),
                         "flag-key chain":randint(2,4),"thumb drive-printer":randint(20,50),"tie clip-wallet":randint(5,15),
                         "bun-cake":randint(2,4),"cap-racket":randint(10,20),"jersey-coat":randint(15,30)}
        
        self.person1 = self.PersonNames[0]
        self.person2 = self.PersonNames[1]
        self.item = self.ItemPool.keys()[randint(0,len(self.ItemPool)-1)]
        self.item1 = self.item.partition("-")[0]
        self.item2 = self.item.partition("-")[2]
        self.price1 = self.ItemPool[self.item]
        self.multiplier = randint(2,7)
        self.price2 = self.price1 * self.multiplier
        self.TotalAmount = 2*(self.price1 + self.price2)
                
        self.answer = self.TotalAmount

        self.problem1 = "A %s costs $%d and a %s costs %d times as much. If %s bought a %s and a %s for himself, and another %s and a %s for %s, how much did he pay in total?"%(self.item1,self.price1,self.item2,self.multiplier,self.person1,self.item1,self.item2,self.item1,self.item2,self.person2)																			
        self.problem2 = "%s bought a %s and a %s for himself. He bought another %s and a %s for %s. If each %s cost $%d and each %s cost %d times as much, find the total amount of money that %s paid."%(self.person1,self.item1,self.item2,self.item1,self.item2,self.person2,self.item1,self.price1,self.item2,self.multiplier,self.person1)																						
        self.problem3 = "%s paid $%d for a %s and %d times as much for a %s. If he purchased a %s and a %s for himself, and another %s and a %s for %s, find the total amount of money that %s paid."%(self.person1,self.price1,self.item1,self.multiplier,self.item2,self.item1,self.item2,self.item1,self.item2,self.person2,self.person1)
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])
        
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType31(self.problem,self.answer,self.person1,self.person2,self.item1,self.item2,self.price1,self.price2,self.multiplier,self.TotalAmount)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"$",'problem_type':"ProblemType31"}

    def ExplainType31(self,problem,answer,person1,person2,item1,item2,price1,price2,multiplier,TotalAmount):
        self.answer_text = "The correct answer is: <b>$"+str(answer)+"</b>"
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'><tr><td></td><td align='center'>$"+str(price1)+"<br>"
        self.table_text = self.table_text + "<img src='/images/explanation/up_curly_braces_pt7cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td>"+item1+"</td><td><img src='/images/explanation/pink_block_pt7cm.png'></td>"
        for _i in range(multiplier-1):
            self.table_text = self.table_text + "<td></td>"
        self.table_text = self.table_text + "<td align='center' rowspan=2><img src='/images/explanation/right_curly_braces_1cm.png'></td>"
        self.table_text = self.table_text + "<td align='center' rowspan=2>?</td></tr>"
        self.table_text = self.table_text + "<tr><td>"+item2+"</td>"
        for _i in range(multiplier):
            self.table_text = self.table_text + "<td><img src='/images/explanation/green_block_pt7cm.png'></td>"        
        self.table_text = self.table_text + "</tr></table><br>"
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>1 unit = $"+str(price1)+"</div>"
        self.solution_text = self.solution_text + "<div>"+str(multiplier+1)+" units = "+str(multiplier+1)+" x $"+str(price1)+" = $"+str((multiplier-1)*price1)+"</div>"
        self.solution_text = self.solution_text + "<div>Cost of a "+item1+" and a "+item2+" is $"+str((multiplier-1)*price1)+".</div><br>"
        self.solution_text = self.solution_text + "<div>Since "+person1+" bought 2 sets (one for himself and one for " +person2+"),2 x $"+str((multiplier-1)*price1)+" = $"+str(2*(multiplier-1)*price1)+"</div>"
        self.solution_text = self.solution_text + "<div>He paid a total of $"+str(2*(multiplier-1)*price1)+".</div>"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    def GenerateProblemType32(self):
        '''e.g.:Bala bought a jersey and a coat for himself, and another jersey and a coat for John. He paid a total of $200. 
		If each coat cost 3 times as much as a jersey, what was the cost of each jersey?'''
            
        self.PersonNames = random.sample(PersonName.BoyName,2)
        self.ItemPool = {"soft drink-pizza":randint(2,4),"sticker-craft book":randint(2,4),"pencil-notebook":randint(2,3),
                         "pen-letter pad":randint(2,4),"marble-board game":randint(2,5),"plant-flower pot":randint(3,6),
                         "toy car-board game":randint(3,7),"shirt-pair of pants":randint(10,20),"kite-spool":randint(2,4),
                         "flag-key chain":randint(2,4),"thumb drive-printer":randint(20,50),"tie clip-wallet":randint(5,15),
                         "bun-cake":randint(2,4),"cap-racket":randint(10,20),"jersey-coat":randint(15,30)}
        
        self.person1 = self.PersonNames[0]
        self.person2 = self.PersonNames[1]
        self.item = self.ItemPool.keys()[randint(0,len(self.ItemPool)-1)]
        self.item1 = self.item.partition("-")[0]
        self.item2 = self.item.partition("-")[2]
        self.price1 = self.ItemPool[self.item]
        self.multiplier = randint(2,7)
        self.price2 = self.price1 * self.multiplier
        self.TotalAmount = 2*(self.price1 + self.price2)
                
        self.answer = self.price1

        self.problem1 = "%s bought a %s and a %s for himself, and another %s and a %s for %s. He paid a total of $%d. If each %s cost %d times as much as a %s, what was the cost of each %s?"%(self.person1,self.item1,self.item2,self.item1,self.item2,self.person2,self.TotalAmount,self.item2,self.multiplier,self.item1,self.item1)
        self.problem2 = "%s bought a %s and a %s for himself. The %s cost %d times as much as the %s. If he also bought a %s and a %s for %s and spent $%d altogether, find the cost of each %s."%(self.person1,self.item1,self.item2,self.item2,self.multiplier,self.item1,self.item1,self.item2,self.person2,self.TotalAmount,self.item1)
        self.problem3 = "%s paid %d times as much for a %s as for a %s. He purchased a %s and a %s for himself, and another %s and a %s for %s. If he spent a total of $%d, what was the cost of each %s?"%(self.person1,self.multiplier,self.item2,self.item1,self.item1,self.item2,self.item1,self.item2,self.person2,self.TotalAmount,self.item1)
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])
        
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType32(self.problem,self.answer,self.person1,self.person2,self.item1,self.item2,self.price1,self.price2,self.multiplier,self.TotalAmount)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"$",'problem_type':"ProblemType32"}

    def ExplainType32(self,problem,answer,person1,person2,item1,item2,price1,price2,multiplier,TotalAmount):
        self.answer_text = "The correct answer is: <b>$"+str(answer)+"</b>"
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'><tr><td></td><td align='center'>?<br>"
        self.table_text = self.table_text + "<img src='/images/explanation/up_curly_braces_pt7cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td>"+item1+"</td><td><img src='/images/explanation/pink_block_pt7cm.png'></td>"
        for _i in range(multiplier-1):
            self.table_text = self.table_text + "<td></td>"
        self.table_text = self.table_text + "<td align='center' rowspan=2><img src='/images/explanation/right_curly_braces_1cm.png'></td>"
        self.table_text = self.table_text + "<td align='center' rowspan=2>$"+str(TotalAmount)+" &divide; 2</td></tr>"
        self.table_text = self.table_text + "<tr><td>"+item2+"</td>"
        for _i in range(multiplier):
            self.table_text = self.table_text + "<td><img src='/images/explanation/green_block_pt7cm.png'></td>"        
        self.table_text = self.table_text + "</tr></table><br>"
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>Since "+person1+" bought 2 sets (one for himself and one for "+person2+"),$"+str(TotalAmount)+" &divide; 2 = $"+str(TotalAmount/2)+"</div>"
        self.solution_text = self.solution_text + "<div>He spent $"+str(TotalAmount/2)+" for each set.</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(multiplier+1)+" units = $"+str(TotalAmount/2)+"</div>"
        self.solution_text = self.solution_text + "<div>1 unit = $"+str(TotalAmount/2)+" &divide; "+str(multiplier+1)+" = $"+str((TotalAmount/2)/(multiplier+1))+"</div>"
        self.solution_text = self.solution_text + "<div>Each "+item1+" cost $"+str((TotalAmount/2)/(multiplier+1))+".</div>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    '''Problem Type 10 starts here'''
    def GenerateProblemType33(self):
        '''e.g.:Annie pays a monthly instalment of $500 for her car. She also pays a monthly instalment of $1500 for her apartment. 
        	How much money does she pay for her car and apartment in a year?'''
            
        self.person = random.choice(PersonName.GirlName)
        '''The value of key in the dictionary is a list consisting of ExpenseType,Amount1 and Amount2'''
        self.ItemPool = {"health insurance-home insurance":["premium",randint(150,250),randint(300,700)],"gym-tuition":["fees",randint(50,150),randint(160,200)],
                         "utilities-groceries":["bill",randint(100,200),randint(250,350)],"internet-cable":["bill",randint(25,55),randint(60,90)],
                         "car-apartment":["instalment",randint(400,800),randint(850,2000)],"home phone-mobile phone":["bill",randint(10,15),randint(25,60)],
                         "home-office":["rental",randint(1000,2500),randint(2600,4000)]}

        self.item = self.ItemPool.keys()[randint(0,len(self.ItemPool)-1)]
        self.item1 = self.item.partition("-")[0]
        self.item2 = self.item.partition("-")[2]
        self.ExpenseType = self.ItemPool[self.item][0]
        self.amount1 = self.ItemPool[self.item][1]
        self.amount2 = self.ItemPool[self.item][2]
        self.TotalAmount = 12*(self.amount1 + self.amount2)                
        
        self.answer = self.TotalAmount

        self.problem1 = "%s pays a monthly %s of $%d for her %s. She also pays a monthly %s of $%d for her %s. How much money does she pay for her %s and %s in a year?"%(self.person,self.ExpenseType,self.amount1,self.item1,self.ExpenseType,self.amount2,self.item2,self.item1,self.item2)
        self.problem2 = "Each month %s pays a $%d %s for her %s and a $%d %s for her %s. Find the amount of money she pays in a year for her %s and %s."%(self.person,self.amount1,self.ExpenseType,self.item1,self.amount2,self.ExpenseType,self.item2,self.item1,self.item2)
        self.problem3 = "%s pays a monthly %s %s of $%d and monthly %s %s of $%d. How much does she pay for her %s and %s in a year?"%(self.person,self.item1,self.ExpenseType,self.amount1,self.item2,self.ExpenseType,self.amount2,self.item1,self.item2)
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])
        
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType33(self.problem,self.answer,self.person,self.item1,self.item2,self.ExpenseType,self.amount1,self.amount2,self.TotalAmount)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"$",'problem_type':"ProblemType33"}

    def ExplainType33(self,problem,answer,person,item1,item2,ExpenseType,amount1,amount2,TotalAmount):
        self.answer_text = "The correct answer is: <b>$"+str(answer)+"</b>"
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'><tr><td align='center'>$"+str(amount1)+"<br>"
        self.table_text = self.table_text + "<img src='/images/explanation/up_curly_braces_pt7cm.png'></td>"
        self.table_text = self.table_text + "<td align='center'>$"+str(amount2)+"<br>"
        self.table_text = self.table_text + "<img src='/images/explanation/up_curly_braces_1cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td><img src='/images/explanation/pink_block_pt7cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/green_block_1cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td align='center' colspan=2><img src='/images/explanation/down_curly_braces_2cm.png'><br>?</td>"
        self.table_text = self.table_text + "</tr></table><br>"
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(amount1)+" + $"+str(amount2)+" = $"+str(amount1+amount2)+"</div>"
        self.solution_text = self.solution_text + "<div>"+person+" pays $"+str(amount1+amount2)+" for her "+item1+" and "+item2+" each month.</div><br>"
        self.solution_text = self.solution_text + "<div>12 x $"+str(amount1+amount2)+" = $"+str(12*(amount1+amount2))+"</div>"
        self.solution_text = self.solution_text + "<div>"+person+" pays $"+str(12*(amount1+amount2))+" for her "+item1+" and "+item2+" in a year.</div>"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    def GenerateProblemType34(self):
        '''e.g.:Annie pays monthly instalments  for  her  car and apartment. She pays $24000 a year for her car and apartment together. 
        	If she pays a monthly instalment of $500 for her car, how much does she pay for her apartment each month?'''
            
        self.person = random.choice(PersonName.GirlName)
        '''The value of key in the dictionary is a list consisting of ExpenseType,Amount1 and Amount2'''
        self.ItemPool = {"health insurance-home insurance":["premium",randint(150,250),randint(300,700)],"gym-tuition":["fees",randint(50,150),randint(160,200)],
                         "utilities-groceries":["bill",randint(100,200),randint(250,350)],"internet-cable":["charge",randint(25,55),randint(60,90)],
                         "car-apartment":["instalment",randint(400,800),randint(850,2000)],"home phone-mobile phone":["bill",randint(10,15),randint(25,60)],
                         "home-office":["rental",randint(1000,2500),randint(2600,4000)]}

        self.item = self.ItemPool.keys()[randint(0,len(self.ItemPool)-1)]
        self.item1 = self.item.partition("-")[0]
        self.item2 = self.item.partition("-")[2]
        self.ExpenseType = self.ItemPool[self.item][0]
        self.amount1 = self.ItemPool[self.item][1]
        self.amount2 = self.ItemPool[self.item][2]
        self.TotalAmount = 12*(self.amount1 + self.amount2)                
        
        self.answer = self.amount2

        self.problem1 = "%s pays monthly %ss for her %s and %s. She pays $%d a year for her %s and %s together. If she pays a monthly %s of $%d for her %s, how much does she pay for her %s each month?"%(self.person,self.ExpenseType,self.item1,self.item2,self.TotalAmount,self.item1,self.item2,self.ExpenseType,self.amount1,self.item1,self.item2)
        self.problem2 = "Each month %s pays %ss for her %s and %s. If she pays $%d a month for her %s and $%d a year for her %s and %s together, find the amount of money she pays for her %s each month."%(self.person,self.ExpenseType,self.item1,self.item2,self.amount1,self.item1,self.TotalAmount,self.item1,self.item2,self.item2)
        self.problem3 = "%s pays monthly %ss for her %s and %s. If she pays a monthly %s of $%d for her %s, and $%d a year for her %s and %s together, how much does she pay for her %s each month?"%(self.person,self.ExpenseType,self.item1,self.item2,self.ExpenseType,self.amount1,self.item1,self.TotalAmount,self.item1,self.item2,self.item2)
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])
        
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType34(self.problem,self.answer,self.person,self.item1,self.item2,self.ExpenseType,self.amount1,self.amount2,self.TotalAmount)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"$",'problem_type':"ProblemType34"}

    def ExplainType34(self,problem,answer,person,item1,item2,ExpenseType,amount1,amount2,TotalAmount):
        self.answer_text = "The correct answer is: <b>$"+str(answer)+"</b>"
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'><tr><td align='center'>$"+str(amount1)+"<br>"
        self.table_text = self.table_text + "<img src='/images/explanation/up_curly_braces_pt7cm.png'></td>"
        self.table_text = self.table_text + "<td align='center'>?<br>"
        self.table_text = self.table_text + "<img src='/images/explanation/up_curly_braces_1cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td align='center'><img src='/images/explanation/pink_block_pt7cm.png'></td>"
        self.table_text = self.table_text + "<td align='center'><img src='/images/explanation/green_block_1cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td align='center' colspan=2><img src='/images/explanation/down_curly_braces_2cm.png'><br>"
        self.table_text = self.table_text + "$"+str(TotalAmount)+"&divide;12 months</td>"
        self.table_text = self.table_text + "</tr></table><br>"
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(TotalAmount)+" &divide; 12 months = $"+str(TotalAmount/12)+"</div>"
        self.solution_text = self.solution_text + "<div>"+person+" pays $"+str(TotalAmount/12)+" for her "+item1+" and "+item2+" each month.</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(TotalAmount/12)+" - $"+str(amount1)+" = $"+str(TotalAmount/12-amount1)+"</div>"
        self.solution_text = self.solution_text + "<div>"+person+" pays $"+str(TotalAmount/12-amount1)+" for her "+item2+" each month.</div>"
        self.solution_text = self.solution_text + "<br><div> Watch below video for explanation of similar problem<br>"
        VideoLink = '<object><param name="movie" value="https://www.youtube.com/v/u1zgFlCw8Aw?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded"><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "md895QiA5Qw";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
       
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    '''Problem Type 11 starts here'''
    def GenerateProblemType35(self):
        '''e.g.:The normal price of a blouse is $24. In a fashion store promotion Annie buys 2 blouses and gets 1 free. 
        	How much does each blouse cost her in this promotion?'''
            
        self.person = random.choice(PersonName.BoyName)
        '''Making sure, price of each item is perfectly divisible by 3'''
        self.ItemPool = {"plant nursery":[["pot","plant"],random.randrange(3,9,3)],"grocery store":[["canned soup","shampoo bottle","pineapple","pumpkin"],random.randrange(3,9,3)],
                         "department store":[["perfume bottle","ring"],random.randrange(48,200,3)],"furniture store":[["chair"],random.randrange(15,40,3)],
                         "electronics shop":[["headphone"],random.randrange(15,40,3)],"fashion store":[["handbag","shirt","T-shirt","neck tie"],random.randrange(15,50,3)],
                         "computer shop":[["DVD pack","flash drive",],random.randrange(21,50,3)],"bakery":[["muffin","cup cake"],random.randrange(3,9,3)],
                         "book store":[["notebook","pen"],random.randrange(3,9,3)],"toy shop":[["ball","toy car","hula hoop"],random.randrange(3,12,3)],
                         "fast food joints":[["burger"],random.randrange(3,9,3)],"office supplies store":[["printer catridge"],random.randrange(21,40,3)],
                         "supermarket":[["pasta packet","rice bag","oil can"],random.randrange(3,9,3)],"art museum":[["painting"],random.randrange(24,100,3)]}

        self.StoreType = self.ItemPool.keys()[randint(0,len(self.ItemPool)-1)]
        self.item = random.choice(self.ItemPool[self.StoreType][0])
        self.BuyNumber = 2
        self.FreeNumber = 1
        self.UP = self.ItemPool[self.StoreType][1]
        self.ActualPrice = (self.UP*self.BuyNumber)/(self.BuyNumber+self.FreeNumber)              
        
        self.answer = self.ActualPrice

        self.problem1 = "The normal price of a %s is $%d. In a %s promotion %s buys 2 %ss and gets 1 free. How much does each %s cost him in this promotion?"%(self.item,self.UP,self.StoreType,self.person,self.item,self.item)
        self.problem2 = "A %s is having a promotion on %ss, in which %s buys 2 at a price of $%d each and gets 1 free.  How much does each %s cost him after promotion?"%(self.StoreType,self.item,self.person,self.UP,self.item)
        self.problem3 = "%s buys 2 %ss and gets 1 free in a promotion. If the normal price of each %s is $%d, find the amount that each %s costs him in this promotion?"%(self.person,self.item,self.item,self.UP,self.item)
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])
        
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType35(self.problem,self.answer,self.person,self.item,self.StoreType,self.UP)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"$",'problem_type':"ProblemType35"}

    def ExplainType35(self,problem,answer,person,item,StoreType,UP):
        self.answer_text = "The correct answer is: <b>$"+str(answer)+"</b>"
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'><tr><td></td><td align='center'>$"+str(UP)+"<br>"
        self.table_text = self.table_text + "<img src='/images/explanation/up_curly_braces_pt7cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td>"+item+"</td><td><img src='/images/explanation/pink_block_pt7cm.png'</td>"
        self.table_text = self.table_text + "<td rowspan=2><img src='/images/explanation/right_curly_braces_1cm.png'></td>"
        self.table_text = self.table_text + "<td rowspan=2>?</td></tr>"
        self.table_text = self.table_text + "<tr><td>"+item+"</td><td><img src='/images/explanation/pink_block_pt7cm.png'</td></tr>"
        self.table_text = self.table_text + "<tr><td>Free "+item+"</td><td><img src='/images/explanation/green_block_pt7cm.png'</td>"
        self.table_text = self.table_text + "</tr></table><br>"
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>2 "+item+"s x $"+str(UP)+" = $"+str(2*UP)+"</div>"
        self.solution_text = self.solution_text + "<div>"+person+" pays $"+str(2*UP)+" for 3 "+item+"s in the promotion.</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(2*UP)+" &divide; 3 "+item+"s = $"+str(2*UP/3)+"</div>"
        self.solution_text = self.solution_text + "<div>Each "+item+" costs him $"+str(2*UP/3)+" in this promotion.</div>"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    def GenerateProblemType36(self):
        '''e.g.:The normal price of a blouse is $24. A fashion store is having a  promotion in which Annie buys 2 blouses and gets 1 free. 
        	How much less than the normal price does each blouse cost her in this promotion?'''
            
        self.person = random.choice(PersonName.BoyName)
        '''Making sure, price of each item is perfectly divisible by 3'''
        self.ItemPool = {"plant nursery":[["pot","plant"],random.randrange(3,9,3)],"grocery store":[["canned soup","shampoo bottle","pineapple","pumpkin"],random.randrange(3,9,3)],
                         "department store":[["perfume bottle","ring"],random.randrange(48,200,3)],"furniture store":[["chair"],random.randrange(15,40,3)],
                         "electronics shop":[["headphone"],random.randrange(15,40,3)],"fashion store":[["handbag","shirt","T-shirt","neck tie"],random.randrange(15,50,3)],
                         "computer shop":[["DVD pack","flash drive",],random.randrange(21,50,3)],"bakery":[["muffin","cup cake"],random.randrange(3,9,3)],
                         "book store":[["notebook","pen"],random.randrange(3,9,3)],"toy shop":[["ball","toy car","hula hoop"],random.randrange(3,12,3)],
                         "fast food joints":[["burger"],random.randrange(3,9,3)],"office supplies store":[["printer catridge"],random.randrange(21,40,3)],
                         "supermarket":[["pasta packet","rice bag","oil can"],random.randrange(3,9,3)],"art museum":[["painting"],random.randrange(24,100,3)]}

        self.StoreType = self.ItemPool.keys()[randint(0,len(self.ItemPool)-1)]
        self.item = random.choice(self.ItemPool[self.StoreType][0])
        self.BuyNumber = 2
        self.FreeNumber = 1
        self.UP = self.ItemPool[self.StoreType][1]
        self.ActualPrice = (self.UP*self.BuyNumber)/(self.BuyNumber+self.FreeNumber)
        self.diff = self.UP - self.ActualPrice
        
        self.answer = self.diff

        self.problem1 = "The normal price of a %s is $%d. A %s is having a promotion in which %s buys 2 %s and gets 1 free. How much less than the normal price does each %s cost him in this promotion?"%(self.item,self.UP,self.StoreType,self.person,self.item,self.item)
        self.problem2 = "In a %s promotion, if %s buys 2 %ss priced at $%d each and gets 1 free, how much less than the normal price does each %s cost him in this promotion?"%(self.StoreType,self.person,self.item,self.UP,self.item)
        self.problem3 = "%s buys 2 %ss and gets 1 free in a %s promotion. If the normal price of each %s is $%d, how much less than the normal price does each %s cost her in this promotion?"%(self.person,self.item,self.StoreType,self.item,self.UP,self.item)
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])
        
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType36(self.problem,self.answer,self.person,self.item,self.StoreType,self.UP,self.diff)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"$",'problem_type':"ProblemType36"}

    def ExplainType36(self,problem,answer,person,item,StoreType,UP,diff):
        self.answer_text = "The correct answer is: <b>$"+str(answer)+"</b>"
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'><tr><td></td><td align='center'>$"+str(UP)+"<br>"
        self.table_text = self.table_text + "<img src='/images/explanation/up_curly_braces_pt7cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td>"+item+"</td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/pink_block_pt7cm.png'</td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/yellow_block_pt4cm.png'</td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/pink_block_pt7cm.png'</td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/yellow_block_pt4cm.png'</td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/pink_block_pt7cm.png'</td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/yellow_block_pt4cm.png'</td></tr>"
        self.table_text = self.table_text + "<tr><td></td><td></td><td align='center'><img src='/images/explanation/down_curly_braces_pt4cm.png'><br>?</td>"
        self.table_text = self.table_text + "</tr></table><br>"
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>2 "+item+"s x $"+str(UP)+" = $"+str(2*UP)+"</div>"
        self.solution_text = self.solution_text + "<div>"+person+" pays $"+str(2*UP)+" for 3 "+item+"s in the promotion.</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(2*UP)+" &divide; 3 "+item+"s = $"+str(2*UP/3)+"</div>"
        self.solution_text = self.solution_text + "<div>Each "+item+" costs him $"+str(2*UP/3)+" in this promotion.</div>"
        self.solution_text = self.solution_text + "<div>$"+str(UP)+" - $"+str(2*UP/3)+" = $"+str(UP-2*UP/3)+"</div>"
        self.solution_text = self.solution_text + "<div>Each "+item+" cost him $"+str(UP-2*UP/3)+" less than the normal price in this promotion.</div>"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    def GenerateProblemType37(self):
        '''e.g.:The normal price of a blouse is $24. A fashion store is having a  promotion in which Annie buys 2 blouses and gets 1 free. 
        	How much less than the normal price does each blouse cost her in this promotion?'''
            
        self.person = random.choice(PersonName.BoyName)
        '''Making sure, price of each item is perfectly divisible by 3'''
        self.ItemPool = {"plant nursery":[["pot","plant"],random.randrange(3,9,3)],"grocery store":[["canned soup","shampoo bottle","pineapple","pumpkin"],random.randrange(3,9,3)],
                         "department store":[["perfume bottle","ring"],random.randrange(48,200,3)],"furniture store":[["chair"],random.randrange(15,40,3)],
                         "electronics shop":[["headphone"],random.randrange(15,40,3)],"fashion store":[["handbag","shirt","T-shirt","neck tie"],random.randrange(15,50,3)],
                         "computer shop":[["DVD pack","flash drive",],random.randrange(21,50,3)],"bakery":[["muffin","cup cake"],random.randrange(3,9,3)],
                         "book store":[["notebook","pen"],random.randrange(3,9,3)],"toy shop":[["ball","toy car","hula hoop"],random.randrange(3,12,3)],
                         "fast food joints":[["burger"],random.randrange(3,9,3)],"office supplies store":[["printer catridge"],random.randrange(21,40,3)],
                         "supermarket":[["pasta packet","rice bag","oil can"],random.randrange(3,9,3)],"art museum":[["painting"],random.randrange(24,100,3)]}

        self.StoreType = self.ItemPool.keys()[randint(0,len(self.ItemPool)-1)]
        self.item = random.choice(self.ItemPool[self.StoreType][0])
        self.BuyNumber = 2
        self.FreeNumber = 1
        self.UP = self.ItemPool[self.StoreType][1]
        self.ActualPrice = (self.UP*self.BuyNumber)/(self.BuyNumber+self.FreeNumber)
        self.diff = self.UP - self.ActualPrice
        
        self.answer = self.diff

        self.problem1 = "The normal price of a %s is $%d. A %s is having a promotion in which %s buys 2 %s and gets 1 free. How much did he save on each %s in this promotion?"%(self.item,self.UP,self.StoreType,self.person,self.item,self.item)
        self.problem2 = "In a %s promotion, if %s buys 2 %ss priced at $%d each and gets 1 free, how much did he save on each %s in this promotion?"%(self.StoreType,self.person,self.item,self.UP,self.item)
        self.problem3 = "%s buys 2 %ss and gets 1 free in a %s promotion. If the normal price of each %s is $%d, how much did he save on each %s in this promotion?"%(self.person,self.item,self.StoreType,self.item,self.UP,self.item)
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])
        
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType37(self.problem,self.answer,self.person,self.item,self.StoreType,self.UP,self.diff)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"$",'problem_type':"ProblemType37"}

    def ExplainType37(self,problem,answer,person,item,StoreType,UP,diff):
        self.answer_text = "The correct answer is: <b>$"+str(answer)+"</b>"
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'><tr><td></td><td align='center'>$"+str(UP)+"<br>"
        self.table_text = self.table_text + "<img src='/images/explanation/up_curly_braces_pt7cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td>"+item+"</td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/pink_block_pt7cm.png'</td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/yellow_block_pt4cm.png'</td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/pink_block_pt7cm.png'</td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/yellow_block_pt4cm.png'</td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/pink_block_pt7cm.png'</td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/yellow_block_pt4cm.png'</td></tr>"
        self.table_text = self.table_text + "<tr><td></td><td></td><td align='center'><img src='/images/explanation/down_curly_braces_pt4cm.png'><br>?</td>"
        self.table_text = self.table_text + "</tr></table><br>"
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>2 "+item+"s x $"+str(UP)+" = $"+str(2*UP)+"</div>"
        self.solution_text = self.solution_text + "<div>"+person+" pays $"+str(2*UP)+" for 3 "+item+"s in the promotion.</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(2*UP)+" &divide; 3 "+item+"s = $"+str(2*UP/3)+"</div>"
        self.solution_text = self.solution_text + "<div>Each "+item+" costs him $"+str(2*UP/3)+" in this promotion.</div>"
        self.solution_text = self.solution_text + "<div>$"+str(UP)+" - $"+str(2*UP/3)+" = $"+str(UP-2*UP/3)+"</div>"
        self.solution_text = self.solution_text + "<div>"+person+" saved $"+str(UP-2*UP/3)+" on each "+item+" in this promotion.</div>"
        self.solution_text = self.solution_text + "<br><div> Watch below video for explanation of similar problem<br>"
        VideoLink = '<object><param name="movie" value="https://www.youtube.com/v/u1zgFlCw8Aw?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded"><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "B1fdOXD7W9I";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    '''Problem type 12 starts here'''
    def GenerateProblemType38(self):
        '''e.g.:The usual price of a blouse is $24. A fashion store is having a 'buy 2 get 3rd at $12 off' 
        	promotion on blouses. If Annie buys 9 blouses, how much does she pay altogether?'''
            
        self.person = random.choice(PersonName.GirlName)
        '''Making sure, price of each item is perfectly divisible by 3'''
        self.ItemPool = {"plant nursery":[["pot","plant"],random.randrange(3,9,3)],"grocery store":[["canned soup","shampoo bottle","pineapple","pumpkin"],random.randrange(3,9,3)],
                         "department store":[["perfume bottle","ring"],random.randrange(48,200,3)],"furniture store":[["chair"],random.randrange(15,40,3)],
                         "electronics shop":[["headphone"],random.randrange(15,40,3)],"fashion store":[["handbag","shirt","T-shirt","blouse"],random.randrange(15,50,3)],
                         "computer shop":[["DVD pack","flash drive",],random.randrange(21,50,3)],"bakery":[["muffin","cup cake"],random.randrange(3,9,3)],
                         "book store":[["notebook","pen"],random.randrange(3,9,3)],"toy shop":[["ball","toy car","hula hoop"],random.randrange(3,12,3)],
                         "fast food joints":[["burger"],random.randrange(3,9,3)],"office supplies store":[["printer catridge"],random.randrange(21,40,3)],
                         "supermarket":[["pasta packet","rice bag","oil can"],random.randrange(3,9,3)],"art museum":[["painting"],random.randrange(24,100,3)]}

        self.StoreType = self.ItemPool.keys()[randint(0,len(self.ItemPool)-1)]
        self.item = random.choice(self.ItemPool[self.StoreType][0])
        self.BuyNumber = random.randrange(6,12,3)
        self.UP = self.ItemPool[self.StoreType][1]
        self.discount = randint(int(self.UP*.25),int(self.UP*.75))
        self.TotalSpent = ((2*self.BuyNumber)*self.UP/3)+(self.BuyNumber*(self.UP-self.discount)/3)
        
        self.answer = self.TotalSpent

        self.problem1 = "The usual price of a %s is $%d. A %s is having a 'buy 2 get 3rd at $%d off' promotion on %ss. If %s buys %d %ss, how much does she pay altogether?"%(self.item,self.UP,self.StoreType,self.discount,self.item,self.person,self.BuyNumber,self.item)
        self.problem2 = "A %s is having a 'buy 2 get 3rd at $%d off' promotion on %ss. If %s buys %d %ss usually priced at $%d each, how much does she pay altogether?"%(self.StoreType,self.discount,self.item,self.person,self.BuyNumber,self.item,self.UP)
        self.problem3 = "%s buys %d %ss in a 'buy 2 get 3rd at $%d off' promotion. If the usual price of each %s is $%d, find the amount that %s pays altogether?"%(self.person,self.BuyNumber,self.item,self.discount,self.item,self.UP,self.person)
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])
        
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType38(self.problem,self.answer,self.person,self.item,self.BuyNumber,self.StoreType,self.UP,self.discount,self.TotalSpent)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"$",'problem_type':"ProblemType38"}

    def ExplainType38(self,problem,answer,person,item,BuyNumber,StoreType,UP,discount,TotalSpent):
        self.answer_text = "The correct answer is: <b>$"+str(answer)+"</b>"
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'><tr><td></td><td align='center'>$"+str(UP)+"<br>"
        self.table_text = self.table_text + "<img src='/images/explanation/up_curly_braces_1cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td>"+item+"1</td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/pink_block_1cm.png'</td>"
        self.table_text = self.table_text + "<td rowspan=3 align='center'><img src='/images/explanation/right_curly_braces_1cm.png'></td>"
        self.table_text = self.table_text + "<td rowspan=3 align='center'>?</td></tr>"
        self.table_text = self.table_text + "<tr><td>"+item+"2</td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/pink_block_1cm.png'</td>"
        self.table_text = self.table_text + "<tr><td>"+item+"3</td>"
        self.table_text = self.table_text + "<td align='center'><img src='/images/explanation/green_block_pt7cm.png'</td></tr>"
        self.table_text = self.table_text + "<tr><td></td><td align='center'><img src='/images/explanation/down_curly_braces_pt7cm.png'><br>"
        self.table_text = self.table_text + "$"+str(UP)+"-$"+str(discount)+"</td>"
        self.table_text = self.table_text + "</tr></table><br>"
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(UP)+" - $"+str(discount)+" = $"+str(UP-discount)+"</div>"
        self.solution_text = self.solution_text + "<div>Cost of 3rd "+item+" is $"+str(UP-discount)+".</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(UP)+" + $"+str(UP)+" + $"+str(UP)+" - $"+str(UP-discount)+" = $"+str(3*UP-discount)+"</div>"
        self.solution_text = self.solution_text + "<div>Each set of 3 "+item+"s costs $"+str(3*UP-discount)+".</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(BuyNumber)+" "+item+"s &divide; 3 "+item+"s = "+str(BuyNumber/3)+" sets</div>"
        self.solution_text = self.solution_text + "<div>"+str(BuyNumber)+" "+item+"s mean "+str(BuyNumber/3)+" sets of 3 "+item+"s each.</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(3*UP-discount)+" x "+str(BuyNumber/3)+" sets = $"+str((3*UP-discount)*(BuyNumber/3))+"</div>"
        self.solution_text = self.solution_text + "<div>"+person+" pays $"+str((3*UP-discount)*(BuyNumber/3))+" altogether.</div>"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    def GenerateProblemType39(self):
        '''e.g.:The usual price of a blouse is $24. A fashion store is having a 'buy 2 get 3rd at $12 off'
        	promotion on blouses. If Annie buys 9 blouses, how much does each blouse cost her in this promotion?'''
            
        self.person = random.choice(PersonName.GirlName)
        '''Making sure, price of each item is perfectly divisible by 3'''
        self.ItemPool = {"plant nursery":[["pot","plant"],random.randrange(3,9,3)],"grocery store":[["canned soup","shampoo bottle","pineapple","pumpkin"],random.randrange(3,9,3)],
                         "department store":[["perfume bottle","ring"],random.randrange(48,200,3)],"furniture store":[["chair"],random.randrange(15,40,3)],
                         "electronics shop":[["headphone"],random.randrange(15,40,3)],"fashion store":[["handbag","shirt","T-shirt","blouse"],random.randrange(15,50,3)],
                         "computer shop":[["DVD pack","flash drive",],random.randrange(21,50,3)],"bakery":[["muffin","cup cake"],random.randrange(3,9,3)],
                         "book store":[["notebook","pen"],random.randrange(3,9,3)],"toy shop":[["ball","toy car","hula hoop"],random.randrange(3,12,3)],
                         "fast food joints":[["burger"],random.randrange(3,9,3)],"office supplies store":[["printer catridge"],random.randrange(21,40,3)],
                         "supermarket":[["pasta packet","rice bag","oil can"],random.randrange(3,9,3)],"art museum":[["painting"],random.randrange(24,100,3)]}

        self.StoreType = self.ItemPool.keys()[randint(0,len(self.ItemPool)-1)]
        self.item = random.choice(self.ItemPool[self.StoreType][0])
        self.BuyNumber = random.randrange(6,12,3)
        self.UP = self.ItemPool[self.StoreType][1]
        self.discount = randint(int(self.UP*.25),int(self.UP*.75))
        self.TotalSpent = ((2*self.BuyNumber)*self.UP/3)+(self.BuyNumber*(self.UP-self.discount)/3)
        
        self.answer = self.TotalSpent/self.BuyNumber

        self.problem1 = "The usual price of a %s is $%d. A %s is having a 'buy 2 get 3rd at $%d off' promotion on %ss. If %s buys %d %ss, how much does each %s cost her in the promotion?"%(self.item,self.UP,self.StoreType,self.discount,self.item,self.person,self.BuyNumber,self.item,self.item)
        self.problem2 = "A %s is having a 'buy 2 get 3rd at $%d off' promotion on %ss. If %s buys %d %ss usually priced at $%d each, how much does each %s cost her in the promotion?"%(self.StoreType,self.discount,self.item,self.person,self.BuyNumber,self.item,self.UP,self.item)
        self.problem3 = "%s buys %d %ss in a 'buy 2 get 3rd at $%d off' promotion. If the usual price of each %s is $%d, find the amount that each %s cost her in this promotion?"%(self.person,self.BuyNumber,self.item,self.discount,self.item,self.UP,self.item)
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])
        
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType39(self.problem,self.answer,self.person,self.item,self.BuyNumber,self.StoreType,self.UP,self.discount,self.TotalSpent)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"$",'problem_type':"ProblemType39"}

    def ExplainType39(self,problem,answer,person,item,BuyNumber,StoreType,UP,discount,TotalSpent):
        self.answer_text = "The correct answer is: <b>$"+str(answer)+"</b>"
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'><tr><td></td><td align='center'>$"+str(UP)+"<br>"
        self.table_text = self.table_text + "<img src='/images/explanation/up_curly_braces_1cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td>"+item+"1</td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/pink_block_1cm.png'</td>"
        self.table_text = self.table_text + "<td rowspan=3 align='center'><img src='/images/explanation/right_curly_braces_1cm.png'></td>"
        self.table_text = self.table_text + "<td rowspan=3 align='center'>?</td></tr>"
        self.table_text = self.table_text + "<tr><td>"+item+"2</td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/pink_block_1cm.png'</td></tr>"
        self.table_text = self.table_text + "<tr><td>"+item+"3</td>"
        self.table_text = self.table_text + "<td align='center'><img src='/images/explanation/green_block_pt7cm.png'</td></tr>"
        self.table_text = self.table_text + "<tr><td></td><td align='center'><img src='/images/explanation/down_curly_braces_pt7cm.png'><br>"
        self.table_text = self.table_text + "$"+str(UP)+"-$"+str(discount)+"</td>"
        self.table_text = self.table_text + "</tr></table><br>"
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(UP)+" - $"+str(discount)+" = $"+str(UP-discount)+"</div>"
        self.solution_text = self.solution_text + "<div>Cost of 3rd "+item+" is $"+str(UP-discount)+".</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(UP)+" + $"+str(UP)+" + $"+str(UP)+" - $"+str(UP-discount)+" = $"+str(3*UP-discount)+"</div>"
        self.solution_text = self.solution_text + "<div>Each set of 3 "+item+"s costs $"+str(3*UP-discount)+".</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(BuyNumber)+" "+item+"s &divide; 3 "+item+"s = "+str(BuyNumber/3)+" sets</div>"
        self.solution_text = self.solution_text + "<div>"+str(BuyNumber)+" "+item+"s mean "+str(BuyNumber/3)+" sets of 3 "+item+"s each.</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(3*UP-discount)+" x "+str(BuyNumber/3)+" sets = $"+str((3*UP-discount)*(BuyNumber/3))+"</div>"
        self.solution_text = self.solution_text + "<div>"+person+" pays $"+str((3*UP-discount)*(BuyNumber/3))+" altogether.</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str((3*UP-discount)*(BuyNumber/3))+" &divide; "+str(BuyNumber)+" "+item+"s = $"+str(((3*UP-discount)*(BuyNumber/3))/BuyNumber)+"</div>"
        self.solution_text = self.solution_text + "<div>Each "+item+" costs her $"+str(((3*UP-discount)*(BuyNumber/3))/BuyNumber)+" in this promotion.</div>"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    '''Problem type 13 starts here'''
    def GenerateProblemType40(self):
        '''e.g.:123 nations are participating in a cycling championship. Each nation sends 12 contestants and 2 coaches. 
        	How many contestants and coaches attend the cycling championship altogether?'''

        self.ItemPool = {"school":["quiz contest","pupils","teachers"],"nation":["cycling championship","contestants","coaches"],
                         "corporation":["trade conference","managers","secretaries"],"college":["training camp","students","lecturers"],
                         "fashion house":["fashion show","models","designers"],"travel agent":["travel fair","salespersons","travel specialists"],
                         "restaurant":["food festival","salespersons","chefs"],"team":["swimming tournament","swimmers","coaches"],
                         "art school":["art exhibition","artists","assistants"],"IT manufacturer":["IT fair","salespersons","supervisors"],
                         "state":["world peace conference","deputy ministers","ministers"],"car manufacturer":["car show","salespersons","engineers"]
                         }
        self.item = self.ItemPool.keys()[randint(0,len(self.ItemPool)-1)]
        self.event = self.ItemPool[self.item][0]
        self.grade1 = self.ItemPool[self.item][1]
        self.grade2 = self.ItemPool[self.item][2]
        self.number1 = randint(50,100)
        self.number2 = randint(5,12)
        self.number3 = randint(2,4)
        self.total = self.number1*(self.number2+self.number3)

        self.answer = self.total

        self.problem1 = "%d %ss are participating in a %s. Each %s sends %d %s and %d %s. How many %s and %s attend the %s altogether?"%(self.number1,self.item,self.event,self.item,self.number2,self.grade1,self.number3,self.grade2,self.grade1,self.grade2,self.event)
        self.problem2 = "%d %ss are taking part in a %s. If each %s sends %d %s and %d %s, how many %s and %s attend the %s altogether?"%(self.number1,self.item,self.event,self.item,self.number2,self.grade1,self.number3,self.grade2,self.grade1,self.grade2,self.event)
        self.problem3 = "Each %s is sending %d %s and %d %s to a %s. If there are %d %ss participating in the %s, how many %s and %s are present altogether?"%(self.item,self.number2,self.grade1,self.number3,self.grade2,self.event,self.number1,self.item,self.event,self.grade1,self.grade2)
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])
        
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType40(self.problem,self.answer,self.item,self.event,self.grade1,self.grade2,self.number1,self.number2,self.number3,self.total)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"",'problem_type':"ProblemType40"}

    def ExplainType40(self,problem,answer,item,event,grade1,grade2,number1,number2,number3,total):
        self.answer_text = "The correct answer is: <b>"+str(answer)+"</b>"
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'><tr><td align='center'>"+str(number2)+"<br>"
        self.table_text = self.table_text + "<img src='/images/explanation/up_curly_braces_3cm.png'></td>"
        self.table_text = self.table_text + "<td align='center'>"+str(number3)+"<br>"
        self.table_text = self.table_text + "<img src='/images/explanation/up_curly_braces_1cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td align='center'><img src='/images/explanation/pink_block_3cm.png'></td>"
        self.table_text = self.table_text + "<td align='cente'><img src='/images/explanation/green_block_1cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td colspan=2 align='center'><img src='/images/explanation/down_curly_braces_3cm.png' width=240><br>"
        self.table_text = self.table_text + "?(# of people from each "+item+")</td>"
        self.table_text = self.table_text + "</tr></table><br>"
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(number2)+" "+grade1+" + "+str(number3)+" "+grade2+" = "+str(number2+number3)+" people</div>"
        self.solution_text = self.solution_text + "<div>Each "+item+" sends "+str(number2+number3)+" people to the "+event+".</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(number1)+" "+item+"s x "+str(number2+number3)+" people ="+str(number1*(number2+number3))+" people</div>"
        self.solution_text = self.solution_text + "<div>"+str(number1*(number2+number3))+" "+grade1+" and "+grade2+" attend the "+event+" altogether.</div>"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    def GenerateProblemType41(self):
        '''e.g.:Some nations are participating in a cycling championship. Each nation sends 12 contestants and 2 coaches. If the total number of 
        	contestants and coaches present is 1722, how many nations are participating in the cycling championship?'''

        self.ItemPool = {"school":["quiz contest","pupils","teachers"],"nation":["cycling championship","contestants","coaches"],
                         "corporation":["trade conference","managers","secretaries"],"college":["training camp","students","lecturers"],
                         "fashion house":["fashion show","models","designers"],"travel agent":["travel fair","salespersons","travel specialists"],
                         "restaurant":["food festival","salespersons","chefs"],"team":["swimming tournament","swimmers","coaches"],
                         "art school":["art exhibition","artists","assistants"],"IT manufacturer":["IT fair","salespersons","supervisors"],
                         "state":["world peace conference","deputy ministers","ministers"],"car manufacturer":["car show","salespersons","engineers"]
                         }
        self.item = self.ItemPool.keys()[randint(0,len(self.ItemPool)-1)]
        self.event = self.ItemPool[self.item][0]
        self.grade1 = self.ItemPool[self.item][1]
        self.grade2 = self.ItemPool[self.item][2]
        self.number1 = randint(50,100)
        self.number2 = randint(5,12)
        self.number3 = randint(2,4)
        self.total = self.number1*(self.number2+self.number3)

        self.answer = self.number1

        self.problem1 = "Some %ss are participating in a %s. Each %s sends %d %s and %d %s. If the total number of %s and %s present is %d, how many %ss are participating in the %s?"%(self.item,self.event,self.item,self.number2,self.grade1,self.number3,self.grade2,self.grade1,self.grade2,self.total,self.item,self.event)
        self.problem2 = "Some %ss are taking part in a %s. If each %s sends %d %s and %d %s, and there are %d %s and %s altogether, find the number of %ss participating in the %s."%(self.item,self.event,self.item,self.number2,self.grade1,self.number3,self.grade2,self.total,self.grade1,self.grade2,self.item,self.event)
        self.problem3 = "Each %s is sending %d %s and %d %s to a %s. If there are %d %s and %s present altogether, how many %ss are participating in the %s?"%(self.item,self.number2,self.grade1,self.number3,self.grade2,self.event,self.total,self.grade1,self.grade2,self.item,self.event)
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])
        
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType41(self.problem,self.answer,self.item,self.event,self.grade1,self.grade2,self.number1,self.number2,self.number3,self.total)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"",'problem_type':"ProblemType41"}

    def ExplainType41(self,problem,answer,item,event,grade1,grade2,number1,number2,number3,total):
        self.answer_text = "The correct answer is: <b>"+str(answer)+"</b>"
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'><tr><td align='center'>"+str(number2)+"<br>"
        self.table_text = self.table_text + "<img src='/images/explanation/up_curly_braces_3cm.png'></td>"
        self.table_text = self.table_text + "<td align='center'>"+str(number3)+"<br>"
        self.table_text = self.table_text + "<img src='/images/explanation/up_curly_braces_1cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td align='center'><img src='/images/explanation/pink_block_3cm.png'></td>"
        self.table_text = self.table_text + "<td align='center'><img src='/images/explanation/green_block_1cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td colspan=2 align='center'><img src='/images/explanation/down_curly_braces_3cm.png' width=240><br>"
        self.table_text = self.table_text + "?(# of people from each "+item+")</td>"
        self.table_text = self.table_text + "</tr></table><br>"
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(number2)+" "+grade1+" + "+str(number3)+" "+grade2+" = "+str(number2+number3)+" people</div>"
        self.solution_text = self.solution_text + "<div>Each "+item+" sends "+str(number2+number3)+" people to the "+event+".</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(total)+" people &divide; "+str(number2+number3)+" people = "+str(total/(number2+number3))+" "+item+"s</div>"
        self.solution_text = self.solution_text + "<div>"+str(total/(number2+number3))+" "+item+" are participating in the "+event+".</div>"
    
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    def GenerateProblemType42(self):
        '''e.g.:123 nations are participating in a cycling championship. Each nation sends 12 contestants and some coaches. If each nation sends the same number of coaches, 
                    and the total number of contestants and coaches attending the cycling championship is 1722, find the number of coaches that each nation sends?'''

        self.ItemPool = {"school":["quiz contest","pupils","teachers"],"nation":["cycling championship","contestants","coaches"],
                         "corporation":["trade conference","managers","secretaries"],"college":["training camp","students","lecturers"],
                         "fashion house":["fashion show","models","designers"],"travel agent":["travel fair","salespersons","travel specialists"],
                         "restaurant":["food festival","salespersons","chefs"],"team":["swimming tournament","swimmers","coaches"],
                         "art school":["art exhibition","artists","assistants"],"IT manufacturer":["IT fair","salespersons","supervisors"],
                         "state":["world peace conference","deputy ministers","ministers"],"car manufacturer":["car show","salespersons","engineers"]
                         }
        self.item = self.ItemPool.keys()[randint(0,len(self.ItemPool)-1)]
        self.event = self.ItemPool[self.item][0]
        self.grade1 = self.ItemPool[self.item][1]
        self.grade2 = self.ItemPool[self.item][2]
        self.number1 = randint(50,100)
        self.number2 = randint(5,12)
        self.number3 = randint(2,4)
        self.total = self.number1*(self.number2+self.number3)

        self.answer = self.number3

        self.problem1 = "%d %ss are participating in a %s. Each %s sends %d %s and some %s. If each %s sends the same number of %s, and the total number of %s and %s attending the %s is %d, find the number of %s that each %s sends?"%(self.number1,self.item,self.event,self.item,self.number2,self.grade1,self.grade2,self.item,self.grade2,self.grade1,self.grade2,self.event,self.total,self.grade2,self.item)
        self.problem2 = "There are %d %ss participating in a %s. Each %s sends %d %s. If the total number of %s and %s attending the %s is %d, and each %s sends the same number of %s, how many %s does each %s send?"%(self.number1,self.item,self.event,self.item,self.number2,self.grade1,self.grade1,self.grade2,self.event,self.total,self.item,self.grade2,self.grade2,self.item)
        self.problem = random.choice([self.problem1,self.problem2])
        
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType42(self.problem,self.answer,self.item,self.event,self.grade1,self.grade2,self.number1,self.number2,self.number3,self.total)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"",'unit':self.grade2,'problem_type':"ProblemType42"}

    def ExplainType42(self,problem,answer,item,event,grade1,grade2,number1,number2,number3,total):
        self.answer_text = "The correct answer is: <b>"+str(answer)+" "+grade2
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'><tr><td align='center'>"+str(number2)+"<br>"
        self.table_text = self.table_text + "<img src='/images/explanation/up_curly_braces_3cm.png'></td>"
        self.table_text = self.table_text + "<td align='center'>?<br>"
        self.table_text = self.table_text + "<img src='/images/explanation/up_curly_braces_1cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td align='center'><img src='/images/explanation/pink_block_3cm.png'></td>"
        self.table_text = self.table_text + "<td align='center'><img src='/images/explanation/green_block_1cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td colspan=2 align='center'><img src='/images/explanation/down_curly_braces_3cm.png' width=240><br>"
        self.table_text = self.table_text + str(total)+" people &divide; "+str(number1)+" "+item+"</td>"
        self.table_text = self.table_text + "</tr></table><br>"
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(total)+" people &divide; "+str(number1)+" "+item+"s = "+str(total/number1)+" people"+"</div>"
        self.solution_text = self.solution_text + "<div>Each "+item+" sends "+str(total/number1)+" "+grade1+" and "+grade2+" combined.</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(total/number1)+" people - "+str(number2)+" "+grade1+" = "+str((total/number1)-number2)+" people</div>"
        self.solution_text = self.solution_text + "<div>Each "+item+" sends "+str((total/number1)-number2)+" "+grade2+"</div>"
    
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    '''Problem type 14 starts here'''
    def GenerateProblemType43(self):
        '''e.g.:Annie, Betty and Charlie sold a total of 104 tickets to a charity concert. Betty sold 8 more tickets than Annie. 
                Charlie sold twice as many tickets as Betty. How many tickets did Annie sell?'''

        self.PersonNames = random.sample(PersonName.PersonName,3)
        self.EventPool = ["charity concert","carnival","music festival","music concert","school fair","tennis tournament",
                          "dance show","movie","soccer game","tech fest","zoo","swimming tournament","museum","computer fair",
                          "painting exhibition","film festival","food festival","road show","book fair","night safari","bird park"]
        self.event = random.choice(self.EventPool)
        self.person1 = self.PersonNames[0]
        self.person2 = self.PersonNames[1]
        self.person3 = self.PersonNames[2]
        self.ticket1 = randint(2,25)
        self.diff = randint(8,19)
        self.ticket2 = self.ticket1 + self.diff
        self.multiplier = randint(2,3)
        self.ticket3 = self.ticket2 * self.multiplier
        self.total = self.ticket1 + self.ticket2 + self.ticket3

        self.answer = self.ticket1

        self.problem1 = "%s, %s and %s sold a total of %s tickets to a %s. %s sold %d more tickets than %s. %s sold %s times as many tickets as %s. How many tickets did %s sell?"%(self.person1,self.person2,self.person3,self.total,self.event,self.person2,self.diff,self.person1,self.person3,self.multiplier,self.person2,self.person1)
        self.problem2 = "%s, %s and %s sold %d tickets to a %s last month. If %s sold %d times as many tickets as %s and %s sold %d fewer tickets than %s, how many tickets did %s sell?"%(self.person1,self.person2,self.person3,self.total,self.event,self.person3,self.multiplier,self.person2,self.person1,self.diff,self.person2,self.person1)
        self.problem3 = "At the %s yesterday, %s, %s and %s sold %d tickets altogether. If %s sold %d more tickets than %s and %s sold %d times as many tickets as %s find the number of tickets sold by %s."%(self.event,self.person1,self.person2,self.person3,self.total,self.person2,self.diff,self.person1,self.person3,self.multiplier,self.person2,self.person1)
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])
        
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType43(self.problem,self.answer,self.event,self.person1,self.person2,self.person3,self.ticket1,self.diff,self.ticket2,self.multiplier,self.ticket3,self.total)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"",'unit':"tickets",'problem_type':"ProblemType43"}

    def ExplainType43(self,problem,answer,event,person1,person2,person3,ticket1,diff,ticket2,multiplier,ticket3,total):
        self.answer_text = "The correct answer is: <b>"+str(answer)+" tickets</b>"
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'><tr><td align='center'>"+person2+"</td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/pink_block_pt7cm.png'></td>"
        self.table_text = self.table_text + "<td align='center' rowspan="+str(1+multiplier)+"><img src='/images/explanation/right_curly_braces_2cm.png'></td>"
        self.table_text = self.table_text + "<td align='center' rowspan="+str(1+multiplier)+">"+str(total)+"</td></tr>"
        self.table_text = self.table_text + "<tr><td>"+person3+"</td><td><img src='/images/explanation/pink_block_pt7cm.png'>"
        for _i in range(multiplier-1):
            self.table_text = self.table_text + "<br><img src='/images/explanation/pink_block_pt7cm.png'>"
        self.table_text = self.table_text + "</tr><tr><td>"+person1+"</td><td><img src='/images/explanation/pink_block_pt5cm.png'><img src='/images/explanation/dotted_block_pt2cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td></td><td align='right'><img src='/images/explanation/down_curly_braces_pt3cm.png'><br>"+str(diff)+"</td>"
        self.table_text = self.table_text + "</tr></table><br>"
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(multiplier+2)+" units = "+str(total)+" tickets + "+str(diff)+" tickets</div>"
        self.solution_text = self.solution_text + "<div>"+str(multiplier+2)+" units = "+str(total+diff)+" tickets</div>"
        self.solution_text = self.solution_text + "<div>1 unit = "+str(total+diff)+" &divide; "+str(multiplier+2)+" = "+str((total+diff)/(multiplier+2))+" tickets</div><br>"
        self.solution_text = self.solution_text + "<div>"+str((total+diff)/(multiplier+2))+" tickets - "+str(diff)+" tickets = "+str(((total+diff)/(multiplier+2))-diff)+" tickets</div>"
        self.solution_text = self.solution_text + "<div>"+person1+" sold "+str(((total+diff)/(multiplier+2))-diff)+" tickets.</div>"
        self.solution_text = self.solution_text + "<br><div> Watch below video for explanation of similar problem<br>"
        VideoLink = '<object><param name="movie" value="https://www.youtube.com/v/u1zgFlCw8Aw?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded"><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "mgbyXs4yDkw";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
    
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    '''Problem type 15 starts here'''
    def GenerateProblemType44(self):
        '''e.g.:Annie shared some stickers equally among 8 friends and herself. She then 
                bought another 5 stickers and had 12 stickers altogether. How many stickers had she at first?'''

        self.person = random.choice(PersonName.GirlName)
        self.ItemPool = ["flags","stamps","pencils","pens","marbles","flowers","balls","toy cars","CDs","kites",
                          "notebooks","red flags","blue flags","candies","rings","key chains","straws","sticks","markers"]
        self.item = random.choice(self.ItemPool)
        self.friends = randint(3,12)
        self.extra = randint(5,15)
        self.share = randint(3,8)
        self.FinalNumber = self.share + self.extra
        self.initial = self.share * (self.friends + 1)
        
        self.answer = self.initial

        self.problem1 = "%s shared some %s equally among %d friends and herself. She then bought another %d %s and had %d %s altogether. How many %s had she at first?"%(self.person,self.item,self.friends,self.extra,self.item,self.FinalNumber,self.item,self.item)
        self.problem2 = "After sharing some %s equally among %d friends and herself, %s bought another %d %s. She then had %d %s altogether. Find the number of %s %s had at first."%(self.item,self.friends,self.person,self.extra,self.item,self.FinalNumber,self.item,self.item,self.person)
        self.problem = random.choice([self.problem1,self.problem2])
        
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType44(self.problem,self.answer,self.item,self.person,self.friends,self.extra,self.share,self.FinalNumber,self.initial)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"",'unit':self.item,'problem_type':"ProblemType44"}

    def ExplainType44(self,problem,answer,item,person,friends,extra,share,FinalNumber,initial):
        self.answer_text = "The correct answer is: <b>"+str(answer)+" "+item
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'><tr><td></td><td height=24 colspan="+str(friends+1)+" align='center'>?<br><img src='/images/explanation/up_curly_braces_3cm.png' width="+str(34*(friends+1))+"></td></tr>"
        self.table_text = self.table_text +"<tr><td>Before sharing</td>"
        for _i in range(friends+1):
            self.table_text = self.table_text + "<td><img src='/images/explanation/pink_block_pt5cm.png'></td>"
        self.table_text = self.table_text + "</tr><tr><td></td><td align='center'>?<br><img src='/images/explanation/up_curly_braces_pt5cm.png'></td>"
        self.table_text = self.table_text + "<td align='center'>"+str(extra)+"<br><img src='/images/explanation/up_curly_braces_pt4cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td>After sharing</td><td><img src='/images/explanation/pink_block_pt5cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/yellow_block_pt4cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td></td><td align='center' colspan=2><img src='/images/explanation/down_curly_braces_pt7cm.png'><br>"
        self.table_text = self.table_text + str(FinalNumber)+"</td></tr>"
        self.table_text = self.table_text + "</tr></table><br>"
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(FinalNumber)+" - "+str(extra)+" = "+str(FinalNumber-extra)+" "+item+"</div>"
        self.solution_text = self.solution_text + "<div>Each person got a share of "+str(FinalNumber-extra)+" "+item+"</div><br>"
        self.solution_text = self.solution_text + "<div>Total number of person including "+person+" = "+str(friends)+" + 1 = "+str(friends+1)+"</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(friends+1)+" x "+str(FinalNumber-extra)+" "+item+" = "+str((friends+1)*(FinalNumber-extra))+" "+item+"</div>"
        self.solution_text = self.solution_text + "<div>"+person+" had "+str((friends+1)*(FinalNumber-extra))+" "+item+" at first.</div>"
    
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain
    
    '''Problem type 16 starts here'''
    def GenerateProblemType45(self):
        '''e.g.:A supermarket is running a customer loyalty program in which it gives away 1 stamp for every $35 spent. 
            If Annie spent $124, how many stamps did she collect?'''
        self.person = random.choice(PersonName.GirlName)
        self.StorePool = {"1":["grocery store","point"],"2":["supermarket","stamp"],"3":["department store","membership point"],
                          "4":["supermarket","soap dispenser"],"5":["gas station","discount coupon"],"6":["flower shop","rose"],
                          "7":["restaurant","meal voucher"],"8":["pizza shop","gift coupon"],"9":["jewelery shop","ring"],
                          "10":["book store","discount voucher"],"11":["grocery store","bonus point"],"12":["toy shop","keychain"],
                          "13":["department store","candle stand"],"14":["computer shop","CD pack"],"15":["petrol pump","reward point"],
                          "14":["flower shop","mini-boquet"],"15":["restaurant","souvenir"],"16":["pizza shop","mug"],
                          "17":["book store","coupon booklet"],"18":["book store","marker"]
                          } 
        self.key = self.StorePool.keys()[randint(0,len(self.StorePool)-1)]
        self.store = self.StorePool[self.key][0]
        self.item = self.StorePool[self.key][1]
        self.MinSpent = randint(15,35)
        self.TotalSpent = randint(40,150)
        self.ItemGot,self.remainder = divmod(self.TotalSpent,self.MinSpent)
        
        self.answer = self.ItemGot

        self.problem1 = "A %s is running a customer loyalty program in which it gives away 1 %s for every $%d spent. If %s spent $%d, how many %ss did she collect?"%(self.store,self.item,self.MinSpent,self.person,self.TotalSpent,self.item)
        self.problem2 = "A %s has a rewards program in which customers can earn 1 %s for every $%d spent. If %s spent $%d, find the number of %ss that %s collected."%(self.store,self.item,self.MinSpent,self.person,self.TotalSpent,self.item,self.person)
        self.problem3 = "%s spent $%d at a %s. If the %s rewards customers with 1 %s for every $%d spent, how many %s did %ss collect?"%(self.person,self.TotalSpent,self.store,self.store,self.item,self.MinSpent,self.item,self.person)
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])
        
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType45(self.problem,self.answer,self.store,self.item,self.person,self.MinSpent,self.TotalSpent,self.ItemGot,self.remainder)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"",'unit':self.item+"s",'problem_type':"ProblemType45"}

    def ExplainType45(self,problem,answer,store,item,person,MinSpent,TotalSpent,ItemGot,remainder):
        if ItemGot>1:
            self.answer_text = "The correct answer is: <b>"+str(answer)+" "+item+"s"
        else:
            self.answer_text = "The correct answer is: <b>"+str(answer)+" "+item
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'><tr><td></td><td height=24 colspan=3 align='center'>$"+str(TotalSpent)+"<br>"
        self.table_text = self.table_text + "<img src='/images/explanation/up_curly_braces_3cm.png' width="+str(34*3)+"></td></tr>"
        self.table_text = self.table_text + "<tr><td>"+item+"</td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/pink_block_pt7cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/broken_pink_block_1cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/yellow_block_pt4cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td></td><td align='center'><img src='/images/explanation/down_curly_braces_pt7cm.png'><br>"
        self.table_text = self.table_text + "$"+str(MinSpent)+"</td><td></td>"
        self.table_text = self.table_text + "<td align='center' width=30><img src='/images/explanation/down_curly_braces_pt4cm.png'><br>R</td>"
        self.table_text = self.table_text + "</tr></table><br>"
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(TotalSpent)+" &divide; $"+str(MinSpent)+" = "+str(ItemGot)+" R "+str(remainder)+"</div>"
        self.solution_text = self.solution_text + "<div>"+person+" collected "+str(ItemGot)+" "+item
        if ItemGot>1:
            self.solution_text = self.solution_text + "s.</div>"
        else:
            self.solution_text = self.solution_text + ".</div>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    def GenerateProblemType46(self):
        '''e.g.:A supermarket gives away 1 stamp for every $35 spent. If Annie spent $124, how much amount did she NOT earn any stamps for?'''
        self.person = random.choice(PersonName.GirlName)
        self.StorePool = {"1":["grocery store","point"],"2":["supermarket","stamp"],"3":["department store","membership point"],
                          "4":["supermarket","soap dispenser"],"5":["gas station","discount coupon"],"6":["flower shop","rose"],
                          "7":["restaurant","meal voucher"],"8":["pizza shop","gift coupon"],"9":["jewelery shop","ring"],
                          "10":["book store","discount voucher"],"11":["grocery store","bonus point"],"12":["toy shop","keychain"],
                          "13":["department store","candle stand"],"14":["computer shop","CD pack"],"15":["petrol pump","reward point"],
                          "14":["flower shop","mini-boquet"],"15":["restaurant","souvenir"],"16":["pizza shop","mug"],
                          "17":["book store","coupon booklet"],"18":["book store","marker"]
                          } 
        self.key = self.StorePool.keys()[randint(0,len(self.StorePool)-1)]
        self.store = self.StorePool[self.key][0]
        self.item = self.StorePool[self.key][1]
        self.MinSpent = randint(15,35)
        self.TotalSpent = randint(40,150)
        self.ItemGot,self.remainder = divmod(self.TotalSpent,self.MinSpent)
        
        self.answer = self.remainder

        self.problem1 = "A %s gives away 1 %s for every $%d spent. If %s spent $%d, how much amount did she NOT earn any %ss for?"%(self.store,self.item,self.MinSpent,self.person,self.TotalSpent,self.item)
        self.problem2 = "A %s has a rewards program in which customers can earn 1 %s for every $%d spent. If %s spent $%d, find the amount of money that she did NOT earn any %ss for."%(self.store,self.item,self.MinSpent,self.person,self.TotalSpent,self.item)
        self.problem3 = "%s spent $%d at a %s. If the %s rewards customers with 1 %s for every $%d spent, how much amount did %s NOT earn any %ss for?"%(self.person,self.TotalSpent,self.store,self.store,self.item,self.MinSpent,self.person,self.item)
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])
        
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType46(self.problem,self.answer,self.store,self.item,self.person,self.MinSpent,self.TotalSpent,self.ItemGot,self.remainder)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"$",'problem_type':"ProblemType46"}

    def ExplainType46(self,problem,answer,store,item,person,MinSpent,TotalSpent,ItemGot,remainder):
        self.answer_text = "The correct answer is: <b>$"+str(answer)+"</b>"
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'><tr><td></td><td height=24 colspan=3 align='center'>$"+str(TotalSpent)+"<br>"
        self.table_text = self.table_text + "<img src='/images/explanation/up_curly_braces_3cm.png' width="+str(34*3)+"></td></tr>"
        self.table_text = self.table_text + "<tr><td>"+item+"</td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/pink_block_pt7cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/broken_pink_block_1cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/yellow_block_pt4cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td></td><td align='center'><img src='/images/explanation/down_curly_braces_pt7cm.png'><br>"
        self.table_text = self.table_text + "$"+str(MinSpent)+"</td><td></td>"
        self.table_text = self.table_text + "<td align='center' width=30><img src='/images/explanation/down_curly_braces_pt4cm.png'><br>R</td>"
        self.table_text = self.table_text + "</tr></table><br>"
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(TotalSpent)+" &divide; $"+str(MinSpent)+" = "+str(ItemGot)+" R "+str(remainder)+"</div>"
        self.solution_text = self.solution_text + "<div>"+person+" did not earn any "+item+" for the remaining $"+str(remainder)+".</div>"

        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    '''problem type 17 starts here'''
    def GenerateProblemType47(self):
        '''e.g.:A boat is helping people cross a river. If the maximum number of people (including the boat captain) that the boat can carry in a single trip is 5, 
                what is the minimum number of trips that the boat must make to transfer a group of 18 people?'''
        self.VehiclePool = {"1":["lift","go to a viewing terrace","lift operator"],"2":["boat","cross a river","boat captain"],
                        "3":["cable car","cross a valley","tour guide"],"4":["buggy","move between gates at the airport","buggy driver"],
                        "5":["ferry","transfer from mainland to the island","ferry captain"],"6":["helicopter","leave a flooded village","pilot"],
                        "7":["tram","go from the car park to the zoo","tram driver"],"8":["bus","transfer from the hotel to the airport","bus driver"],
                        "9":["cable trolley","ride from the ground to the mountain top","tour guide"],"10":["speed boat","sail to the island","speed boat captain"]
                        } 
        self.key = self.VehiclePool.keys()[randint(0,len(self.VehiclePool)-1)]
        self.vehicle = self.VehiclePool[self.key][0]
        self.place = self.VehiclePool[self.key][1]
        self.person = self.VehiclePool[self.key][2]
        self.MaxPerson = randint(5,20)
        self.TotalPerson = randint(21,101)
        self.trips,self.remainder = divmod(self.TotalPerson,self.MaxPerson-1)
        if(self.remainder!=0):
            self.answer = self.trips + 1
        else:
            self.answer = self.trips

        self.problem1 = "A %s is helping people %s. If the maximum number of people (including the %s) that the %s can carry in a single trip is %d, what is the minimum number of trips that the %s must make to transfer a group of %d people?"%(self.vehicle,self.place,self.person,self.vehicle,self.MaxPerson,self.vehicle,self.TotalPerson)
        self.problem2 = "A group of %d people has to %s using a %s. The maximum number of people (including the %s) that the %s can carry in a single trip is %d. Find the minimum number of trips that the %s must make."%(self.TotalPerson,self.place,self.vehicle,self.person,self.vehicle,self.MaxPerson,self.vehicle)
        self.problem3 = "A group of %d people has to %s using a %s. In a single trip, the %s can carry a maximum of %d people (including the %s). What is the minimum number of trips that the %s must make to transfer the group?"%(self.TotalPerson,self.place,self.vehicle,self.vehicle,self.MaxPerson,self.person,self.vehicle)
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])

        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType47(self.problem,self.answer,self.vehicle,self.place,self.person,self.MaxPerson,self.TotalPerson,self.trips,self.remainder)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"",'unit':"trips",'problem_type':"ProblemType47"}

    def ExplainType47(self,problem,answer,vehicle,place,person,MaxPerson,TotalPerson,trips,remainder):
        self.answer_text = "The correct answer is: <b>"+str(answer)+" trips"
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'><tr><td></td><td height=24 colspan=3 align='center'>$"+str(TotalPerson)+"<br>"
        self.table_text = self.table_text + "<img src='/images/explanation/up_curly_braces_3cm.png' width="+str(34*3)+"></td></tr>"
        self.table_text = self.table_text + "<tr><td>Trips</td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/pink_block_pt7cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/broken_pink_block_1cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/yellow_block_pt4cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td></td><td align='center'><img src='/images/explanation/down_curly_braces_pt7cm.png'><br>"
        self.table_text = self.table_text + "$"+str(MaxPerson)+"</td><td></td>"
        self.table_text = self.table_text + "<td align='center' width=30><img src='/images/explanation/down_curly_braces_pt4cm.png'><br>R</td>"
        self.table_text = self.table_text + "</tr></table><br>"
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>Total number of passengers allowed on the "+vehicle+" <b>NOT</b> including the "+person+" is "+str(MaxPerson)+" - 1 = "+str(MaxPerson-1)+"</div>"
        self.solution_text = self.solution_text + "<div>So the "+vehicle+" can transfer a maximum of "+str(MaxPerson-1)+" passengers in one trip.</div><br>"
        if(remainder!=0):
            self.solution_text = self.solution_text + "<div>"+str(TotalPerson)+" people &divide; "+str(MaxPerson-1)+" = "+str(trips)+" and "+str(remainder)+" remaining passengers"+"</div>"
            self.solution_text = self.solution_text + "<div>"+str(remainder)+" passengers will be left after making "+str(trips)+" trips."+"</div>"
            self.solution_text = self.solution_text + "<div>One more trip is needed to transfer the last "+str(remainder)+" passengers.</div><br>"
            if (trips>1):
                self.solution_text = self.solution_text + "<div>"+str(trips)+" trips + 1 trip = "+str(trips+1)+" trips"+"</div>"
            else:
                self.solution_text = self.solution_text + "<div>"+str(trips)+" trip + 1 trip = "+str(trips+1)+" trips"+"</div>"
            self.solution_text = self.solution_text + "<div>The minimum number of trips that the "+vehicle+" must make to transfer the group is "+str(trips+1)+".</div>"
        else:
            self.solution_text = self.solution_text + "<div>"+str(TotalPerson)+" people &divide; "+str(MaxPerson-1)+" = "+str(trips)+"</div>"
            self.solution_text = self.solution_text + "<div>The minimum number of trips that the "+vehicle+" must make to transfer the group is "+str(trips)+".</div>"
            
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    '''problem type 18 starts here'''
    def GenerateProblemType48(self):
        '''e.g.:8 skirts and 5 blouses cost $466. Each skirt cost $16 more than a blouse. How much did each blouse cost?'''
        self.GirlName = random.choice(PersonName.GirlName)
        self.ItemPool = {"1":["table","chair",randint(15,85)],"2":["toy","book",randint(5,50)],"3":["notebook","marker",randint(3,10)],
                        "4":["bracelet","ring",randint(15,50)],"5":["plate","bowl",randint(5,20)],"6":["mug","spoon",randint(5,10)],
                        "7":["DVD","CD",randint(5,20)],"8":["coat","jersey",randint(15,100)],"9":["T-shirt","cap",randint(10,30)],
                        "10":["jar","cup",randint(5,10)],"11":["shirt","tie",randint(10,50)],"12":["book","magazine",randint(5,20)],
                        "13":["lamp","flashlight",randint(15,35)],"14":["bedsheet","towel",randint(15,45)],"15":["hair clip","rubber band",randint(5,10)],
                        "16":["candle holder","candle",randint(5,15)],"17":["pillow","cushion",randint(10,25)],"18":["racket","bowl",randint(15,35)]
                        } 
        self.key = self.ItemPool.keys()[randint(0,len(self.ItemPool)-1)]
        self.item1 = self.ItemPool[self.key][0]
        self.item2 = self.ItemPool[self.key][1]
        self.amount1 = self.ItemPool[self.key][2]
        '''making sure diff is not zero'''
        self.diff = 1 + int(self.amount1 * randint(2,5)/10)
        self.amount2 = self.amount1 - self.diff
        self.number1 = randint(3,8)
        self.number2 = randint(3,8)
        self.TotalSpent = (self.number1*self.amount1 + self.number2*self.amount2)
        
        self.answer = self.amount2

        self.problem1 = "%d %ss and %d %ss cost $%d. Each %s cost $%d more than a %s. How much did each %s cost?"%(self.number1,self.item1,self.number2,self.item2,self.TotalSpent,self.item1,self.diff,self.item2,self.item2)
        self.problem2 = "The total cost of %d %ss and %d %ss was $%d. If each %s cost $%d more than a %s, find the cost of each %s."%(self.number1,self.item1,self.number2,self.item2,self.TotalSpent,self.item1,self.diff,self.item2,self.item2)
        self.problem3 = "The total cost of %d %ss and %d %ss was $%d. If each %s cost $%d less than a %s, find the cost of each %s."%(self.number1,self.item1,self.number2,self.item2,self.TotalSpent,self.item2,self.diff,self.item1,self.item2)
        self.problem4 = "A %s cost $%d less than a %s. If %s bought %d %ss and %d %ss for $%d altogether, what was the cost of each %s?"%(self.item2,self.diff,self.item1,self.GirlName,self.number1,self.item1,self.number2,self.item2,self.TotalSpent,self.item2)
        self.problem5 = "%s bought %d %ss and %d %ss for a total of $%d. If a %s cost her $%d more than a %s, find the cost of each %s."%(self.GirlName,self.number1,self.item1,self.number2,self.item2,self.TotalSpent,self.item1,self.diff,self.item2,self.item2)
        self.problem = random.choice([self.problem1,self.problem2,self.problem3,self.problem4,self.problem5])

        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType48(self.problem,self.answer,self.item1,self.item2,self.amount1,self.diff,self.amount2,self.number1,self.number2,self.TotalSpent)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"$",'problem_type':"ProblemType48"}

    def ExplainType48(self,problem,answer,item1,item2,amount1,diff,amount2,number1,number2,TotalSpent):
        self.answer_text = "The correct answer is: <b>$"+str(answer)+"</b>"
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'><tr><td align='center' rowspan="+str(number1)+" align='center'>"+str(number1)+" "+item1+"s</td>"
        self.table_text = self.table_text + "<td align='center' rowspan="+str(number1)+"><img src='/images/explanation/left_curly_braces_2cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/pink_block_pt7cm.png'></td>"
        self.table_text = self.table_text + "<td align='center' rowspan="+str(number1+number2)+"><img src='/images/explanation/right_curly_braces_3cm.png'></td>"
        self.table_text = self.table_text + "<td align='center' rowspan="+str(number1+number2)+">$"+str(TotalSpent)+"</td></tr>"
        for _i in range(number1-1):
            self.table_text = self.table_text + "<tr><td><img src='/images/explanation/pink_block_pt7cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td align='center' rowspan="+str(number2)+" align='center'>"+str(number2)+" "+item2+"s</td>"
        self.table_text = self.table_text + "<td align='center' rowspan="+str(number2)+"><img src='/images/explanation/left_curly_braces_2cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/pink_block_pt5cm.png'><img src='/images/explanation/dotted_block_pt2cm.png'></td></tr>"
        for _i in range(number2-1):
            self.table_text = self.table_text + "<tr><td><img src='/images/explanation/pink_block_pt5cm.png'><img src='/images/explanation/dotted_block_pt2cm.png'></td></tr>"       
        self.table_text = self.table_text + "<tr><td></td><td></td><td align='right'><img src ='/images/explanation/down_curly_braces_pt3cm.png'><br>$"+str(diff)+"</td>"
        self.table_text = self.table_text + "</tr></table><br>"
        
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(number1+number2)+" units = $"+str(TotalSpent)+" + ("+str(number2)+" x $"+str(diff)+")"
        self.solution_text = self.solution_text + " = $"+str(TotalSpent)+" + $"+str(number2*diff)+" = $"+str(TotalSpent+number2*diff)+"</div>"
        self.solution_text = self.solution_text + "<div>1 unit = $"+str(TotalSpent+number2*diff)+" &divide; "+str(number1+number2)+" = $"+str(amount1)+"</div>"
        self.solution_text = self.solution_text + "<div>Cost of each "+item1+" is $"+str((TotalSpent+number2*diff)/(number1+number2))+".</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(amount1)+" - $"+str(diff)+" = $"+str(amount2)+"</div>"
        self.solution_text = self.solution_text + "<div>Cost of each "+item2+" is $"+str(amount2)+".</div>"
                    
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    '''problem type 19 starts here'''
    def GenerateProblemType49(self):
        '''e.g.:Annie bought some skirts and 5 blouses. Each blouse cost $26. Each skirt cost $16 more than a blouse. 
                She spent $466 altogether. How many skirts did she buy?'''
        self.GirlName = random.choice(PersonName.GirlName)
        self.ItemPool = {"1":["table","chair",randint(15,85)],"2":["toy","book",randint(5,50)],"3":["notebook","marker",randint(3,10)],
                        "4":["bracelet","ring",randint(15,50)],"5":["plate","bowl",randint(5,20)],"6":["mug","spoon",randint(5,10)],
                        "7":["DVD","CD",randint(5,20)],"8":["coat","jersey",randint(15,100)],"9":["T-shirt","cap",randint(10,30)],
                        "10":["jar","cup",randint(5,10)],"11":["shirt","tie",randint(10,50)],"12":["book","magazine",randint(5,20)],
                        "13":["lamp","flashlight",randint(15,35)],"14":["bedsheet","towel",randint(15,45)],"15":["hair clip","rubber band",randint(5,10)],
                        "16":["candle holder","candle",randint(5,15)],"17":["pillow","cushion",randint(10,25)],"18":["racket","bowl",randint(15,35)]
                        } 
        self.key = self.ItemPool.keys()[randint(0,len(self.ItemPool)-1)]
        self.item1 = self.ItemPool[self.key][0]
        self.item2 = self.ItemPool[self.key][1]
        self.amount1 = self.ItemPool[self.key][2]
        '''making sure diff is not zero'''
        self.diff = 1 + int(self.amount1 * randint(2,5)/10)
        self.amount2 = self.amount1 - self.diff
        self.number1 = randint(3,8)
        self.number2 = randint(3,8)
        self.TotalSpent = (self.number1*self.amount1 + self.number2*self.amount2)
        
        self.answer = self.number1
        
        self.problem1 = "%s bought some %ss and %d %ss. Each %s cost $%d. Each %s cost $%d more than a %s. She spent $%d altogether. How many %ss did she buy?"%(self.GirlName,self.item1,self.number2,self.item2,self.item2,self.amount2,self.item1,self.diff,self.item2,self.TotalSpent,self.item1)
        self.problem2 = "%s spent a total of $%d on %d %ss and some %ss. Each %s cost $%d and each %s cost $%d more than a %s. Find the number of %ss that %s bought."%(self.GirlName,self.TotalSpent,self.number2,self.item2,self.item1,self.item2,self.amount2,self.item1,self.diff,self.item2,self.item1,self.GirlName)
        self.problem3 = "A %s cost $%d which is $%d less than a %s. If %s spent $%d altogether for %d %ss and some %ss, how many %ss did she buy?"%(self.item2,self.amount2,self.diff,self.item1,self.GirlName,self.TotalSpent,self.number2,self.item2,self.item1,self.item1)
        self.problem4 = "%s bought %d %ss and some %ss for $%d altogether. If a %s cost her $%d which is $%d less than a %s, how many %ss did she buy?"%(self.GirlName,self.number2,self.item2,self.item1,self.TotalSpent,self.item2,self.amount2,self.diff,self.item1,self.item1)
        self.problem = random.choice([self.problem1,self.problem2,self.problem3,self.problem4])

        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType49(self.problem,self.answer,self.GirlName,self.item1,self.item2,self.amount1,self.diff,self.amount2,self.number1,self.number2,self.TotalSpent)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"",'unit':self.item1+"s",'problem_type':"ProblemType49"}

    def ExplainType49(self,problem,answer,GirlName,item1,item2,amount1,diff,amount2,number1,number2,TotalSpent):
        self.answer_text = "The correct answer is: <b>"+str(answer)+" "+item1+"s"
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'><tr><td></td><td align='right'>$"+str(diff)+"<br>"
        self.table_text = self.table_text + "<img src='/images/explanation/up_curly_braces_pt3cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td>"+item1+"s</td>"
        for _i in range(2):
            self.table_text = self.table_text + "<td><img src='/images/explanation/pink_green_block_pt8cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/broken_pink_green_block_left_pt8cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/broken_pink_green_block_right_pt8cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/pink_green_block_pt8cm.png'></td>"
        for _i in range(number2-5):
            self.table_text = self.table_text + "<td></td>"
        self.table_text = self.table_text + "<td rowspan=2><img src='/images/explanation/right_curly_braces_pt7cm.png'></td>"
        self.table_text = self.table_text + "<td align='center' rowspan=2>$"+str(TotalSpent)+"</td></tr>"
        self.table_text = self.table_text + "<tr><td>"+item2+"s</td>"
        for _i in range(number2):
            self.table_text = self.table_text + "<td><img src='/images/explanation/pink_block_pt7cm.png' width=51 height=24></td>"
        self.table_text = self.table_text + "</tr><tr><td></td><td><img src='/images/explanation/down_curly_braces_pt7cm.png'><br>"
        self.table_text = self.table_text + "$"+str(amount2)+"</td>"
        self.table_text = self.table_text + "</tr></table><br>"
        
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(amount2)+" + $"+str(diff)+" = $"+str(amount2+diff)+"</div>"
        self.solution_text = self.solution_text + "<div>Cost of each "+item1+" is $"+str(amount2+diff)+".</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(number2)+" units x $"+str(amount2)+" = $"+str(number2*amount2)+"</div>"
        self.solution_text = self.solution_text + "<div>Total cost of all "+item2+"s is = $"+str(number2*amount2)+".</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(TotalSpent)+" - $"+str(number2*amount2)+" = $"+str(TotalSpent-number2*amount2)+"</div>"
        self.solution_text = self.solution_text + "<div>Total cost of all "+item1+"s is $"+str(TotalSpent-number2*amount2)+".</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(TotalSpent-number2*amount2)+" &divide; "+str(amount1)+" = "+str(number1)+"</div>"
        self.solution_text = self.solution_text + "<div>"+GirlName+" bought "+str(number1)+" "+item1+"s.</div>"
                    
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    '''problem type 20 starts here'''
    def GenerateProblemType50(self):
        '''e.g.:A curtain merchant had 100 m of cloth that he divided into pieces of 3 m each. He sold each 3-m piece for $37 and the leftover at a discount. 
                He collected $1241 altogether. How much did he sell the leftover cloth for?'''
        self.MerchantPool = {"1":["cloth merchant","m","cloth","piece",randint(15,65)],"2":["plant nursery keeper","kg","soil","bag",randint(10,50)],
                             "3":["vegetable seller","kg","potatoes","bag",randint(3,10)],"4":["fruit vendor","kg","grapes","bag",randint(15,25)],
                             "5":["rope merchant","m","rope","piece",randint(5,20)],"6":["farmer","kg","rice","bag",randint(5,20)],
                             "7":["juice seller","l","orange juice","bottle",randint(5,20)],"8":["herbal tea wholesaler","kg","tea","carton",randint(15,30)],
                             "9":["shopkeeper","m","ribbon","piece",randint(10,30)],"10":["florist","kg","fertilizer","packet",randint(15,40)],
                             "11":["grocer","g","meat","packet",randint(10,50)],"12":["fruit seller","kg","berries","packet",randint(15,35)],
                             "13":["kite seller","m","kite string","spool",randint(5,15)],"14":["cooking oil supplier","l","oil","can",randint(15,45)],
                             "15":["cement supplier","kg","cement","pack",randint(25,100)],"16":["coffee supplier","kg","coffee","pack",randint(15,40)],
                             "17":["supplier","kg","sugar","pack",randint(5,15)]
                             } 
        self.key = self.MerchantPool.keys()[randint(0,len(self.MerchantPool)-1)]
        self.merchant = self.MerchantPool[self.key][0]
        self.unit = self.MerchantPool[self.key][1]
        self.item = self.MerchantPool[self.key][2]
        self.container = self.MerchantPool[self.key][3]
        self.price = self.MerchantPool[self.key][4]
        self.total = randint(50,100)
        self.SingleUnit = randint(3,9)
        while(self.total%self.SingleUnit==0):
            self.SingleUnit = randint(3,9)
        self.remainder = self.total%self.SingleUnit
        self.discount = int((self.price * randint(5,8)/10)*self.remainder/self.SingleUnit)
        '''making sure discount price is not zero'''
        if self.discount == 0:
            self.discount = 1
        self.TotalAmount = int(self.total/self.SingleUnit)*self.price + self.discount
        
        self.answer = self.discount

        self.problem1 = "A %s had %d %s of %s that he divided into %ss of %d %s each. He sold each %d-%s %s for $%d and the leftover at a discount. He collected $%d altogether. How much did he sell the leftover %s for?"%(self.merchant,self.total,self.unit,self.item,self.container,self.SingleUnit,self.unit,self.SingleUnit,self.unit,self.container,self.price,self.TotalAmount,self.item)
        self.problem2 = "A %s divided %d %s of %s into %d-%s %ss and sold each %s for $%d. He sold the leftover %s at a discount. If he collected $%d altogether, how much did he sell the leftover %s for?"%(self.merchant,self.total,self.unit,self.item,self.SingleUnit,self.unit,self.container,self.container,self.price,self.item,self.TotalAmount,self.item)
        self.problem3 = "A %s had %d %s of %s that he divided into %d-%s %ss and sold each %s for $%d. He sold the leftover %s at a discount. If he collected $%d altogether, find the amount of money that he sold the leftover %s for."%(self.merchant,self.total,self.unit,self.item,self.SingleUnit,self.unit,self.container,self.container,self.price,self.item,self.TotalAmount,self.item)
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])

        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType50(self.problem,self.answer,self.merchant,self.unit,self.item,self.container,self.price,self.total,self.SingleUnit,self.remainder,self.discount,self.TotalAmount)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"$",'problem_type':"ProblemType50"}

    def ExplainType50(self,problem,answer,merchant,unit,item,container,price,total,SingleUnit,remainder,discount,TotalAmount):
        self.answer_text = "The correct answer is: <b>$"+str(answer)+"</b>"
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'><tr><td></td><td align='center' colspan=5>"+str(total)+" "+unit+"<br>"
        self.table_text = self.table_text + "<img src='/images/explanation/up_curly_braces_3cm.png' width=200 height=24></td></tr>"
        self.table_text = self.table_text + "<tr><td>"+item+"</td>"
        for _i in range(2):
            self.table_text = self.table_text + "<td><img src='/images/explanation/pink_block_pt7cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/broken_pink_block_pt7cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/pink_block_pt7cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/yellow_block_pt4cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td></td><td align='center'><img src='/images/explanation/down_curly_braces_pt7cm.png'><br>"
        self.table_text = self.table_text + str(SingleUnit)+"<td><td></td><td></td>"
        self.table_text = self.table_text + "<td align='center'><img src='/images/explanation/down_curly_braces_pt4cm.png'><br>R</td>"
        self.table_text = self.table_text + "</tr></table><br>"
        
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(total)+" "+unit+" &divide; "+str(SingleUnit)+" = "+str(int(total/SingleUnit))+" units and "+str(remainder)+" "+unit+" remaining</div>"
        self.solution_text = self.solution_text + "<div>"+str(total)+" can be divided into "+str(int(total/SingleUnit))+" "+container+"s of "+str(SingleUnit)+" "+unit+" each.</div>"
        self.solution_text = self.solution_text + "<div>There will be "+str(remainder)+" "+unit+" of leftover "+item+".</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(int(total/SingleUnit))+" units x $"+str(price)+" = $"+str((int(total/SingleUnit))*price)+"</div>"
        self.solution_text = self.solution_text + "<div>$"+str((int(total/SingleUnit))*price)+" is collected by selling the "+str(int(total/SingleUnit))+" "+container+"s.</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(TotalAmount)+" - $"+str((int(total/SingleUnit))*price)+" = $"+str(TotalAmount-((int(total/SingleUnit))*price))+"</div>"
        self.solution_text = self.solution_text + "<div>He sold the leftover "+item+" for $"+str(TotalAmount-((int(total/SingleUnit))*price))+".</div>"
        self.solution_text = self.solution_text + "<br><div> Watch below video for explanation of similar problem<br>"
        VideoLink = '<object><param name="movie" value="https://www.youtube.com/v/u1zgFlCw8Aw?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded"><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "aBb5YVWOo5U";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
                    
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    def GenerateProblemType51(self):
        '''e.g.:A curtain merchant had 100 m of cloth that he divided into pieces of 3 m each. He sold each 3-m piece for $37 and the leftover for $20. 
                How much money did he collect altogether?'''
        self.MerchantPool = {"1":["cloth merchant","m","cloth","piece",randint(15,65)],"2":["plant nursery keeper","kg","soil","bag",randint(10,50)],
                             "3":["vegetable seller","kg","potatoes","bag",randint(3,10)],"4":["fruit vendor","kg","grapes","bag",randint(15,25)],
                             "5":["rope merchant","m","rope","piece",randint(5,20)],"6":["farmer","kg","rice","bag",randint(5,20)],
                             "7":["juice seller","l","orange juice","bottle",randint(5,20)],"8":["herbal tea wholesaler","kg","tea","carton",randint(15,30)],
                             "9":["shopkeeper","m","ribbon","piece",randint(10,30)],"10":["florist","kg","fertilizer","packet",randint(15,40)],
                             "11":["grocer","g","meat","packet",randint(10,50)],"12":["fruit seller","kg","berries","packet",randint(15,35)],
                             "13":["kite seller","m","kite string","spool",randint(5,15)],"14":["cooking oil supplier","l","oil","can",randint(15,45)],
                             "15":["cement supplier","kg","cement","pack",randint(25,100)],"16":["coffee supplier","kg","coffee","pack",randint(15,40)],
                             "17":["supplier","kg","sugar","pack",randint(5,15)]
                             } 
        self.key = self.MerchantPool.keys()[randint(0,len(self.MerchantPool)-1)]
        self.merchant = self.MerchantPool[self.key][0]
        self.unit = self.MerchantPool[self.key][1]
        self.item = self.MerchantPool[self.key][2]
        self.container = self.MerchantPool[self.key][3]
        self.price = self.MerchantPool[self.key][4]
        self.total = randint(50,100)
        self.SingleUnit = randint(3,9)
        while(self.total%self.SingleUnit==0):
            self.SingleUnit = randint(3,9)
        self.remainder = self.total%self.SingleUnit
        self.discount = int((self.price * randint(5,8)/10)*self.remainder/self.SingleUnit)
        '''making sure discount price is not zero'''
        if self.discount == 0:
            self.discount = 1
        self.TotalAmount = int(self.total/self.SingleUnit)*self.price + self.discount
        
        self.answer = self.TotalAmount

        self.problem1 = "A %s had %d %s of %s that he divided into %ss of %d %s each. He sold each %d-%s %s for $%d and the leftover for $%d. How much money did he collect altogether?"%(self.merchant,self.total,self.unit,self.item,self.container,self.SingleUnit,self.unit,self.SingleUnit,self.unit,self.container,self.price,self.discount)
        self.problem2 = "A %s divided %d %s of %s into %d-%s %ss and sold each %s for $%d. He sold the leftover %s for $%d. How much money did he collect altogether?"%(self.merchant,self.total,self.unit,self.item,self.SingleUnit,self.unit,self.container,self.container,self.price,self.item,self.discount)
        self.problem3 = "A %s had %d %s of %s that he divided into %d-%s %ss and sold each %s for $%d. He sold the leftover %s for $%d. Find the amount of money that he collected altogether."%(self.merchant,self.total,self.unit,self.item,self.SingleUnit,self.unit,self.container,self.container,self.price,self.item,self.discount)
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])

        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType51(self.problem,self.answer,self.merchant,self.unit,self.item,self.container,self.price,self.total,self.SingleUnit,self.remainder,self.discount,self.TotalAmount)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"$",'problem_type':"ProblemType51"}

    def ExplainType51(self,problem,answer,merchant,unit,item,container,price,total,SingleUnit,remainder,discount,TotalAmount):
        self.answer_text = "The correct answer is: <b>$"+str(answer)+"</b>"
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'><tr><td></td><td align='center' colspan=5>"+str(total)+" "+unit+"<br>"
        self.table_text = self.table_text + "<img src='/images/explanation/up_curly_braces_3cm.png' width=200 height=24></td></tr>"
        self.table_text = self.table_text + "<tr><td>"+item+"</td>"
        for _i in range(2):
            self.table_text = self.table_text + "<td><img src='/images/explanation/pink_block_pt7cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/broken_pink_block_pt7cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/pink_block_pt7cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/yellow_block_pt4cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td></td><td align='center'><img src='/images/explanation/down_curly_braces_pt7cm.png'><br>"
        self.table_text = self.table_text + str(SingleUnit)+"<td><td></td><td></td>"
        self.table_text = self.table_text + "<td align='center'><img src='/images/explanation/down_curly_braces_pt4cm.png'><br>R</td>"
        self.table_text = self.table_text + "</tr></table><br>"
        
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(total)+" "+unit+" &divide; "+str(SingleUnit)+" = "+str(int(total/SingleUnit))+" units and "+str(remainder)+" "+unit+" remaining</div>"
        self.solution_text = self.solution_text + "<div>"+str(total)+" can be divided into "+str(int(total/SingleUnit))+" "+container+"s of "+str(SingleUnit)+" "+unit+" each.</div>"
        self.solution_text = self.solution_text + "<div>There will be "+str(remainder)+" "+unit+" of leftover "+item+".</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(int(total/SingleUnit))+" units x $"+str(price)+" = $"+str((int(total/SingleUnit))*price)+"</div>"
        self.solution_text = self.solution_text + "<div>$"+str((int(total/SingleUnit))*price)+" is collected by selling the "+str(int(total/SingleUnit))+" "+container+"s.</div><br>"
        self.solution_text = self.solution_text + "<div>The leftover "+item+" is sold for $"+str(discount)+".</div>"
        self.solution_text = self.solution_text + "<div>$"+str((int(total/SingleUnit))*price)+" + $"+str(discount)+" = $"+str(((int(total/SingleUnit))*price)+discount)+"</div>"      
        self.solution_text = self.solution_text + "<div>He collected $"+str(((int(total/SingleUnit))*price)+discount)+" altogether.</div>"
                    
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    '''Problem type 21 starts here'''
    def GenerateProblemType52(self):
        '''e.g.:Annie had 2 times as many flags as Betty. How many flags must Annie give Betty so that each of them will have 75 flags?'''
        self.PersonNames = random.sample(PersonName.PersonName,2)
        self.ItemPool = ["notebooks","stamps","pencils","pens","marbles","flowers","buttons","toy cars","CDs","sticks",
                         "kites","books","red flags","blue flags","paper boats","rings","key chains","buns","straws","markers"]
        self.item = random.choice(self.ItemPool)
        self.person1 = self.PersonNames[0]
        self.person2 = self.PersonNames[1]
        self.MultiplierPool = {2:random.randrange(3,100,3),3:random.randrange(4,100,4),4:random.randrange(5,100,5)}
        self.multiplier = self.MultiplierPool.keys()[randint(0,len(self.MultiplierPool)-1)]
        self.number = self.MultiplierPool[self.multiplier]
        self.give = self.number/(self.multiplier+1)
        
        self.answer = self.give

        self.problem1 = "%s had %d times as many %s as %s. How many %s must %s give %s so that each of them will have %d %s?"%(self.person1,self.multiplier,self.item,self.person2,self.item,self.person1,self.person2,self.number,self.item)
        self.problem = self.problem1

        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType52(self.problem,self.answer,self.item,self.person1,self.person2,self.multiplier,self.number,self.give)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"",'unit':self.item,'problem_type':"ProblemType52"}

    def ExplainType52(self,problem,answer,item,person1,person2,multiplier,number,give):
        self.answer_text = "The correct answer is: <b>"+str(answer)+" "+item
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'><tr>"
        for _i in range(multiplier+2):
            self.table_text = self.table_text + "<td></td>"
        self.table_text = self.table_text + "<td align='center' colspan="+str(multiplier-1)+">?<br><img src='/images/explanation/up_curly_braces_1cm.png' height=24 width="+str(34*(multiplier-1))+"></td></tr>"
        self.table_text = self.table_text + "<tr><td>"+person1+"</td>"
        for _i in range(multiplier+1):
            self.table_text = self.table_text + "<td><img src='/images/explanation/pink_block_pt5cm.png'></td>"
        for _i in range(2*multiplier-(multiplier+1)):
            self.table_text = self.table_text + "<td><img src='/images/explanation/green_block_pt5cm.png'></td>"
        self.table_text = self.table_text + "</tr><tr>"
        for _i in range(multiplier+1):
            self.table_text = self.table_text + "<td></td>"
        self.table_text = self.table_text + "<td colspan="+str(2*multiplier-(multiplier+1))+"><img src='/images/explanation/down_arrow.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td>"+person2+"</td>"
        for _i in range(2):
            self.table_text = self.table_text + "<td><img src='/images/explanation/green_block_pt5cm.png'></td>"
        for _i in range(multiplier-1):
            self.table_text = self.table_text + "<td><img src='/images/explanation/dotted_block_pt5cm.png'></td>"
        self.table_text = self.table_text + "</tr><tr><td></td><td align='center' colspan="+str(multiplier+1)+"><img src='/images/explanation/down_curly_braces_2cm.png' height=24 width="+str((multiplier+1)*34)+">"
        self.table_text = self.table_text + "<br>"+str(number)+"</td>"
        self.table_text = self.table_text + "</tr></table><br>"
        
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(multiplier+1)+" units = "+str(number)+" "+item+"</div>"
        self.solution_text = self.solution_text + "<div>1 unit = "+str(number)+" "+item+" &divide; "+str(multiplier+1)+" = "+str(number/(multiplier+1))+" "+item+"</div>"
        if(multiplier==2):
            self.solution_text = self.solution_text + "<div>"+person1+" must give "+str(number/(multiplier+1))+" "+item+" to "+person2+"</div>"
        else:
            self.solution_text = self.solution_text + "<div>"+str(multiplier-1)+" units = "+str(number*multiplier/(multiplier+1))+"</div>"
            self.solution_text = self.solution_text + "<div>"+person1+" must give "+str(number*multiplier/(multiplier+1))+" "+item+" to "+person2+"</div>"
            
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    def GenerateProblemType53(self):
        '''e.g.:Annie had 2 times as many flags as Betty. After Annie gave 25 flags to Betty, they both had the same number of flags. 
                How many flags did Annie have at first?'''
        self.PersonNames = random.sample(PersonName.PersonName,2)
        self.ItemPool = ["notebooks","stamps","pencils","pens","marbles","flowers","buttons","toy cars","CDs","sticks",
                         "kites","books","red flags","blue flags","paper boats","rings","key chains","buns","straws","markers"]
        self.item = random.choice(self.ItemPool)
        self.person1 = self.PersonNames[0]
        self.person2 = self.PersonNames[1]
        self.MultiplierPool = {2:random.randrange(3,100,3)}
        self.multiplier = self.MultiplierPool.keys()[randint(0,len(self.MultiplierPool)-1)]
        self.number = self.MultiplierPool[self.multiplier]
        self.give = self.number/(self.multiplier+1)
        
        self.answer = self.give * 2 * self.multiplier

        self.problem1 = "%s had %d times as many %s as %s. After %s gave %d %s to %s, they both had the same number of %s. How many %s did %s have at first?"%(self.person1,self.multiplier,self.item,self.person2,self.person1,self.give,self.item,self.person2,self.item,self.item,self.person1)
        self.problem = self.problem1

        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType53(self.problem,self.answer,self.item,self.person1,self.person2,self.multiplier,self.number,self.give)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"",'unit':self.item,'problem_type':"ProblemType53"}

    def ExplainType53(self,problem,answer,item,person1,person2,multiplier,number,give):
        self.answer_text = "The correct answer is: <b>"+str(answer)+" "+item
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'><tr>"
        self.table_text = self.table_text + "<td></td><td colspan=4 align='center'>?<br><img src='/images/explanation/up_curly_braces_2cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td>"+person1+"</td>"
        for _i in range(multiplier+1):
            self.table_text = self.table_text + "<td><img src='/images/explanation/pink_block_pt5cm.png'></td>"
        for _i in range(2*multiplier-(multiplier+1)):
            self.table_text = self.table_text + "<td><img src='/images/explanation/green_block_pt5cm.png'></td>"
        self.table_text = self.table_text + "</tr><tr>"
        for _i in range(multiplier+1):
            self.table_text = self.table_text + "<td></td>"
        self.table_text = self.table_text + "<td colspan="+str(2*multiplier-(multiplier+1))+"><img src='/images/explanation/down_arrow.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td>"+person2+"</td>"
        for _i in range(2):
            self.table_text = self.table_text + "<td><img src='/images/explanation/green_block_pt5cm.png'></td>"
        for _i in range(multiplier-1):
            self.table_text = self.table_text + "<td><img src='/images/explanation/dotted_block_pt5cm.png'>"
        self.table_text = self.table_text + "</tr><tr>"    
        for _i in range(3):
            self.table_text = self.table_text + "<td></td>"
        self.table_text = self.table_text + "<td align='center'><img src='/images/explanation/down_curly_braces_pt5cm.png'><br>"+str(give)+"</td>"
        self.table_text = self.table_text + "</tr></table><br>"
        
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>1 unit = "+str(give)+" "+item+"</div>"
        self.solution_text = self.solution_text + "<div>"+str(multiplier*2)+" units = "+str(multiplier*2)+" x "+str(give)+" "+item+" = "+str(give*multiplier*2)+" "+item+"</div>"
        self.solution_text = self.solution_text + "<div>"+person1+" had "+str(give*multiplier*2)+" "+item+" at first.</div>"   
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain
    
    def GenerateProblemType54(self):
        '''e.g.:Annie had 2 times as many flags as Betty. After Annie gave 25 flags to Betty, they both had the same number of flags.
                How many flags did Betty have at first? '''
        self.PersonNames = random.sample(PersonName.PersonName,2)
        self.ItemPool = ["notebooks","stamps","pencils","pens","marbles","flowers","buttons","toy cars","CDs","sticks",
                         "kites","books","red flags","blue flags","paper boats","rings","key chains","buns","straws","markers"]
        self.item = random.choice(self.ItemPool)
        self.person1 = self.PersonNames[0]
        self.person2 = self.PersonNames[1]
        self.MultiplierPool = {2:random.randrange(3,100,3)}
        self.multiplier = self.MultiplierPool.keys()[randint(0,len(self.MultiplierPool)-1)]
        self.number = self.MultiplierPool[self.multiplier]
        self.give = self.number/(self.multiplier+1)
        
        self.answer = self.give * 2

        self.problem1 = "%s had %d times as many %s as %s. After %s gave %d %s to %s, they both had the same number of %s. How many %s did %s have at first?"%(self.person1,self.multiplier,self.item,self.person2,self.person1,self.give,self.item,self.person2,self.item,self.item,self.person2) 
        self.problem = self.problem1

        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType54(self.problem,self.answer,self.item,self.person1,self.person2,self.multiplier,self.number,self.give)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"",'unit':self.item,'problem_type':"ProblemType54"}

    def ExplainType54(self,problem,answer,item,person1,person2,multiplier,number,give):
        self.answer_text = "The correct answer is: <b>"+str(answer)+" "+item
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'><tr>"
        for _i in range(multiplier+2):
            self.table_text = self.table_text + "<td></td>"
        self.table_text = self.table_text + "<td align='center'>"+str(give)+"<br><img src='/images/explanation/up_curly_braces_pt5cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td>"+person1+"</td>"
        for _i in range(multiplier+1):
            self.table_text = self.table_text + "<td><img src='/images/explanation/pink_block_pt5cm.png'></td>"
        for _i in range(2*multiplier-(multiplier+1)):
            self.table_text = self.table_text + "<td><img src='/images/explanation/green_block_pt5cm.png'></td>"
        self.table_text = self.table_text + "</tr><tr>"
        for _i in range(multiplier+1):
            self.table_text = self.table_text + "<td></td>"
        self.table_text = self.table_text + "<td colspan="+str(2*multiplier-(multiplier+1))+"><img src='/images/explanation/down_arrow.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td>"+person2+"</td>"
        for _i in range(2):
            self.table_text = self.table_text + "<td><img src='/images/explanation/green_block_pt5cm.png'></td>"
        for _i in range(multiplier-1):
            self.table_text = self.table_text + "<td><img src='/images/explanation/dotted_block_pt5cm.png'>"
        self.table_text = self.table_text + "</tr><tr><td></td>"    
        self.table_text = self.table_text + "<td align='center' colspan=2><img src='/images/explanation/down_curly_braces_1cm.png'><br>?</td>"
        self.table_text = self.table_text + "</tr></table><br>"
        
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>1 unit = "+str(give)+" "+item+"</div>"
        self.solution_text = self.solution_text + "<div>2 units = "+str(2)+" x "+str(give)+" "+item+" = "+str(give*2)+" "+item+"</div>"
        self.solution_text = self.solution_text + "<div>"+person2+" had "+str(give*2)+" "+item+" at first.</div>"   
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    def GenerateProblemType55(self):
        '''e.g.:Annie had 2 times as many flags as Betty. After Annie gave 25 flags to Betty, they both had the same number of flags. 
                How many flags does Annie have now? '''
        self.PersonNames = random.sample(PersonName.PersonName,2)
        self.ItemPool = ["notebooks","stamps","pencils","pens","marbles","flowers","buttons","toy cars","CDs","sticks",
                         "kites","books","red flags","blue flags","paper boats","rings","key chains","buns","straws","markers"]
        self.item = random.choice(self.ItemPool)
        self.person1 = self.PersonNames[0]
        self.person2 = self.PersonNames[1]
        self.MultiplierPool = {2:random.randrange(3,100,3)}
        self.multiplier = self.MultiplierPool.keys()[randint(0,len(self.MultiplierPool)-1)]
        self.number = self.MultiplierPool[self.multiplier]
        self.give = self.number/(self.multiplier+1)
        
        self.answer = self.give * 3

        self.problem1 = "%s had %d times as many %s as %s. After %s gave %d %s to %s, they both had the same number of %s. How many %s does %s have now?"%(self.person1,self.multiplier,self.item,self.person2,self.person1,self.give,self.item,self.person2,self.item,self.item,self.person1)
        self.problem = self.problem1

        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType55(self.problem,self.answer,self.item,self.person1,self.person2,self.multiplier,self.number,self.give)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"",'unit':self.item,'problem_type':"ProblemType55"}

    def ExplainType55(self,problem,answer,item,person1,person2,multiplier,number,give):
        self.answer_text = "The correct answer is: <b>"+str(answer)+" "+item
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'><tr>"
        self.table_text = self.table_text + "<td></td><td colspan=3 align='center'>?<br><img src='/images/explanation/up_curly_braces_2cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td>"+person1+"</td>"
        for _i in range(multiplier+1):
            self.table_text = self.table_text + "<td><img src='/images/explanation/pink_block_pt5cm.png'></td>"
        for _i in range(2*multiplier-(multiplier+1)):
            self.table_text = self.table_text + "<td><img src='/images/explanation/green_block_pt5cm.png'></td>"
        self.table_text = self.table_text + "</tr><tr>"
        for _i in range(multiplier+1):
            self.table_text = self.table_text + "<td></td>"
        self.table_text = self.table_text + "<td colspan="+str(2*multiplier-(multiplier+1))+"><img src='/images/explanation/down_arrow.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td>"+person2+"</td>"
        for _i in range(2):
            self.table_text = self.table_text + "<td><img src='/images/explanation/green_block_pt5cm.png'></td>"
        for _i in range(multiplier-1):
            self.table_text = self.table_text + "<td><img src='/images/explanation/dotted_block_pt5cm.png'>"
        self.table_text = self.table_text + "</tr><tr>"    
        for _i in range(3):
            self.table_text = self.table_text + "<td></td>"
        self.table_text = self.table_text + "<td align='center'><img src='/images/explanation/down_curly_braces_pt5cm.png'><br>"+str(give)+"</td>"
        self.table_text = self.table_text + "</tr></table><br>"
        
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>1 unit = "+str(give)+" "+item+"</div>"
        self.solution_text = self.solution_text + "<div>3 units = "+str(3)+" x "+str(give)+" "+item+" = "+str(give*3)+" "+item+"</div>"
        self.solution_text = self.solution_text + "<div>"+person1+" had "+str(give*multiplier*2)+" "+item+" now.</div>"   
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    '''Problem type 22 starts here'''
    def GenerateProblemType56(self):
        '''e.g.:Annie had 2 times as many flags as Betty. After borrowing some flags from Betty, Annie now has 5 times as many 
                flags as Betty. If they have 150 flags altogether, how many flags had Annie at first? '''
        self.PersonNames = random.sample(PersonName.GirlName,2)
        self.ItemPool = ["notebooks","stamps","pencils","pens","marbles","flowers","buttons","toy cars","CDs","sticks",
                         "kites","books","red flags","blue flags","paper boats","rings","key chains","buns","straws","markers"]
        self.item = random.choice(self.ItemPool)
        self.person1 = self.PersonNames[0]
        self.person2 = self.PersonNames[1]
        self.multiplier = 2
        self.number = random.randrange(6,100,6)
        self.give = self.number/(6)
        
        self.answer = self.give * 4
        
        self.problem1 = "%s had 2 times as many %s as %s. After borrowing some %s from %s, %s now has 5 times as many %s as %s. If they have %d %s altogether, how many %s had %s at first?"%(self.person1,self.item,self.person2,self.item,self.person2,self.person1,self.item,self.person2,self.number,self.item,self.item,self.person1)
        self.problem2 = "%s had 2 times as many %s as %s. After %s gave some of her %s to %s, %s had 5 times as many %s as %s. If they had %d %s altogether, how many %s had %s at first?"%(self.person1,self.item,self.person2,self.person2,self.item,self.person1,self.person1,self.item,self.person2,self.number,self.item,self.item,self.person1)
        self.problem3 = "%s had 2 times as many %s as %s. After %s got some %s from %s, %s had 5 times as many %s as %s. If they had %d %s altogether, find the number of %s that %s had at first."%(self.person1,self.item,self.person2,self.person1,self.item,self.person2,self.person1,self.item,self.person2,self.number,self.item,self.item,self.person1)
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])

        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType56(self.problem,self.answer,self.item,self.person1,self.person2,self.number,self.give)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"",'unit':self.item,'problem_type':"ProblemType56"}

    def ExplainType56(self,problem,answer,item,person1,person2,number,give):
        self.answer_text = "The correct answer is: <b>"+str(answer)+" "+item
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'><tr><td></td><td align='center' colspan=4>?<br>"
        self.table_text = self.table_text + "<img src='/images/explanation/up_curly_braces_2cm.png' width=128 height=24></td></tr>"
        self.table_text = self.table_text + "<tr><td>"+person1+"</td>"
        for _i in range(4):
            self.table_text = self.table_text + "<td><img src='/images/explanation/pink_block_pt5cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/green_block_pt5cm.png'></td>"
        self.table_text = self.table_text + "<td rowspan=3><img src='/images/explanation/right_curly_braces_2cm.png'></td>"
        self.table_text = self.table_text + "<td rowspan=3>"+str(number)+"</td></tr>"
        self.table_text = self.table_text + "<tr><td></td><td></td><td></td><td colspan=2><img src='/images/explanation/up_arrow_1cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td>"+person2+"</td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/green_block_pt5cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/dotted_block_pt5cm.png'></td>"
        self.table_text = self.table_text + "</tr></table><br>"
        
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>6 units = "+str(number)+" "+item+"</div>"
        self.solution_text = self.solution_text + "<div>1 unit = "+str(number)+" &divide; "+str(6)+" "+item+" = "+str(number/6)+" "+item+"</div>"
        self.solution_text = self.solution_text + "<div>4 units = "+str(4)+" x "+str(number/6)+" "+item+" = "+str(number*4/6)+" "+item+"</div>"
        self.solution_text = self.solution_text + "<div>"+person1+" had "+str(number*4/6)+" "+item+" at first.</div>"
        self.solution_text = self.solution_text + "<br><div> Watch below video for explanation of similar problem<br>"
        VideoLink = '<object><param name="movie" value="https://www.youtube.com/v/u1zgFlCw8Aw?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded"><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "uNMdYXnj6es";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
           
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    def GenerateProblemType57(self):
        '''e.g.:Annie had 2 times as many flags as Betty. After borrowing some flags from Betty, Annie now has 5 times as many flags as Betty. 
            If they have 150 flags altogether, how many flags had Betty at first?'''
        self.PersonNames = random.sample(PersonName.GirlName,2)
        self.ItemPool = ["notebooks","stamps","pencils","pens","marbles","flowers","buttons","toy cars","CDs","sticks",
                         "kites","books","red flags","blue flags","paper boats","rings","key chains","buns","straws","markers"]
        self.item = random.choice(self.ItemPool)
        self.person1 = self.PersonNames[0]
        self.person2 = self.PersonNames[1]
        self.multiplier = 2
        self.number = random.randrange(6,100,6)
        self.give = self.number/(6)
        
        self.answer = self.give * 2
        
        self.problem1 = "%s had 2 times as many %s as %s. After borrowing some %s from %s, %s now has 5 times as many %s as %s. If they have %d %s altogether, how many %s had %s at first?"%(self.person1,self.item,self.person2,self.item,self.person2,self.person1,self.item,self.person2,self.number,self.item,self.item,self.person2)
        self.problem2 = "%s had 2 times as many %s as %s. After %s gave some of her %s to %s, %s had 5 times as many %s as %s. If they had %d %s altogether, how many %s had %s at first?"%(self.person1,self.item,self.person2,self.person2,self.item,self.person1,self.person1,self.item,self.person2,self.number,self.item,self.item,self.person2) 
        self.problem3 = "%s had 2 times as many %s as %s. After %s got some %s from %s, %s had 5 times as many %s as %s. If they had %d %s altogether, find the number of %s that %s had at first."%(self.person1,self.item,self.person2,self.person1,self.item,self.person2,self.person1,self.item,self.person2,self.number,self.item,self.item,self.person2)
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])

        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType57(self.problem,self.answer,self.item,self.person1,self.person2,self.number,self.give)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"",'unit':self.item,'problem_type':"ProblemType57"}

    def ExplainType57(self,problem,answer,item,person1,person2,number,give):
        self.answer_text = "The correct answer is: <b>"+str(answer)+" "+item
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'>"
        self.table_text = self.table_text + "<tr><td>"+person1+"</td>"
        for _i in range(4):
            self.table_text = self.table_text + "<td><img src='/images/explanation/pink_block_pt5cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/green_block_pt5cm.png'></td>"
        self.table_text = self.table_text + "<td rowspan=3><img src='/images/explanation/right_curly_braces_2cm.png'></td>"
        self.table_text = self.table_text + "<td rowspan=3>"+str(number)+"</td></tr>"
        self.table_text = self.table_text + "<tr><td></td><td></td><td></td><td colspan=2><img src='/images/explanation/up_arrow_1cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td>"+person2+"</td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/green_block_pt5cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/dotted_block_pt5cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td></td><td align='center' colspan=2><img src='/images/explanation/down_curly_braces_1cm.png'><br>"
        self.table_text = self.table_text + "?</td>"
        self.table_text = self.table_text + "</tr></table><br>"
        
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>6 units = "+str(number)+" "+item+"</div>"
        self.solution_text = self.solution_text + "<div>1 unit = "+str(number)+" &divide; "+str(6)+" "+item+" = "+str(number/6)+" "+item+"</div>"
        self.solution_text = self.solution_text + "<div>2 units = "+str(2)+" x "+str(number/6)+" "+item+" = "+str(number*2/6)+" "+item+"</div>"
        self.solution_text = self.solution_text + "<div>"+person2+" had "+str(number*2/6)+" "+item+" at first.</div>"
           
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    def GenerateProblemType58(self):
        '''e.g.:Annie had 2 times as many flags as Betty. After borrowing some flags from Betty, Annie now has 5 times as many flags as Betty. 
                If they have 150 flags altogether, how many flags has Annie now?'''
        self.PersonNames = random.sample(PersonName.GirlName,2)
        self.ItemPool = ["notebooks","stamps","pencils","pens","marbles","flowers","buttons","toy cars","CDs","sticks",
                         "kites","books","red flags","blue flags","paper boats","rings","key chains","buns","straws","markers"]
        self.item = random.choice(self.ItemPool)
        self.person1 = self.PersonNames[0]
        self.person2 = self.PersonNames[1]
        self.multiplier = 2
        self.number = random.randrange(6,100,6)
        self.give = self.number/(6)
        
        self.answer = self.give * 5
        
        self.problem1 = "%s had 2 times as many %s as %s. After borrowing some %s from %s, %s now has 5 times as many %s as %s. If they have %d %s altogether, how many %s has %s now?"%(self.person1,self.item,self.person2,self.item,self.person2,self.person1,self.item,self.person2,self.number,self.item,self.item,self.person1)
        self.problem2 = "%s had 2 times as many %s as %s. After receiving some %s from %s, %s now has 5 times as many %s as %s. If they had %d %s altogether, how many %s has %s now?"%(self.person1,self.item,self.person2,self.item,self.person2,self.person1,self.item,self.person2,self.number,self.item,self.item,self.person1)
        self.problem3 = "%s had 2 times as many %s as %s. After getting some %s from %s, %s now has 5 times as many %s as %s. If they had %d %s altogether, find the number of %s that %s has now?"%(self.person1,self.item,self.person2,self.item,self.person2,self.person1,self.item,self.person2,self.number,self.item,self.item,self.person1)
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])

        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType58(self.problem,self.answer,self.item,self.person1,self.person2,self.number,self.give)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"",'unit':self.item,'problem_type':"ProblemType58"}

    def ExplainType58(self,problem,answer,item,person1,person2,number,give):
        self.answer_text = "The correct answer is: <b>"+str(answer)+" "+item
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'><tr><td></td><td align='center' colspan=5>?<br>"
        self.table_text = self.table_text + "<img src='/images/explanation/up_curly_braces_2cm.png' width=170 height=24></td></tr>"
        self.table_text = self.table_text + "<tr><td>"+person1+"</td>"
        for _i in range(4):
            self.table_text = self.table_text + "<td><img src='/images/explanation/pink_block_pt5cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/green_block_pt5cm.png'></td>"
        self.table_text = self.table_text + "<td rowspan=3><img src='/images/explanation/right_curly_braces_2cm.png'></td>"
        self.table_text = self.table_text + "<td rowspan=3>"+str(number)+"</td></tr>"
        self.table_text = self.table_text + "<tr><td></td><td></td><td></td><td colspan=2><img src='/images/explanation/up_arrow_1cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td>"+person2+"</td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/green_block_pt5cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/dotted_block_pt5cm.png'></td>"
        self.table_text = self.table_text + "</tr></table><br>"
        
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>6 units = "+str(number)+" "+item+"</div>"
        self.solution_text = self.solution_text + "<div>1 unit = "+str(number)+" &divide; "+str(6)+" "+item+" = "+str(number/6)+" "+item+"</div>"
        self.solution_text = self.solution_text + "<div>5 units = "+str(5)+" x "+str(number/6)+" "+item+" = "+str(number*5/6)+" "+item+"</div>"
        self.solution_text = self.solution_text + "<div>"+person1+" has "+str(number*5/6)+" "+item+" now.</div>"
           
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain
    
    def GenerateProblemType59(self):
        '''e.g.:Annie had 2 times as many flags as Betty. After borrowing some flags from Betty, Annie now has 5 times as many flags as Betty. 
            If they have 150 flags altogether, how many flags has Betty now?'''
        self.PersonNames = random.sample(PersonName.GirlName,2)
        self.ItemPool = ["notebooks","stamps","pencils","pens","marbles","flowers","buttons","toy cars","CDs","sticks",
                         "kites","books","red flags","blue flags","paper boats","rings","key chains","buns","straws","markers"]
        self.item = random.choice(self.ItemPool)
        self.person1 = self.PersonNames[0]
        self.person2 = self.PersonNames[1]
        self.multiplier = 2
        self.number = random.randrange(6,100,6)
        self.give = self.number/(6)
        
        self.answer = self.give
        
        self.problem1 = "%s had 2 times as many %s as %s. After borrowing some %s from %s, %s now has 5 times as many %s as %s. If they have %d %s altogether, how many %s has %s now?"%(self.person1,self.item,self.person2,self.item,self.person2,self.person1,self.item,self.person2,self.number,self.item,self.item,self.person2)
        self.problem2 = "%s had 2 times as many %s as %s. After %s gave some of her %s to %s, %s had 5 times as many %s as %s. If they had %d %s altogether, how many %s has %s now?"%(self.person1,self.item,self.person2,self.person2,self.item,self.person1,self.person1,self.item,self.person2,self.number,self.item,self.item,self.person2) 
        self.problem3 = "%s had 2 times as many %s as %s. After %s got some %s from %s, %s had 5 times as many %s as %s. If they had %d %s altogether, find the number of %s that %s has now."%(self.person1,self.item,self.person2,self.person1,self.item,self.person2,self.person1,self.item,self.person2,self.number,self.item,self.item,self.person2)
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])

        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType59(self.problem,self.answer,self.item,self.person1,self.person2,self.number,self.give)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"",'unit':self.item,'problem_type':"ProblemType59"}

    def ExplainType59(self,problem,answer,item,person1,person2,number,give):
        self.answer_text = "The correct answer is: <b>"+str(answer)+" "+item
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'>"
        self.table_text = self.table_text + "<tr><td>"+person1+"</td>"
        for _i in range(4):
            self.table_text = self.table_text + "<td><img src='/images/explanation/pink_block_pt5cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/green_block_pt5cm.png'></td>"
        self.table_text = self.table_text + "<td rowspan=3><img src='/images/explanation/right_curly_braces_1cm.png'></td>"
        self.table_text = self.table_text + "<td rowspan=3>"+str(number)+"</td></tr>"
        self.table_text = self.table_text + "<tr><td></td><td></td><td></td><td colspan=2><img src='/images/explanation/up_arrow_1cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td>"+person2+"</td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/green_block_pt5cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/dotted_block_pt5cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td></td><td align='center'><img src='/images/explanation/down_curly_braces_pt5cm.png'><br>"
        self.table_text = self.table_text + "?</td>"
        self.table_text = self.table_text + "</tr></table><br>"
        
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>6 units = "+str(number)+" "+item+"</div>"
        self.solution_text = self.solution_text + "<div>1 unit = "+str(number)+" &divide; "+str(6)+" "+item+" = "+str(number/6)+" "+item+"</div>"
        self.solution_text = self.solution_text + "<div>"+person2+" has "+str(number/6)+" "+item+" now.</div>"
           
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    '''Problem Type 26 starts here'''
    def GenerateProblemType60(self):
        '''e.g.:Annie had 4 times as many flags as Betty. Charles had 3 times as many flags as Betty. 
                After Charles gave 10 flags away and Annie gave 30 flags to Betty, 
                they each had the same number of flags left. How many flags had Betty at first?'''
        self.PersonNames = random.sample(PersonName.PersonName,3)
        self.ItemPool = ["notebooks","stamps","pencils","pens","marbles","flowers","buttons","toy cars","CDs","sticks",
                         "kites","books","red flags","blue flags","paper boats","rings","key chains","buns","straws","markers"]
        self.item = random.choice(self.ItemPool)
        self.person1 = self.PersonNames[0]
        self.person2 = self.PersonNames[1]
        self.person3 = self.PersonNames[2]
        self.b = random.randrange(10,100,2)
        self.a = 4 * self.b
        self.c = 3 * self.b
        self.a_give = self.a - (self.a+self.b)/2
        self.c_give = self.c - (self.a+self.b)/2
        
        self.answer = self.b

        self.problem1 = "%s had 4 times as many %s as %s. %s had 3 times as many %s as %s. After %s gave %d %s away and %s gave %d %s to %s, they each had the same number of %s left. How many %s had %s at first?"%(self.person1,self.item,self.person2,self.person3,self.item,self.person2,self.person3,self.c_give,self.item,self.person1,self.a_give,self.item,self.person2,self.item,self.item,self.person2)
        self.problem = random.choice([self.problem1])

        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType60(self.problem,self.answer,self.item,self.person1,self.person2,self.person3,self.b,self.a,self.c,self.a_give,self.c_give)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"",'unit':self.item,'problem_type':"ProblemType60"}

    def ExplainType60(self,problem,answer,item,person1,person2,person3,b,a,c,a_give,c_give):
        self.answer_text = "The correct answer is: <b>"+str(answer)+" "+item
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'>"
        self.table_text = self.table_text + "<tr><td>"+person1+"</td>"
        self.table_text = self.table_text + "<td colspan=4><img src='/images/explanation/P5_WN_PT60_A.png'></td><tr>"
        self.table_text = self.table_text + "<tr><td>"+person3+"</td>"
        self.table_text = self.table_text + "<td colspan=4><img src='/images/explanation/P5_WN_PT60_B.png'></td><tr>"
        self.table_text = self.table_text + "<tr><td>"+person2+"</td>"
        self.table_text = self.table_text + "<td colspan=4><img src='/images/explanation/P5_WN_PT60_C.png'></td><tr>"
        self.table_text = self.table_text + "<tr><td></td><td colspan=3><img src='/images/explanation/down_curly_braces_1cm.png'>"
        self.table_text = self.table_text + "<img src='/images/explanation/down_curly_braces_1pt5cm.png'>"
        self.table_text = self.table_text + "<img src='/images/explanation/down_curly_braces_pt5cm.png'></td>"
        self.table_text = self.table_text + "<tr><td></td><td align='center'>?</td>"
        self.table_text = self.table_text + "<td align='center'>"+str(a_give)+"</td>"
        self.table_text = self.table_text + "<td>"+str(c_give)+"</td>"      
        self.table_text = self.table_text + "</tr></table><br>"
        
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>Let 1 unit (or 1 pink block) represent "+person2+"'s "+item+".</div>" 
        self.solution_text = self.solution_text + "<div>The dotted yellow block represents the "+str(a_give)+" "+item+" that "+person1+" gave "+person2+".</div>"
        self.solution_text = self.solution_text + "<div>The grey block represents the "+str(c_give)+" "+item+" that "+person3+" gave away.</div><br>"
        self.solution_text = self.solution_text + "<div>2 units = "+str(a_give)+" "+item+" + "+str(c_give)+" "+item+" = "+str(a_give+c_give)+" "+item+"</div>"
        self.solution_text = self.solution_text + "<div>1 unit = "+str(a_give+c_give)+" &divide; "+str(2)+" "+item+" = "+str((a_give+c_give)/2)+" "+item+"</div>"
        self.solution_text = self.solution_text + "<div>"+person2+" had "+str((a_give+c_give)/2)+" "+item+" at first.</div>"
        self.solution_text = self.solution_text + "<br><div> Watch below video for explanation of similar problem<br>"
        VideoLink = '<object><param name="movie" value="https://www.youtube.com/v/u1zgFlCw8Aw?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded"><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "XNvBwS86uAM";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
           
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    def GenerateProblemType61(self):
        '''e.g.:Annie had 4 times as many flags as Betty. Charles had 3 times as many flags as Betty. After Charles gave 10 flags away and Annie gave 
                30 flags to Betty, they each had the same number of flags. How many flags had each of them now?'''
        self.PersonNames = random.sample(PersonName.PersonName,3)
        self.ItemPool = ["notebooks","stamps","pencils","pens","marbles","flowers","buttons","toy cars","CDs","sticks",
                         "kites","books","red flags","blue flags","paper boats","rings","key chains","buns","straws","markers"]
        self.item = random.choice(self.ItemPool)
        self.person1 = self.PersonNames[0]
        self.person2 = self.PersonNames[1]
        self.person3 = self.PersonNames[2]
        self.b = random.randrange(10,100,2)
        self.a = 4 * self.b
        self.c = 3 * self.b
        self.a_give = self.a - (self.a+self.b)/2
        self.c_give = self.c - (self.a+self.b)/2
        
        self.answer = self.b + self.a_give
        
        self.problem1 = "%s had 4 times as many %s as %s. %s had 3 times as many %s as %s. After %s gave %d %s away and %s gave %d %s to %s, they each had the same number of %s. How many %s have each of them now?"%(self.person1,self.item,self.person2,self.person3,self.item,self.person2,self.person3,self.c_give,self.item,self.person1,self.a_give,self.item,self.person2,self.item,self.item)
        self.problem2 = "%s had 3 times as many %s as %s. %s had 4 times as many %s as %s. After %s gave %d %s away and %s gave %d %s to %s, they each had the same number of %s. Find the number of %s they each have now."%(self.person3,self.item,self.person2,self.person1,self.item,self.person2,self.person3,self.c_give,self.item,self.person1,self.a_give,self.item,self.person1,self.item,self.item)
        self.problem = random.choice([self.problem1,self.problem2])

        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType61(self.problem,self.answer,self.item,self.person1,self.person2,self.person3,self.b,self.a,self.c,self.a_give,self.c_give)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"",'unit':self.item,'problem_type':"ProblemType61"}

    def ExplainType61(self,problem,answer,item,person1,person2,person3,b,a,c,a_give,c_give):
        self.answer_text = "The correct answer is: <b>"+str(answer)+" "+item
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'>"
        self.table_text = self.table_text + "<tr><td>"+person1+"</td>"
        self.table_text = self.table_text + "<td colspan=4><img src='/images/explanation/P5_WN_PT60_A.png'></td><tr>"
        self.table_text = self.table_text + "<tr><td>"+person3+"</td>"
        self.table_text = self.table_text + "<td colspan=4><img src='/images/explanation/P5_WN_PT60_B.png'></td><tr>"
        self.table_text = self.table_text + "<tr><td>"+person2+"</td>"
        self.table_text = self.table_text + "<td colspan=4><img src='/images/explanation/P5_WN_PT60_C.png'></td><tr>"
        self.table_text = self.table_text + "<tr><td></td><td width=50></td><td colspan=2>"
        self.table_text = self.table_text + "<img src='/images/explanation/down_curly_braces_1pt5cm.png'>"
        self.table_text = self.table_text + "<img src='/images/explanation/down_curly_braces_pt5cm.png'></td>"
        self.table_text = self.table_text + "<tr><td></td><td></td>"
        self.table_text = self.table_text + "<td align='center'>"+str(a_give)+"</td>"
        self.table_text = self.table_text + "<td align='left'>"+str(c_give)+"</td><tr>"
        self.table_text = self.table_text + "<tr><td></td><td colspan=2><img src ='/images/explanation/down_curly_braces_3cm.png' width=152><br>?</td>"      
        self.table_text = self.table_text + "</tr></table><br>"
        
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>Let 1 unit (or 1 pink block) represent "+person2+"'s "+item+".</div>" 
        self.solution_text = self.solution_text + "<div>The dotted yellow block represents the "+str(a_give)+" "+item+" that "+person1+" gave "+person2+".</div>"
        self.solution_text = self.solution_text + "<div>The grey block represents the "+str(c_give)+" "+item+" that "+person3+" gave away.</div><br>"
        self.solution_text = self.solution_text + "<div>2 units = "+str(a_give)+" "+item+" + "+str(c_give)+" "+item+" = "+str(a_give+c_give)+" "+item+"</div>"
        self.solution_text = self.solution_text + "<div>1 unit = "+str(a_give+c_give)+" &divide; "+str(2)+" "+item+" = "+str((a_give+c_give)/2)+" "+item+"</div>"
        self.solution_text = self.solution_text + "<div>"+str((a_give+c_give)/2)+" "+item+" + "+str(a_give)+" "+item+" = "+str(((a_give+c_give)/2)+a_give)+" "+item+"</div>"
        self.solution_text = self.solution_text + "<div>Each of them had "+str(((a_give+c_give)/2)+a_give)+" "+item+" now.</div>"
           
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    def GenerateProblemType62(self):
        '''e.g.:Annie had 4 times as many flags as Betty. Charles had 3 times as many flags as Betty. 
                After Charles gave 10 flags away and Annie gave 30 flags to Betty, they each had the same number of flags. 
                How many flags had Annie at first?'''
        self.PersonNames = random.sample(PersonName.PersonName,3)
        self.ItemPool = ["notebooks","stamps","pencils","pens","marbles","flowers","buttons","toy cars","CDs","sticks",
                         "kites","books","red flags","blue flags","paper boats","rings","key chains","buns","straws","markers"]
        self.item = random.choice(self.ItemPool)
        self.person1 = self.PersonNames[0]
        self.person2 = self.PersonNames[1]
        self.person3 = self.PersonNames[2]
        self.b = random.randrange(10,100,2)
        self.a = 4 * self.b
        self.c = 3 * self.b
        self.a_give = self.a - (self.a+self.b)/2
        self.c_give = self.c - (self.a+self.b)/2
        
        self.answer = self.a
        
        self.problem1 = "%s had 4 times as many %s as %s. %s had 3 times as many %s as %s. After %s gave %d %s away and %s gave %d %s to %s, they each had the same number of %s. How many %s had %s at first?"%(self.person1,self.item,self.person2,self.person3,self.item,self.person2,self.person3,self.c_give,self.item,self.person1,self.a_give,self.item,self.person2,self.item,self.item,self.person1)
        self.problem2 = "%s had 3 times as many %s as %s. %s had 4 times as many %s as %s. After %s gave %d %s away and %s gave %d %s to %s, they each had the same number of %s. Find the number of %s %s had at first."%(self.person3,self.item,self.person2,self.person1,self.item,self.person2,self.person3,self.c_give,self.item,self.person1,self.a_give,self.item,self.person1,self.item,self.item,self.person1)
        self.problem = random.choice([self.problem1,self.problem2])

        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType62(self.problem,self.answer,self.item,self.person1,self.person2,self.person3,self.b,self.a,self.c,self.a_give,self.c_give)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"",'unit':self.item,'problem_type':"ProblemType62"}

    def ExplainType62(self,problem,answer,item,person1,person2,person3,b,a,c,a_give,c_give):
        self.answer_text = "The correct answer is: <b>"+str(answer)+" "+item
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'>"
        self.table_text = self.table_text + "<tr><td></td><td colspan=3 align='center'>?<br><img src ='/images/explanation/up_curly_braces_3cm.png' width=240 height=24></td></tr>"
        self.table_text = self.table_text + "<tr><td>"+person1+"</td>"
        self.table_text = self.table_text + "<td colspan=4><img src='/images/explanation/P5_WN_PT60_A.png'></td><tr>"
        self.table_text = self.table_text + "<tr><td>"+person3+"</td>"
        self.table_text = self.table_text + "<td colspan=4><img src='/images/explanation/P5_WN_PT60_B.png'></td><tr>"
        self.table_text = self.table_text + "<tr><td>"+person2+"</td>"
        self.table_text = self.table_text + "<td colspan=4><img src='/images/explanation/P5_WN_PT60_C.png'></td><tr>"
        self.table_text = self.table_text + "<tr><td></td><td width=50></td><td colspan=2>"
        self.table_text = self.table_text + "<img src='/images/explanation/down_curly_braces_1pt5cm.png'>"
        self.table_text = self.table_text + "<img src='/images/explanation/down_curly_braces_pt5cm.png'></td>"
        self.table_text = self.table_text + "<tr><td></td><td></td>"
        self.table_text = self.table_text + "<td align='center'>"+str(a_give)+"</td>"
        self.table_text = self.table_text + "<td align='left'>"+str(c_give)+"</td><tr>"
        self.table_text = self.table_text + "</tr></table><br>"
        
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>Let 1 unit (or 1 pink block) represent "+person2+"'s "+item+".</div>" 
        self.solution_text = self.solution_text + "<div>The dotted yellow block represents the "+str(a_give)+" "+item+" that "+person1+" gave "+person2+".</div>"
        self.solution_text = self.solution_text + "<div>The grey block represents the "+str(c_give)+" "+item+" that "+person3+" gave away.</div><br>"
        self.solution_text = self.solution_text + "<div>2 units = "+str(a_give)+" "+item+" + "+str(c_give)+" "+item+" = "+str(a_give+c_give)+" "+item+"</div>"
        self.solution_text = self.solution_text + "<div>1 unit = "+str(a_give+c_give)+" &divide; "+str(2)+" "+item+" = "+str((a_give+c_give)/2)+" "+item+"</div>"
        self.solution_text = self.solution_text + "<div>4 units = "+str(4)+" x "+str((a_give+c_give)/2)+" "+item+" = "+str(4*((a_give+c_give)/2))+" "+item+"</div><br>"
        self.solution_text = self.solution_text + "<div>"+person1+" had "+str(4*((a_give+c_give)/2))+" "+item+" at first.</div>"
           
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    '''Problem Type 26 starts here'''
    def GenerateProblemType63(self):
        '''e.g.:Annie earns $2450 a month. Betty earns $300 less than Annie each month. How much do they earn together in a year?'''
        self.PersonNames = random.sample(PersonName.PersonName,2)
        self.MoneyPool = {"earn":randint(1700,8800),"spend":randint(1500,5500),"save":randint(1500,6000),"donate":randint(100,400)}
        self.money = self.MoneyPool.keys()[randint(0,len(self.MoneyPool)-1)]
        self.amount = self.MoneyPool[self.money]
        self.person1 = self.PersonNames[0]
        self.person2 = self.PersonNames[1]
        self.diff = self.amount * randint(8,40)/100
       
        self.answer = (self.amount + self.amount - self.diff)*12
        
        self.problem1 = "%s %ss $%d a month. %s %ss $%d less than %s each month. How much do they %s together in a year?"%(self.person1,self.money,self.amount,self.person2,self.money,self.diff,self.person1,self.money)
        self.problem2 = "%s %ss $%d less than %s each month. If %s %ss $%d a month, find how much they %s together in a year."%(self.person2,self.money,self.diff,self.person1,self.person1,self.money,self.amount,self.money)
        self.problem3 = "%s %ss $%d more than %s each month. If %s %ss $%d a month, find how much they %s together in a year."%(self.person1,self.money,self.diff,self.person2,self.person1,self.money,self.amount,self.money)
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])

        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType63(self.problem,self.answer,self.person1,self.person2,self.money,self.amount,self.diff)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"$",'unit':"",'problem_type':"ProblemType63"}

    def ExplainType63(self,problem,answer,person1,person2,money,amount,diff):
        self.answer_text = "The correct answer is: <b>$"+str(answer)
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'>"
        self.table_text = self.table_text + "<tr><td></td><td align='center' colspan=2>$"+str(amount)+"<br>"
        self.table_text = self.table_text + "<img src='/images/explanation/up_curly_braces_2cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td>"+person1+"</td><td colspan=2><img src='/images/explanation/pink_block_3cm.png'></td>"
        self.table_text = self.table_text + "<td rowspan=2><img src='/images/explanation/right_curly_braces_1cm.png'></td>"
        self.table_text = self.table_text + "<td rowspan=2>?</td></tr>"
        self.table_text = self.table_text + "<tr><td>"+person2+"</td><td><img src='/images/explanation/green_block_2cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td></td><td></td><td align='center'><img src='/images/explanation/down_curly_braces_pt7cm.png'><br>$"+str(diff)+"</td>"
        self.table_text = self.table_text + "</tr></table><br>"
        
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(amount)+" - $"+str(diff)+" = $"+str(amount-diff)+"</div>" 
        self.solution_text = self.solution_text + "<div>"+person2+" "+money+"s $"+str(amount-diff)+" a month.</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(amount)+" + $"+str(amount-diff)+" = $"+str(2*amount-diff)+"</div>"
        self.solution_text = self.solution_text + "<div>They "+money+" $"+str(2*amount-diff)+" together in a month.</div><br>"
        self.solution_text = self.solution_text + "<div>12 x $"+str(2*amount-diff)+" = $"+str(12*(2*amount-diff))+"</div>"
        self.solution_text = self.solution_text + "<div>They "+money+" $"+str(12*(2*amount-diff))+" together in a year.</div>"
           
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    '''Problem Type 27 starts here'''
    def GenerateProblemType64(self):
        '''e.g.:Annie earns $300 a month more than Betty. Betty earns $2150 a month. How much do they earn together in a year?'''
        self.PersonNames = random.sample(PersonName.PersonName,2)
        self.MoneyPool = {"earn":randint(1700,8800),"spend":randint(1500,5500),"save":randint(1500,6000),"donate":randint(100,400)}
        self.money = self.MoneyPool.keys()[randint(0,len(self.MoneyPool)-1)]
        self.amount = self.MoneyPool[self.money]
        self.person1 = self.PersonNames[0]
        self.person2 = self.PersonNames[1]
        self.diff = self.amount * randint(8,40)/100
                
        self.answer = (self.amount + self.amount + self.diff)*12
        
        self.problem1 = "%s %ss $%d a month more than %s. %s %ss $%d a month. How much do they %s together in a year?"%(self.person1,self.money,self.diff,self.person2,self.person2,self.money,self.amount,self.money)
        self.problem2 = "%s %ss $%d a month. If %s %ss $%d more than %s each month, how much do they %s together in a year?"%(self.person2,self.money,self.amount,self.person1,self.money,self.diff,self.person2,self.money)
        self.problem3 = "%s %ss $%d less than %s a month. If %s %ss $%d each month, find how much they %s together in a year."%(self.person2,self.money,self.diff,self.person1,self.person2,self.money,self.amount,self.money)
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])

        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType64(self.problem,self.answer,self.person1,self.person2,self.money,self.amount,self.diff)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"$",'unit':"",'problem_type':"ProblemType64"}

    def ExplainType64(self,problem,answer,person1,person2,money,amount,diff):
        self.answer_text = "The correct answer is: <b>$"+str(answer)
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'>"
        self.table_text = self.table_text + "<tr><td>"+person1+"</td><td colspan=2><img src='/images/explanation/pink_block_3cm.png'></td>"
        self.table_text = self.table_text + "<td rowspan=2><img src='/images/explanation/right_curly_braces_1cm.png'></td>"
        self.table_text = self.table_text + "<td rowspan=2>?</td></tr>"
        self.table_text = self.table_text + "<tr><td>"+person2+"</td><td><img src='/images/explanation/green_block_2cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td></td><td align='center'><img src='/images/explanation/down_curly_braces_2cm.png'><br>$"+str(amount)+"</td>"
        self.table_text = self.table_text + "<td align='center'><img src='/images/explanation/down_curly_braces_1cm.png'><br>$"+str(diff)+"</td>"
        self.table_text = self.table_text + "</tr></table><br>"
        
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(amount)+" + $"+str(diff)+" = $"+str(amount+diff)+"</div>" 
        self.solution_text = self.solution_text + "<div>"+person1+" "+money+"s $"+str(amount+diff)+" a month.</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(amount)+" + $"+str(amount+diff)+" = $"+str(2*amount+diff)+"</div>"
        self.solution_text = self.solution_text + "<div>They "+money+" $"+str(2*amount+diff)+" together in a month.</div><br>"
        self.solution_text = self.solution_text + "<div>12 x $"+str(2*amount+diff)+" = $"+str(12*(2*amount+diff))+"</div>"
        self.solution_text = self.solution_text + "<div>They "+money+" $"+str(12*(2*amount+diff))+" together in a year.</div>"
           
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    '''Problem Type 28 starts here'''
    def GenerateProblemType65(self):
        '''e.g.:Annie and Betty earn a total of $55200 a year. If Annie earns $2450 a month, how much more than Betty does she earn each month?'''
        self.PersonNames = random.sample(PersonName.GirlName,2)
        self.MoneyPool = {"earn":randint(1700,8800),"spend":randint(1500,5500),"save":randint(1500,6000),"donate":randint(100,400)}
        self.money = self.MoneyPool.keys()[randint(0,len(self.MoneyPool)-1)]
        self.amount = self.MoneyPool[self.money]
        self.person1 = self.PersonNames[0]
        self.person2 = self.PersonNames[1]
        self.diff = self.amount * randint(8,40)/100
        self.total = (2*self.amount-self.diff)*12
       
        self.answer = self.diff
        
        self.problem1 = "%s and %s %s a total of $%d a year. If %s %ss $%d a month, how much more than %s does she %s each month?"%(self.person1,self.person2,self.money,self.total,self.person1,self.money,self.amount,self.person2,self.money)
        self.problem2 = "%s %ss $%d a month. %s and %s %s a total of $%d a year. How much more than %s does %s %s each month?"%(self.person1,self.money,self.amount,self.person1,self.person2,self.money,self.total,self.person2,self.person1,self.money)
        self.problem = random.choice([self.problem1,self.problem2])

        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType65(self.problem,self.answer,self.person1,self.person2,self.money,self.amount,self.diff,self.total)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"$",'unit':"",'problem_type':"ProblemType65"}

    def ExplainType65(self,problem,answer,person1,person2,money,amount,diff,total):
        self.answer_text = "The correct answer is: <b>$"+str(answer)
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'>"
        self.table_text = self.table_text + "<tr><td></td><td align='center' colspan=2>$"+str(amount)+"<br>"
        self.table_text = self.table_text + "<img src='/images/explanation/up_curly_braces_2cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td>"+person1+"</td><td colspan=2><img src='/images/explanation/pink_block_3cm.png'></td>"
        self.table_text = self.table_text + "<td rowspan=2><img src='/images/explanation/right_curly_braces_1cm.png'></td>"
        self.table_text = self.table_text + "<td rowspan=2>$"+str(total)+"&divide;"+str(12)+"</td></tr>"
        self.table_text = self.table_text + "<tr><td>"+person2+"</td><td><img src='/images/explanation/green_block_2cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td></td><td></td><td align='center'><img src='/images/explanation/down_curly_braces_pt7cm.png'><br>?</td>"
        self.table_text = self.table_text + "</tr></table><br>"
        
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(total)+" &divide; "+str(12)+" = $"+str(total/12)+"</div>"
        self.solution_text = self.solution_text + "<div>"+person1+" and "+person2+" "+money+" $"+str(total/12)+" together in a month.</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(total/12)+" - $"+str(amount)+" = $"+str((total/12)-amount)+"</div>"
        self.solution_text = self.solution_text + "<div>"+person2+" "+money+"s $"+str((total/12)-amount)+" a month.</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(amount)+" - $"+str((total/12)-amount)+" = $"+str(amount-((total/12)-amount))+"</div>"
        self.solution_text = self.solution_text + "<div>"+person1+" "+money+"s $"+str(amount-((total/12)-amount))+" more than "+person2+" each month.</div>"
           
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    def GenerateProblemType66(self):
        '''e.g.:Annie and Betty earn a total of $55200 a year. If Annie earns $2450 a month, how much less than Annie does Betty earn each month?'''
        self.PersonNames = random.sample(PersonName.GirlName,2)
        self.MoneyPool = {"earn":randint(1700,8800),"spend":randint(1500,5500),"save":randint(1500,6000),"donate":randint(100,400)}
        self.money = self.MoneyPool.keys()[randint(0,len(self.MoneyPool)-1)]
        self.amount = self.MoneyPool[self.money]
        self.person1 = self.PersonNames[0]
        self.person2 = self.PersonNames[1]
        self.diff = self.amount * randint(8,40)/100
        self.total = (2*self.amount-self.diff)*12
        
        self.answer = self.diff

        self.problem1 = "%s and %s %s a total of $%d a year. If %s %ss $%d a month, how much less than %s does %s %s each month?"%(self.person1,self.person2,self.money,self.total,self.person1,self.money,self.amount,self.person1,self.person2,self.money)
        self.problem2 = "%s %ss $%d a month. %s and %s %s a total of $%d a year. How much less than %s does %s %s each month?"%(self.person1,self.money,self.amount,self.person1,self.person2,self.money,self.total,self.person1,self.person2,self.money)
        self.problem = random.choice([self.problem1,self.problem2])

        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType66(self.problem,self.answer,self.person1,self.person2,self.money,self.amount,self.diff,self.total)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"$",'unit':"",'problem_type':"ProblemType66"}

    def ExplainType66(self,problem,answer,person1,person2,money,amount,diff,total):
        self.answer_text = "The correct answer is: <b>$"+str(answer)
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'>"
        self.table_text = self.table_text + "<tr><td></td><td align='center' colspan=2>$"+str(amount)+"<br>"
        self.table_text = self.table_text + "<img src='/images/explanation/up_curly_braces_3cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td>"+person1+"</td><td colspan=2><img src='/images/explanation/pink_block_3cm.png'></td>"
        self.table_text = self.table_text + "<td rowspan=2><img src='/images/explanation/right_curly_braces_1cm.png'></td>"
        self.table_text = self.table_text + "<td rowspan=2>$"+str(total)+"&divide;"+str(12)+"</td></tr>"
        self.table_text = self.table_text + "<tr><td>"+person2+"</td><td><img src='/images/explanation/green_block_2cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td></td><td></td><td align='center'><img src='/images/explanation/down_curly_braces_pt7cm.png'><br>?</td>"
        self.table_text = self.table_text + "</tr></table><br>"
        
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(total)+" &divide; "+str(12)+" = $"+str(total/12)+"</div>"
        self.solution_text = self.solution_text + "<div>"+person1+" and "+person2+" "+money+" $"+str(total/12)+" together in a month.</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(total/12)+" - $"+str(amount)+" = $"+str((total/12)-amount)+"</div>"
        self.solution_text = self.solution_text + "<div>"+person2+" "+money+"s $"+str((total/12)-amount)+" a month.</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(amount)+" - $"+str((total/12)-amount)+" = $"+str(amount-((total/12)-amount))+"</div>"
        self.solution_text = self.solution_text + "<div>"+person2+" "+money+"s $"+str(amount-((total/12)-amount))+" less than "+person1+" each month.</div>"
           
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    '''Problem type 29 starts here'''
    def GenerateProblemType67(self):
        '''e.g.:Annie receives 3 times as much monthly salary as Betty. If their total monthly salary is $6000, find the difference in the monthly salary that they receive.'''
        self.PersonNames = random.sample(PersonName.PersonName,2)
        self.ItemPool = {"monthly salary":randint(1700,4500),"monthly allowance":randint(1300,2000),"weekly allowance":randint(100,400),"weekly pocket money":randint(100,400),
        		"monthly pocket money":randint(100,1000),"sales commission":randint(1000,2500),"sales income":randint(1000,2500),"weekly stipend":randint(100,300),
        		"monthly stipend":randint(1200,2000),"monthly fees":randint(150,1500),"weekly fees":randint(50,500),"monthly subsidy":randint(100,200),
        		"yearly subsidy":randint(200,700),"yearly bonus":randint(1000,5000),"monthly bonus":randint(200,700),"yearly child care subsidy":randint(200,500),
        		"monthly child care subsidy":randint(50,200),"yearly tax benefit":randint(1000,2000),"monthly tax benefit":randint(100,200)
        		}
        self.item = self.ItemPool.keys()[randint(0,len(self.ItemPool)-1)]
        self.amount = self.ItemPool[self.item]
        self.person1 = self.PersonNames[0]
        self.person2 = self.PersonNames[1]
        self.multiplier = randint(2,5)
        self.total = self.amount + self.multiplier*self.amount
        self.diff = (self.multiplier-1)*self.amount
    
        self.answer = self.diff

        self.problem1 = "%s receives %d times as much %s as %s. If their total %s is $%d, find the difference in the %s that they receive."%(self.person1,self.multiplier,self.item,self.person2,self.item,self.total,self.item)
        self.problem2 = "%s and %s receive a combined %s of $%d. If %s receives %d times as much %s as %s, what is the difference in the %s that they receive?"%(self.person1,self.person2,self.item,self.total,self.person1,self.multiplier,self.item,self.person2,self.item)
        self.problem3 = "%s and %s receive a total of $%d in %s. If %s receives %d times as much %s as %s, find the difference in the %s that they receive."%(self.person1,self.person2,self.total,self.item,self.person1,self.multiplier,self.item,self.person2,self.item)
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])

        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType67(self.problem,self.answer,self.person1,self.person2,self.item,self.amount,self.multiplier,self.total,self.diff)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"$",'unit':"",'problem_type':"ProblemType67"}

    def ExplainType67(self,problem,answer,person1,person2,item,amount,multiplier,total,diff):
        self.answer_text = "The correct answer is: <b>$"+str(answer)
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'>"
        self.table_text = self.table_text + "<tr><td>"+person1+"</td>"
        for _i in range(multiplier):
            self.table_text = self.table_text + "<td><img src='/images/explanation/pink_block_pt5cm.png'></td>"
        self.table_text = self.table_text + "<td rowspan=2><img src='/images/explanation/right_curly_braces_1cm.png'></td>"
        self.table_text = self.table_text + "<td rowspan=2>$"+str(total)+"</td></tr>"
        self.table_text = self.table_text + "<tr><td>"+person2+"</td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/green_block_pt5cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td></td><td></td><td align='center' colspan="+str(multiplier-1)+"><img src='/images/explanation/down_curly_braces_pt5cm.png' height=24 width="+str((multiplier-1)*33)+"><br>?</td>"
        self.table_text = self.table_text + "</tr></table><br>"
        
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(multiplier+1)+" units = $"+str(total)+"</div>"
        self.solution_text = self.solution_text + "<div>1 unit = $"+str(total)+" &divide; "+str(multiplier+1)+" = $"+str(total/(multiplier+1))+"</div>"
        if multiplier>2:
            self.solution_text = self.solution_text + "<div>"+str(multiplier-1)+" units = "+str(multiplier-1)+" x $"+str(total/(multiplier+1))+" = $"+str(diff)+"</div>"
        self.solution_text = self.solution_text + "<div>$"+str(diff)+" is the diffrence in the "+item+" that they receive.</div>"
           
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    def GenerateProblemType68(self):
        '''e.g.:Annie receives 3 times as much monthly salary as Betty. If Annie receives $3000 more than Betty, how much monthly salary do they receive together?'''
        self.PersonNames = random.sample(PersonName.PersonName,2)
        self.ItemPool = {"monthly salary":randint(1700,4500),"monthly allowance":randint(1300,2000),"weekly allowance":randint(100,400),"weekly pocket money":randint(100,400),
        		"monthly pocket money":randint(100,1000),"sales commission":randint(1000,2500),"sales income":randint(1000,2500),"weekly stipend":randint(100,300),
        		"monthly stipend":randint(1200,2000),"monthly fees":randint(150,1500),"weekly fees":randint(50,500),"monthly subsidy":randint(100,200),
        		"yearly subsidy":randint(200,700),"yearly bonus":randint(1000,5000),"monthly bonus":randint(200,700),"yearly child care subsidy":randint(200,500),
        		"monthly child care subsidy":randint(50,200),"yearly tax benefit":randint(1000,2000),"monthly tax benefit":randint(100,200)
        		}
        self.item = self.ItemPool.keys()[randint(0,len(self.ItemPool)-1)]
        self.amount = self.ItemPool[self.item]
        self.person1 = self.PersonNames[0]
        self.person2 = self.PersonNames[1]
        self.multiplier = randint(2,5)
        self.total = self.amount + self.multiplier*self.amount
        self.diff = (self.multiplier-1)*self.amount
        
        self.answer = self.total

        self.problem1 = "%s receives %d times as much %s as %s. If %s receives $%d more than %s, how much %s do they receive together?"%(self.person1,self.multiplier,self.item,self.person2,self.person1,self.diff,self.person2,self.item)
        self.problem2 = "%s receives a %s of $%d more than %s. If %s receives %d times as much %s as %s, how much %s do they receive together?"%(self.person1,self.item,self.diff,self.person2,self.person1,self.multiplier,self.item,self.person2,self.item)
        self.problem3 = "%s receives a %s of $%d less than %s. If %s receives %d times as much %s as %s, how much %s do they receive together?"%(self.person2,self.item,self.diff,self.person1,self.person1,self.multiplier,self.item,self.person2,self.item)
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])

        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType68(self.problem,self.answer,self.person1,self.person2,self.item,self.amount,self.multiplier,self.total,self.diff)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"$",'unit':"",'problem_type':"ProblemType68"}

    def ExplainType68(self,problem,answer,person1,person2,item,amount,multiplier,total,diff):
        self.answer_text = "The correct answer is: <b>$"+str(answer)
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'>"
        self.table_text = self.table_text + "<tr><td>"+person1+"</td>"
        for _i in range(multiplier):
            self.table_text = self.table_text + "<td><img src='/images/explanation/pink_block_pt5cm.png'></td>"
        self.table_text = self.table_text + "<td rowspan=2><img src='/images/explanation/right_curly_braces_1cm.png'></td>"
        self.table_text = self.table_text + "<td rowspan=2>?</td></tr>"
        self.table_text = self.table_text + "<tr><td>"+person2+"</td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/green_block_pt5cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td></td><td></td><td align='center' colspan="+str(multiplier-1)+"><img src='/images/explanation/down_curly_braces_pt5cm.png' height=24 width="+str((multiplier-1)*33)+"><br>$"+str(diff)+"</td>"
        self.table_text = self.table_text + "</tr></table><br>"
        
        self.solution_text = "<div>Solution:</div><br>"
        if multiplier>2:
            self.solution_text = self.solution_text + "<div>"+str(multiplier-1)+" units = $"+str(diff)+"</div>"
            self.solution_text = self.solution_text + "<div>1 unit = $"+str(diff)+" &divide; "+str(multiplier-1)+" = $"+str(diff/(multiplier-1))+"</div>"
        else:
            self.solution_text = self.solution_text + "<div>"+str(multiplier-1)+" unit = $"+str(diff)+"</div>"      
        self.solution_text = self.solution_text + "<div>"+str(multiplier+1)+" units = "+str(multiplier+1)+" x $"+str(diff/(multiplier-1))+" = $"+str(total)+"</div>"
        self.solution_text = self.solution_text + "<div>They receive a "+item+" of $"+str(total)+" together.</div>"
           
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    def GenerateProblemType69(self):
        '''e.g.:Annie and Betty receive a monthly salary of $6000 together. If Betty receives a monthly salary of $1500, how many times as much monthly salary as Betty does Annie receive?'''
        self.PersonNames = random.sample(PersonName.PersonName,2)
        self.ItemPool = {"monthly salary":randint(1700,4500),"monthly allowance":randint(1300,2000),"weekly allowance":randint(100,400),"weekly pocket money":randint(100,400),
        		"monthly pocket money":randint(100,1000),"sales commission":randint(1000,2500),"sales income":randint(1000,2500),"weekly stipend":randint(100,300),
        		"monthly stipend":randint(1200,2000),"monthly fees":randint(150,1500),"weekly fees":randint(50,500),"monthly subsidy":randint(100,200),
        		"yearly subsidy":randint(200,700),"yearly bonus":randint(1000,5000),"monthly bonus":randint(200,700),"yearly child care subsidy":randint(200,500),
        		"monthly child care subsidy":randint(50,200),"yearly tax benefit":randint(1000,2000),"monthly tax benefit":randint(100,200)
        		}
        self.item = self.ItemPool.keys()[randint(0,len(self.ItemPool)-1)]
        self.amount = self.ItemPool[self.item]
        self.person1 = self.PersonNames[0]
        self.person2 = self.PersonNames[1]
        self.multiplier = randint(2,5)
        self.total = self.amount + self.multiplier*self.amount
        self.diff = (self.multiplier-1)*self.amount
       
        self.answer = self.multiplier

        self.problem1 = "%s and %s receive a %s of $%d together. If %s receives a %s of $%d, how many times as much %s as %s does %s receive?"%(self.person1,self.person2,self.item,self.total,self.person2,self.item,self.amount,self.item,self.person2,self.person1)
        self.problem2 = "%s receives a %s of $%d. If %s and %s receive a combined %s of $%d, how many times as much %s as %s does %s receive?"%(self.person2,self.item,self.amount,self.person1,self.person2,self.item,self.total,self.item,self.person2,self.person1)
        self.problem3 = "%s and %s receive a total of $%d %s. If %s receives a %s of $%d, find how many times as much %s as %s does %s receive."%(self.person1,self.person2,self.total,self.item,self.person2,self.item,self.amount,self.item,self.person2,self.person1)
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])

        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType69(self.problem,self.answer,self.person1,self.person2,self.item,self.amount,self.multiplier,self.total,self.diff)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"",'unit':"times",'problem_type':"ProblemType69"}

    def ExplainType69(self,problem,answer,person1,person2,item,amount,multiplier,total,diff):
        self.answer_text = "The correct answer is: <b>"+str(answer)+" times"
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'>"
        self.table_text = self.table_text + "<tr><td>"+person1+"</td>"
        self.table_text = self.table_text + "<td align='right'><img src='/images/explanation/pink_block_pt5cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/broken_pink_block_pt7cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/pink_block_pt5cm.png'></td>"
        self.table_text = self.table_text + "<td rowspan=2><img src='/images/explanation/right_curly_braces_1cm.png'></td>"
        self.table_text = self.table_text + "<td rowspan=2>$"+str(total)+"</td></tr>"
        self.table_text = self.table_text + "<tr><td>"+person2+"</td>"
        self.table_text = self.table_text + "<td align='right'><img src='/images/explanation/green_block_pt5cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td></td><td><img src='/images/explanation/down_curly_braces_pt5cm.png'><br>$"+str(amount)+"</td>"
        self.table_text = self.table_text + "</tr></table><br>"
        
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(total)+" - $"+str(amount)+" = $"+str(total-amount)+"</div>"
        self.solution_text = self.solution_text + "<div>"+person1+" receives a "+item+" of $"+str(total-amount)+".</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(total-amount)+" &divide; $"+str(amount)+" = "+str((total-amount)/amount)+"</div>"
        self.solution_text = self.solution_text + "<div>"+person1+" receives "+str((total-amount)/amount)+" times as much "+item+" as "+person2+".</div>"
        self.solution_text = self.solution_text + "<br><div> Watch below video for explanation of similar problem<br>"
        VideoLink = '<object><param name="movie" value="https://www.youtube.com/v/u1zgFlCw8Aw?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded"><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "SZSb55KccC4";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
           
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    '''Problem type 30 starts here'''
    def GenerateProblemType70(self):
        '''e.g.:Annie had 3 times as much money as Betty. After Annie donated $60 to charity and Betty received $40, they had the same amount of money. How much money had Annie at first?'''
        self.PersonNames = random.sample(PersonName.PersonName,3)
        self.person1 = self.PersonNames[0]
        self.person2 = self.PersonNames[1]
        self.person3 = self.PersonNames[2]
        self.ItemPool = {"1":["donated","to charity"],"2":["gave","away"],"3":["spent","shopping"],"4":["lost","on the road"],
        		"5":["lent","to "+self.person3],"6":["paid","in fees"],"7":["paid","in bills"]
        		}
        self.key = self.ItemPool.keys()[randint(0,len(self.ItemPool)-1)]
        self.action = self.ItemPool[self.key][0]
        self.to = self.ItemPool[self.key][1]
        self.EarnPool = ["received","won","earned","got a pocket money of","borrowed","got a prize of"]
        self.earn = random.choice(self.EarnPool)
        self.initial2 = random.randrange(50,150,2)
        self.initial1 = 3*self.initial2
        self.received = randint(50,self.initial2)
        self.gave = 2*self.initial2 - self.received

        self.answer = self.initial1

        self.problem1 = "%s had 3 times as much money as %s. After %s %s $%d %s and %s %s $%d, they had the same amount of money. How much money had %s at first?"%(self.person1,self.person2,self.person1,self.action,self.gave,self.to,self.person2,self.earn,self.received,self.person1)
        self.problem2 = "%s had 3 times as much money as %s. They had the same amount of money after %s %s $%d %s and %s %s $%d. Find the sum of money %s had at first."%(self.person1,self.person2,self.person1,self.action,self.gave,self.to,self.person2,self.earn,self.received,self.person1)
        self.problem = random.choice([self.problem1,self.problem2])

        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType70(self.problem,self.answer,self.person1,self.person2,self.initial1,self.initial2,self.gave,self.received)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"$",'unit':"",'problem_type':"ProblemType70"}

    def ExplainType70(self,problem,answer,person1,person2,initial1,initial2,gave,received):
        self.answer_text = "The correct answer is: <b>$"+str(answer)
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'>"
        self.table_text = self.table_text + "<tr><td></td><td colspan=4 align='center'>?<br>"
        self.table_text = self.table_text + "<img src='/images/explanation/up_curly_braces_3cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td>"+person1+"</td>"
        self.table_text = self.table_text + "<td colspan=4><img src='/images/explanation/P5_WN_PT70_A.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td>"+person2+"</td>"
        self.table_text = self.table_text + "<td colspan=2><img src='/images/explanation/P5_WN_PT70_B.png'></td><td></td><td></td></tr>"
        self.table_text = self.table_text + "<tr><td></td><td></td><td align='right'><img src='/images/explanation/down_curly_braces_pt7cm.png'><br>$"+str(received)+"</td>"
        self.table_text = self.table_text + "<td colspan=2 align='center'><img src='/images/explanation/down_curly_braces_1cm.png'><br>$"+str(gave)+"</td>"
        self.table_text = self.table_text + "</tr></table><br>"
        
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>2 units = $"+str(received)+" + $"+str(gave)+" = $"+str(received+gave)+"</div>"
        self.solution_text = self.solution_text + "<div>1 unit = $"+str(received+gave)+" &divide; 2 = $"+str((received+gave)/2)+"</div>"
        self.solution_text = self.solution_text + "<div>3 units = 3 x $"+str((received+gave)/2)+" = $"+str(initial1)+"</div>"
        self.solution_text = self.solution_text + "<div>"+person1+" had $"+str(initial1)+" at first.</div>"
           
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    '''Problem type 31 starts here'''
    def GenerateProblemType71(self):
        '''e.g.:Annie bought 2 similar shirts and a coat at a department store. She paid the cashier $200 and received $39 change. If the coat cost $115, find the cost of each shirt.'''
        self.person = random.choice(PersonName.BoyName)
        self.ItemPool = {"1":["furniture store","chair","sofa set",randint(200,600)],"2":["toys shop","figurine","board game",randint(15,45)],"3":["bookstore","marker","book",randint(5,30)],
        		"4":["jewelry shop","ring","bracelet",randint(25,200)],"5":["store","plate","cooking pot",randint(10,50)],"6":["store","mug","electric kettle",randint(15,40)],
        		"7":["hypermarket","DVD","DVD player",randint(30,100)],"8":["department store","shirt","jacket",randint(25,125)],"9":["fashion store","T-shirt","pair of pants",randint(25,125)],
        		"10":["sports store","ball","racket",randint(15,80)],"11":["bookstore","folder","pack of CDs",randint(5,15)],"12":["fashion store","bag","suit",randint(40,200)],
        		"13":["grocery store","juice can","box of cookies",randint(5,15)],"14":["supermarket","ketchup bottle","bag of rice",randint(5,15)],"15":["fast food centre","drink","sandwich",randint(5,10)],
        		"16":["bakery","muffin","cake",randint(10,25)],"17":["plant nursery","flower pot","plant",randint(5,25)],"18":["computer store","thumb drive","printer",randint(50,250)],
        		"19":["department store","bed sheet","mattress",randint(200,800)],"20":["sports store","jersey","pair of shoes",randint(50,200)],"21":["department store","shirt","coat",randint(50,150)]
        		}
        self.key = self.ItemPool.keys()[randint(0,len(self.ItemPool)-1)]
        self.store = self.ItemPool[self.key][0]
        self.item2 = self.ItemPool[self.key][1]
        self.item1 = self.ItemPool[self.key][2]
        self.price1 = self.ItemPool[self.key][3]
        self.price2 = self.price1 * randint(10,25)/100
        self.number2 = randint(3,5)
        self.total = self.price1 + self.number2*self.price2
        if self.total<100:
            self.paid = int(round(self.total,-1)+10)
        else:
            if round(self.total,-2)>self.total:
                self.paid = int(round(self.total,-2))
            else:
                self.paid = int(round(self.total,-2)+100)
        self.change = self.paid - self.total

        self.answer = self.price2

        self.problem1 = "%s bought %d similar %ss and a %s at a %s. He paid the cashier $%d and received $%d change. If the %s cost $%d, find the cost of each %s."%(self.person,self.number2,self.item2,self.item1,self.store,self.paid,self.change,self.item1,self.price1,self.item2)
        self.problem2 = "%s paid $%d at a %s and received a change of $%d. He bought %d similar %ss and a %s. If the %s cost $%d, what was the cost of each %s?"%(self.person,self.paid,self.store,self.change,self.number2,self.item2,self.item1,self.item1,self.price1,self.item2)
        self.problem3 = "%s bought a %s which costs $%d at a %s. He also bought %d similar %ss. If he paid $%d to the cashier and received a change of $%d, what was the cost of each %s?"%(self.person,self.item1,self.price1,self.store,self.number2,self.item2,self.paid,self.change,self.item2)
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])

        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType71(self.problem,self.answer,self.person,self.item1,self.item2,self.price1,self.price2,self.number2,self.paid,self.change,self.total)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"$",'unit':"",'problem_type':"ProblemType71"}

    def ExplainType71(self,problem,answer,person,item1,item2,price1,price2,number,paid,change,total):
        self.answer_text = "The correct answer is: <b>$"+str(answer)
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'>"
        self.table_text = self.table_text + "<tr><td align='center'>?<br><img src='/images/explanation/up_curly_braces_pt5cm.png'></td>"
        for _i in range(number-1):
            self.table_text = self.table_text + "<td></td>"
        self.table_text = self.table_text + "<td align='center'>$"+str(price1)+"<br><img src='/images/explanation/up_curly_braces_pt7cm.png'></td></tr><tr>"
        for _i in range(number):
            self.table_text = self.table_text + "<td><img src='/images/explanation/pink_block_pt5cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/green_block_pt7cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td align='center' colspan="+str(number+1)+"><img src='/images/explanation/down_curly_braces_3cm.png'><br>"
        self.table_text = self.table_text + "$"+str(paid)+"-$"+str(change)+"</td>"
        self.table_text = self.table_text + "</tr></table><br>"
        
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(paid)+" - $"+str(change)+" = $"+str(total)+"</div>"
        self.solution_text = self.solution_text + "<div>"+person+" spent a total of $"+str(total)+".</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(total)+" - $"+str(price1)+" = $"+str(total-price1)+"</div>"
        self.solution_text = self.solution_text + "<div>He spent $"+str(total-price1)+" on the "+str(number)+" "+item2+"s together.</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(total-price1)+" &divide; "+str(number)+" = $"+str(price2)+"</div>"
        self.solution_text = self.solution_text + "<div>The cost of each "+item2+" was $"+str(price2)+".</div>"
           
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    def GenerateProblemType72(self):
        '''e.g.:Annie bought 2 similar frocks and a coat at a department store. She paid the cashier $200 and received $39 change. If each frock cost $23, find the cost of the coat.'''
        self.person = random.choice(PersonName.BoyName)
        self.ItemPool = {"1":["furniture store","chair","sofa set",randint(200,600)],"2":["toys shop","figurine","board game",randint(15,45)],"3":["bookstore","marker","book",randint(5,30)],
        		"4":["jewelry shop","ring","bracelet",randint(25,200)],"5":["store","plate","cooking pot",randint(10,50)],"6":["store","mug","electric kettle",randint(15,40)],
        		"7":["hypermarket","DVD","DVD player",randint(30,100)],"8":["department store","shirt","jacket",randint(25,125)],"9":["fashion store","T-shirt","pair of pants",randint(25,125)],
        		"10":["sports store","ball","racket",randint(15,80)],"11":["bookstore","folder","pack of CDs",randint(5,15)],"12":["fashion store","bag","suit",randint(40,200)],
        		"13":["grocery store","juice can","box of cookies",randint(5,15)],"14":["supermarket","ketchup bottle","bag of rice",randint(5,15)],"15":["fast food centre","drink","sandwich",randint(5,10)],
        		"16":["bakery","muffin","cake",randint(10,25)],"17":["plant nursery","flower pot","plant",randint(5,25)],"18":["computer store","thumb drive","printer",randint(50,250)],
        		"19":["department store","bed sheet","mattress",randint(200,800)],"20":["sports store","jersey","pair of shoes",randint(50,200)],"21":["department store","shirt","coat",randint(50,200)]
        		}
        self.key = self.ItemPool.keys()[randint(0,len(self.ItemPool)-1)]
        self.store = self.ItemPool[self.key][0]
        self.item2 = self.ItemPool[self.key][1]
        self.item1 = self.ItemPool[self.key][2]
        self.price1 = self.ItemPool[self.key][3]
        self.price2 = self.price1 * randint(10,25)/100
        self.number2 = randint(3,5)
        self.total = self.price1 + self.number2*self.price2
        if self.total<100:
            self.paid = int(round(self.total,-1)+10)
        else:
            if round(self.total,-2)>self.total:
                self.paid = int(round(self.total,-2))
            else:
                self.paid = int(round(self.total,-2)+100)
        self.change = self.paid - self.total

        self.answer = self.price1

        self.problem1 = "%s bought %d similar %ss and a %s at a %s. He paid the cashier $%d and received $%d change. If each %s cost $%d, find the cost of the %s."%(self.person,self.number2,self.item2,self.item1,self.store,self.paid,self.change,self.item2,self.price2,self.item1)
        self.problem2 = "%s paid $%d at a %s and received a change of $%d. He bought %d similar %ss and a %s. If each %s cost $%d, what was the cost of the %s?"%(self.person,self.paid,self.store,self.change,self.number2,self.item2,self.item1,self.item2,self.price2,self.item1)
        self.problem3 = "%s paid $%d for each of the %d %ss he bought at a %s. He also bought a %s. If he paid $%d to the cashier and received a change of $%d, find the cost of the %s."%(self.person,self.price2,self.number2,self.item2,self.store,self.item1,self.paid,self.change,self.item1)
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])

        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType72(self.problem,self.answer,self.person,self.item1,self.item2,self.price1,self.price2,self.number2,self.paid,self.change,self.total)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"$",'unit':"",'problem_type':"ProblemType72"}

    def ExplainType72(self,problem,answer,person,item1,item2,price1,price2,number,paid,change,total):
        self.answer_text = "The correct answer is: <b>$"+str(answer)
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'>"
        self.table_text = self.table_text + "<tr><td align='center'>$"+str(price2)+"<br><img src='/images/explanation/up_curly_braces_pt5cm.png'></td>"
        for _i in range(number-1):
            self.table_text = self.table_text + "<td></td>"
        self.table_text = self.table_text + "<td align='center'>?<br><img src='/images/explanation/up_curly_braces_pt7cm.png'></td></tr><tr>"
        for _i in range(number):
            self.table_text = self.table_text + "<td><img src='/images/explanation/pink_block_pt5cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/green_block_pt7cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td align='center' colspan="+str(number+1)+"><img src='/images/explanation/down_curly_braces_3cm.png'><br>"
        self.table_text = self.table_text + "$"+str(paid)+"-$"+str(change)+"</td>"
        self.table_text = self.table_text + "</tr></table><br>"
        
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(paid)+" - $"+str(change)+" = $"+str(total)+"</div>"
        self.solution_text = self.solution_text + "<div>"+person+" spent a total of $"+str(total)+".</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(number)+" x $"+str(price2)+" = $"+str(number*price2)+"</div>"
        self.solution_text = self.solution_text + "<div>He spent $"+str(number*price2)+" on the "+str(number)+" "+item2+"s together.</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(total)+" - $"+str(number*price2)+" = $"+str(price1)+"</div>"
        self.solution_text = self.solution_text + "<div>The cost of the "+item1+" was $"+str(price1)+"</div>"
                   
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    '''Problem type 32 starts here'''
    def GenerateProblemType73(self):
        '''e.g.:A fruiterer bought 320 peaches from a wholesale market. He kept 15 peaches for his family and sold the rest at 5 for $2. How much money did he receive?'''
        self.ItemPool = {"1":["fruit-seller","guavas","supplier","kept","guavas for his staff"],
			"2":["grocer","oranges","bulk supplier","gave away","oranges to his friends"],
			"3":["fruit vendor","mandarins","wholesale fruit market","threw away","overripe ones"],
			"4":["stationer","CDs","wholesaler","threw away","damaged ones"],
			"5":["stationer","pencils","bulk trader","kept","pencils for himself"],
			"6":["stationer","erasers","wholesale supplier","gave","erasers to his children"],
			"7":["bookseller","notebooks","trader","threw away","torn ones"],
			"8":["jewelry shop merchant","rings","dealer","returned","damaged ones to the supplier"],
			"9":["vendor","stickers","wholesale supplier","kept","stickers for his grandchildren"],
			"10":["merchant","rubber bands","dealer","threw away","broken ones"],
			"11":["grocer","lemons","wholesale vegetable market","threw away","squashed ones"],
			"12":["vegetable seller","cucumbers","wholesale market","threw away","unripe ones"],
			"13":["jewelry shop merchant","hair clips","jewelry supplier","recycled","broken ones"],
			"14":["florist","roses","bulk market","gave","roses to his wife"],
			"15":["fashion store merchant","T-shirts","bulk supplier","kept","T-shirts for himself"],
			"16":["fashion store merchant","handkerchiefs","dealer","recycled","damaged ones"],
			"17":["fruiterer","peaches","wholesale market","kept","peaches for his family"]
        		}
        self.key = self.ItemPool.keys()[randint(0,len(self.ItemPool)-1)]
        self.seller = self.ItemPool[self.key][0]
        self.item = self.ItemPool[self.key][1]
        self.place = self.ItemPool[self.key][2]
        self.action1 = self.ItemPool[self.key][3]
        self.action2 = self.ItemPool[self.key][4]
        self.number = randint(5,9)
        self.number1 = random.randrange(self.number*20,500,self.number)
        self.number2 = random.randrange(self.number*2,self.number*10,self.number)
        self.price = randint(2,10)
        self.money = (self.number1-self.number2)*self.price/self.number

        self.answer = self.money

        self.problem1 = "A %s bought %d %s from a %s. He %s %d %s and sold the rest at %d for $%d. How much money did he receive?"%(self.seller,self.number1,self.item,self.place,self.action1,self.number2,self.action2,self.number,self.price)
        self.problem2 = "A %s purchased %d %s from the %s. He %s %d %s and sold the rest at %d for $%d. How much money did he receive?"%(self.seller,self.number1,self.item,self.place,self.action1,self.number2,self.action2,self.number,self.price)
        self.problem = random.choice([self.problem1,self.problem2])

        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType73(self.problem,self.answer,self.seller,self.item,self.number,self.number1,self.number2,self.price)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"$",'unit':"",'problem_type':"ProblemType73"}

    def ExplainType73(self,problem,answer,seller,item,number,number1,number2,price):
        self.answer_text = "The correct answer is: <b>$"+str(answer)
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'>"
        self.table_text = self.table_text + "<tr><td></td><td align='center'>"+str(number)+"<br><img src='/images/explanation/up_curly_braces_pt5cm.png'></td><td></td><td></td><td></td><td></td><td></td><td></td>"
        self.table_text = self.table_text + "<td align='center'>"+str(number2)+"<br><img src='/images/explanation/up_curly_braces_1cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td>"+item+"</td>"
        for _i in range(3):
            self.table_text = self.table_text + "<td><img src='/images/explanation/green_block_pt5cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/broken_green_block_pt5cm.png'></td>"
        for _i in range(3):
            self.table_text = self.table_text + "<td><img src='/images/explanation/green_block_pt5cm.png'></td>"	
        self.table_text = self.table_text + "<td><img src='/images/explanation/dotted_yellow_block_1cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td></td><td align='center' colspan=8><img src='/images/explanation/down_curly_braces_3cm.png' width=280 height=24><br>"+str(number1)+"</td>"
        self.table_text = self.table_text + "</tr></table><br>"
        
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(number1)+" "+item+" - "+str(number2)+" "+item+" = "+str(number1-number2)+" "+item+"</div>"
        self.solution_text = self.solution_text + "<div>The "+seller+" had "+str(number1-number2)+" "+item+" remaining.</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(number1-number2)+" "+item+" &divide; "+str(number)+" = "+str((number1-number2)/number)+" sets</div>"
        self.solution_text = self.solution_text + "<div>He made "+str((number1-number2)/number)+" sets of "+str(number)+" "+item+" each.</div><br>"
        self.solution_text = self.solution_text + "<div>He sold each set of "+str(number)+" "+item+" for $"+str(price)+".</div>"
        self.solution_text = self.solution_text + "<div>Therefore, "+str((number1-number2)/number)+"  x $"+str(price)+" = $"+str(((number1-number2)/number)*price)+"</div>"
        self.solution_text = self.solution_text + "<div>The "+seller+" received $"+str(((number1-number2)/number)*price)+".</div>"
                   
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    def GenerateProblemType74(self):
        '''e.g.:A fruiterer bought 320 peaches from a wholesale market. He kept 15 peaches for his family and sold the rest at 5 for $2. How much money did he receive?'''
        self.ItemPool = {"1":["fruit-seller","guavas","supplier","kept","guavas for his staff"],
			"2":["grocer","oranges","bulk supplier","gave away","oranges to his friends"],
			"3":["fruit vendor","mandarins","wholesale fruit market","threw away","overripe ones"],
			"4":["stationer","CDs","wholesaler","threw away","damaged ones"],
			"5":["stationer","pencils","bulk trader","kept","pencils for himself"],
			"6":["stationer","erasers","wholesale supplier","gave","erasers to his children"],
			"7":["bookseller","notebooks","trader","threw away","torn ones"],
			"8":["jewelry shop merchant","rings","dealer","returned","damaged ones to the supplier"],
			"9":["vendor","stickers","wholesale supplier","kept","stickers for his grandchildren"],
			"10":["merchant","rubber bands","dealer","threw away","broken ones"],
			"11":["grocer","lemons","wholesale vegetable market","threw away","squashed ones"],
			"12":["vegetable seller","cucumbers","wholesale market","threw away","unripe ones"],
			"13":["jewelry shop merchant","hair clips","jewelry supplier","recycled","broken ones"],
			"14":["florist","roses","bulk market","gave","roses to his wife"],
			"15":["fashion store merchant","T-shirts","bulk supplier","kept","T-shirts for himself"],
			"16":["fashion store merchant","handkerchiefs","dealer","recycled","damaged ones"],
			"17":["fruiterer","peaches","wholesale market","kept","peaches for his family"]
        		}
        self.key = self.ItemPool.keys()[randint(0,len(self.ItemPool)-1)]
        self.seller = self.ItemPool[self.key][0]
        self.item = self.ItemPool[self.key][1]
        self.place = self.ItemPool[self.key][2]
        self.action1 = self.ItemPool[self.key][3]
        self.action2 = self.ItemPool[self.key][4]
        self.number = randint(5,9)
        self.number1 = random.randrange(self.number*20,500,self.number)
        self.number2 = random.randrange(self.number*2,self.number*10,self.number)
        self.price = randint(2,10)
        self.money = (self.number1-self.number2)*self.price/self.number

        self.answer = self.number1

        self.problem1 = "A %s bought some %s from the %s. He %s %d %s and sold the rest at %d for $%d. If he received $%d, how many %s had he bought from the %s?"%(self.seller,self.item,self.place,self.action1,self.number2,self.action2,self.number,self.price,self.money,self.item,self.place)
        self.problem2 = "A %s purchased some %s from the %s. He %s %d %s. He sold the rest at %d for $%d and received a total of $%d. Find the number of %s he had bought from the %s."%(self.seller,self.item,self.place,self.action1,self.number2,self.action2,self.number,self.price,self.money,self.item,self.place)
        self.problem = random.choice([self.problem1,self.problem2])

        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType74(self.problem,self.answer,self.seller,self.item,self.number,self.number1,self.number2,self.price,self.money,self.place)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"",'unit':self.item,'problem_type':"ProblemType74"}

    def ExplainType74(self,problem,answer,seller,item,number,number1,number2,price,money,place):
        self.answer_text = "The correct answer is: <b>"+str(answer)+" "+item
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'>"
        self.table_text = self.table_text + "<tr><td></td><td align='center'>"+str(number)+"<br><img src='/images/explanation/up_curly_braces_pt5cm.png'></td><td></td><td></td><td></td><td></td><td></td><td></td>"
        self.table_text = self.table_text + "<td align='center'>"+str(number2)+"<br><img src='/images/explanation/up_curly_braces_1cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td>"+item+"</td>"
        for _i in range(3):
            self.table_text = self.table_text + "<td><img src='/images/explanation/green_block_pt5cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/broken_green_block_pt5cm.png'></td>"
        for _i in range(3):
            self.table_text = self.table_text + "<td><img src='/images/explanation/green_block_pt5cm.png'></td>"	
        self.table_text = self.table_text + "<td><img src='/images/explanation/dotted_yellow_block_1cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td></td><td align='center' colspan=8><img src='/images/explanation/down_curly_braces_3cm.png' width=280 height=24><br>?</td>"
        self.table_text = self.table_text + "</tr></table><br>"
        
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(money)+" &divide; "+str(price)+" = "+str(money/price)+"</div>"
        self.solution_text = self.solution_text + "<div>The "+seller+" made "+str(money/price)+" sets of "+str(number)+" "+item+" each.</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(money/price)+" x "+str(number)+" "+item+" = "+str(money*number/price)+" "+item+"</div>"
        self.solution_text = self.solution_text + "<div>He sold "+str(money*number/price)+" "+item+".</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(money*number/price)+" "+item+" + "+str(number2)+" "+item+" = "+str(number1)+" "+item+"</div>"
        self.solution_text = self.solution_text + "<div>The "+seller+" had bought "+str(number1)+" "+item+" from the "+place+".</div>"
        self.solution_text = self.solution_text + "<br><div> Watch below video for explanation of similar problem<br>"
        VideoLink = '<object><param name="movie" value="https://www.youtube.com/v/u1zgFlCw8Aw?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded"><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "Jgon2zzLXNw";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
                   
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain
        
    def GenerateProblemType75(self):
        '''e.g.:A fruiterer bought 320 peaches from the wholesale market. He kept some for his family and sold the rest at 5 for $2. 
        	If he received $122, find the number of peaches he kept for his family.'''
        self.ItemPool = {"1":["fruiterer","peaches","wholesale market","kept some for his family","kept for his family","kept","for his family"],
			"2":["fruit-seller","guavas","supplier","kept some for his staff","kept for his staff","kept","for his staff"],
			"3":["grocer","oranges","bulk supplier","gave away some to his friends","gave away to his friends","gave away","to his friends"],
			"4":["fruit vendor","mandarins","wholesale fruit market","threw away some overripe ones","threw away","threw","away"],
			"5":["stationer","CDs","wholesaler","threw away some damaged ones","threw away","threw","away"],
			"6":["shopkeeper","pencils","bulk trader","kept some for himself","kept for himself","kept","for himself"],
			"7":["stationery keeper","erasers","wholesale supplier","gave some to his children","gave to his children","gave","to his children"],
			"8":["bookseller","notebooks","trader","threw away some torn ones","threw away","threw","away"],
			"9":["jewelry shop merchant","rings","dealer","returned some damaged ones to the supplier","returned to the supplier","returned","to the supplier"],
			"10":["vendor","stickers","wholesale supplier","kept some stickers for his grandchildren","kept for his grandchildren","kept","for his grandchildren"],
			"11":["merchant","rubber bands","dealer","threw away some broken ones","threw away","threw","away"],
			"12":["grocery storekeeper","lemons","wholesale vegetable market","threw away some squashed ones","threw away","threw","away"],
			"13":["vegetable seller","cucumbers","wholesale market","threw away some unripe ones","threw away","threw","away"],
			"14":["jewelry seller","hair clips","jewelry supplier","recycled some broken ones","recycled","recycled",""],
			"15":["florist","roses","bulk market","gave some roses to his wife","gave to his wife","gave","to his wife"],
			"16":["fashion store merchant","T-shirts","bulk supplier","kept some for himself","kept for himself","kept","for himself"],
			"17":["fashion storekeeper","handkerchiefs","dealer","recycled some damaged ones","recycled","recycled",""]
        		}
        self.key = self.ItemPool.keys()[randint(0,len(self.ItemPool)-1)]
        self.seller = self.ItemPool[self.key][0]
        self.item = self.ItemPool[self.key][1]
        self.place = self.ItemPool[self.key][2]
        self.action1 = self.ItemPool[self.key][3]
        self.action2 = self.ItemPool[self.key][4]
        self.SolutionAction1 = self.ItemPool[self.key][5]
        self.SolutionAction2 = self.ItemPool[self.key][6]
        
        self.number = randint(5,9)
        self.number1 = random.randrange(self.number*20,500,self.number)
        self.number2 = random.randrange(self.number*2,self.number*10,self.number)
        self.price = randint(2,10)
        self.money = (self.number1-self.number2)*self.price/self.number

        self.answer = self.number2

        self.problem1 = "A %s bought %d %s from the %s. He %s and sold the rest at %d for $%d. If he received $%d, find the number of %s he %s."%(self.seller,self.number1,self.item,self.place,self.action1,self.number,self.price,self.money,self.item,self.action2)
        self.problem2 = "A %s purchased %d %s from the %s. He %s. He sold the rest at %d for $%d and received a total of $%d. Find the number of %s he %s."%(self.seller,self.number1,self.item,self.place,self.action1,self.number,self.price,self.money,self.item,self.action2)     
        self.problem = random.choice([self.problem1,self.problem2])

        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType75(self.problem,self.answer,self.seller,self.item,self.number,self.number1,self.number2,self.price,self.money,self.SolutionAction1,self.SolutionAction2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"",'unit':self.item,'problem_type':"ProblemType75"}

    def ExplainType75(self,problem,answer,seller,item,number,number1,number2,price,money,SolutionAction1,SolutionAction2):
        self.answer_text = "The correct answer is: <b>"+str(answer)+" "+item
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'>"
        self.table_text = self.table_text + "<tr><td></td><td align='center'>"+str(number)+"<br><img src='/images/explanation/up_curly_braces_pt5cm.png'></td><td></td><td></td><td></td><td></td><td></td><td></td>"
        self.table_text = self.table_text + "<td align='center'>?<br><img src='/images/explanation/up_curly_braces_1cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td>"+item+"</td>"
        for _i in range(3):
            self.table_text = self.table_text + "<td><img src='/images/explanation/green_block_pt5cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/broken_green_block_pt5cm.png'></td>"
        for _i in range(3):
            self.table_text = self.table_text + "<td><img src='/images/explanation/green_block_pt5cm.png'></td>"	
        self.table_text = self.table_text + "<td><img src='/images/explanation/dotted_yellow_block_1cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td></td><td align='center' colspan=8><img src='/images/explanation/down_curly_braces_3cm.png' width=280 height=24><br>"+str(number1)+"</td>"
        self.table_text = self.table_text + "</tr></table><br>"
        
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(money)+" &divide; "+str(price)+" = "+str(money/price)+"</div>"
        self.solution_text = self.solution_text + "<div>The "+seller+" made "+str(money/price)+" sets of "+str(number)+" "+item+" each.</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(money/price)+" x "+str(number)+" "+item+" = "+str(money*number/price)+" "+item+"</div>"
        self.solution_text = self.solution_text + "<div>He sold "+str(money*number/price)+" "+item+".</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(number1)+" "+item+" - "+str(money*number/price)+" "+item+" = "+str(number2)+" "+item+"</div>"
        self.solution_text = self.solution_text + "<div>The "+seller+" "+SolutionAction1+" "+str(number2)+" "+SolutionAction2+".</div>"
                   
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    '''Problem type 33 starts here'''
    def GenerateProblemType76(self):
        '''e.g.:A fruit seller had 35 oranges at first of which 15 were rotten. He threw away the rotten oranges and bought another 2 boxes of 50 oranges each. 
        	He then sold the oranges at 10 for $5. How much money did the fruit seller receive?'''
        self.ItemPool = {"1":["fruit-seller","guavas","spoilt","threw away","cartons"],
			"2":["grocer","apples","overripe","threw away","baskets"],
			"3":["farmer","eggs","stale","threw away","boxes"],
			"4":["stationer","CDs","damaged","recycled","packs"],
			"5":["stationer","pencils","broken","threw away","bundles"],
			"6":["stationer","erasers","damaged","recycled","cases"],
			"7":["bookseller","notebooks","torn","recycled","bundles"],
			"8":["jewelry shop merchant","rings","damaged","recycled","cases"],
			"9":["vendor","stickers","torn","threw away","boxes"],
			"10":["merchant","rubber bands","broken","threw away","bags"],
			"11":["grocer","lemons","squashed","threw away","baskets"],
			"12":["vegetable seller","cucumbers","unripe","threw away","cartons"],
			"13":["jewelry shop merchant","hair clips","broken","threw away","bags"],
			"14":["florist","roses","dried","threw away","bundles"],
			"15":["fashion store merchant","T-shirts","torn","recycled","bags"],
			"16":["fashion store merchant","handkerchiefs","damaged","recycled","cases"]
        		}
        self.key = self.ItemPool.keys()[randint(0,len(self.ItemPool)-1)]
        self.seller = self.ItemPool[self.key][0]
        self.item = self.ItemPool[self.key][1]
        self.event = self.ItemPool[self.key][2]
        self.action = self.ItemPool[self.key][3]
        self.container = self.ItemPool[self.key][4]

        self.number = randint(5,9)
        self.number1 = random.randrange(self.number*5,100,self.number)
        self.number2 = random.randrange(self.number*1,self.number*3,self.number)
        self.number3 = randint(2,5)
        self.number4 = random.randrange(self.number*5,100,self.number)
        self.price = randint(2,10)
        self.money = (self.number1-self.number2+self.number3*self.number4)*self.price/self.number

        self.answer = self.money

        self.problem1 = "A %s had %d %s at first of which %d were %s. He %s the %s %s and bought another %d %s of %d %s each. He then sold the %s at %d for $%d. How much money did the %s receive?"%(self.seller,self.number1,self.item,self.number2,self.event,self.action,self.event,self.item,self.number3,self.container,self.number4,self.item,self.item,self.number,self.price,self.seller)
        self.problem2 = "A %s %s %d %s ones of his %d %s. Then he bought another %d %s of %d %s each. If he sold all his %s at %d for $%d, find the amount of money that the %s received."%(self.seller,self.action,self.number2,self.event,self.number1,self.item,self.number3,self.container,self.number4,self.item,self.item,self.number,self.price,self.seller)
        self.problem = random.choice([self.problem1,self.problem2])

        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType76(self.problem,self.answer,self.seller,self.item,self.number,self.number1,self.number2,self.number3,self.number4,self.price,self.money,self.action,self.event,self.container)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"$",'unit':"",'problem_type':"ProblemType76"}

    def ExplainType76(self,problem,answer,seller,item,number,number1,number2,number3,number4,price,money,action,event,container):
        self.answer_text = "The correct answer is: <b>$"+str(answer)
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'>"
        self.table_text = self.table_text + "<tr><td></td><td align='center'>"+str(number4)+"<br><img src='/images/explanation/up_curly_braces_1cm.png'></td>"
        for _i in range(number3):
            self.table_text = self.table_text + "<td></td>"
        self.table_text = self.table_text + "<td align='center'>"+str(number2)+"<br><img src='/images/explanation/up_curly_braces_pt5cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td>"+item+"</td>"
        for _i in range(number3):
            self.table_text = self.table_text + "<td><img src='/images/explanation/pink_block_1cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/green_block_pt5cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/dotted_block_pt5cm.png'></td></tr><tr>"
        for _i in range(number3+1):
            self.table_text = self.table_text + "<td></td>"
        self.table_text = self.table_text + "<td align='center' colspan=2><img src='/images/explanation/down_curly_braces_1cm.png'><br>"+str(number1)+"</td>"
        self.table_text = self.table_text + "</tr></table><br>"
        
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(number1)+" "+item+" - "+str(number2)+" "+item+" = "+str(number1-number2)+" "+item+"</div>"
        self.solution_text = self.solution_text + "<div>The "+seller+" had "+str(number1-number2)+" "+item+" after he "+action+" "+str(number2)+" "+event+" ones.</div><br>"                   
        self.solution_text = self.solution_text + "<div>"+str(number3)+" x "+str(number4)+" "+item+" = "+str(number3*number4)+" "+item+"</div>"
        self.solution_text = self.solution_text + "<div>There were "+str(number3*number4)+" "+item+" in the "+str(number3)+" "+container+".</div><br>"                   
        self.solution_text = self.solution_text + "<div>"+str(number1-number2)+" "+item+" + "+str(number3*number4)+" "+item+" = "+str(number1-number2+number3*number4)+" "+item+"</div>"
        self.solution_text = self.solution_text + "<div>The "+seller+" sold "+str(number1-number2+number3*number4)+" "+item+" altogether.</div><br>"                   
        self.solution_text = self.solution_text + "<div>"+str(number1-number2+number3*number4)+" "+item+" &divide; "+str(number)+" = "+str((number1-number2+number3*number4)/number)+" sets</div>"
        self.solution_text = self.solution_text + "<div>He made "+str((number1-number2+number3*number4)/number)+" sets of "+str(number)+" "+item+" each.</div><br>"                   
        self.solution_text = self.solution_text + "<div>He sold each set of "+str(number)+" "+item+" for $"+str(price)+". Therefore,"+str((number1-number2+number3*number4)/number)+" x $"+str(price)+" = $"+str(((number1-number2+number3*number4)/number)*price)+"</div>"
        self.solution_text = self.solution_text + "<div>The "+seller+" received $"+str(((number1-number2+number3*number4)/number)*price)+".</div>"                   
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    '''Problem type 34 starts here'''
    def GenerateProblemType77(self):
        '''e.g.:A fruit vendor bought 32 boxes of apples containing 96 apples each. He divided the apples into bags of 10. 
        	He sold each bag for $7 and the remaining apples for $1 each. How much money did the fruit vendor get?'''
        self.ItemPool = {"1":["fruit-seller","cartons","guavas","packet",randint(5,15)],
			"2":["fruit-seller","cartons","oranges","bag",randint(5,15)],
			"3":["fruit vendor","cartons","mandarins","pack",randint(5,15)],
			"4":["stationer","cartons","CDs","pack",randint(5,15)],
			"5":["stationer","cartons","pencils","packet",randint(5,15)],
			"6":["stationer","cartons","erasers","pack",randint(5,15)],
			"7":["bookseller","boxes","notebooks","pack",randint(5,15)],
			"8":["jewelry shop merchant","boxes","rings","pack",randint(15,25)],
			"9":["vendor","boxes","stickers","pack",randint(5,15)],
			"10":["merchant","cartons","rubber bands","packet",randint(5,15)],
			"11":["vegetable seller","cartons","lemons","packet",randint(5,15)],
			"12":["vegetable seller","cartons","cucumbers","pack",randint(5,15)],
			"13":["jewelry shop merchant","cartons","hair clips","packet",randint(5,15)],
			"14":["florist","cartons","roses","bouquet",randint(15,25)],
			"15":["fashion store merchant","boxes","T-shirts","pack",randint(85,185)],
			"16":["fashion store merchant","boxes","handkerchiefs","pack",randint(5,15)],
			"17":["fruit vendor","boxes","apples","bag",randint(5,15)]
        		}
        self.key = self.ItemPool.keys()[randint(0,len(self.ItemPool)-1)]
        self.seller = self.ItemPool[self.key][0]
        self.item = self.ItemPool[self.key][2]
        self.container1 = self.ItemPool[self.key][1]
        self.container2 = self.ItemPool[self.key][3]

        self.number1 = randint(25,50)
        self.number2 = randint(50,100)
        self.number3 = randint(3,15)
        while(self.number1*self.number2%self.number3==0):
            self.number3=randint(3,15)
        self.number4,self.remainder = divmod(self.number1*self.number2,self.number3)
        self.price1 = self.ItemPool[self.key][4]
        self.price2 = int(self.price1/(self.number3))+1
        self.money = self.number4*self.price1+self.remainder*self.price2

        self.answer = self.money

        self.problem1 = "A %s bought %d %s of %s containing %d %s each. He divided the %s into %ss of %d. He sold each %s for $%d and the remaining %s for $%d each. How much money did the %s get?"%(self.seller,self.number1,self.container1,self.item,self.number2,self.item,self.item,self.container2,self.number3,self.container2,self.price1,self.item,self.price2,self.seller)
        self.problem2 = "A %s bought %d %s of %s containing %d %s each. He divided the %s into %ss of %d. If he sold each %s for $%d and the remaining %s for $%d each, find the amount of money that the %s got."%(self.seller,self.number1,self.container1,self.item,self.number2,self.item,self.item,self.container2,self.number3,self.container2,self.price1,self.item,self.price2,self.seller)
        self.problem = random.choice([self.problem1,self.problem2])

        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType77(self.problem,self.answer,self.seller,self.item,self.container1,self.container2,self.number1,self.number2,self.number3,self.number4,self.price1,self.price2,self.money,self.remainder)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"$",'unit':"",'problem_type':"ProblemType77"}

    def ExplainType77(self,problem,answer,seller,item,container1,container2,number1,number2,number3,number4,price1,price2,money,remainder):
        self.answer_text = "The correct answer is: <b>$"+str(answer)
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'>"
        self.table_text = self.table_text + "<tr><td></td><td align='center' colspan=6>"+str(number1)+" "+container1+" x "+str(number2)+"<br>"
        self.table_text = self.table_text + "<img src='/images/explanation/up_curly_braces_3cm.png' width=200 height=24></td></tr>"
        self.table_text = self.table_text + "<tr><td>"+item+"</td>"
        for _i in range(2):
            self.table_text = self.table_text + "<td><img src='/images/explanation/pink_block_pt5cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/broken_pink_block_pt5cm.png'></td>"
        for _i in range(2):
            self.table_text = self.table_text + "<td><img src='/images/explanation/pink_block_pt5cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/yellow_block_pt4cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td></td><td align='center'><img src='/images/explanation/down_curly_braces_pt5cm.png'><br>"+str(number3)+"</td>"
        self.table_text = self.table_text + "<td widht=33></td><td widht=33></td><td widht=33></td><td widht=33></td>"
        self.table_text = self.table_text + "<td align='center'><img src='/images/explanation/down_curly_braces_pt4cm.png'><br>R</td>"
        self.table_text = self.table_text + "</tr></table><br>"
        
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(number1)+" "+container1+" x "+str(number2)+" = "+str(number1*number2)+" "+item+"</div>"
        self.solution_text = self.solution_text + "<div>The "+seller+" had a total of "+str(number1*number2)+" "+item+".</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(number1*number2)+" "+item+" &divide; "+str(number3)+" = "+str(number4)+" "+container2+", "+str(remainder)+" remaining</div>"
        self.solution_text = self.solution_text + "<div>There are "+str(number4)+" "+container2+" of "+str(number3)+" "+item+" each.</div>"
        self.solution_text = self.solution_text + "<div>There are "+str(remainder)+" "+item+" remaining.</div><br>"
        self.solution_text = self.solution_text + "<div>Each "+container2+" is sold for $"+str(price1)+". Therefore,"+str(number4)+" x $"+str(price1)+" = $"+str(number4*price1)+"</div>"
        self.solution_text = self.solution_text + "<div>He sold the "+str(number4)+" "+container2+" for $"+str(number4*price1)+".</div><br>"
        self.solution_text = self.solution_text + "<div>He sold the remaining "+item+" for $"+str(price2)+" each. Therefore, "+str(remainder)+" x $"+str(price2)+" = $"+str(remainder*price2)+"</div>"
        self.solution_text = self.solution_text + "<div>He sold the remaining "+str(remainder)+" for $"+str(remainder*price2)+".</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(number4*price1)+" + $"+str(remainder*price2)+" = $"+str(number4*price1+remainder*price2)+"</div>"
        self.solution_text = self.solution_text + "<div>The "+seller+" got $"+str(number4*price1+remainder*price2)+".</div>"
        self.solution_text = self.solution_text + "<br><div> Watch below video for explanation of similar problem<br>"
        VideoLink = '<object><param name="movie" value="https://www.youtube.com/v/u1zgFlCw8Aw?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded"><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "2B6uVbPdbCw";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    def GenerateProblemType78(self):
        '''e.g.:A fruit vendor bought 32 boxes of apples containing 96 apples each. He divided the apples into bags of 10. 
                He sold each bag for $7 and the leftover apples by the piece. He collected $2151 altogether. 
                How much did he sell each of the leftover apples for?'''
        self.ItemPool = {"1":["fruit-seller","cartons","guavas","packet",randint(5,15)],
            "2":["fruit-seller","cartons","oranges","bag",randint(5,15)],
            "3":["fruit vendor","cartons","mandarins","pack",randint(5,15)],
            "4":["stationer","cartons","CDs","pack",randint(5,15)],
            "5":["stationer","cartons","pencils","packet",randint(5,15)],
            "6":["stationer","cartons","erasers","pack",randint(5,15)],
            "7":["bookseller","boxes","notebooks","pack",randint(5,15)],
            "8":["jewelry shop merchant","boxes","rings","pack",randint(15,25)],
            "9":["vendor","boxes","stickers","pack",randint(5,15)],
            "10":["merchant","cartons","rubber bands","packet",randint(5,15)],
            "11":["vegetable seller","cartons","lemons","packet",randint(5,15)],
            "12":["vegetable seller","cartons","cucumbers","pack",randint(5,15)],
            "13":["jewelry shop merchant","cartons","hair clips","packet",randint(5,15)],
            "14":["florist","cartons","roses","bouquet",randint(15,25)],
            "15":["fashion store merchant","boxes","T-shirts","pack",randint(85,185)],
            "16":["fashion store merchant","boxes","handkerchiefs","pack",randint(5,15)],
            "17":["fruit vendor","boxes","apples","bag",randint(5,15)]
                }
        self.key = self.ItemPool.keys()[randint(0,len(self.ItemPool)-1)]
        self.seller = self.ItemPool[self.key][0]
        self.item = self.ItemPool[self.key][2]
        self.container1 = self.ItemPool[self.key][1]
        self.container2 = self.ItemPool[self.key][3]

        self.number1 = randint(25,50)
        self.number2 = randint(50,100)
        self.number3 = randint(3,15)
        while(self.number1*self.number2%self.number3==0):
            self.number3=randint(3,15)
        self.number4,self.remainder = divmod(self.number1*self.number2,self.number3)
        self.price1 = self.ItemPool[self.key][4]
        self.price2 = int(self.price1/(self.number3))+1
        self.money = self.number4*self.price1+self.remainder*self.price2

        self.answer = self.price2

        self.problem1 = "A %s bought %d %s of %s containing %d %s each. He divided the %s into %ss of %d. He sold each %s for $%d and the leftover %s by the piece. He collected $%d altogether. How much did he sell each of the leftover %s for?"%(self.seller,self.number1,self.container1,self.item,self.number2,self.item,self.item,self.container2,self.number3,self.container1,self.price1,self.item,self.money,self.item)
        self.problem2 = "A %s bought %d %s of %s containing %d %s each. He divided the %s into %ss of %d and sold each %s for $%d. He sold the remaining %s by the piece. If he collected $%d altogether, find the amount of money that he sold each of the leftover %s for."%(self.seller,self.number1,self.container1,self.item,self.number2,self.item,self.item,self.container2,self.number3,self.container2,self.price1,self.item,self.money,self.item)      
        self.problem = random.choice([self.problem1,self.problem2])

        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType78(self.problem,self.answer,self.seller,self.item,self.container1,self.container2,self.number1,self.number2,self.number3,self.number4,self.price1,self.price2,self.money,self.remainder)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"$",'unit':"",'problem_type':"ProblemType78"}

    def ExplainType78(self,problem,answer,seller,item,container1,container2,number1,number2,number3,number4,price1,price2,money,remainder):
        self.answer_text = "The correct answer is: <b>$"+str(answer)
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'>"
        self.table_text = self.table_text + "<tr><td></td><td align='center' colspan=6>"+str(number1)+" "+container1+" x "+str(number2)+"<br>"
        self.table_text = self.table_text + "<img src='/images/explanation/up_curly_braces_3cm.png' width=200 height=24></td></tr>"
        self.table_text = self.table_text + "<tr><td>"+item+"</td>"
        for _i in range(2):
            self.table_text = self.table_text + "<td><img src='/images/explanation/pink_block_pt5cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/broken_pink_block_pt5cm.png'></td>"
        for _i in range(2):
            self.table_text = self.table_text + "<td><img src='/images/explanation/pink_block_pt5cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/yellow_block_pt4cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td></td><td align='center'><img src='/images/explanation/down_curly_braces_pt5cm.png'><br>"+str(number3)+"</td>"
        self.table_text = self.table_text + "<td widht=33></td><td widht=33></td><td widht=33></td><td widht=33></td>"
        self.table_text = self.table_text + "<td align='center'><img src='/images/explanation/down_curly_braces_pt4cm.png'><br>R</td>"
        self.table_text = self.table_text + "</tr></table><br>"
        
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(number1)+" "+container1+" x "+str(number2)+" = "+str(number1*number2)+" "+item+"</div>"
        self.solution_text = self.solution_text + "<div>The "+seller+" had a total of "+str(number1*number2)+" "+item+".</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(number1*number2)+" "+item+" &divide; "+str(number3)+" = "+str(number4)+" "+container2+", "+str(remainder)+" remaining</div>"
        self.solution_text = self.solution_text + "<div>There are "+str(number4)+" "+container2+" of "+str(number3)+" "+item+" each.</div>"
        self.solution_text = self.solution_text + "<div>There are "+str(remainder)+" "+item+" remaining.</div><br>"
        self.solution_text = self.solution_text + "<div>Each "+container2+" is sold for $"+str(price1)+". Therefore,"+str(number4)+" x $"+str(price1)+" = $"+str(number4*price1)+"</div>"
        self.solution_text = self.solution_text + "<div>He sold the "+str(number4)+" "+container2+" for $"+str(number4*price1)+".</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(money)+" - $"+str(number4*price1)+" = $"+str(money-number4*price1)+"</div>"
        self.solution_text = self.solution_text + "<div>He sold the remaining "+str(remainder)+" "+item+" for $"+str(money-number4*price1)+".</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(money-number4*price1)+" &divide; "+str(remainder)+" = $"+str((money-number4*price1)/remainder)+"</div>"
        self.solution_text = self.solution_text + "<div>He sold the leftover "+item+" for $"+str((money-number4*price1)/remainder)+" each.</div>"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    '''Problem Type 35 starts here'''
    def GenerateProblemType79(self):
        '''e.g.:Annie had 14 DVDs at first. She received a pack of 100 DVDs from her father. She and her 5 brothers then shared 
        	the DVDs equally among themselves. How many DVDs has Annie now?'''
        
        self.person = random.choice(PersonName.GirlName)
        self.ItemPool = ["flags","stamps","pencils","pens","marbles","flowers","balls","toy cars","CDs","cookies","kites","notebooks","red flags","blue flags",
        		"candies","rings","key chains","straws","sticks","markers"]
        self.item = random.choice(self.ItemPool)
        self.RelationPool = ["father","mother","uncle","grandmother","teacher","grandfather"]
        self.relation = random.choice(self.RelationPool)
        self.SiblingPool = ["brothers","sisters","cousins","classmates"]
        self.sibling = random.choice(self.SiblingPool)
        self.number = randint(3,5)
        self.initial = random.randrange((self.number+1)*2,30,(self.number+1))
        self.received = random.randrange((self.number+1)*10,100,(self.number+1))
        self.now = (self.initial + self.received)/(self.number+1)

        self.answer = self.now

        self.problem1 = "%s had %d %s at first. She received a pack of %d %s from her %s. She and her %d %s then shared the %s equally among themselves. How many %s has %s now?"%(self.person,self.initial,self.item,self.received,self.item,self.relation,self.number,self.sibling,self.item,self.item,self.person)
        self.problem2 = "%s had %d %s at first. Then she received %d more %s from her %s. She and her %d %s divided the %s equally among themselves. Find the number of %s %s has now."%(self.person,self.initial,self.item,self.received,self.item,self.relation,self.number,self.sibling,self.item,self.item,self.person)
        self.problem = random.choice([self.problem1,self.problem2])

        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType79(self.problem,self.answer,self.person,self.item,self.relation,self.sibling,self.number,self.initial,self.received,self.now)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"",'unit':self.item,'problem_type':"ProblemType79"}

    def ExplainType79(self,problem,answer,person,item,relation,sibling,number,initial,received,now):
        self.answer_text = "The correct answer is: <b>"+str(answer)+" "+item
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'>"
        self.table_text = self.table_text + "<tr><td></td><td align='center'>"+str(initial)+"<br><img src='/images/explanation/up_curly_braces_pt5cm.png'></td>"
        self.table_text = self.table_text + "<td align='center' colspan="+str(number-1)+">"+str(received)+"<br><img src='/images/explanation/up_curly_braces_1cm.png' height=24 width="+str((number-1)*34)+"></td></tr>"
        self.table_text = self.table_text + "<tr><td>"+item+"</td><td><img src='/images/explanation/pink_block_pt5cm.png'></td>"
        self.table_text = self.table_text + "<td colspan="+str(number-1)+"><img src='/images/explanation/yellow_block_1cm.png' height=24 width="+str((number-1)*34)+"></td></tr>"
        self.table_text = self.table_text + "<tr><td>"+item+"<br>shared</td>"
        for _i in range(number):
            self.table_text = self.table_text + "<td><img src='/images/explanation/green_block_pt5cm.png'></td>"
        self.table_text = self.table_text + "</tr><tr><td></td><td align='center'><img src='/images/explanation/down_curly_braces_pt5cm.png'><br>?</td>"  
        self.table_text = self.table_text + "</tr></table><br>"
        
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(initial)+" "+item+" + "+str(received)+" "+item+" = "+str(initial+received)+" "+item+"</div>"
        self.solution_text = self.solution_text + "<div>"+person+" had "+str(initial+received)+" "+item+" after she received "+str(received)+" "+item+" from her "+relation+".</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(number)+" "+sibling+" + 1 = "+str(number+1)+" people</div>"
        self.solution_text = self.solution_text + "<div>The "+item+" are to be divided among "+str(number+1)+" people.</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(initial+received)+" "+item+" &divide; "+str(number+1)+" = "+str((initial+received)/(number+1))+" "+item+"</div>"
        self.solution_text = self.solution_text + "<div>Each person has "+str((initial+received)/(number+1))+" "+item+" now.</div>"
        self.solution_text = self.solution_text + "<div>"+person+" has "+str((initial+received)/(number+1))+" "+item+" now.</div>"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    def GenerateProblemType80(self):
        '''e.g.:Annie had 14 DVDs at first. She received a pack of some DVDs from her father. She and her 5 brothers then shared the DVDs equally among themselves. 
        	If Annie has 19 DVDs Annie now, how many DVDs did she receive from her father?'''
        
        self.person = random.choice(PersonName.GirlName)
        self.ItemPool = ["flags","stamps","pencils","pens","marbles","flowers","balls","toy cars","CDs","cookies","kites","notebooks","red flags","blue flags",
        		"candies","rings","key chains","straws","sticks","markers"]
        self.item = random.choice(self.ItemPool)
        self.RelationPool = ["father","mother","uncle","grandmother","teacher","grandfather"]
        self.relation = random.choice(self.RelationPool)
        self.SiblingPool = ["brothers","sisters","cousins","classmates"]
        self.sibling = random.choice(self.SiblingPool)
        self.number = randint(3,5)
        self.initial = random.randrange((self.number+1)*2,30,(self.number+1))
        self.received = random.randrange((self.number+1)*10,100,(self.number+1))
        self.now = (self.initial + self.received)/(self.number+1)

        self.answer = self.received

        self.problem1 = "%s had %d %s at first. She received a pack of some %s from her %s. She and her %d %s then shared the %s equally among themselves. If %s has %d %s now, how many %s did she receive from her %s?"%(self.person,self.initial,self.item,self.item,self.relation,self.number,self.sibling,self.item,self.person,self.now,self.item,self.item,self.relation)
        self.problem2 = "%s had %d %s at first. Then she received a few more %s from her %s. She and her %d %s divided the %s equally among themselves and they each got %d %s. Find the number of %s %s received from her %s."%(self.person,self.initial,self.item,self.item,self.relation,self.number,self.sibling,self.item,self.now,self.item,self.item,self.person,self.relation)
        self.problem = random.choice([self.problem1,self.problem2])

        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType80(self.problem,self.answer,self.person,self.item,self.relation,self.sibling,self.number,self.initial,self.received,self.now)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"",'unit':self.item,'problem_type':"ProblemType80"}

    def ExplainType80(self,problem,answer,person,item,relation,sibling,number,initial,received,now):
        self.answer_text = "The correct answer is: <b>"+str(answer)+" "+item
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'>"
        self.table_text = self.table_text + "<tr><td></td><td align='center'>"+str(initial)+"<br><img src='/images/explanation/up_curly_braces_pt5cm.png'></td>"
        self.table_text = self.table_text + "<td align='center' colspan="+str(number-1)+">?<br><img src='/images/explanation/up_curly_braces_1cm.png' height=24 width="+str((number-1)*34)+"></td></tr>"
        self.table_text = self.table_text + "<tr><td>"+item+"</td><td><img src='/images/explanation/pink_block_pt5cm.png'></td>"
        self.table_text = self.table_text + "<td colspan="+str(number-1)+"><img src='/images/explanation/yellow_block_1cm.png' height=24 width="+str((number-1)*34)+"></td></tr>"
        self.table_text = self.table_text + "<tr><td>"+item+"</td>"
        for _i in range(number):
            self.table_text = self.table_text + "<td><img src='/images/explanation/green_block_pt5cm.png'></td>"
        self.table_text = self.table_text + "</tr><tr><td></td><td align='center'><img src='/images/explanation/down_curly_braces_pt5cm.png'><br>"+str(now)+"</td>"  
        self.table_text = self.table_text + "</tr></table><br>"
        
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(number)+" "+sibling+" + 1 = "+str(number+1)+" people</div>"
        self.solution_text = self.solution_text + "<div>The "+item+" were divided among "+str(number+1)+" people.</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(number+1)+" x "+str(now)+" "+item+" = "+str(now*(number+1))+" "+item+"</div>"
        self.solution_text = self.solution_text + "<div>"+person+" and her "+sibling+" had "+str(now*(number+1))+" "+item+" altogether.</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(now*(number+1))+" "+item+" - "+str(initial)+" "+item+" = "+str((now*(number+1))-initial)+" "+item+"</div>"
        self.solution_text = self.solution_text + "<div>"+person+" received "+str((now*(number+1))-initial)+" "+item+" from her "+relation+".</div>"
        self.solution_text = self.solution_text + "<br><div> Watch below video for explanation of similar problem<br>"
        VideoLink = '<object><param name="movie" value="https://www.youtube.com/v/u1zgFlCw8Aw?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded"><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "N_u3FSaeYqA";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    '''Problem Type 36 starts here'''
    def GenerateProblemType81(self):
        '''e.g.:Annie had 2 times as much money as Betty. After Annie bought a coat for $115 and Betty bought a skirt for $38, 
        	Betty had 2 times as much money as Annie. How much money had Annie at first?'''
        
        self.PersonNames = random.sample(PersonName.GirlName,2)
        self.person1 = self.PersonNames[0]
        self.person2 = self.PersonNames[1]
        self.ItemPool = {"1":["laptop","printer",random.randrange(150,300,2)],"2":["computer","thumb drive",random.randrange(50,100,2)],"3":["magazine","notebook",random.randrange(4,10,2)],
        		"4":["dress","handbag",random.randrange(16,50,2)],"5":["box of chocolates","bag of potato chips",random.randrange(2,6,2)],"6":["bicycle","bicycle accessories",random.randrange(16,30,2)],
        		"7":["coffee maker","mug",random.randrange(4,15,2)],"8":["DVD player","movie DVD",random.randrange(8,20,2)],"9":["box of berries","bunch of banana",random.randrange(2,6,2)],
        		"10":["swimsuit","ear plugs",random.randrange(4,10,2)],"11":["TV","phone",random.randrange(150,300,2)],"12":["jacket","shirt",random.randrange(20,50,2)],
        		"13":["pair of shoes","jersey",random.randrange(16,40,2)],"14":["book","pencil",random.randrange(2,6,2)],"15":["pizza","can of soft drink",random.randrange(2,4,2)],
        		"16":["book","toy",random.randrange(4,10,2)],"17":["table","lamp",random.randrange(10,30,2)],"18":["set meal","cup of coffee",random.randrange(2,6,2)],
        		"19":["sofa","carpet",random.randrange(100,300,2)],"20":["bouquet of flowers","flower vase",random.randrange(6,20,2)]}
        self.key = self.ItemPool.keys()[randint(0,len(self.ItemPool)-1)]
        self.item1 = self.ItemPool[self.key][0]
        self.item2 = self.ItemPool[self.key][1]
        self.price2 = self.ItemPool[self.key][2]
        self.InitialAmount2 = randint(3,5) * self.price2
        self.InitialAmount1 = 2 * self.InitialAmount2
        self.price1 = (3*self.InitialAmount2 + self.price2)/2
        self.FinalAmount1 = self.InitialAmount1 - self.price1
        self.FinalAmount2 = self.InitialAmount2 - self.price2

        self.answer = self.InitialAmount1

        self.problem1 = "%s had 2 times as much money as %s. After %s bought a %s for $%d and %s bought a %s for $%d, %s had 2 times as much money as %s. How much money had %s at first?"%(self.person1,self.person2,self.person1,self.item1,self.price1,self.person2,self.item2,self.price2,self.person2,self.person1,self.person1)
        self.problem = self.problem1

        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType81(self.problem,self.answer,self.person1,self.person2,self.item1,self.item2,self.price1,self.price2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"$",'unit':'','problem_type':"ProblemType81"}

    def ExplainType81(self,problem,answer,person1,person2,item1,item2,price1,price2):
        self.answer_text = "The correct answer is: <b>$"+str(answer)
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'>"
        self.table_text = self.table_text + "<tr><td></td><td align='center' colspan=2>?<br><img src='/images/up_curly_braces_2cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td></td><td align='right' colspan=2>$"+str(price1)+"</td></tr>"
        self.table_text = self.table_text + "<tr><td>"+person1+"</td><td colspan=2><img src='/images/explanation/P5_WN_PT81_A.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td>"+person2+"</td><td><img src='/images/explanation/P5_WN_PT81_B.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td></td><td align='right'><img src='/images/explanation/down_curly_braces_pt5cm.png'><br>$"+str(price2)+"</td>"
        self.table_text = self.table_text + "</tr></table><br>"
        
        self.solution_text = ""
        self.solution_text = self.solution_text + "<div><b>At first:</b></div>"
        self.solution_text = self.solution_text + "<div>Let 1 pink block represent the amount of money that "+person2+" had at first.</div>"
        self.solution_text = self.solution_text + "<div>Since "+person1+" had 2 times as much money as "+person2+", "+person1+"'s money can be represented by 2 pink blocks.</div><br>"
        self.solution_text = self.solution_text + "<div><b>After the purchases:</b></div>"
        self.solution_text = self.solution_text + "<div>Let 1 yellow block represents the amount of money "+person1+" had left.</div>"
        self.solution_text = self.solution_text + "<div>Since "+person2+" had 2 times as much money left as "+person1+", "+person2+"' money can be represented by 2 yellow blocks.</div><br>"
        self.solution_text = self.solution_text + "<div>Therefore, at first, "+person2+" had $"+str(price2)+" + 1 yellow block + 1 yellow block = 1 pink block</div>"
        self.solution_text = self.solution_text + "<div>Since at first, "+person1+" had 2 times as much money as "+person2+", she had 2 pink blocks = 2x($"+str(price2)+" + 2 yellow blocks)</div><br>"
        self.solution_text = self.solution_text + "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>Consider each yellow block as 1 unit.</div>"
        self.solution_text = self.solution_text + "<div>3 units = $"+str(price1)+" - (2 x $"+str(price2)+") = $"+str(price1-2*price2)+"</div>"
        self.solution_text = self.solution_text + "<div>1 unit = $"+str(price1-2*price2)+" &divide; 3 = $"+str((price1-2*price2)/3)+"</div><br>"
        self.solution_text = self.solution_text + "<div>1 unit + $"+str(price1)+" = $"+str((price1-2*price2)/3)+" + $"+str(price1)+" = $"+str(((price1-2*price2)/3)+price1)+"</div>"
        self.solution_text = self.solution_text + "<div>"+person1+" had $"+str(((price1-2*price2)/3)+price1)+" at first.</div>"
        self.solution_text = self.solution_text + "<br><div> Watch below video for explanation of similar problem<br>"
        VideoLink = '<object><param name="movie" value="https://www.youtube.com/v/u1zgFlCw8Aw?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded"><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "UArFG4sEyCQ";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    '''Problem Type 37 starts here'''
    def GenerateProblemType82(self):
        '''e.g.:A piece of cloth was used to make a dress and 2 similar skirts. 3 times as much cloth was used for the dress as for each skirt. 
        	If the dress used 4 metres more than each skirt, how much cloth was used altogether?'''
        
        self.person = random.choice(PersonName.GirlName)
        self.ItemPool = {"1":["jacket","skirt"],"2":["shirt","top"],"3":["blouse","skirt"],"4":["suit","jacket"],"5":["table cover","cushion case"],
        		"6":["bath towel","hand towel"],"7":["bed sheet","pillow case"]}
        self.key = self.ItemPool.keys()[randint(0,len(self.ItemPool)-1)]
        self.item1 = self.ItemPool[self.key][0]
        self.item2 = self.ItemPool[self.key][1]
        self.multiplier = randint(3,5)
        self.number = randint(2,5)
        self.diff = random.randrange((self.multiplier-1)*2,16,(self.multiplier-1))

        self.answer = (self.diff/(self.multiplier-1)*(self.number+self.multiplier))

        self.problem1 = "A piece of cloth was used to make a %s and %d similar %ss. %d times as much cloth was used for the %s as for each %s. If the %s used %d metres more than each %s, how much cloth was used altogether?"%(self.item1,self.number,self.item2,self.multiplier,self.item1,self.item2,self.item1,self.diff,self.item2)
        self.problem2 = "A %s and %d similar %ss were made using a piece of cloth. The %s used %d metres more cloth than each %s. If the %s used %d times as much cloth as each %s, how much cloth was used altogether?"%(self.item1,self.number,self.item2,self.item1,self.diff,self.item2,self.item1,self.multiplier,self.item2)
        self.problem3 = "%s made %d similar %ss and a %s using a piece of cloth. The %s used %d times as much cloth as each %s. If the %s used %d metres more cloth than each %s, how much cloth was used altogether?"%(self.person,self.number,self.item2,self.item1,self.item1,self.multiplier,self.item2,self.item1,self.diff,self.item2)
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])

        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType82(self.problem,self.answer,self.person,self.item1,self.item2,self.number,self.multiplier,self.diff)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"",'unit':'m','problem_type':"ProblemType82"}

    def ExplainType82(self,problem,answer,person,item1,item2,number,multiplier,diff):
        self.answer_text = "The correct answer is: <b>"+str(answer)+" m"
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'>"
        self.table_text = self.table_text + "<tr><td>"+item2+"</td><td><img src='/images/explanation/pink_block_pt5cm.png'></td>"
        for _i in range(multiplier-1):
            self.table_text = self.table_text + "<td></td>"    
        self.table_text = self.table_text + "<td rowspan="+str(number+1)+"><img src='/images/explanation/right_curly_braces_2cm.png'></td>"
        self.table_text = self.table_text + "<td align='center' rowspan="+str(number+1)+">?</td></tr>"
        for _i in range(number-1):
            self.table_text = self.table_text + "<tr><td>"+item2+"</td><td><img src='/images/explanation/pink_block_pt5cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td>"+item1+"</td>"
        for _i in range(multiplier):
            self.table_text = self.table_text + "<td><img src='/images/explanation/green_block_pt5cm.png'></td>"
        self.table_text = self.table_text + "</tr><tr><td></td><td></td><td align='center' colspan="+str(multiplier-1)+"><img src='/images/explanation/down_curly_braces_1cm.png' height=24 width="+str((multiplier-1)*45)+"><br>"
        self.table_text = self.table_text + str(diff)+" m </td>"
        self.table_text = self.table_text + "</tr></table><br>"
        
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(multiplier-1)+" units = "+str(diff)+" m</div>"
        self.solution_text = self.solution_text + "<div>1 unit = "+str(diff)+" m &divide; "+str(multiplier-1)+" = "+str(diff/(multiplier-1))+" m</div>"
        self.solution_text = self.solution_text + "<div>"+str(multiplier+number)+" units ="+str(multiplier+number)+" x "+str(diff/(multiplier-1))+" m = "+str((multiplier+number)*(diff/(multiplier-1)))+" m</div>"
        self.solution_text = self.solution_text + "<div>"+str((multiplier+number)*(diff/(multiplier-1)))+" m of cloth used altogether.</div>"
                
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    def GenerateProblemType83(self):
        '''e.g.:Annie made 2 similar skirts and a skirt using a 10 metre cloth. If the dress used 3 times as much cloth as each skirt, 
        	how much more cloth was used for the dress than for each skirt?'''
        
        self.person = random.choice(PersonName.GirlName)
        self.ItemPool = {"1":["jacket","skirt"],"2":["shirt","top"],"3":["blouse","skirt"],"4":["suit","jacket"],"5":["table cover","cushion case"],
        		"6":["bath towel","hand towel"],"7":["bed sheet","pillow case"]}
        self.key = self.ItemPool.keys()[randint(0,len(self.ItemPool)-1)]
        self.item1 = self.ItemPool[self.key][0]
        self.item2 = self.ItemPool[self.key][1]
        self.multiplier = randint(3,5)
        self.number = randint(2,5)
        self.diff = random.randrange((self.multiplier-1)*2,16,(self.multiplier-1))
        self.total = (self.diff/(self.multiplier-1)*(self.number+self.multiplier))
        
        self.answer = self.diff
        
        self.problem1 = "%s made %d similar %ss and a %s using a %d metre cloth. If the %s used %d times as much cloth as each %s, how much more cloth was used for the %s than for each %s?"%(self.person,self.number,self.item2,self.item1,self.total,self.item1,self.multiplier,self.item2,self.item1,self.item2)
        self.problem2 = "A %d metre cloth was used to make %d similar %ss and a %s. The %s used %d times as much cloth as each %s. How much more cloth was used for the %s than for each %s?"%(self.total,self.number,self.item2,self.item1,self.item1,self.multiplier,self.item2,self.item1,self.item2)
        self.problem3 = "A %s used %d times as much cloth as each %s. %s made %d %ss and a %s. If  she used %d metres of cloth altogether, how much more cloth was used for the %s than for each %s?"%(self.item1,self.multiplier,self.item2,self.person,self.number,self.item2,self.item1,self.total,self.item1,self.item2)
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])

        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType83(self.problem,self.answer,self.person,self.item1,self.item2,self.number,self.multiplier,self.diff,self.total)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"",'unit':'m','problem_type':"ProblemType83"}

    def ExplainType83(self,problem,answer,person,item1,item2,number,multiplier,diff,total):
        self.answer_text = "The correct answer is: <b>"+str(answer)+" m"
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'>"
        self.table_text = self.table_text + "<tr><td>"+item2+"</td><td><img src='/images/explanation/pink_block_pt5cm.png'></td>"
        for _i in range(multiplier-1):
            self.table_text = self.table_text + "<td></td>"    
        self.table_text = self.table_text + "<td rowspan="+str(number+1)+"><img src='/images/explanation/right_curly_braces_2cm.png'></td>"
        self.table_text = self.table_text + "<td align='center' rowspan="+str(number+1)+">"+str(total)+" m</td></tr>"
        for _i in range(number-1):
            self.table_text = self.table_text + "<tr><td>"+item2+"</td><td><img src='/images/explanation/pink_block_pt5cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td>"+item1+"</td>"
        for _i in range(multiplier):
            self.table_text = self.table_text + "<td><img src='/images/explanation/green_block_pt5cm.png'></td>"
        self.table_text = self.table_text + "</tr><tr><td></td><td></td><td align='center' colspan="+str(multiplier-1)+"><img src='/images/explanation/down_curly_braces_1cm.png' height=24 width="+str((multiplier-1)*45)+"><br>?</td>"       
        self.table_text = self.table_text + "</tr></table><br>"
        
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(multiplier+number)+" units = "+str(total)+" m</div>"
        self.solution_text = self.solution_text + "<div>1 unit = "+str(total)+" m &divide; "+str(multiplier+number)+" = "+str(total/(multiplier+number))+" m</div>"
        self.solution_text = self.solution_text + "<div>"+str(multiplier-1)+" units ="+str(multiplier-1)+" x "+str(total/(multiplier+number))+" m = "+str((multiplier-1)*(total/(multiplier+number)))+" m</div>"
        self.solution_text = self.solution_text + "<div>"+str((multiplier-1)*(total/(multiplier+number)))+" m more cloth was used for the "+item1+" than for each "+item2+".</div>"
                
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    '''Problem type 38 starts here'''
    def GenerateProblemType84(self):
        '''e.g.:A specialty bakery earned $2722 by selling 486 muffins and 632 buns. If each muffin cost $3, what was the price of each bun?'''

        self.ItemPool = {"1":["department store","tie","wallet",randint(10,50),randint(15,80)],"2":["home furnishings","carpet","coffee table",randint(150,300),randint(150,300)],
		"3":["bookstore","notebook","pen",randint(3,10),randint(3,10)],"4":["fashion store","handbag","belt",randint(15,50),randint(15,50)],
		"5":["supermarket","shampoo bottle","cream bottle",randint(5,15),randint(5,15)],"6":["lifestyle shop","ceramic plate","wooden tray",randint(5,15),randint(5,15)],
		"7":["lifestyle store","designer mug","designer jar",randint(5,15),randint(5,15)],"8":["department store","photo frame","candle holder",randint(5,15),randint(5,15)],
		"9":["bakery","cake","cupcake",randint(10,50),randint(5,15)],"10":["department store","blouse","shirt",randint(15,50),randint(25,75)],
		"11":["pets supplies shop","fish food bottle","dog food can",randint(5,25),randint(5,25)],"12":["toys shop","toy car","toy airplane",randint(5,25),randint(5,25)],
		"13":["sports shop","jersey","cap",randint(25,80),randint(15,40)],"14":["bookshop","pencil","pen",randint(2,5),randint(2,5)],
		"15":["fast food centre","soft drink can","burger",randint(2,3),randint(3,7)],"16":["general store","book","toy",randint(5,20),randint(5,20)],
		"17":["furniture store","table","chair",randint(45,80),randint(20,40)],"18":["florist","flower pot","plant",randint(5,25),randint(5,25)],
		"19":["home furnishings","pillow","blanket",randint(15,45),randint(50,100)],"20":["general store","pail","tumbler",randint(5,15),randint(5,15)],
		"21":["speciality bakery","muffin","bun",randint(2,4),randint(2,4)]}

        self.key = self.ItemPool.keys()[randint(0,len(self.ItemPool)-1)]
        self.store = self.ItemPool[self.key][0]
        self.item1 = self.ItemPool[self.key][1]
        self.item2 = self.ItemPool[self.key][2]
        self.price1 = self.ItemPool[self.key][3]
        self.price2 = self.ItemPool[self.key][4]
        self.number1 = randint(50,800)
        self.number2 = randint(50,800)
        self.total = self.number1*self.price1 + self.number2*self.price2

        self.answer = self.price2

        self.problem1 = "A %s earned $%d by selling %d %ss and %d %ss. If each %s cost $%d, what was the price of each %s?"%(self.store,self.total,self.number1,self.item1,self.number2,self.item2,self.item1,self.price1,self.item2)
        self.problem2 = "A %s sold %d %ss for $%d each. It also sold %d %ss. If it earned $%d altogether, find the price of each %s."%(self.store,self.number1,self.item1,self.price1,self.number2,self.item2,self.total,self.item2)
        self.problem3 = "A %s sold %d %ss and %d %ss, and earned $%d altogether. If the %ss were sold for $%d each, find the price of each %s."%(self.store,self.number1,self.item1,self.number2,self.item2,self.total,self.item1,self.price1,self.item2)
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])

        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType84(self.problem,self.answer,self.store,self.item1,self.item2,self.number1,self.number2,self.price1,self.price2,self.total)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"$",'unit':'','problem_type':"ProblemType84"}

    def ExplainType84(self,problem,answer,store,item1,item2,number1,number2,price1,price2,total):
        self.answer_text = "The correct answer is: <b>$"+str(answer)
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'>"
        self.table_text = self.table_text + "<tr><td align='center'>"+item1+"<br>"+str(number1)+" x $"+str(price1)+"<br><img src='/images/explanation/up_curly_braces_2cm.png'></td>"
        self.table_text = self.table_text + "<td align='center'>"+item2+"<br>?<br><img src='/images/explanation/up_curly_braces_2cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td><img src='/images/explanation/pink_block_2cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/green_block_2cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td align='center' colspan=2><img src='/images/explanation/down_curly_braces_2cm.png' width=90 height=24><br>$"+str(total)+"</td>"     
        self.table_text = self.table_text + "</tr></table><br>"
        
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(number1)+" x $"+str(price1)+" = $"+str(number1*price1)+"</div>"
        self.solution_text = self.solution_text + "<div>The "+item1+"s were sold for a total of $"+str(number1*price1)+".</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(total)+" - $"+str(number1*price1)+" = $"+str(total-number1*price1)+"</div>"
        self.solution_text = self.solution_text + "<div>The "+item2+"s were sold for a total of "+str(total-number1*price1)+"</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(total-number1*price1)+" &divide; "+str(number2)+" = $"+str((total-number1*price1)/number2)+"</div>"
        self.solution_text = self.solution_text + "<div>The price of each "+item2+" was $"+str((total-number1*price1)/number2)+".</div>"
                
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    def GenerateProblemType85(self):
        '''e.g.:A specialty bakery earned $2722 by selling muffins and buns. Each muffin was priced at $3 and each bun was priced at $2. 
        	If 486 muffins were sold, find the number of buns that were sold.'''

        self.ItemPool = {"1":["department store","tie","wallet",randint(10,50),randint(15,80)],"2":["home furnishings","carpet","coffee table",randint(150,300),randint(150,300)],
		"3":["bookstore","notebook","pen",randint(3,10),randint(3,10)],"4":["fashion store","handbag","belt",randint(15,50),randint(15,50)],
		"5":["supermarket","shampoo bottle","cream bottle",randint(5,15),randint(5,15)],"6":["lifestyle shop","ceramic plate","wooden tray",randint(5,15),randint(5,15)],
		"7":["lifestyle store","designer mug","designer jar",randint(5,15),randint(5,15)],"8":["department store","photo frame","candle holder",randint(5,15),randint(5,15)],
		"9":["bakery","cake","cupcake",randint(10,50),randint(5,15)],"10":["department store","blouse","shirt",randint(15,50),randint(25,75)],
		"11":["pets supplies shop","fish food bottle","dog food can",randint(5,25),randint(5,25)],"12":["toys shop","toy car","toy airplane",randint(5,25),randint(5,25)],
		"13":["sports shop","jersey","cap",randint(25,80),randint(15,40)],"14":["bookshop","pencil","pen",randint(2,5),randint(2,5)],
		"15":["fast food centre","soft drink can","burger",randint(2,3),randint(3,7)],"16":["general store","book","toy",randint(5,20),randint(5,20)],
		"17":["furniture store","table","chair",randint(45,80),randint(20,40)],"18":["florist","flower pot","plant",randint(5,25),randint(5,25)],
		"19":["home furnishings","pillow","blanket",randint(15,45),randint(50,100)],"20":["general store","pail","tumbler",randint(5,15),randint(5,15)],
		"21":["speciality bakery","muffin","bun",randint(2,4),randint(2,4)]}

        self.key = self.ItemPool.keys()[randint(0,len(self.ItemPool)-1)]
        self.store = self.ItemPool[self.key][0]
        self.item1 = self.ItemPool[self.key][1]
        self.item2 = self.ItemPool[self.key][2]
        self.price1 = self.ItemPool[self.key][3]
        self.price2 = self.ItemPool[self.key][4]
        self.number1 = randint(50,800)
        self.number2 = randint(50,800)
        self.total = self.number1*self.price1 + self.number2*self.price2

        self.answer = self.number2

        self.problem1 = "A %s earned $%d by selling %ss and %ss. Each %s was priced at $%d and each %s was priced at $%d. If %d %ss were sold, find the number of %ss that were sold."%(self.store,self.total,self.item1,self.item2,self.item1,self.price1,self.item2,self.price2,self.number1,self.item1,self.item2)
        self.problem2 = "A %s sold %d %ss at $%d each. It also sold some %ss at $%d each. If it earned $%d altogether, how many %ss were sold?"%(self.store,self.number1,self.item1,self.price1,self.item2,self.price2,self.total,self.item2)
        self.problem = random.choice([self.problem1,self.problem2])

        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType85(self.problem,self.answer,self.store,self.item1,self.item2,self.number1,self.number2,self.price1,self.price2,self.total)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"",'unit':self.item2+"s",'problem_type':"ProblemType85"}

    def ExplainType85(self,problem,answer,store,item1,item2,number1,number2,price1,price2,total):
        self.answer_text = "The correct answer is: <b>"+str(answer)+" "+item2+"s"
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'>"
        self.table_text = self.table_text + "<tr><td align='center'>"+item1+"<br>"+str(number1)+" x $"+str(price1)+"<br><img src='/images/explanation/up_curly_braces_2cm.png'></td>"
        self.table_text = self.table_text + "<td align='center'>"+item2+"<br>?<br><img src='/images/explanation/up_curly_braces_2cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td><img src='/images/explanation/pink_block_2cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/broken_green_block_2cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td align='center' colspan=2><img src='/images/explanation/down_curly_braces_2cm.png'><br>$"+str(total)+"</td>"     
        self.table_text = self.table_text + "</tr></table><br>"
        
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(number1)+" x $"+str(price1)+" = $"+str(number1*price1)+"</div>"
        self.solution_text = self.solution_text + "<div>The "+item1+"s were sold for a total of $"+str(number1*price1)+".</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(total)+" - $"+str(number1*price1)+" = $"+str(total-number1*price1)+"</div>"
        self.solution_text = self.solution_text + "<div>The "+item2+"s were sold for a total of "+str(total-number1*price1)+"</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(total-number1*price1)+" &divide; "+str(price2)+" = $"+str((total-number1*price1)/price2)+"</div>"
        self.solution_text = self.solution_text + "<div>"+str(number2)+" "+item2+"s were sold.</div>"
                
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    def GenerateProblemType86(self):
        '''e.g.:A specialty store sold 486 muffins and 632 buns. If each muffin was priced at $3 and each bun at $2, how much money were they sold altogether for?'''

        self.ItemPool = {"1":["department store","tie","wallet",randint(10,50),randint(15,80)],"2":["home furnishings","carpet","coffee table",randint(150,300),randint(150,300)],
		"3":["bookstore","notebook","pen",randint(3,10),randint(3,10)],"4":["fashion store","handbag","belt",randint(15,50),randint(15,50)],
		"5":["supermarket","shampoo bottle","cream bottle",randint(5,15),randint(5,15)],"6":["lifestyle shop","ceramic plate","wooden tray",randint(5,15),randint(5,15)],
		"7":["lifestyle store","designer mug","designer jar",randint(5,15),randint(5,15)],"8":["department store","photo frame","candle holder",randint(5,15),randint(5,15)],
		"9":["bakery","cake","cupcake",randint(10,50),randint(5,15)],"10":["department store","blouse","shirt",randint(15,50),randint(25,75)],
		"11":["pets supplies shop","fish food bottle","dog food can",randint(5,25),randint(5,25)],"12":["toys shop","toy car","toy airplane",randint(5,25),randint(5,25)],
		"13":["sports shop","jersey","cap",randint(25,80),randint(15,40)],"14":["bookshop","pencil","pen",randint(2,5),randint(2,5)],
		"15":["fast food centre","soft drink can","burger",randint(2,3),randint(3,7)],"16":["general store","book","toy",randint(5,20),randint(5,20)],
		"17":["furniture store","table","chair",randint(45,80),randint(20,40)],"18":["florist","flower pot","plant",randint(5,25),randint(5,25)],
		"19":["home furnishings","pillow","blanket",randint(15,45),randint(50,100)],"20":["general store","pail","tumbler",randint(5,15),randint(5,15)],
		"21":["speciality bakery","muffin","bun",randint(2,4),randint(2,4)]}

        self.key = self.ItemPool.keys()[randint(0,len(self.ItemPool)-1)]
        self.store = self.ItemPool[self.key][0]
        self.item1 = self.ItemPool[self.key][1]
        self.item2 = self.ItemPool[self.key][2]
        self.price1 = self.ItemPool[self.key][3]
        self.price2 = self.ItemPool[self.key][4]
        self.number1 = randint(50,800)
        self.number2 = randint(50,800)
        self.total = self.number1*self.price1 + self.number2*self.price2

        self.answer = self.total

        self.problem1 = "A %s sold %d %ss and %d %ss. If each %s was priced at $%d and each %s at $%d, how much money were they sold altogether for?"%(self.store,self.number1,self.item1,self.number2,self.item2,self.item1,self.price1,self.item2,self.price2)
        self.problem2 = "A %s was selling %ss for $%d each and %ss for $%d each. If it sold %d %ss and %d %ss, find the amount of money that they were sold altogether for."%(self.store,self.item1,self.price1,self.item2,self.price2,self.number1,self.item1,self.number2,self.item2)
        self.problem3 = "A %s sold %d %ss for $%d each. It also sold %d %ss for $%d each. How much money were the %ss and %ss sold altogether for?"%(self.store,self.number1,self.item1,self.price1,self.number2,self.item2,self.price2,self.item1,self.item2)
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])

        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType86(self.problem,self.answer,self.store,self.item1,self.item2,self.number1,self.number2,self.price1,self.price2,self.total)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"$",'unit':"",'problem_type':"ProblemType86"}

    def ExplainType86(self,problem,answer,store,item1,item2,number1,number2,price1,price2,total):
        self.answer_text = "The correct answer is: <b>$"+str(answer)
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'>"
        self.table_text = self.table_text + "<tr><td align='center'>"+item1+"<br>"+str(number1)+" x $"+str(price1)+"<br><img src='/images/explanation/up_curly_braces_2cm.png'></td>"
        self.table_text = self.table_text + "<td align='center'>"+item2+"<br>"+str(number2)+" x $"+str(price2)+"<br><img src='/images/explanation/up_curly_braces_2cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td><img src='/images/explanation/pink_block_2cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/green_block_2cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td align='center' colspan=2><img src='/images/explanation/down_curly_braces_2cm.png'><br>?</td>"     
        self.table_text = self.table_text + "</tr></table><br>"
        
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(number1)+" x $"+str(price1)+" = $"+str(number1*price1)+"</div>"
        self.solution_text = self.solution_text + "<div>The "+item1+"s were sold for a total of $"+str(number1*price1)+".</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(number2)+" x $"+str(price2)+" = $"+str(number2*price2)+"</div>"
        self.solution_text = self.solution_text + "<div>The "+item2+"s were sold for a total of $"+str(number2*price2)+".</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(number1*price1)+" + $"+str(number2*price2)+" = $"+str(number1*price1+number2*price2)+"</div>"
        self.solution_text = self.solution_text + "<div>The "+item1+"s and "+item2+"s were sold for $"+str(number1*price1+number2*price2)+" altogether.</div>"
                
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    '''Problem Type 39 starts here'''
    def GenerateProblemType87(self):
        '''e.g.:At a zoo, an adult ticket costs $16 and a child ticket costs $9. If 130 adults and 110 children visited the zoo, how much money was collected altogether?'''

        self.ItemPool = {"1":["community picnic","attended",randint(5,15)],"2":["bird park","visited",randint(15,25)],"3":["butterfly park","visited",randint(15,25)],
			"4":["movie show","went to",randint(15,25)],"5":["tennis game","attended",randint(25,40)],"6":["badminton game","attended",randint(25,40)],
			"7":["concert","attended",randint(25,40)],"8":["school fair","attended",randint(5,15)],"9":["fair","attended",randint(5,15)],
			"10":["theme park","visited",randint(30,60)],"11":["soccer game","attended",randint(30,60)],"12":["food festival","went to",randint(5,15)],
			"13":["zoo","visited",randint(15,25)]}

        self.key = self.ItemPool.keys()[randint(0,len(self.ItemPool)-1)]
        self.place = self.ItemPool[self.key][0]
        self.action = self.ItemPool[self.key][1]
        self.price1 = self.ItemPool[self.key][2]
        '''child ticket is 25-75% of an adult'''
        self.price2 = int(randint(25,75)*self.price1/100)+1
        self.number1 = randint(100,1000)
        self.number2 = randint(100,1000)
        self.total = self.number1*self.price1 + self.number2*self.price2

        self.answer = self.total


        self.problem1 = "At a %s, an adult ticket costs $%d and a child ticket costs $%d. If %d adults and %d children %s the %s, how much money was collected altogether?"%(self.place,self.price1,self.price2,self.number1,self.number2,self.action,self.place)
        self.problem2 = "%d adults and %d children %s a %s. If an adult ticket cost $%d and a child ticket cost $%d, how much money was collected altogether?"%(self.number1,self.number2,self.action,self.place,self.price1,self.price2)
        self.problem3 = "At a %s, %d adult tickets and %d child tickets were sold.  If each adult ticket cost $%d and each child ticket cost $%d, find the sum of money that was collected altogether."%(self.place,self.number1,self.number2,self.price1,self.price2)
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])

        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType87(self.problem,self.answer,self.place,self.number1,self.number2,self.price1,self.price2,self.total)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"$",'unit':"",'problem_type':"ProblemType87"}

    def ExplainType87(self,problem,answer,place,number1,number2,price1,price2,total):
        self.answer_text = "The correct answer is: <b>$"+str(answer)
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'>"
        self.table_text = self.table_text + "<tr><td align='center'>Adults<br>"+str(number1)+" x $"+str(price1)+"<br><img src='/images/explanation/up_curly_braces_2cm.png'></td>"
        self.table_text = self.table_text + "<td align='center'>Children<br>"+str(number2)+" x $"+str(price2)+"<br><img src='/images/explanation/up_curly_braces_2cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td><img src='/images/explanation/pink_block_2cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/green_block_2cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td align='center' colspan=2><img src='/images/explanation/down_curly_braces_2cm.png'><br>?</td>"     
        self.table_text = self.table_text + "</tr></table><br>"
        
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(number1)+" x $"+str(price1)+" = $"+str(number1*price1)+"</div>"
        self.solution_text = self.solution_text + "<div>A total of $"+str(number1*price1)+" was collected from the sale of adult tickets.</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(number2)+" x $"+str(price2)+" = $"+str(number2*price2)+"</div>"
        self.solution_text = self.solution_text + "<div>A total of $"+str(number2*price2)+" was collected from the sale of child tickets.</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(number1*price1)+" + $"+str(number2*price2)+" = $"+str(number1*price1+number2*price2)+"</div>"
        self.solution_text = self.solution_text + "<div>A sum of $"+str(number1*price1+number2*price2)+" was collected altogether.</div>"
        self.solution_text = self.solution_text + "<br><div> Watch below video for explanation of similar problem<br>"
        VideoLink = '<object><param name="movie" value="https://www.youtube.com/v/u1zgFlCw8Aw?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded"><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "nraJqwZ3q1I";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
                
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    def GenerateProblemType88(self):
        '''e.g.:At a zoo, an adult ticket costs $16 and a child ticket costs $9. If 130 adults and 110 children visited the zoo, how much money was collected altogether?'''

        self.ItemPool = {"1":["community picnic","attended",randint(5,15)],"2":["bird park","visited",randint(15,25)],"3":["butterfly park","visited",randint(15,25)],
            "4":["movie show","went to",randint(15,25)],"5":["tennis game","attended",randint(25,40)],"6":["badminton game","attended",randint(25,40)],
            "7":["concert","attended",randint(25,40)],"8":["school fair","attended",randint(5,15)],"9":["fair","attended",randint(5,15)],
            "10":["theme park","visited",randint(30,60)],"11":["soccer game","attended",randint(30,60)],"12":["food festival","went to",randint(5,15)],
            "13":["zoo","visited",randint(15,25)]}

        self.key = self.ItemPool.keys()[randint(0,len(self.ItemPool)-1)]
        self.place = self.ItemPool[self.key][0]
        self.action = self.ItemPool[self.key][1]
        self.price1 = self.ItemPool[self.key][2]
        '''child ticket is 25-75% of an adult'''
        self.price2 = int(randint(25,75)*self.price1/100)+1
        self.number1 = randint(100,1000)
        self.number2 = randint(100,1000)
        self.total = self.number1*self.price1 + self.number2*self.price2

        self.answer = self.number2

        self.problem1 = "A %s earned $%d by selling tickets to adults and children. Each adult ticket cost $%d and each child ticket cost $%d. If %d adults %s the %s, find the number of children who %s the %s."%(self.place,self.total,self.price1,self.price2,self.number1,self.action,self.place,self.action,self.place)
        self.problem2 = "A %s sold %d adult tickets for $%s each. It also sold some child tickets for $%d each. If it earned $%d altogether, how many children %s the %s?"%(self.place,self.number1,self.price1,self.price2,self.total,self.action,self.place) 
        self.problem = random.choice([self.problem1,self.problem2])

        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType88(self.problem,self.answer,self.place,self.number1,self.number2,self.price1,self.price2,self.total,self.action)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"",'unit':"children",'problem_type':"ProblemType88"}

    def ExplainType88(self,problem,answer,place,number1,number2,price1,price2,total,action):
        self.answer_text = "The correct answer is: <b>"+str(answer)+" children"
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'>"
        self.table_text = self.table_text + "<tr><td align='center'>Adults<br>"+str(number1)+" x $"+str(price1)+"<br><img src='/images/explanation/up_curly_braces_2cm.png'></td>"
        self.table_text = self.table_text + "<td align='center'>Children<br>?<br><img src='/images/explanation/up_curly_braces_2cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td><img src='/images/explanation/pink_block_2cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/broken_green_block_2cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td align='center' colspan=2><img src='/images/explanation/down_curly_braces_2cm.png'><br>$"+str(total)+"</td>"     
        self.table_text = self.table_text + "</tr></table><br>"
        
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(number1)+" x $"+str(price1)+" = $"+str(number1*price1)+"</div>"
        self.solution_text = self.solution_text + "<div>The adult tickets were sold for a total of $"+str(number1*price1)+".</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(total)+" - $"+str(number1*price1)+" = $"+str(total-number1*price1)+"</div>"
        self.solution_text = self.solution_text + "<div>The child tickets were sold for a total of $"+str(total-number1*price1)+".</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(total-number1*price1)+" &divide; $"+str(price2)+" = "+str((total-number1*price1)/price2)+"</div>"
        self.solution_text = self.solution_text + "<div>There were "+str((total-number1*price1)/price2)+" children who "+str(action)+" the "+str(place)+".</div>"
                
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    def GenerateProblemType89(self):
        '''e.g.:A zoo earned $2930 by selling tickets to members and non-members. Each member ticket cost $9 and each non-member ticket cost $16. 
            If 130 members visited the zoo, find the number of non-members who visited the zoo. '''

        self.ItemPool = {"1":["community picnic","attended","veteran","non-veteran",randint(5,15)],"2":["bird park","visited","member","non-member",randint(15,25)],
                         "3":["butterfly park","visited","member","non-member",randint(15,25)],"4":["movie show","went to","coupon holder","non-coupon holder",randint(5,15)],
                         "5":["tennis game","attended","VIP","non-VIP",randint(25,40)],"6":["badminton game","attended","VIP","non-VIP",randint(25,40)],
                         "7":["concert","attended","special pass holder","regular pass holder",randint(30,60)],"8":["museum","visited","season-pass holder","non-pass holder",randint(5,15)],
                         "9":["soccer game","attended","class A spectator","class B spectator",randint(30,60)],"10":["bird park","visited","season-pass holder","non-pass holder",randint(15,25)],
                         "11":["butterfly park","visited","season-pass holder","non-pass holder",randint(15,25)],"12":["movie show","went to","season-pass holder","non-pass holder",randint(5,15)],
                         "13":["theme park","visited","member","non-member",randint(30,60)],"14":["theme park","visited","season-pass holder","non-pass holder",randint(30,60)],
                         "15":["film festival","attended","VIP","non-VIP",randint(15,25)],"16":["charity run","signed up for","veteran","non-veteran",randint(15,25)],
                         "17":["zoo","visited","member","non-member",randint(15,25)]}

        self.key = self.ItemPool.keys()[randint(0,len(self.ItemPool)-1)]
        self.place = self.ItemPool[self.key][0]
        self.action = self.ItemPool[self.key][1]
        self.person1 = self.ItemPool[self.key][2]
        self.person2 = self.ItemPool[self.key][3]
        self.price2 = self.ItemPool[self.key][4]
        '''member ticket is 50-75% of a non-member'''
        self.price1 = int(randint(25,75)*self.price2/100)+1
        self.number1 = randint(100,1000)
        self.number2 = randint(100,1000)
        self.total = self.number1*self.price1 + self.number2*self.price2

        self.answer = self.number2

        self.problem1 = "A %s earned $%d by selling tickets to %ss and %ss. Each %s ticket cost $%d and each %s ticket cost $%d. If %d %ss %s the %s, find the number of %ss who %s the %s."%(self.place,self.total,self.person1,self.person2,self.person1,self.price1,self.person2,self.price2,self.number1,self.person1,self.action,self.place,self.person2,self.action,self.place)
        self.problem2 = "A %s sold %d %s tickets for $%d each. It also sold some %s tickets for $%d each. If it earned $%d altogether, how many %ss %s the %s?"%(self.place,self.number1,self.person1,self.price1,self.person2,self.price2,self.total,self.person2,self.action,self.place) 
        self.problem = random.choice([self.problem1,self.problem2])

        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType89(self.problem,self.answer,self.place,self.person1,self.person2,self.number1,self.number2,self.price1,self.price2,self.total,self.action)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"",'unit':self.person2,'problem_type':"ProblemType89"}

    def ExplainType89(self,problem,answer,place,person1,person2,number1,number2,price1,price2,total,action):
        self.answer_text = "The correct answer is: <b>"+str(answer)+" "+person2
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'>"
        self.table_text = self.table_text + "<tr><td align='center'>"+person1+"s<br>"+str(number1)+" x $"+str(price1)+"<br><img src='/images/explanation/up_curly_braces_2cm.png'></td>"
        self.table_text = self.table_text + "<td align='center'>"+person2+"s<br>?<br><img src='/images/explanation/up_curly_braces_2cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td><img src='/images/explanation/pink_block_2cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/broken_green_block_2cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td align='center' colspan=2><img src='/images/explanation/down_curly_braces_2cm.png'><br>$"+str(total)+"</td>"     
        self.table_text = self.table_text + "</tr></table><br>"
        
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(number1)+" x $"+str(price1)+" = $"+str(number1*price1)+"</div>"
        self.solution_text = self.solution_text + "<div>The "+person1+" tickets were sold for a total of $"+str(number1*price1)+".</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(total)+" - $"+str(number1*price1)+" = $"+str(total-number1*price1)+"</div>"
        self.solution_text = self.solution_text + "<div>The "+person2+" tickets were sold for a total of $"+str(total-number1*price1)+".</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(total-number1*price1)+" &divide; $"+str(price2)+" = "+str((total-number1*price1)/price2)+"</div>"
        self.solution_text = self.solution_text + "<div>There were "+str((total-number1*price1)/price2)+" "+person2+" who "+str(action)+" the "+str(place)+".</div>"
                
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    def GenerateProblemType90(self):
        '''e.g.:A zoo earned $2930 by selling 130 member tickets and 110 non-member tickets. 
            If each member ticket cost $16, what was the cost of each non-member ticket?'''

        self.ItemPool = {"1":["community picnic","attended","veteran","non-veteran",randint(5,15)],"2":["bird park","visited","member","non-member",randint(15,25)],
                         "3":["butterfly park","visited","member","non-member",randint(15,25)],"4":["movie show","went to","coupon holder","non-coupon holder",randint(5,15)],
                         "5":["tennis game","attended","VIP","non-VIP",randint(25,40)],"6":["badminton game","attended","VIP","non-VIP",randint(25,40)],
                         "7":["concert","attended","special pass holder","regular pass holder",randint(30,60)],"8":["museum","visited","season-pass holder","non-pass holder",randint(5,15)],
                         "9":["soccer game","attended","class A spectator","class B spectator",randint(30,60)],"10":["bird park","visited","season-pass holder","non-pass holder",randint(15,25)],
                         "11":["butterfly park","visited","season-pass holder","non-pass holder",randint(15,25)],"12":["movie show","went to","season-pass holder","non-pass holder",randint(5,15)],
                         "13":["theme park","visited","member","non-member",randint(30,60)],"14":["theme park","visited","season-pass holder","non-pass holder",randint(30,60)],
                         "15":["film festival","attended","VIP","non-VIP",randint(15,25)],"16":["charity run","signed up for","veteran","non-veteran",randint(15,25)],
                         "17":["zoo","visited","member","non-member",randint(15,25)]}

        self.key = self.ItemPool.keys()[randint(0,len(self.ItemPool)-1)]
        self.place = self.ItemPool[self.key][0]
        self.action = self.ItemPool[self.key][1]
        self.person1 = self.ItemPool[self.key][2]
        self.person2 = self.ItemPool[self.key][3]
        self.price2 = self.ItemPool[self.key][4]
        '''member ticket is 50-75% of a non-member'''
        self.price1 = int(randint(25,75)*self.price2/100)+1
        self.number1 = randint(100,1000)
        self.number2 = randint(100,1000)
        self.total = self.number1*self.price1 + self.number2*self.price2

        self.answer = self.price2

        self.problem1 = "A %s earned $%d by selling %d %s tickets and %d %s tickets. If each %s ticket cost $%d, what was the cost of each %s ticket?"%(self.place,self.total,self.number1,self.person1,self.number2,self.person2,self.person1,self.price1,self.person2) 
        self.problem2 = "A %s sold %d %s tickets for $%d each. It also sold %d %s tickets. If it earned $%d altogether, find the cost of each %s ticket?"%(self.place,self.number1,self.person1,self.price1,self.number2,self.person2,self.total,self.person2)
        self.problem3 = "A %s sold %d %s tickets and %d %s tickets, and earned $%d altogether. If the %s tickets were sold for $%d each, find the cost of each %s ticket."%(self.place,self.number1,self.person1,self.number2,self.person2,self.total,self.person1,self.price1,self.person2)
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])

        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType90(self.problem,self.answer,self.place,self.person1,self.person2,self.number1,self.number2,self.price1,self.price2,self.total,self.action)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"$",'unit':"",'problem_type':"ProblemType90"}

    def ExplainType90(self,problem,answer,place,person1,person2,number1,number2,price1,price2,total,action):
        self.answer_text = "The correct answer is: <b>$"+str(answer)
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'>"
        self.table_text = self.table_text + "<tr><td align='center'>"+person1+"s<br>"+str(number1)+" x $"+str(price1)+"<br><img src='/images/explanation/up_curly_braces_2cm.png'></td>"
        self.table_text = self.table_text + "<td align='center'>"+person2+"s<br>?<br><img src='/images/explanation/up_curly_braces_2cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td><img src='/images/explanation/pink_block_2cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/broken_green_block_2cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td align='center' colspan=2><img src='/images/explanation/down_curly_braces_2cm.png'><br>$"+str(total)+"</td>"     
        self.table_text = self.table_text + "</tr></table><br>"
        
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(number1)+" x $"+str(price1)+" = $"+str(number1*price1)+"</div>"
        self.solution_text = self.solution_text + "<div>The "+person1+" tickets were sold for a total of $"+str(number1*price1)+".</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(total)+" - $"+str(number1*price1)+" = $"+str(total-number1*price1)+"</div>"
        self.solution_text = self.solution_text + "<div>The "+person2+" tickets were sold for a total of $"+str(total-number1*price1)+".</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(total-number1*price1)+" &divide; "+str(number2)+" = "+str((total-number1*price1)/number2)+"</div>"
        self.solution_text = self.solution_text + "<div>The cost of each "+person2+" ticket was $"+str((total-number1*price1)/number2)+".</div>"
                
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    '''ProblemType 40 starts here'''
    def GenerateProblemType91(self):
        '''e.g.:A notebook costs twice as much as a pen. Annie bought 5 notebooks and 3 pens. Betty bought 4 notebooks and 3 pens. 
                If each notebook costs $2, how much money did they spend altogether?'''

        self.Persons = random.sample(PersonName.GirlName,2)
        self.person1 = self.Persons[0]
        self.person2= self.Persons[1]
        self.ItemPool = {"1":["sharpener","pencil",randint(2,4)],"2":["toy robot","toy car",randint(10,30)],"3":["shirt","T-shirt",randint(10,20)],
                         "4":["cap","bandana",randint(10,20)],"5":["tie","tie clip",randint(10,20)],"6":["hair band","hair clip",randint(2,6)],
                         "7":["bracelet","ring",randint(10,30)],"8":["drawing book","photo album",randint(2,6)],"9":["novel","text book",randint(5,12)],
                         "10":["ruler","eraser",randint(2,4)],"11":["red card","blue card",randint(2,4)],"12":["stamp","envelope",randint(2,4)],
                         "13":["hoop","Rubber duck",randint(4,7)],"14":["pineapple","apple",randint(2,4)],"15":["dvd","DVD case",randint(3,5)],
                         "16":["tray","plate",randint(3,5)],"17":["bowl","spoon",randint(3,5)],"18":["cup","saucer",randint(3,5)],
                         "19":["mug","teaspoon",randint(3,5)],"20":["folder","binding ring",randint(3,5)],"21":["notebook","pen",randint(3,5)]
                         }
        self.key = self.ItemPool.keys()[randint(0,len(self.ItemPool)-1)]
        self.item1 = self.ItemPool[self.key][0]
        self.item2 = self.ItemPool[self.key][1]
        self.price2 = self.ItemPool[self.key][2]
        self.multiplier = randint(2,5)
        self.price1 = self.price2 * self.multiplier
        self.number1 = randint(3,8)
        self.number2 = randint(3,8)
        self.number3 = randint(3,8)
        self.number4 = randint(3,8)
        self.total = ((self.number1+self.number3)*self.price1 + (self.number2+self.number4)*self.price2)

        self.answer = self.total

        self.problem1 = "A %s costs %d times as much as a %s. %s bought %d %ss and %d %ss. %s bought %d %ss and %d %ss. If each %s costs $%d, how much money did they spend altogether?"%(self.item1,self.multiplier,self.item2,self.person1,self.number1,self.item1,self.number2,self.item2,self.person2,self.number3,self.item1,self.number4,self.item2,self.item1,self.price1)
        self.problem2 = "%s bought %d %ss and %d %ss. %s bought %d %ss and %d %ss. A %s cost %d times as much as a %s. If each %s cost $%d, find the sum of money they spent altogether."%(self.person1,self.number1,self.item1,self.number2,self.item2,self.person2,self.number3,self.item1,self.number4,self.item2,self.item1,self.multiplier,self.item2,self.item1,self.price1)
        self.problem3 = "%s bought %d %ss and %d %ss. %s bought %d %ss and %d %ss. If each %s cost $%d, and each %s cost %d times as much as a %s, how much money did they spend altogether?"%(self.person1,self.number1,self.item1,self.number2,self.item2,self.person2,self.number3,self.item1,self.number4,self.item2,self.item1,self.price1,self.item1,self.multiplier,self.item2)      
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])

        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType91(self.problem,self.answer,self.person1,self.person2,self.item1,self.item2,self.price1,self.price2,self.number1,self.number2,self.number3,self.number4,self.multiplier,self.total)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"$",'unit':"",'problem_type':"ProblemType91"}

    def ExplainType91(self,problem,answer,person1,person2,item1,item2,price1,price2,number1,number2,number3,number4,multiplier,total):
        self.answer_text = "The correct answer is: <b>$"+str(answer)
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'>"
        self.table_text = self.table_text + "<tr><td></td><td align='center'>$"+str(price1)+"<br>"
        self.table_text = self.table_text + "<img src='/images/explanation/up_curly_braces_pt5cm.png' height=24></td></tr>"
        self.table_text = self.table_text + "<tr><td>"+item1+"</td>"
        for _i in range(multiplier):
            self.table_text = self.table_text + "<td><img src='/images/explanation/green_block_pt5cm.png'></td>"
        self.table_text = self.table_text + "</tr><tr><td>"+item2+"</td><td><img src='/images/explanation/pink_block_pt5cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td></td><td align='center'><img src='/images/explanation/down_curly_braces_pt5cm.png'><br>?"  
        self.table_text = self.table_text + "</tr></table><br>"
        
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>Cost of each "+item1+" = $"+str(price1)+"</div>"
        self.solution_text = self.solution_text + "<div>Cost of each "+item2+" = $"+str(price1)+" &divide; "+str(multiplier)+" = $"+str(price1/multiplier)+"</div><br>"
        self.solution_text = self.solution_text + "<div><table border=1 id ='explain' cellpadding=10><tr><th border=1>Name</th><th>Number of "+item1+"s<br>x<br>Unit cost</th>"
        self.solution_text = self.solution_text + "<th>Number of <br>"+item2+"s<br>x<br>Unit cost</th><th>Amount<br>spent</th></tr>"
        self.solution_text = self.solution_text + "<tr><td align='center'>"+person1+"<td align='center'>"+str(number1)+" x $"+str(price1)+" = $"+str(number1*price1)+"</td>"
        self.solution_text = self.solution_text + "<td align='center'>"+str(number2)+" x $"+str(price2)+" = $"+str(number2*price2)+"</td>"
        self.solution_text = self.solution_text + "<td align='center'>$"+str(number1*price1+number2*price2)+"</td></tr>"       
        self.solution_text = self.solution_text + "<tr><td align='center'>"+person2+"<td align='center'>"+str(number3)+" x $"+str(price1)+" = $"+str(number3*price1)+"</td>"
        self.solution_text = self.solution_text + "<td align='center'>"+str(number4)+" x $"+str(price2)+" = $"+str(number4*price2)+"</td>"
        self.solution_text = self.solution_text + "<td align='center'>$"+str(number3*price1+number4*price2)+"</td></tr>" 
        self.solution_text = self.solution_text + "<tr><td colspan=3 align='right'>Total</td>"
        self.solution_text = self.solution_text + "<td align='center'>$"+str(number3*price1+number4*price2+number1*price1+number2*price2)+"</td></tr><br></table></div><br>"
        self.solution_text = self.solution_text + "<div>They spent $"+str(number3*price1+number4*price2+number1*price1+number2*price2)+" altogether.</div>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain
    
    '''ProblemType 43 starts here'''
    def GenerateProblemType92(self):
        '''e.g.: Annie was born 16 years  before Betty. What is Annie's age when she is 3 times as old as Betty?'''

        self.Persons = random.sample(PersonName.BoyName,2)
        self.person1 = self.Persons[0]
        self.person2= self.Persons[1]
        self.multiplier = randint(3,5)
        self.diff = random.randrange(self.multiplier-1,50,self.multiplier-1)
        
        self.answer = (self.diff*(self.multiplier)/(self.multiplier-1))

        self.problem1 = "%s was born %d years before %s. What is %s's age when he is %d times as old as %s?"%(self.person1,self.diff,self.person2,self.person1,self.multiplier,self.person2)
        self.problem2 = "%s was born %d years after %s. Find %s's age when he is %d times as old as %s."%(self.person2,self.diff,self.person1,self.person1,self.multiplier,self.person2)
        self.problem = random.choice([self.problem1,self.problem2])

        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType92(self.problem,self.answer,self.person1,self.person2,self.multiplier,self.diff)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"",'unit':"years",'problem_type':"ProblemType92"}

    def ExplainType92(self,problem,answer,person1,person2,multiplier,diff):
        self.answer_text = "The correct answer is: <b>"+str(answer)+" years"
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'>"
        self.table_text = self.table_text + "<tr><td></td><td></td><td align='center' colspan="+str(multiplier-1)+">"+str(diff)+"<br>"
        self.table_text = self.table_text + "<img src='/images/explanation/up_curly_braces_1cm.png' height=24 width="+str((multiplier-1)*34)+"></td></tr>"
        self.table_text = self.table_text + "<tr><td>"+person1+"</td>"
        for _i in range(multiplier):
            self.table_text = self.table_text + "<td><img src='/images/explanation/pink_block_pt5cm.png'></td>"
        self.table_text = self.table_text + "</tr><tr><td>"+person2+"</td><td><img src='/images/explanation/pink_block_pt5cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td></td><td align='center'><img src='/images/explanation/down_curly_braces_pt5cm.png'><br>?</td>"     
        self.table_text = self.table_text + "</tr></table><br>"
        
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div><b>Fact:</b> "+person1+" will always be "+str(diff)+" years older than "+person2+".</div>"
        self.solution_text = self.solution_text + "<div>So, when "+person1+" is "+str(multiplier)+" times as old as "+person2+", "
        self.solution_text = self.solution_text + person1+" will still be "+str(diff)+" years older than "+person2+".</div>"
        self.solution_text = self.solution_text + "<div>This is represented by above model diagram.</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(multiplier-1)+" units = "+str(diff)+" years</div>"
        self.solution_text = self.solution_text + "<div>1 unit = "+str(diff)+" years &divide; "+str(multiplier-1)+" = "+str(diff/(multiplier-1))+" years</div>"
        self.solution_text = self.solution_text + "<div>"+str(multiplier)+" units = "+str(multiplier)+" x "+str(diff/(multiplier-1))+" = "+str(multiplier*(diff/(multiplier-1)))+" years</div>"
        self.solution_text = self.solution_text + "<div>"+person1+" is "+str(multiplier*(diff/(multiplier-1)))+" years old when he is "+str(multiplier)+" times as old as "+person2+".</div>"
        self.solution_text = self.solution_text + "<br><div> Watch below video for explanation of similar problem<br>"
        VideoLink = '<object><param name="movie" value="https://www.youtube.com/v/u1zgFlCw8Aw?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded"><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "9D8JMJ0D-ow";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
                
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    '''ProblemType 44 starts here'''
    def GenerateProblemType93(self):
        '''e.g.: Annie buys a computer for $1400. She has to make a payment of $200 upfront followed by 24 monthly instalments. How much is each monthly instalment?'''
        self.person = random.choice(PersonName.GirlName)
        self.ItemPool = {"1":["computer",randint(50,100),random.choice([10,12,20,24])],"2":["mattress",randint(10,30),random.choice([10,12,20,24])],
                         "3":["sofa-set",randint(10,30),random.choice([10,12,20,24])],"4":["farm",randint(100,500),random.choice([100,120,200,240])],
                         "5":["land",randint(100,500),random.choice([100,120,200,240])],"6":["apartment",randint(200,600),random.choice([100,120,200,240])],
                         "7":["dining table",randint(10,30),random.choice([10,12,20,24])],"8":["bed",randint(10,30),random.choice([10,12,20,24])],
                         "9":["laptop",randint(30,80),random.choice([10,12,20,24])],"10":["desktop",randint(30,60),random.choice([10,12,20,24])],
                         "11":["refrigetor",randint(20,40),random.choice([10,12,20])],"12":["photocopier",randint(30,50),random.choice([10,12,20])],
                         "13":["pool table",randint(20,40),random.choice([10,12,20,24])],"14":["spa package",randint(20,40),random.choice([10,12,20,24])],
                         "15":["facial package",randint(20,40),random.choice([10,12,20,24])],"16":["plastic surgery package",randint(20,50),random.choice([10,12,20,24])],
                         "17":["massage package",randint(20,40),random.choice([10,12,20,24])],"18":["cosmetic surgery package",randint(30,50),random.choice([10,12,20,24])]
                         }
        self.key = self.ItemPool.keys()[randint(0,len(self.ItemPool)-1)]
        self.item = self.ItemPool[self.key][0]
        self.instalment = self.ItemPool[self.key][1]
        self.period = self.ItemPool[self.key][2]
        self.upfront = int(randint(10,20)*self.instalment*self.period/100)
        self.total = self.upfront + self.period*self.instalment
        
        self.answer = self.instalment

        self.problem1 = "%s buys a %s for $%d. She has to make a payment of $%d upfront followed by %d monthly instalments. How much is each monthly instalment?"%(self.person,self.item,self.total,self.upfront,self.period)
        self.problem2 = "%s buys a %s for which she pays $%d upfront. She pays the remaining sum of money by %d monthly instalments. If the %s cost her $%d, how much is each monthly instalment?"%(self.person,self.item,self.upfront,self.period,self.item,self.total)
        self.problem3 = "%s buys a %s for $%d for which she pays $%d upfront. If she pays the remaining sum of money by %d monthly instalments, how much is each monthly instalment?"%(self.person,self.item,self.total,self.upfront,self.period)
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])

        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType93(self.problem,self.answer,self.person,self.item,self.instalment,self.period,self.upfront,self.total)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"$",'unit':"",'problem_type':"ProblemType93"}

    def ExplainType93(self,problem,answer,person,item,instalment,period,upfront,total):
        self.answer_text = "The correct answer is: <b>$"+str(answer)
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'>"
        self.table_text = self.table_text + "<tr><td></td><td align='center'>$"+str(upfront)+"<br><img src='/images/explanation/up_curly_braces_pt5cm.png'></td>"
        self.table_text = self.table_text + "<td align='center'>$"+str(total)+" - $"+str(upfront)+"<br><img src='/images/explanation/up_curly_braces_2cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td>"+item+"</td><td><img src='/images/explanation/pink_block_pt5cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/yellow_block_2cm.png'></td>"
        self.table_text = self.table_text + "</tr></table><br>"
        
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(total)+" - $"+str(upfront)+" = $"+str(total-upfront)+"</div>"
        self.solution_text = self.solution_text + "<div>Total amount to be paid by instalments is $"+str(total-upfront)+".</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(total-upfront)+" &divide; "+str(period)+" = $"+str(instalment)+"</div>"
        self.solution_text = self.solution_text + "<div>Each monthly instalment is $"+str(instalment)+"</div>"
                
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    def GenerateProblemType94(self):
        '''e.g.: . Annie buys a computer. She has to make a payment of $200 upfront followed by 24 monthly instalments of $50 each. What is the cost of the computer?'''
        self.person = random.choice(PersonName.GirlName)
        self.ItemPool = {"1":["computer",randint(50,100),random.choice([10,12,20,24])],"2":["mattress",randint(10,30),random.choice([10,12,20,24])],
                         "3":["sofa-set",randint(10,30),random.choice([10,12,20,24])],"4":["farm",randint(100,500),random.choice([100,120,200,240])],
                         "5":["land",randint(100,500),random.choice([100,120,200,240])],"6":["apartment",randint(200,600),random.choice([100,120,200,240])],
                         "7":["dining table",randint(10,30),random.choice([10,12,20,24])],"8":["bed",randint(10,30),random.choice([10,12,20,24])],
                         "9":["laptop",randint(30,80),random.choice([10,12,20,24])],"10":["desktop",randint(30,60),random.choice([10,12,20,24])],
                         "11":["refrigetor",randint(20,40),random.choice([10,12,20])],"12":["photocopier",randint(30,50),random.choice([10,12,20])],
                         "13":["pool table",randint(20,40),random.choice([10,12,20,24])],"14":["spa package",randint(20,40),random.choice([10,12,20,24])],
                         "15":["facial package",randint(20,40),random.choice([10,12,20,24])],"16":["plastic surgery package",randint(20,50),random.choice([10,12,20,24])],
                         "17":["massage package",randint(20,40),random.choice([10,12,20,24])],"18":["cosmetic surgery package",randint(30,50),random.choice([10,12,20,24])]
                         }
        self.key = self.ItemPool.keys()[randint(0,len(self.ItemPool)-1)]
        self.item = self.ItemPool[self.key][0]
        self.instalment = self.ItemPool[self.key][1]
        self.period = self.ItemPool[self.key][2]
        self.upfront = int(randint(10,20)*self.instalment*self.period/100)
        self.total = self.upfront + self.period*self.instalment
        
        self.answer = self.total

        self.problem1 = "%s buys a %s. She has to make a payment of $%d upfront followed by %d monthly instalments of $%d each. What is the cost of the %s?"%(self.person,self.item,self.upfront,self.period,self.instalment,self.item)
        self.problem2 = "%s buys a %s for which she pays $%d upfront. If she pays the remaining sum of money by %d monthly instalments of $%d each, what is the cost of the %s?"%(self.person,self.item,self.upfront,self.period,self.instalment,self.item)
        self.problem3 = "%s buys a %s for which she pays $%d upfront followed by monthly instalments of $%d each for %d months. Find the cost of the %s."%(self.person,self.item,self.upfront,self.instalment,self.period,self.item)
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])

        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType94(self.problem,self.answer,self.person,self.item,self.instalment,self.period,self.upfront,self.total)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"$",'unit':"",'problem_type':"ProblemType94"}

    def ExplainType94(self,problem,answer,person,item,instalment,period,upfront,total):
        self.answer_text = "The correct answer is: <b>$"+str(answer)
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'>"
        self.table_text = self.table_text + "<tr><td></td><td align='center'>$"+str(upfront)+"<br><img src='/images/explanation/up_curly_braces_pt5cm.png'></td>"
        self.table_text = self.table_text + "<td align='center'>$"+str(period)+" x $"+str(instalment)+"<br><img src='/images/explanation/up_curly_braces_2cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td>"+item+"</td><td><img src='/images/explanation/pink_block_pt5cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/yellow_block_2cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td></td><td align='center' colspan=2><img src='/images/explanation/down_curly_braces_2cm.png' height=24 width=160><br>?</td>"
        self.table_text = self.table_text + "</tr></table><br>"
        
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(period)+" x $"+str(instalment)+" = $"+str(period*instalment)+"</div>"
        self.solution_text = self.solution_text + "<div>Total amount to be paid by instalments is $"+str(period*instalment)+".</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(period*instalment)+" + "+str(upfront)+" = $"+str(total)+"</div>"
        self.solution_text = self.solution_text + "<div>The cost of the "+item+" is $"+str(total)+".</div>"
                
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    def GenerateProblemType95(self):
        '''e.g.: Annie buys a computer for $1400. She has to make a payment of $200 upfront followed by monthly instalments of $50 each. 
                How long (in months) will it take Annie to pay off all the instalments?'''
        self.person = random.choice(PersonName.GirlName)
        self.ItemPool = {"1":["computer",randint(50,100),random.choice([10,12,20,24])],"2":["mattress",randint(10,30),random.choice([10,12,20,24])],
                         "3":["sofa-set",randint(10,30),random.choice([10,12,20,24])],"4":["farm",randint(100,500),random.choice([100,120,200,240])],
                         "5":["land",randint(100,500),random.choice([100,120,200,240])],"6":["apartment",randint(200,600),random.choice([100,120,200,240])],
                         "7":["dining table",randint(10,30),random.choice([10,12,20,24])],"8":["bed",randint(10,30),random.choice([10,12,20,24])],
                         "9":["laptop",randint(30,80),random.choice([10,12,20,24])],"10":["desktop",randint(30,60),random.choice([10,12,20,24])],
                         "11":["refrigetor",randint(20,40),random.choice([10,12,20])],"12":["photocopier",randint(30,50),random.choice([10,12,20])],
                         "13":["pool table",randint(20,40),random.choice([10,12,20,24])],"14":["spa package",randint(20,40),random.choice([10,12,20,24])],
                         "15":["facial package",randint(20,40),random.choice([10,12,20,24])],"16":["plastic surgery package",randint(20,50),random.choice([10,12,20,24])],
                         "17":["massage package",randint(20,40),random.choice([10,12,20,24])],"18":["cosmetic surgery package",randint(30,50),random.choice([10,12,20,24])]
                         }
        self.key = self.ItemPool.keys()[randint(0,len(self.ItemPool)-1)]
        self.item = self.ItemPool[self.key][0]
        self.instalment = self.ItemPool[self.key][1]
        self.period = self.ItemPool[self.key][2]
        self.upfront = int(randint(10,20)*self.instalment*self.period/100)
        self.total = self.upfront + self.period*self.instalment
        
        self.answer = self.period

        self.problem1 = "%s buys a %s for $%d. She has to make a payment of $%d upfront followed by monthly instalments of $%d each. How long (in months) will it take %s to pay off all the instalments?"%(self.person,self.item,self.total,self.upfront,self.instalment,self.person)
        self.problem2 = "%s pays $%d upfront for a %s priced at $%d. She pays the remaining sum of money by monthly instalments of $%d each. How long will it take %s to pay off all the instalments?"%(self.person,self.upfront,self.item,self.total,self.instalment,self.person)
        self.problem3 = "%s buys a %s priced at $%d and pays $%d upfront. If she pays the remaining sum of money by monthly instalments of $%d each, how many months will it take %s to pay off all the instalments?"%(self.person,self.item,self.total,self.upfront,self.instalment,self.person)
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])

        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType95(self.problem,self.answer,self.person,self.item,self.instalment,self.period,self.upfront,self.total)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"",'unit':"months",'problem_type':"ProblemType95"}

    def ExplainType95(self,problem,answer,person,item,instalment,period,upfront,total):
        self.answer_text = "The correct answer is: <b>"+str(answer)+" months"
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'>"
        self.table_text = self.table_text + "<tr><td></td><td align='center'>$"+str(upfront)+"<br><img src='/images/explanation/up_curly_braces_pt5cm.png'></td>"
        self.table_text = self.table_text + "<td align='center'>?<br><img src='/images/explanation/up_curly_braces_2cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td>"+item+"</td><td><img src='/images/explanation/pink_block_pt5cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/yellow_block_2cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td></td><td align='center' colspan=2><img src='/images/explanation/down_curly_braces_2cm.png' height=24 width=160><br>$"+str(total)+"</td>"
        self.table_text = self.table_text + "</tr></table><br>"
        
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(total)+" - $"+str(upfront)+" = $"+str(total-upfront)+"</div>"
        self.solution_text = self.solution_text + "<div>Total amount to be paid by instalments is $"+str(total-upfront)+".</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(total-upfront)+" &divide; $"+str(instalment)+" = "+str(period)+"</div>"
        self.solution_text = self.solution_text + "<div>It will take "+str(period)+" months to pay off all the instalments.</div>"
                
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    def GenerateProblemType96(self):
        '''e.g.: Annie bought a condominium for $1064000. She made a payment of $200000 upfront followed by equal monthly instalments over a period of 30 years. How much was each monthly instalment?'''
        self.person = random.choice(PersonName.BoyName)
        self.ItemPool = {"1":["condominium",randint(1000,2000),random.choice([10,12,15,20,25,30])],"2":["house",randint(1000,2000),random.choice([10,12,15,20,25,30])],
                         "3":["farm",randint(100,500),random.choice([10,12,15,20,25,30])],"4":["factory",randint(1000,2000),random.choice([10,12,15,20,25,30])],
                         "5":["land",randint(100,500),random.choice([10,12,15,20,25,30])],"6":["apartment",randint(200,600),random.choice([10,12,15,20,25,30])]                         
                         }
        self.key = self.ItemPool.keys()[randint(0,len(self.ItemPool)-1)]
        self.item = self.ItemPool[self.key][0]
        self.instalment = self.ItemPool[self.key][1]
        self.period = self.ItemPool[self.key][2]
        self.upfront = int(randint(10,20)*self.instalment*self.period*12/100)
        self.total = self.upfront + self.period*self.instalment*12
        
        self.answer = self.instalment

        self.problem1 = "%s bought a %s for $%d and paid $%d upfront. If he paid the remaining sum of money by equal monthly instalments over a period of %d years, how much was each monthly instalment?"%(self.person,self.item,self.total,self.upfront,self.period)
        self.problem2 = "%s bought a %s for which he paid $%d upfront. He paid the remaining sum of money by equal monthly instalments over a period of %d years. If the %s cost him $%d, how much was each monthly instalment?"%(self.person,self.item,self.upfront,self.period,self.item,self.total)
        self.problem = random.choice([self.problem1,self.problem2])

        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType96(self.problem,self.answer,self.person,self.item,self.instalment,self.period,self.upfront,self.total)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"$",'unit':"",'problem_type':"ProblemType96"}

    def ExplainType96(self,problem,answer,person,item,instalment,period,upfront,total):
        self.answer_text = "The correct answer is: <b>$"+str(answer)
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'>"
        self.table_text = self.table_text + "<tr><td></td><td align='center'>$"+str(upfront)+"<br><img src='/images/explanation/up_curly_braces_pt5cm.png'></td>"
        self.table_text = self.table_text + "<td align='center'>$"+str(total)+" - $"+str(upfront)+"<br><img src='/images/explanation/up_curly_braces_2cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td>"+item+"</td><td><img src='/images/explanation/pink_block_pt5cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/yellow_block_2cm.png'></td>"
        self.table_text = self.table_text + "</tr></table><br>"
        
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(total)+" - $"+str(upfront)+" = $"+str(total-upfront)+"</div>"
        self.solution_text = self.solution_text + "<div>Total amount to be paid by instalments was $"+str(total-upfront)+".</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(total-upfront)+" &divide; "+str(period)+" = $"+str((total-upfront)/period)+"</div>"
        self.solution_text = self.solution_text + "<div>"+person+" paid $"+str((total-upfront)/period)+" each year.</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str((total-upfront)/period)+" &divide; 12 = $"+str(((total-upfront)/period)/12)+"</div>"
        self.solution_text = self.solution_text + "<div>Each monthly instalment was $"+str(((total-upfront)/period)/12)+"</div>"
                
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    def GenerateProblemType97(self):
        '''e.g.: Annie bought a condominium. She paid $200000 upfront for it followed by $2400 in monthly instalments over a period of 30 years. How much did the condominium cost her?'''
        self.person = random.choice(PersonName.BoyName)
        self.ItemPool = {"1":["condominium",randint(1000,2000),random.choice([10,12,15,20,25,30])],"2":["house",randint(1000,2000),random.choice([10,12,15,20,25,30])],
                         "3":["farm",randint(100,500),random.choice([10,12,15,20,25,30])],"4":["factory",randint(1000,2000),random.choice([10,12,15,20,25,30])],
                         "5":["land",randint(100,500),random.choice([10,12,15,20,25,30])],"6":["apartment",randint(300,600),random.choice([10,12,15,20,25,30])]                         
                         }
        self.key = self.ItemPool.keys()[randint(0,len(self.ItemPool)-1)]
        self.item = self.ItemPool[self.key][0]
        self.instalment = self.ItemPool[self.key][1]
        self.period = self.ItemPool[self.key][2]
        self.upfront = int(randint(10,20)*self.instalment*self.period*12/100)
        self.total = self.upfront + self.period*self.instalment*12
        
        self.answer = self.total

        self.problem1 = "%s bought a %s. He paid $%d upfront for it followed by $%d in monthly instalments over a period of %d years. How much did the %s cost him?"%(self.person,self.item,self.upfront,self.instalment,self.period,self.item)
        self.problem2 = "%s bought a %s and paid $%d upfront for it. He paid the remaining sum of money by monthly instalments of $%d each over a period of %d years. How much did the %s cost him?"%(self.person,self.item,self.upfront,self.instalment,self.period,self.item)
        self.problem3 = "%s bought a %s for which he paid $%d upfront. If he paid the remaining sum of money by monthly instalments of $%d each over a period of %d years, find the cost of the %s."%(self.person,self.item,self.upfront,self.instalment,self.period,self.item)
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])

        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType97(self.problem,self.answer,self.person,self.item,self.instalment,self.period,self.upfront,self.total)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"$",'unit':"",'problem_type':"ProblemType97"}

    def ExplainType97(self,problem,answer,person,item,instalment,period,upfront,total):
        self.answer_text = "The correct answer is: <b>$"+str(answer)
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'>"
        self.table_text = self.table_text + "<tr><td></td><td align='center'>$"+str(upfront)+"<br><img src='/images/explanation/up_curly_braces_1cm.png'></td>"
        self.table_text = self.table_text + "<td align='center'>$"+str(period)+" x 12 x $"+str(instalment)+"<br><img src='/images/explanation/up_curly_braces_3cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td>"+item+"</td><td><img src='/images/explanation/pink_block_1cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/yellow_block_3cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td></td><td align='center' colspan=2><img src='/images/explanation/down_curly_braces_3cm.png' height=24 width=220><br>?</td>"
        self.table_text = self.table_text + "</tr></table><br>"

        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(period)+" x 12 months = "+str(period*12)+" months</div>"
        self.solution_text = self.solution_text + "<div>There are "+str(period*12)+" months in "+str(period)+" years.</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(period*12)+" x $"+str(instalment)+" = $"+str(period*instalment)+"</div>"
        self.solution_text = self.solution_text + "<div>Total amount to be paid by instalments is $"+str(period*12*instalment)+".</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(period*12*instalment)+" + "+str(upfront)+" = $"+str(total)+"</div>"
        self.solution_text = self.solution_text + "<div>The cost of the "+item+" is $"+str(total)+".</div>"
                
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    def GenerateProblemType98(self):
        '''e.g.: Annie bought a condominium for $1064000. She made a payment of $200000 upfront followed by monthly instalments of $2400 each. 
                How many years will it take Annie to pay off all the instalments?'''
        self.person = random.choice(PersonName.BoyName)
        self.ItemPool = {"1":["condominium",randint(1000,2000),random.choice([10,12,15,20,25,30])],"2":["house",randint(1000,2000),random.choice([10,12,15,20,25,30])],
                         "3":["farm",randint(100,500),random.choice([10,12,15,20,25,30])],"4":["factory",randint(1000,2000),random.choice([10,12,15,20,25,30])],
                         "5":["land",randint(100,500),random.choice([10,12,15,20,25,30])],"6":["apartment",randint(300,600),random.choice([10,12,15,20,25,30])]                         
                         }
        self.key = self.ItemPool.keys()[randint(0,len(self.ItemPool)-1)]
        self.item = self.ItemPool[self.key][0]
        self.instalment = self.ItemPool[self.key][1]
        self.period = self.ItemPool[self.key][2]
        self.upfront = int(randint(10,20)*self.instalment*self.period*12/100)
        self.total = self.upfront + self.period*self.instalment*12
        
        self.answer = self.period

        self.problem1 = "%s bought a %s for $%d. He made a payment of $%d upfront followed by monthly instalments of $%d each. How many years will it take %s to pay off all the instalments?"%(self.person,self.item,self.total,self.upfront,self.instalment,self.person)
        self.problem2 = "%s bought a %s and paid $%d upfront for it. He paid the remaining sum of money by monthly instalments of $%d each. If he bought the %s for $%d, how many years will it take him to pay off all the instalments?"%(self.person,self.item,self.upfront,self.instalment,self.item,self.total)
        self.problem3 = "%s bought a %s $%d and paid $%d upfront. If he paid the remaining sum of money by monthly instalments of $%d each, find the number of years it will take him to pay off all the instalments."%(self.person,self.item,self.total,self.upfront,self.instalment)
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])

        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType98(self.problem,self.answer,self.person,self.item,self.instalment,self.period,self.upfront,self.total)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"",'unit':"years",'problem_type':"ProblemType98"}

    def ExplainType98(self,problem,answer,person,item,instalment,period,upfront,total):
        self.answer_text = "The correct answer is: <b>"+str(answer)+" years"
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'>"
        self.table_text = self.table_text + "<tr><td></td><td align='center'>$"+str(upfront)+"<br><img src='/images/explanation/up_curly_braces_1cm.png'></td>"
        self.table_text = self.table_text + "<td align='center'>?<br><img src='/images/explanation/up_curly_braces_3cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td>"+item+"</td><td><img src='/images/explanation/pink_block_1cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/yellow_block_3cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td></td><td align='center' colspan=2><img src='/images/explanation/down_curly_braces_3cm.png' height=24 width=220><br>$"+str(total)+"</td>"
        self.table_text = self.table_text + "</tr></table><br>"
        
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(total)+" - $"+str(upfront)+" = $"+str(total-upfront)+"</div>"
        self.solution_text = self.solution_text + "<div>Total amount to be paid by instalments is $"+str(total-upfront)+".</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(total-upfront)+" &divide; $"+str(instalment)+" = "+str((total-upfront)/instalment)+"</div>"
        self.solution_text = self.solution_text + "<div>It will take "+str((total-upfront)/instalment)+" months to pay off all the instalments.</div><br>" 
        self.solution_text = self.solution_text + "<div>"+str((total-upfront)/instalment)+" &divide; 12 = "+str(((total-upfront)/instalment)/12)+"</div>"
        self.solution_text = self.solution_text + "<div>It will take "+str(period)+" years to pay off all the instalments.</div>"
        self.solution_text = self.solution_text + "<br><div> Watch below video for explanation of similar problem<br>"
        VideoLink = '<object><param name="movie" value="https://www.youtube.com/v/u1zgFlCw8Aw?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded"><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "FESW-uqQlN4";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
                
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    '''Problem Type 45 starts here'''
    def GenerateProblemType99(self):
        '''e.g.: A TV costs $13998 if paid by cash. If paid by instalments, it costs $325 monthly over 4 years. 
            If Annie paid by monthly instalments, how much more than the cash price did she pay?'''
        self.person = random.choice(PersonName.BoyName)
        self.period = randint(2,4)
        self.ItemPool = {"1":["plasma TV",randint(100,200)],"2":["mattress",randint(50,100)],"3":["sofa set",randint(50,100)],"4":["desktop",randint(50,100)],
                         "5":["refrigerator",randint(50,100)],"6":["computer",randint(50,100)],"7":["dining table",randint(50,100)],"8":["bed",randint(50,100)],
                         "9":["laptop",randint(50,100)],"10":["ring",randint(100,200)],"11":["photocopier",randint(50,100)],"12":["pool table",randint(50,100)],
                         "13":["diamond necklace",randint(100,200)],"14":["diamond ring",randint(100,200)],"15":["bracelet",randint(50,100)]                        
                         }
        self.key = self.ItemPool.keys()[randint(0,len(self.ItemPool)-1)]
        self.item = self.ItemPool[self.key][0]
        self.instalment = self.ItemPool[self.key][1]
        self.loan = self.instalment * self.period * 12
        self.cash = int(self.loan*randint(90,97)/100)
        self.diff = self.loan - self.cash
        
        self.answer = self.diff

        self.problem1 = "A %s costs $%d if paid by cash. If paid by instalments, it costs $%d monthly over %d years. If %s paid by monthly instalments, how much more than the cash price did he pay?"%(self.item,self.cash,self.instalment,self.period,self.person)
        self.problem2 = "%s purchased a %s and paid monthly instalments of $%d over %d years. If the cash price of the %s was $%d, how much more than the cash price did he pay?"%(self.person,self.item,self.instalment,self.period,self.item,self.cash)
        self.problem3 = "%s bought a %s priced at $%d if paid by cash. %s paid for it by instalments of $%d over %d years. How much more than the cash price did he pay?"%(self.person,self.item,self.cash,self.person,self.instalment,self.period)
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])

        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType99(self.problem,self.answer,self.person,self.item,self.instalment,self.period,self.cash,self.loan,self.diff)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"$",'unit':"",'problem_type':"ProblemType99"}

    def ExplainType99(self,problem,answer,person,item,instalment,period,cash,loan,diff):
        self.answer_text = "The correct answer is: <b>$"+str(answer)
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'>"
        self.table_text = self.table_text + "<tr><td></td><td align='center'>$"+str(cash)+"<br><img src='/images/explanation/up_curly_braces_2cm.png'></td>"
        self.table_text = self.table_text + "<td align='center'>?<br><img src='/images/explanation/up_curly_braces_1cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td>By cash</td><td><img src='/images/explanation/pink_block_2cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td>By instalments</td><td colspan=2><img src='/images/explanation/yellow_block_3cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td></td><td align='center' colspan=2><img src='/images/explanation/down_curly_braces_3cm.png'><br>$"+str(instalment)+" x "+str(period)+" x 12</td>"
        self.table_text = self.table_text + "</tr></table><br>"
        
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(period)+" x 12 months = "+str(period*12)+" months</div>"
        self.solution_text = self.solution_text + "<div>"+person+" paid instalments for "+str(period*12)+" months.</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(period*12)+" x $"+str(instalment)+" = $"+str(period*12*instalment)+"</div>"
        self.solution_text = self.solution_text + "<div>"+person+" paid $"+str(period*12*instalment)+" for the "+item+".</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(period*12*instalment)+" - $"+str(cash)+" = $"+str(period*12*instalment-cash)+"</div>"
        self.solution_text = self.solution_text + "<div>"+person+" paid $"+str(period*12*instalment-cash)+" more for than the cash price.</div>"
                
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    def GenerateProblemType100(self):
        '''e.g.: A TV costs $13998 if paid by cash. If paid by monthly instalments, it costs $1602 more. 
                If Annie paid by monthly instalments over a period of 4 years, how much instalment did she pay each month?'''
        self.person = random.choice(PersonName.BoyName)
        self.period = randint(2,4)
        self.ItemPool = {"1":["plasma TV",randint(100,200)],"2":["mattress",randint(50,100)],"3":["sofa set",randint(50,100)],"4":["desktop",randint(50,100)],
                         "5":["refrigerator",randint(50,100)],"6":["computer",randint(50,100)],"7":["dining table",randint(50,100)],"8":["bed",randint(50,100)],
                         "9":["laptop",randint(50,100)],"10":["ring",randint(100,200)],"11":["photocopier",randint(50,100)],"12":["pool table",randint(50,100)],
                         "13":["diamond necklace",randint(100,200)],"14":["diamond ring",randint(100,200)],"15":["bracelet",randint(50,100)]                        
                         }
        self.key = self.ItemPool.keys()[randint(0,len(self.ItemPool)-1)]
        self.item = self.ItemPool[self.key][0]
        self.instalment = self.ItemPool[self.key][1]
        self.loan = self.instalment * self.period * 12
        self.cash = int(self.loan*randint(90,97)/100)
        self.diff = self.loan - self.cash
        
        self.answer = self.instalment

        self.problem1 = "A %s costs $%d if paid by cash. If paid by monthly instalments, it costs $%d more. If %s paid by monthly instalments over a period of %d years, how much instalment did he pay each month?"%(self.item,self.cash,self.diff,self.person,self.period)
        self.problem = random.choice([self.problem1])

        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType100(self.problem,self.answer,self.person,self.item,self.instalment,self.period,self.cash,self.loan,self.diff)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"$",'unit':"",'problem_type':"ProblemType100"}

    def ExplainType100(self,problem,answer,person,item,instalment,period,cash,loan,diff):
        self.answer_text = "The correct answer is: <b>$"+str(answer)
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'>"
        self.table_text = self.table_text + "<tr><td></td><td align='center'>$"+str(cash)+"<br><img src='/images/explanation/up_curly_braces_2cm.png'></td>"
        self.table_text = self.table_text + "<td align='center'>$"+str(diff)+"<br><img src='/images/explanation/up_curly_braces_1cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td>By cash</td><td><img src='/images/explanation/pink_block_2cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td>By instalments</td><td colspan=2><img src='/images/explanation/yellow_block_3cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td></td><td align='center' colspan=2><img src='/images/explanation/down_curly_braces_3cm.png'><br>?</td>"
        self.table_text = self.table_text + "</tr></table><br>"
        
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(cash)+" + $"+str(diff)+" = $"+str(cash+diff)+"</div>"
        self.solution_text = self.solution_text + "<div>"+person+" paid $"+str(cash+diff)+" for the "+item+".</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(cash+diff)+" &divide; "+str(period)+" = $"+str((cash+diff)/period)+"</div>"
        self.solution_text = self.solution_text + "<div>"+person+" paid $"+str((cash+diff)/period)+" each year for the "+item+".</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str((cash+diff)/period)+" &divide 12 = $"+str(((cash+diff)/period)/12)+"</div>"
        self.solution_text = self.solution_text + "<div>"+person+" paid an instalment of $"+str(instalment)+" each month.</div>"
                
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    '''Problem Type 46 starts here '''
    def GenerateProblemType101(self):
        '''e.g.: Annie wants to tile her kitchen wall measuring 700 cm by 500 cm. 
            If each 100-cm2 tile costs $2, how much will it cost Annie to tile her kitchen wall?'''
        self.person = random.choice(PersonName.BoyName)
        self.ItemPool = ["bathroom wall","bathroom floor","shop floor","shop wall","showroom floor","showroom wall","living room wall",
                         "living room floor","bedroom floor","bedroom wall","kitchen floor","dining room wall","dining room floor",
                         "living room wall","living room floor","office floor","office wall","study room floor","study room wall"
                         ]
        self.item = random.choice(self.ItemPool)
        self.length = random.randrange(100,1000,10)
        self.breadth = random.randrange(100,1000,10)
        self.tile = random.choice([10,100])
        self.price = randint(2,5)
        
        self.answer = (self.length*self.breadth/self.tile)*self.price

        self.problem1 = "%s wants to tile his %s measuring %d cm by %d cm. If each %d-cm<sup>2</sup> tile costs $%d, how much will it cost %s to tile his %s?"%(self.person,self.item,self.length,self.breadth,self.tile,self.price,self.person,self.item)
        self.problem2 = "%s is tiling his %s using %d-cm<sup>2</sup> tiles. The %s measures %d cm by %d cm. If each tile costs $%d, how much will it cost to tile his %s?"%(self.person,self.item,self.tile,self.item,self.length,self.breadth,self.price,self.item)
        self.problem3 = "%s is using %d-cm<sup>2</sup> tiles costing $%d each to tile her %s. If the %s measures %d cm by %d cm, how much will it cost %s to tile his %s?"%(self.person,self.tile,self.price,self.item,self.item,self.length,self.breadth,self.person,self.item)
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])

        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType101(self.problem,self.answer,self.person,self.item,self.length,self.breadth,self.tile,self.price)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"$",'unit':"",'problem_type':"ProblemType101"}

    def ExplainType101(self,problem,answer,person,item,length,breadth,tile,price):
        self.answer_text = "The correct answer is: <b>$"+str(answer)
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'>"
        self.table_text = self.table_text + "<tr><td><img src='/images/explanation/P5_WN_PT101.png'></td><td>"+str(length)+"</td></tr>"
        self.table_text = self.table_text + "<tr><td align='center'>"+str(breadth)+"</td>"
        self.table_text = self.table_text + "</tr></table><br>"
        
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(length)+" cm x "+str(breadth)+" cm = "+str(length*breadth)+" cm<sup>2</sup></div>"
        self.solution_text = self.solution_text + "<div>The area of the "+item+" is "+str(length*breadth)+" cm<sup>2</sup>.</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(length*breadth)+" &divide; "+str(tile)+" = "+str(length*breadth/tile)+"</div>"
        self.solution_text = self.solution_text + "<div>Total number of tiles needed for the "+item+" is "+str(length*breadth/tile)+".</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(length*breadth/tile)+" x $"+str(price)+" = $"+str((length*breadth/tile)*price)+"</div>"
        self.solution_text = self.solution_text + "<div>It will cost $"+str((length*breadth/tile)*price)+" to tile the "+item+".</div>"
        self.solution_text = self.solution_text + "<br><div> Watch below video for explanation of similar problem<br>"
        VideoLink = '<object><param name="movie" value="https://www.youtube.com/v/u1zgFlCw8Aw?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded"><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "Y-7EspSDgjM";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
                
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    def GenerateProblemType102(self):
        '''e.g.: Annie tiled her kitchen wall using 100-cm2 tiles. The kitchen wall measured 700 cm by 500 cm. 
            If it cost her $7000 to tile her kitchen wall, how much did each tile cost her?'''
        self.person = random.choice(PersonName.BoyName)
        self.ItemPool = ["bathroom wall","bathroom floor","shop floor","shop wall","showroom floor","showroom wall","living room wall",
                         "living room floor","bedroom floor","bedroom wall","kitchen floor","dining room wall","dining room floor",
                         "living room wall","living room floor","office floor","office wall","study room floor","study room wall"
                         ]
        self.item = random.choice(self.ItemPool)
        self.length = random.randrange(100,1000,10)
        self.breadth = random.randrange(100,1000,10)
        self.tile = random.choice([10,100])
        self.price = randint(2,5)
        self.total = (self.length*self.breadth/self.tile)*self.price
        
        self.answer = self.price

        self.problem1 = "%s tiled his %s using %d-cm<sup>2</sup> tiles. The %s measured %d cm by %d cm. If it cost him $%d to tile his %s, how much did each tile cost him?"%(self.person,self.item,self.tile,self.item,self.length,self.breadth,self.total,self.item)
        self.problem2 = "%s tiled his %s measuring %d cm by %d cm. He used %d-cm<sup>2</sup> tiles. If he spent $%d on tiling his %s, how much did each tile cost him?"%(self.person,self.item,self.length,self.breadth,self.tile,self.total,self.item)
        self.problem3 = "%s spent $%d on tiling his %s using %d-cm<sup>2</sup> tiles. If the %s measured %d cm by %d cm, how much did each tile cost him?"%(self.person,self.total,self.item,self.tile,self.item,self.length,self.breadth)
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])

        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType102(self.problem,self.answer,self.person,self.item,self.length,self.breadth,self.tile,self.price,self.total)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"$",'unit':"",'problem_type':"ProblemType102"}

    def ExplainType102(self,problem,answer,person,item,length,breadth,tile,price,total):
        self.answer_text = "The correct answer is: <b>$"+str(answer)
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'>"
        self.table_text = self.table_text + "<tr><td><img src='/images/explanation/P5_WN_PT101.png'></td><td>"+str(length)+"</td></tr>"
        self.table_text = self.table_text + "<tr><td align='center'>"+str(breadth)+"</td>"
        self.table_text = self.table_text + "</tr></table><br>"
        
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(length)+" cm x "+str(breadth)+" cm = "+str(length*breadth)+" cm<sup>2</sup></div>"
        self.solution_text = self.solution_text + "<div>The area of the "+item+" is "+str(length*breadth)+" cm<sup>2</sup>.</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(length*breadth)+" &divide; "+str(tile)+" = "+str(length*breadth/tile)+"</div>"
        self.solution_text = self.solution_text + "<div>Total number of tiles needed for the "+item+" is "+str(length*breadth/tile)+".</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(total)+" &divide; "+str(length*breadth/tile)+" = $"+str(total/(length*breadth/tile))+"</div>"
        self.solution_text = self.solution_text + "<div>Each tile cost him $"+str(total/(length*breadth/tile))+".</div>"
                
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    def GenerateProblemType103(self):
        '''e.g.: A construction worker is building a wall measuring 500 cm by 750 cm using bricks measuring 75 cm2 each. 
                How many bricks will he need for the wall?'''
        self.ItemPool = {"1":["contractor","renovating","bathroom wall","tiles"],"2":["contractor","renovating","bathroom floor","tiles"],
                         "3":["worker","designing","showroom floor","tiles"],"4":["construction worker","building","showroom wall","bricks"],
                         "5":["contractor","designing","floor","tiles"],"6":["construction worker","building","living room wall","bricks"],
                         "7":["contractor","renovating","living room floor","bricks"],"8":["designer","tiling","living room floor","tiles"],
                         "9":["designer","tiling","bedroom floor","tiles"],"10":["designer","covering","bedroom wall","pieces of wallpaper"],
                         "11":["construction worker","tiling","kitchen floor","tiles"],"12":["construction worker","building","dining room wall","bricks"],
                         "13":["renovation contractor","tiling","dining room floor","tiles"],"14":["designer","covering","living room wall","pieces of wallpaper"],
                         "15":["worker","designing","living room floor","tiles"],"16":["contractor","parqueting","office floor","blocks"],
                         "17":["designer","covering","office wall","pieces of wallpaper"],"18":["contractor","parqueting","study room floor","blocks"],
                         "19":["designer","covering","study room wall","pieces of wallpaper"],"20":["construction worker","building","wall","bricks"]
                         }
        self.key = self.ItemPool.keys()[randint(0,len(self.ItemPool)-1)]
        self.person = self.ItemPool[self.key][0]
        self.action = self.ItemPool[self.key][1]
        self.wall = self.ItemPool[self.key][2]
        self.item = self.ItemPool[self.key][3]
        self.length = random.randrange(100,400,10)
        self.tile = random.randrange(100,400,5)
        self.breadth = random.randrange(self.tile*2,1000,self.tile)
        self.number = (self.breadth*self.length)/self.tile
        
        self.answer = self.number

        self.problem1 = "A %s is %s a %s measuring %d cm by %d cm using %s measuring %d cm<sup>2</sup> each. How many %s will he need for the %s?"%(self.person,self.action,self.wall,self.length,self.breadth,self.item,self.tile,self.item,self.wall)
        self.problem2 = "A %s is %s a %s using %d cm<sup>2</sup> %s. How many %s will he need for a %s measuring %d cm by %d cm?"%(self.person,self.action,self.wall,self.tile,self.item,self.item,self.wall,self.length,self.breadth)
        self.problem3 = "A %s is %s a %s using %d cm<sup>2</sup> %s. Find the number of %s he will need for a %s measuring %d cm by %d cm."%(self.person,self.action,self.wall,self.tile,self.item,self.item,self.wall,self.length,self.breadth)
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])

        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType103(self.problem,self.answer,self.person,self.item,self.length,self.breadth,self.tile,self.wall,self.number)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"",'unit':self.item,'problem_type':"ProblemType103"}

    def ExplainType103(self,problem,answer,person,item,length,breadth,tile,wall,number):
        self.answer_text = "The correct answer is: <b>"+str(answer)+" "+item
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'>"
        self.table_text = self.table_text + "<tr><td><img src='/images/explanation/P5_WN_PT101.png'></td><td>"+str(length)+"</td></tr>"
        self.table_text = self.table_text + "<tr><td align='center'>"+str(breadth)+"</td>"
        self.table_text = self.table_text + "</tr></table><br>"
        
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(length)+" cm x "+str(breadth)+" cm = "+str(length*breadth)+" cm<sup>2</sup></div>"
        self.solution_text = self.solution_text + "<div>The area of the "+wall+" is "+str(length*breadth)+" cm<sup>2</sup>.</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(length*breadth)+" cm<sup>2</sup> &divide; "+str(tile)+" cm<sup>2</sup> = "+str(length*breadth/tile)+"</div>"
        self.solution_text = self.solution_text + "<div>Total number of "+item+" needed for the "+wall+" is "+str(length*breadth/tile)+".</div><br>"
                
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    '''Problem Type 47 starts here'''
    def GenerateProblemType104(self):
        '''e.g.: A worker is laying out a combination of black and white marble tiles on a rectangular floor. 
        	The black marble tiles measure 25 cm2 each and the white marble tiles measure 100 cm2 each. 
        	If he uses 50 black marble tiles and 40 white marble tiles to cover the floor, what is the area of the floor covered?'''

        self.ItemPool = {"1":["contractor","blue","white","tiles","bathroom wall"],"2":["contractor","blue","white","tiles","bathroom floor"],"3":["worker","brown","red","wooden blocks","showroom floor"],
			"4":["construction worker","brown","red","wooden blocks","showroom wall"],"5":["contractor","glass","marble","tiles","floor"],"6":["construction worker","red","black","bricks","living room wall"],
			"7":["contractor","green","white","marble tiles","living room floor"],"8":["designer","brown","white","bricks","living room floor"],"9":["designer","light brown","dark brown","parquet blocks","bedroom floor"],
			"10":["designer","black","white","blocks","bedroom wall"],"11":["construction worker","painted","plain","tiles","kitchen floor"],"12":["construction worker","small","big","bricks","dining room wall"],
			"13":["renovation contractor","decorated","plain","tiles","dining room floor"],"14":["designer","purple","white","tiles","living room wall"],"15":["worker","glass","wooden","tiles","shop floor"],
			"16":["worker","mosaic","plain","glass tiles","shop wall"],"17":["contractor","yellow","black","wooden blocks","office wall"],"18":["designer","pink","blue","carpet patches","office floor"],
			"19":["contractor","black","red","parquet blocks","study room floor"],"20":["designer","orange","purple","blocks","study room wall"],"21":["worker","black","white","marble tiles","floor"]
                         }
        self.key = self.ItemPool.keys()[randint(0,len(self.ItemPool)-1)]
        self.person = self.ItemPool[self.key][0]
        self.colour1 = self.ItemPool[self.key][1]
        self.colour2 = self.ItemPool[self.key][2]
        self.item = self.ItemPool[self.key][3]
        self.place = self.ItemPool[self.key][4]
        self.area1 = random.randrange(10,100,5)
        self.area2 = random.randrange(10,100,5)
        self.number1 = random.randrange(10,100,5)
        self.number2 = random.randrange(10,100,5)
        self.total = (self.number1*self.area1+self.number2*self.area2)
        
        self.answer = self.total

        self.problem1 = "A %s is laying out a combination of %s and %s %s on a rectangular %s. The %s %s measure %d cm<sup>2</sup> each and the %s %s measure %d cm<sup>2</sup> each. If he uses %d %s %s and %d %s %s to cover the %s, what is the area of the %s covered?"%(self.person,self.colour1,self.colour2,self.item,self.place,self.colour1,self.item,self.area1,self.colour2,self.item,self.area2,self.number1,self.colour1,self.item,self.number2,self.colour2,self.item,self.place,self.place)
        self.problem2 = "A %s is laying out a combination of %d %s %s and %d %s %s on a rectangular %s. If the %s %s measure %d cm<sup>2</sup> each and the %s %s measure %d cm<sup>2</sup> each, what is the area of the %s covered?"%(self.person,self.number1,self.colour1,self.item,self.number2,self.colour2,self.item,self.place,self.colour1,self.item,self.area1,self.colour2,self.item,self.area2,self.place)
        self.problem = random.choice([self.problem1,self.problem2])  

        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType104(self.problem,self.answer,self.person,self.colour1,self.colour2,self.item,self.area1,self.area2,self.number1,self.number2,self.place,self.total)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"",'unit':"cm<sup>2</sup>",'problem_type':"ProblemType104"}

    def ExplainType104(self,problem,answer,person,colour1,colour2,item,area1,area2,number1,number2,place,total):
        self.answer_text = "The correct answer is: <b>"+str(answer)+" cm<sup>2</sup>"
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'>"
        self.table_text = self.table_text + "<tr><td></td><td align='center'>"+str(area1)+" cm<sup>2</sup> x "+str(number1)+"<br><img src='/images/explanation/up_curly_braces_2cm.png'></td>"
        self.table_text = self.table_text + "<td align='center'>"+str(area2)+" cm<sup>2</sup> x "+str(number2)+"<br><img src='/images/explanation/up_curly_braces_2cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td>"+item+"</td><td><img src='/images/explanation/pink_block_2cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/green_block_2cm.png'></td></td>"
        self.table_text = self.table_text + "<tr><td></td><td align='center' colspan=2><img src='/images/explanation/down_curly_braces_3cm.png'><br>?</td>"
        self.table_text = self.table_text + "</tr></table><br>"
        
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(area1)+" cm<sup>2</sup> x "+str(number1)+" = "+str(area1*number1)+" cm<sup>2</sup></div>"
        self.solution_text = self.solution_text + "<div>Area covered by "+colour1+" "+item+" is "+str(area1*number1)+" cm<sup>2</sup>.</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(area2)+" cm<sup>2</sup> x "+str(number2)+" = "+str(area2*number2)+" cm<sup>2</sup></div>"
        self.solution_text = self.solution_text + "<div>Area covered by "+colour2+" "+item+" is "+str(area2*number2)+" cm<sup>2</sup>.</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(area1*number1)+" cm<sup>2</sup> + "+str(area2*number2)+" cm<sup>2</sup> = "+str(area1*number1+area2*number2)+" cm<sup>2</sup></div>"
        self.solution_text = self.solution_text + "<div>Area of the "+place+" covered is "+str(area1*number1+area2*number2)+" cm<sup>2</sup>.</div>"
                
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    '''Problem Type 48 starts here'''
    def GenerateProblemType105(self):
        '''e.g.: The table below shows the charges for outgoing calls that a telephone service provider charges.
        	How much does an outgoing call lasting 2 minutes 25 seconds cost (in cents)?'''
       
        self.charge1 = random.randrange(20,80,10)
        self.charge2 = self.charge1/10
        self.minute = randint(2,9)
        self.second = randint(2,59)
        self.ExtraSeconds = (self.minute*60+self.second)-60
        if (self.ExtraSeconds%10==0):
            self.cycle = self.ExtraSeconds/10
        else:
            self.cycle = int(self.ExtraSeconds/10)+1
        self.total = (self.cycle*self.charge2+self.charge1)
        
        self.answer = self.total

        self.problem1 = "<div>The table below shows the charges for outgoing calls that a telephone service provider charges.</div><br>"
        self.problem1 = self.problem1 + "<div><table cellpadding=10 border=1><tr><th>Duration of outgoing call</th><th>Charge</th></tr>"
        self.problem1 = self.problem1 + "<tr><td>First 60 seconds or less</td><td>"+str(self.charge1)+" &cent;</td></tr>"
        self.problem1 = self.problem1 + "<tr><td>Every additional 10 seconds<br>or less</td><td>"+str(self.charge2)+" &cent;</td></tr></table></div><br>"
        self.problem1 = self.problem1 + "<div>How much does an outgoing call lasting "+str(self.minute)+" minutes "+str(self.second)+" seconds cost in (&cent;)</div>"
        self.problem = self.problem1      

        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType105(self.problem,self.answer,self.charge1,self.charge2,self.minute,self.second,self.cycle,self.total)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"",'unit':"&cent;",'problem_type':"ProblemType105"}

    def ExplainType105(self,problem,answer,charge1,charge2,minute,second,cycle,total):
        self.answer_text = "The correct answer is: <b>"+str(answer)+" &cent;"
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'>"
        self.table_text = self.table_text + "<tr><td></td><td align='center'>60 s<br><img src='/images/explanation/up_curly_braces_2cm.png'></td>"
        self.table_text = self.table_text + "<td align='center'>10 s<br><img src='/images/explanation/up_curly_braces_pt5cm.png'></td>"
        self.table_text = self.table_text + "<td></td><td></td><td></td><td align='center'>10 s or<br>less<br><img src='/images/explanation/up_curly_braces_pt5cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td>Duration</td><td><img src='/images/explanation/pink_block_2cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/green_block_pt5cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/green_block_pt5cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/broken_green_block_pt5cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/green_block_pt5cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/yellow_block_pt5cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td></td><td align='center' colspan=6><img src='/images/explanation/down_curly_braces_3cm.png' width=280 height=24><br>"+str(minute)+"min "+str(second)+"s</td>"
        self.table_text = self.table_text + "</tr></table><br>"
        
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(minute)+" minutes "+str(second)+" seconds = ("+str(minute)+" x 60 seconds) + "+str(second)+" seconds = "+str(minute*60+second)+" seconds</div><br>"
        self.solution_text = self.solution_text + "<div>Charge of first 60 seconds of outgoing call = "+str(charge1)+" &cent;</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(minute*60+second)+" seconds - 60 seconds = "+str(minute*60+second-60)+" seconds</div><br>"
        self.solution_text = self.solution_text + "<div>The next "+str(minute*60+second-60)+" seonds of outgoing call will be charged "+str(cycle)+" times in increments of 10 seconds or less.</div><br>"
        self.solution_text = self.solution_text + "<div>Charge of the next "+str(minute*60+second-60)+" seconds of outgoing call = "+str(cycle)+" x "+str(charge2)+" &cent; = "+str(cycle*charge2)+" &cent;</div><br>"
        self.solution_text = self.solution_text + "<div>Total charge for "+str(minute)+" minutes "+str(second)+" seconds of outgoing call = "+str(charge1)+" &cent; + "+str(cycle*charge2)+" &cent; = "+str(charge1+(cycle*charge2))+" &cent;</div>"
        self.solution_text = self.solution_text + "<div>An outgoing call lasting "+str(minute)+" minutes "+str(second)+" seconds costs "+str(charge1+(cycle*charge2))+" &cent;</div>"
                        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    def GenerateProblemType106(self):
        '''e.g.: The table below shows the charges for outgoing calls that a telephone service provider charges.
        	What is the total cost (in cents) for two calls with durations of 3 minutes and 5 minutes?'''
       
        self.charge1 = random.randrange(20,80,10)
        self.charge2 = self.charge1/10
        self.minutes = random.sample([2,3,4,5,6,7,8,9],2)
        self.minute1 = self.minutes[0]
        self.minute2 = self.minutes[1]
        self.cycle1 = (self.minute1*60-60)/10
        self.cycle2 = (self.minute2*60-60)/10
        self.total1 = (self.cycle1*self.charge2+self.charge1)
        self.total2 = (self.cycle2*self.charge2+self.charge1)
        self.total = self.total1+self.total2
        
        self.answer = self.total

        self.problem1 = "<div>The table below shows the charges for outgoing calls that a telephone service provider charges.</div><br>"
        self.problem1 = self.problem1 + "<div><table border=1 cellpadding=10><tr><th>Duration of outgoing call</th><th>Charge</th></tr>"
        self.problem1 = self.problem1 + "<tr><td>First 60 seconds or less</td><td>"+str(self.charge1)+" &cent;</td></tr>"
        self.problem1 = self.problem1 + "<tr><td>Every additional 10 seconds<br>or less</td><td>"+str(self.charge2)+" &cent;</td></tr></table></div><br>"
        self.problem1 = self.problem1 + "<div>What is total cost (in &cent;) for two calls with durations of "+str(self.minute1)+" minutes "+str(self.minute2)+" minutes?</div>"
        self.problem = self.problem1      

        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType106(self.problem,self.answer,self.charge1,self.charge2,self.minute1,self.minute2,self.cycle1,self.cycle2,self.total)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"",'unit':"&cent;",'problem_type':"ProblemType106"}

    def ExplainType106(self,problem,answer,charge1,charge2,minute1,minute2,cycle1,cycle2,total):
        self.answer_text = "The correct answer is: <b>"+str(answer)+" &cent;"
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'>"
        self.table_text = self.table_text + "<tr><td></td><td align='center'>60 s<br><img src='/images/explanation/up_curly_braces_2cm.png'></td>"
        self.table_text = self.table_text + "<td align='center'>10 s<br><img src='/images/explanation/up_curly_braces_pt5cm.png'></td>"
        self.table_text = self.table_text + "<td></td><td></td><td></td><td align='center'>10 s or<br>less<br><img src='/images/explanation/up_curly_braces_pt5cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td>Duration</td><td><img src='/images/explanation/pink_block_2cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/green_block_pt5cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/green_block_pt5cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/broken_green_block_pt5cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/green_block_pt5cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/yellow_block_pt5cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td></td><td align='center' colspan=6><img src='/images/explanation/down_curly_braces_3cm.png' height=24 width=280><br>"+str(minute1)+" min / "+str(minute2)+" min</td>"
        self.table_text = self.table_text + "</tr></table><br>"
        
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div><b>Cost for first outgoing call with duration of "+str(minute1)+" minutes</b></div><br>"
        self.solution_text = self.solution_text + "<div>"+str(minute1)+" minutes = "+str(minute1)+" x 60 seconds = "+str(minute1*60)+" seconds</div>"
        self.solution_text = self.solution_text + "<div>The first outgoing call lasted for a duration of "+str(minute1*60)+" seconds.</div><br>"
        self.solution_text = self.solution_text + "<div>Charge of first 60 seconds of outgoing call = "+str(charge1)+" &cent;</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(minute1*60)+" seconds - 60 seconds = "+str(minute1*60-60)+" seconds</div>"
        self.solution_text = self.solution_text + "<div>The next "+str(minute1*60-60)+" seconds of outgoing call will be charged "+str(cycle1)+" times in increments of 10 seconds or less.</div><br>"
        self.solution_text = self.solution_text + "<div>Charge of the next "+str(minute1*60-60)+" seconds of outgoing call = "+str(cycle1)+" x "+str(charge2)+" &cent; = "+str(cycle1*charge2)+" &cent;</div>"
        self.solution_text = self.solution_text + "<div>Total charge for first outgoing call of "+str(minute1)+" minutes = "+str(charge1)+" &cent; + "+str(cycle1*charge2)+" &cent; = "+str(charge1+(cycle1*charge2))+" &cent;</div><br>"
        
        self.solution_text = self.solution_text + "<div><b>Cost for second outgoing call with duration of "+str(minute2)+" minutes</b></div>"
        self.solution_text = self.solution_text + "<div>"+str(minute2)+" minutes = "+str(minute2)+" x 60 seconds = "+str(minute2*60)+" seconds</div>"
        self.solution_text = self.solution_text + "<div>The second outgoing call lasted for a duration of "+str(minute2*60)+" seconds.</div><br>"
        self.solution_text = self.solution_text + "<div>Charge of first 60 seconds of outgoing call = "+str(charge1)+" &cent;</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(minute2*60)+" seconds - 60 seconds = "+str(minute2*60-60)+" seconds</div>"
        self.solution_text = self.solution_text + "<div>The next "+str(minute2*60-60)+" seonds of outgoing call will be charged "+str(cycle2)+" times in increments of 10 seconds or less.</div><br>"
        self.solution_text = self.solution_text + "<div>Charge of the next "+str(minute2*60-60)+" seconds of outgoing call = "+str(cycle2)+" x "+str(charge2)+" &cent; = "+str(cycle2*charge2)+" &cent;</div>"
        self.solution_text = self.solution_text + "<div>Total charge for first outgoing call of "+str(minute2)+" minutes = "+str(charge1)+" &cent; + "+str(cycle2*charge2)+" &cent; = "+str(charge1+(cycle2*charge2))+" &cent;</div><br>"
        
        self.solution_text = self.solution_text + "<div>Total charge for first and second outgoing calls = "+str(charge1+(cycle1*charge2))+" &cent; + "+str(charge1+(cycle2*charge2))+" &cent; = "+str(charge1+(cycle1*charge2)+(charge1+(cycle2*charge2)))+" &cent;</div>"
        self.solution_text = self.solution_text + "<div>Total cost for two outgoing calls with duration of "+str(minute1)+" minutes "+str(minute2)+" minutes is "+str(charge1+(cycle1*charge2)+(charge1+(cycle2*charge2)))+" &cent;.</div>"
                        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    '''Problem type 49 starts here'''
    def GenerateProblemType107(self):
        '''e.g.: The table below shows the rates that a taxi charges.
        	How much does Annie pay (in $) for a 5 km ride?'''
        
        self.person = random.choice(PersonName.PersonName)
        self.charge1 = randint(2,5)
        self.charge2 = random.choice([25,50])
        self.distance = randint(3,30)
        self.cycle = (self.distance-2)*1000/250
        self.total = (self.cycle*self.charge2/100)+self.charge1
        
        self.answer = self.total

        self.problem1 = "<div>The table below shows the rates that a taxi charges.</div><br>"
        self.problem1 = self.problem1 + "<div><table border=1 cellpadding=10><tr><th>Distance traveled</th><th>Rate</th></tr>"
        self.problem1 = self.problem1 + "<tr><td>First 2 km or less</td><td>$"+str(self.charge1)+"</td></tr>"
        self.problem1 = self.problem1 + "<tr><td>Every additional 250 m<br>or less</td><td>"+str(self.charge2)+" &cent;</td></tr></table></div><br>"
        self.problem1 = self.problem1 + "<div>How much does "+self.person+" pay (in $) for a "+str(self.distance)+" km ride?</div>"
        self.problem = self.problem1      

        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType107(self.problem,self.answer,self.person,self.charge1,self.charge2,self.distance,self.total,self.cycle)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"$",'unit':"",'problem_type':"ProblemType107"}

    def ExplainType107(self,problem,answer,person,charge1,charge2,distance,total,cycle):
        self.answer_text = "The correct answer is: <b>$"+str(answer)
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'>"
        self.table_text = self.table_text + "<tr><td></td><td align='center'>2 km<br><img src='/images/explanation/up_curly_braces_2cm.png'></td>"
        self.table_text = self.table_text + "<td align='center'>250 m<br><img src='/images/explanation/up_curly_braces_pt7cm.png'></td>"
        self.table_text = self.table_text + "<td></td><td></td><td></td><td align='center'>250 m or<br>less<br><img src='/images/explanation/up_curly_braces_pt7cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td>Distance</td><td><img src='/images/explanation/pink_block_2cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/green_block_pt7cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/green_block_pt7cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/broken_green_block_pt7cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/green_block_pt7cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/yellow_block_pt7cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td></td><td align='center' colspan=6><img src='/images/explanation/down_curly_braces_3cm.png' width=330 height=24><br>"+str(distance)+" km</td>"
        self.table_text = self.table_text + "</tr></table><br>"
        
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>Charge for first 2 km distace = $"+str(charge1)+"</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(distance)+" km - 2 km = "+str(distance-2)+" km = "+str((distance-2)*1000)+" m</div>"
        self.solution_text = self.solution_text + "<div>"+str((distance-2)*1000)+" m &divide; 250 m = "+str(((distance-2)*1000)/250)+"</div><br>"
        self.solution_text = self.solution_text + "<div>The next "+str(distance-2)+" km or "+str((distance-2)*1000)+" m distance will be charged "+str(cycle)+" times in increments of 250m or less.</div><br>"
        self.solution_text = self.solution_text + "<div>Charge for the next "+str(distance-2)+" km or "+str((distance-2)*1000)+" m = "+str(cycle)+" x "+str(charge2)+" &cent; = "+str(cycle*charge2)+" &cent; = $"+str(cycle*charge2/100)+"</div><br>"
        self.solution_text = self.solution_text + "<div>Total charge for "+str(distance)+" km distance = $"+str(charge1)+" + $"+str(cycle*charge2/100)+" = $"+str(charge1+cycle*charge2/100)+"</div><br>"
        self.solution_text = self.solution_text + "<div>"+person+" pays $"+str(charge1+cycle*charge2/100)+" for a "+str(distance)+" km ride.</div>"
        self.solution_text = self.solution_text + "<br><div> Watch below video for explanation of similar problem<br>"
        VideoLink = '<object><param name="movie" value="https://www.youtube.com/v/u1zgFlCw8Aw?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded"><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "AF2pO0co5qw";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
                     
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    def GenerateProblemType108(self):
        '''e.g.: The table below shows the rates that a taxi charges.
        	If Annie pays $10, what is the longest distance she can travel?'''

        self.person = random.choice(PersonName.GirlName)
        self.charge1 = randint(2,5)
        self.charge2 = random.choice([25,50])
        self.distance = randint(3,30)
        self.cycle = (self.distance-2)*1000/250
        self.total = (self.cycle*self.charge2)/100+self.charge1
        
        self.answer = self.distance

        self.problem1 = "<div>The table below shows the rates that a taxi charges.</div><br>"
        self.problem1 = self.problem1 + "<div><table border=1 cellpadding=10><tr><th>Distance traveled</th><th>Rate</th></tr>"
        self.problem1 = self.problem1 + "<tr><td>First 2 km or less</td><td>$"+str(self.charge1)+"</td></tr>"
        self.problem1 = self.problem1 + "<tr><td>Every additional 250 m<br>or less</td><td>"+str(self.charge2)+" &cent;</td></tr></table></div><br>"
        self.problem1 = self.problem1 + "<div>If "+self.person+" pays $"+str(self.total)+", what is the longest distance she can travel?</div>"
        self.problem = self.problem1      

        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType108(self.problem,self.answer,self.person,self.charge1,self.charge2,self.distance,self.total)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"",'unit':"km",'problem_type':"ProblemType108"}

    def ExplainType108(self,problem,answer,person,charge1,charge2,distance,total):
        self.answer_text = "The correct answer is: <b>"+str(answer)+" km"
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'>"
        self.table_text = self.table_text + "<tr><td></td><td align='center'>2 km<br><img src='/images/explanation/up_curly_braces_2cm.png'></td>"
        self.table_text = self.table_text + "<td align='center'>250 m<br><img src='/images/explanation/up_curly_braces_pt7cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td>Distance</td><td><img src='/images/explanation/pink_block_2cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/green_block_pt7cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/green_block_pt7cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/broken_green_block_pt7cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/green_block_pt7cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/green_block_pt7cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td></td><td align='center' colspan=6><img src='/images/explanation/down_curly_braces_3cm.png' width=330 height=24><br>?</td>"
        self.table_text = self.table_text + "</tr></table><br>"
        
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>Charge for first 2 km distace = $"+str(charge1)+"</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(total)+" - $"+str(charge1)+" = $"+str(total-charge1)+" = "+str((total-charge1)*100)+" &cent;</div>"
        self.solution_text = self.solution_text + "<div>After traveling the first 2 km, "+person+" has "+str((total-charge1)*100)+" &cent; worth of ride left.</div><br>"
        self.solution_text = self.solution_text + "<div>"+str((total-charge1)*100)+" &cent; &divide; "+str(charge2)+" &cent; = "+str(((total-charge1)*100)/charge2)+"</div>"
        self.solution_text = self.solution_text + "<div>"+person+" can travel a maximum of "+str(((total-charge1)*100)/charge2)+" increments of 250m with "+str((total-charge1)*100)+" &cent;.</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(((total-charge1)*100)/charge2)+" x 250 m = "+str((((total-charge1)*100)/charge2)*250)+" m = "+str((((total-charge1)*100)/charge2)*250/1000)+" km</div>"
        self.solution_text = self.solution_text + "<div>After traveling the first 2 km, "+person+" can travel a maximum of another "+str((((total-charge1)*100)/charge2)*250/1000)+" km.</div><br>"
        self.solution_text = self.solution_text + "<div>2 km + "+str((((total-charge1)*100)/charge2)*250/1000)+" km = "+str(((((total-charge1)*100)/charge2)*250/1000)+2)+" km</div><br>"
        self.solution_text = self.solution_text + "<div>The longest distance that "+person+" can travel with $"+str(total)+" is "+str(((((total-charge1)*100)/charge2)*250/1000)+2)+" km.</div>"
                        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    '''Problem Type 50 starts here'''
    def GenerateProblemType109(self):
        '''e.g.: The table below shows the rates that a car parking garage charges.
        	How much did Annie pay if she parked her car from 3:40 pm to 8:00 pm?'''
        
        self.person = random.choice(PersonName.GirlName)
        self.charge1 = randint(1,3)
        self.charge2 = randint(4,10)
        self.StartHour = randint(1,3)
        self.StartMinute = random.randrange(10,50,10)
        self.EndHour = randint(7,10)
        self.HourDiff = 6 - self.StartHour - 1
        self.MinuteDiff = 60 - self.StartMinute
        self.total = (self.HourDiff+1) * self.charge1 + self.charge2        
        
        self.answer = self.total

        self.problem1 = "<div>The table below shows the rates that a car parking garage charges.</div><br>"
        self.problem1 = self.problem1 + "<div><table border=1 cellpadding=10><tr><th>Time</th><th>Rate</th></tr>"
        self.problem1 = self.problem1 + "<tr><td>8 am to 6 pm</td><td>$"+str(self.charge1)+" per hour or part thereof</td></tr>"
        self.problem1 = self.problem1 + "<tr><td>6 pm to 8 am</td><td>$"+str(self.charge2)+" per entry</td></tr></table></div><br>"
        self.problem1 = self.problem1 + "<div>How much did "+self.person+" pay if she parked her car from "+str(self.StartHour)+":"+str(self.StartMinute)+" pm to "+str(self.EndHour)+":00 pm?</div>"
        self.problem = self.problem1      

        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType109(self.problem,self.answer,self.person,self.charge1,self.charge2,self.StartHour,self.EndHour,self.StartMinute,self.HourDiff,self.MinuteDiff)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"$",'unit':"",'problem_type':"ProblemType109"}

    def ExplainType109(self,problem,answer,person,charge1,charge2,StartHour,EndHour,StartMinute,HourDiff,MinuteDiff):
        self.answer_text = "The correct answer is: <b>$"+str(answer)
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'>"
        self.table_text = self.table_text + "<tr><td></td><td align='center'>1 hour<br>or less<br><img src='/images/explanation/up_curly_braces_pt7cm.png'></td>"
        self.table_text = self.table_text + "<td></td><td></td><td align='center'>1 hour<br><img src='/images/explanation/up_curly_braces_pt7cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td>Time</td><td><img src='/images/explanation/yellow_block_pt7cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/green_block_pt7cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/broken_green_block_pt7cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/green_block_pt7cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/pink_block_2cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td></td><td align='center' colspan=4><img src='/images/explanation/down_curly_braces_3cm.png'><br>"+str(StartHour)+":"+str(StartMinute)+" pm - 6 pm</td>"
        self.table_text = self.table_text + "<td align='center'><img src='/images/explanation/down_curly_braces_2cm.png'><br>6pm - 8 am</td>"
        self.table_text = self.table_text + "</tr></table><br>"
        
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>Duration of time between "+str(StartHour)+":"+str(StartMinute)+" pm and 6 pm = "+str(HourDiff)+" hours and "+str(MinuteDiff)+" minutes</div><br>"
        self.solution_text = self.solution_text + "<div>Since the charges are by the hour from 8am to 6pm, "+person+" pays a parking charge for "+str(HourDiff+1)+" hours from "+str(StartHour)+":"+str(StartMinute)+" pm and 6 pm.</div><br>"
        self.solution_text = self.solution_text + "<div>Charges for parking from "+str(StartHour)+":"+str(StartMinute)+" pm and 6 pm = "+str(HourDiff+1)+" x $"+str(charge1)+" = $"+str((HourDiff+1)*charge1)+"</div><br>"
        self.solution_text = self.solution_text + "<div>Charges for parking from 6 pm to 8 pm = $"+str(charge2)+"</div><br>"
        self.solution_text = self.solution_text + "<div>Total charge for parking from "+str(self.StartHour)+":"+str(self.StartMinute)+" pm to "+str(self.EndHour)+":00 pm = $"+str((HourDiff+1)*charge1)+" + $"+str(charge2)+" = $"+str((HourDiff+1)*charge1+charge2)+"</div><br>"
        self.solution_text = self.solution_text + "<div>"+person+" paid $"+str((HourDiff+1)*charge1+charge2)+" for parking her car from "+str(self.StartHour)+":"+str(self.StartMinute)+" pm to "+str(self.EndHour)+":00 pm.</div>"
                        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    '''Problem Type 51 starts here'''
    def GenerateProblemType110(self):
        '''e.g.: A printer prints 14 newsletters in 10 seconds. How many newsletters does it print in 2 minutes?'''
        
        self.person = random.choice(PersonName.PersonName)
        self.ItemPool = ["sheets","pamphlets","letters","images","photos","exam sets","stickers","coupons"]       
        self.item = random.choice(self.ItemPool)
        self.letter = randint(4,20)
        self.time1 = random.choice([4,5,6,10,12,15,20,30])
        self.time2 = randint(2,30)
        self.cycle = 60/self.time1
        self.OneMinute = self.cycle*self.letter
        self.total = self.OneMinute*self.time2
        
        self.answer = self.total
        
        self.problem1 = "A printer prints %d %s in %d seconds. How many %s does it print in %d minutes?"%(self.letter,self.item,self.time1,self.item,self.time2)
        self.problem2 = "%s's printer prints %d %s in %d seconds. How many %s does it print in %d minutes?"%(self.person,self.letter,self.item,self.time1,self.item,self.time2)
        self.problem = random.choice([self.problem1,self.problem2])    

        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType110(self.problem,self.answer,self.person,self.item,self.letter,self.time1,self.time2,self.cycle)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"",'unit':self.item,'problem_type':"ProblemType110"}

    def ExplainType110(self,problem,answer,person,item,letter,time1,time2,cycle):
        self.answer_text = "The correct answer is: <b>"+str(answer)+" "+item
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'>"
        self.table_text = self.table_text + "<tr><td align='center'>"+str(time1)+" s</td>"
        self.table_text = self.table_text + "<td align='center'>x "+str(cycle)+"<br><img src ='/images/explanation/right_arrow.png'></td>"
        self.table_text = self.table_text + "<td align='center'>1 min (60s)</td><td>"+str(time2)+"min ("+str(time2*60)+" s)</td></tr>"
        self.table_text = self.table_text + "<tr><td colspan=4><img src='/images/explanation/P5_WN_PT110.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td align='center'>"+str(letter)+"<br>"+item+"</td>"
        self.table_text = self.table_text + "<td align='center'><img src ='/images/explanation/right_arrow.png'><br>x "+str(cycle)+"</td>"
        self.table_text = self.table_text + "<td align='center'>?</td><td align='center'>?</td>"
        self.table_text = self.table_text + "</tr></table><br>"
        
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>The printer takes "+str(time1)+"s to print "+str(letter)+" "+item+".</div>"
        self.solution_text = self.solution_text + "<div>"+str(time1)+"s &rarr; "+str(letter)+" "+item+"</div><br>"
        self.solution_text = self.solution_text + "<div>Multiplying both sides by "+str(cycle)+", we get "+str(time1)+"s x "+str(cycle)+" &rarr; "+str(letter)+" "+item+" x "+str(cycle)+"</div>"
        self.solution_text = self.solution_text + "<div>1 minute or 60s &rarr; "+str(letter*cycle)+" "+item+"</div>"
        self.solution_text = self.solution_text + "<div>The printer prints at the rate of "+str(letter*cycle)+" "+item+" per minute.</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(time2)+" minutes &rarr; "+str(time2)+" x "+str(letter*cycle)+" = "+str(time2*letter*cycle)+" "+item+"</div><br>"
        self.solution_text = self.solution_text + "<div>The printer prints "+str(time2*letter*cycle)+" "+item+" in "+str(time2)+" minutes.</div>"
                        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    def GenerateProblemType111(self):
        '''e.g.: A printer prints 14 newsletters in 10 seconds. At this rate, how many minutes does it take to print 840 newsletters?'''
        
        self.person = random.choice(PersonName.PersonName)
        self.ItemPool = ["sheets","newsletters","letters","images","photos","examaniation sets","stickers","coupon sheets"]       
        self.item = random.choice(self.ItemPool)
        self.letter = randint(4,20)
        self.time1 = random.choice([4,5,6,10,12,15,20,30])
        self.time2 = randint(2,30)
        self.cycle = 60/self.time1
        self.OneMinute = self.cycle*self.letter
        self.total = self.OneMinute*self.time2
        
        self.answer = self.time2
        
        self.problem1 = "A printer prints %d %s in %d seconds. At this rate, how many minutes does it take to print %d %s?"%(self.letter,self.item,self.time1,self.total,self.item)
        self.problem2 = "%s's printer prints %d %s in %d seconds. At this rate, how many minutes does it take to print %d %s?"%(self.person,self.letter,self.item,self.time1,self.total,self.item)
        self.problem = random.choice([self.problem1,self.problem2]) 

        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType111(self.problem,self.answer,self.person,self.item,self.letter,self.time1,self.time2,self.total,self.cycle)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"",'unit':"minutes",'problem_type':"ProblemType111"}

    def ExplainType111(self,problem,answer,person,item,letter,time1,time2,total,cycle):
        self.answer_text = "The correct answer is: <b>"+str(answer)+" minutes"
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'>"
        self.table_text = self.table_text + "<tr><td align='center'>"+str(time1)+" s</td>"
        self.table_text = self.table_text + "<td align='center'>x "+str(cycle)+"<br><img src ='/images/explanation/right_arrow.png'></td>"
        self.table_text = self.table_text + "<td align='center'>1 min (60s)</td></tr>"
        self.table_text = self.table_text + "<tr><td colspan=3><img src='/images/explanation/P5_WN_PT111.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td align='center'>"+str(letter)+"<br>"+item+"</td>"
        self.table_text = self.table_text + "<td align='center'><img src ='/images/explanation/right_arrow.png'><br>x "+str(cycle)+"</td>"
        self.table_text = self.table_text + "<td align='center'>?</td>"
        self.table_text = self.table_text + "</tr></table><br>"
        
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>The printer takes "+str(time1)+"s to print "+str(letter)+" "+item+".</div>"
        self.solution_text = self.solution_text + "<div>"+str(time1)+"s &rarr; "+str(letter)+" "+item+"</div><br>"
        self.solution_text = self.solution_text + "<div>Multiplying both sides by "+str(cycle)+", we get "+str(time1)+"s x "+str(cycle)+" &rarr; "+str(letter)+" "+item+" x "+str(cycle)+"</div>"
        self.solution_text = self.solution_text + "<div>1 minute or 60s &rarr; "+str(letter*cycle)+" "+item+"</div>"
        self.solution_text = self.solution_text + "<div>The printer prints at the rate of "+str(letter*cycle)+" "+item+" per minute.</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(total)+" &divide; "+str(letter*cycle)+" = "+str(total/(letter*cycle))+"</div>"
        self.solution_text = self.solution_text + "<div>The printer takes "+str(total/(letter*cycle))+" minutes to print "+str(total)+" "+item+".</div>"
                        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    def GenerateProblemType112(self):
        '''e.g.: Annie can type 25 words in 1 minute. At this rate, how long will she take to type a composition of 450  words?'''
        
        self.person = random.choice(PersonName.GirlName)
        self.ItemPool = ["composition","story","letter","newsletter","blog","dictation"]       
        self.item = random.choice(self.ItemPool)
        self.speed = randint(10,40)
        self.times = randint(10,50)
        self.words = self.times * self.speed
        
        self.answer = self.times

        self.problem1 = "%s can type %d words in 1 minute. At this rate, how long will she take to type a %s of %d words?"%(self.person,self.speed,self.item,self.words)
        self.problem = self.problem1      

        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType112(self.problem,self.answer,self.person,self.item,self.speed,self.words,self.times)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"",'unit':"minutes",'problem_type':"ProblemType112"}

    def ExplainType112(self,problem,answer,person,item,speed,words,times):
        self.answer_text = "The correct answer is: <b>"+str(answer)+" minutes"
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'>"
        self.table_text = self.table_text + "<tr><td align='center'>1 min</td>"
        self.table_text = self.table_text + "<td align='center'>x "+str(times)+"<br><img src ='/images/explanation/right_arrow.png'></td>"
        self.table_text = self.table_text + "<td align='center'>?</td></tr>"
        self.table_text = self.table_text + "<tr><td colspan=3><img src='/images/explanation/P5_WN_PT111.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td align='center'>"+str(speed)+"<br>words</td>"
        self.table_text = self.table_text + "<td align='center'><img src ='/images/explanation/right_arrow.png'><br>x "+str(times)+"</td>"
        self.table_text = self.table_text + "<td align='center'>"+str(words)+"<br>words</td>"
        self.table_text = self.table_text + "</tr></table><br>"
        
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(words)+" words &divide; "+str(speed)+" words = "+str(words/speed)+" times</div>"
        self.solution_text = self.solution_text + "<div>"+person+" types "+str(speed)+" words per minute.</div>"
        self.solution_text = self.solution_text + "<div>"+str(speed)+" words &rarr; 1 min</div><br>"
        self.solution_text = self.solution_text + "<div>Multiplying both sides by "+str(words/speed)+", we get "+str(speed)+" words x "+str(times)+" &rarr; 1 min x "+str(times)+"</div>"
        self.solution_text = self.solution_text + "<div>"+str(words)+" words &rarr; "+str(times)+" min</div>"
        self.solution_text = self.solution_text + "<div>"+person+" will take "+str(times)+" min to type the "+item+".</div>"
                       
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    def GenerateProblemType113(self):
        '''e.g.: Annie can type 25 words in 1 minute. If she took 18 minutes to type a composition, how many words did the composition have?'''
        
        self.person = random.choice(PersonName.GirlName)
        self.ItemPool = ["composition","story","letter","newsletter","blog","dictation"]       
        self.item = random.choice(self.ItemPool)
        self.speed = randint(10,40)
        self.times = randint(10,50)
        self.words = self.times * self.speed
        
        self.answer = self.words

        self.problem1 = "%s can type %d words in 1 minute. If she took %d minutes to type a %s, how many words did the %s have?"%(self.person,self.speed,self.times,self.item,self.item)
        self.problem = self.problem1      

        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType113(self.problem,self.answer,self.person,self.item,self.speed,self.words,self.times)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"",'unit':"words",'problem_type':"ProblemType113"}

    def ExplainType113(self,problem,answer,person,item,speed,words,times):
        self.answer_text = "The correct answer is: <b>"+str(answer)+" words"
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'>"
        self.table_text = self.table_text + "<tr><td align='center'>1 min</td>"
        self.table_text = self.table_text + "<td align='center'>x "+str(times)+"<br><img src ='/images/explanation/right_arrow.png'></td>"
        self.table_text = self.table_text + "<td align='center'>"+str(times)+" min</td></tr>"
        self.table_text = self.table_text + "<tr><td colspan=3><img src='/images/explanation/P5_WN_PT111.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td align='center'>"+str(speed)+"<br>words</td>"
        self.table_text = self.table_text + "<td align='center'><img src ='/images/explanation/right_arrow.png'><br>x "+str(times)+"</td>"
        self.table_text = self.table_text + "<td align='center'>?</td>"
        self.table_text = self.table_text + "</tr></table><br>"
        
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>"+person+" types at a rate of "+str(speed)+" words per minute.</div>"
        self.solution_text = self.solution_text + "<div>1 min &rarr; "+str(speed)+" words</div><br>"
        self.solution_text = self.solution_text + "<div>Multiplying both sides by "+str(words/speed)+", we get 1 min x "+str(times)+" &rarr; "+str(speed)+" words x "+str(times)+"</div>"
        self.solution_text = self.solution_text + "<div>"+str(times)+" min &rarr; "+str(words)+" words</div>"
        self.solution_text = self.solution_text + "<div>The "+item+" had "+str(words)+" words.</div>"
        self.solution_text = self.solution_text + "<br><div> Watch below video for explanation of similar problem<br>"
        VideoLink = '<object><param name="movie" value="https://www.youtube.com/v/u1zgFlCw8Aw?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded"><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "e-bhW5zDJxY";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
                      
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    def GenerateProblemType114(self):
        '''e.g.: A water fountain dispenses 25 ml of water in 1 second. At this rate, how long does it take to fill a 650 ml bottle?'''

        self.ItemPool = {"1":["tea dispenser","tea","cup"],"2":["soft drink fountain","soft drink","cup"],"3":["coffee vending machine","coffee","cup"],
			"4":["juice dispenser","juice","bottle"],"5":["thermos flask","hot water","cup"],
			}       
        self.key = self.ItemPool.keys()[randint(0,len(self.ItemPool)-1)]
        self.fountain = self.ItemPool[self.key][0]
        self.item = self.ItemPool[self.key][1]
        self.holder = self.ItemPool[self.key][2]
        self.capacity = random.randrange(100,1000,50)
        self.speed = random.choice([5,10,25,50])
        self.times = self.capacity/self.speed
        
        self.answer = self.times

        self.problem1 = "A %s dispenses %d ml of %s in 1 second. At this rate, how long does it take to fill a %d ml %s?"%(self.fountain,self.speed,self.item,self.capacity,self.holder)
        self.problem = self.problem1      

        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType114(self.problem,self.answer,self.fountain,self.item,self.holder,self.capacity,self.speed,self.times)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"",'unit':"seconds",'problem_type':"ProblemType114"}

    def ExplainType114(self,problem,answer,fountain,item,holder,capacity,speed,times):
        self.answer_text = "The correct answer is: <b>"+str(answer)+" seconds"
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'>"
        self.table_text = self.table_text + "<tr><td align='center'>1 s</td>"
        self.table_text = self.table_text + "<td align='center'>x "+str(times)+"<br><img src ='/images/explanation/right_arrow.png'></td>"
        self.table_text = self.table_text + "<td align='center'>?</td></tr>"
        self.table_text = self.table_text + "<tr><td colspan=3><img src='/images/explanation/P5_WN_PT111.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td align='center'>"+str(speed)+" ml</td>"
        self.table_text = self.table_text + "<td align='center'><img src ='/images/explanation/right_arrow.png'><br>x "+str(times)+"</td>"
        self.table_text = self.table_text + "<td align='center'>"+str(capacity)+" ml</td>"
        self.table_text = self.table_text + "</tr></table><br>"
        
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(capacity)+" ml &divide; "+str(speed)+" ml = "+str(capacity/speed)+" times</div><br>"
        self.solution_text = self.solution_text + "<div>The "+fountain+" dispenses "+str(speed)+" ml in 1 second.</div>"
        self.solution_text = self.solution_text + "<div>"+str(speed)+" ml &rarr; 1 sec</div><br>"
        self.solution_text = self.solution_text + "<div>Multiplying both sides by "+str(times)+", we get "+str(speed)+" ml x "+str(times)+" &rarr; 1 sec x "+str(times)+"</div>"
        self.solution_text = self.solution_text + "<div>"+str(capacity)+" ml &rarr; "+str(times)+" sec</div><br>"
        self.solution_text = self.solution_text + "<div>It takes "+str(times)+" seconds to fill the "+holder+".</div>"
                       
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    '''Problem Type 52 starts here'''
    def GenerateProblemType115(self):
        '''e.g.: Following are the charges for electricity consumption:
        	How much did Annie pay (in $) if she consumed 149 kWh of electricity in one month?'''
        
        self.person = random.choice(PersonName.GirlName)
        self.charge1 = randint(10,30)
        self.charge2 = self.charge1 + random.choice([1,2,3,4,5,6,7])
        self.consumed = randint(135,300)
        self.total = float((self.charge1 * 121 + self.charge2 * (self.consumed - 121)))/100
        
        self.answer = self.total

        self.problem1 = "<div>Following are the charges for electricity consumption:</div><br>"
        self.problem1 = self.problem1 + "<div><table border=1 cellpadding=10><tr><th>Amount of electricity consumed</th><th>Charge</th></tr>"
        self.problem1 = self.problem1 + "<tr><td>Up to 121 kWh</td><td>"+str(self.charge1)+" &cent; per kWh</td></tr>"
        self.problem1 = self.problem1 + "<tr><td>Above 121 kWh</td><td>"+str(self.charge2)+" &cent; per kWh</td></tr></table></div><br>"
        self.problem1 = self.problem1 + "<div>How much did "+self.person+" pay (in $) if she consumed "+str(self.consumed)+" kWh electricity in one month?</div>"
        self.problem = self.problem1      

        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType115(self.problem,self.answer,self.person,self.charge1,self.charge2,self.consumed,self.total)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,
                'explain':self.explain,'dollar_unit':"$",'unit':"",'problem_type':"ProblemType115",'CheckAnswerType':2}

    def ExplainType115(self,problem,answer,person,charge1,charge2,consumption,total):
        self.answer_text = "The correct answer is: <b>$"+str(answer)
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'>"
        self.table_text = self.table_text + "<tr><td></td><td align='center'>121<br><img src='/images/explanation/up_curly_braces_1cm.png'></td>"
        self.table_text = self.table_text + "<td align='center'>("+str(consumption)+"-121)<br><img src='/images/explanation/up_curly_braces_1cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td>Electricity</td><td><img src='/images/explanation/pink_block_1cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/green_block_1cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td></td><td align='center' colspan=2><img src='/images/explanation/down_curly_braces_2cm.png'><br>"+str(consumption)+" kWh</td>"     
        self.table_text = self.table_text + "</tr></table><br>"
        
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>Charge for first 121 kWh of electricity = "+str(charge1)+" &cent; x 121 = "+str(charge1*121)+" &cent; = $"+str(Decimal(charge1*121)/100)+"</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(consumption)+" kWh - 121 kWh = "+str(consumption-121)+" kWh</div>"
        self.solution_text = self.solution_text + "<div>Charge for next "+str(consumption-121)+" kWh of electricity = "+str(charge2)+" &cent; x "+str(consumption-121)+" = "+str(charge2*(consumption-121))+" &cent; = $"+str(Decimal((charge2*(consumption-121)))/100)+"</div><br>"
        self.solution_text = self.solution_text + "<div>Total charge for "+str(consumption)+" kWh of electricity = $"+str(Decimal(charge1*121)/100)+" + $"+str(Decimal((charge2*(consumption-121)))/100)+" = $"+str(total)+"</div><br>"

        self.solution_text = self.solution_text + "<div>"+person+" paid $"+str(total)+"</div><br>"
                        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    def GenerateProblemType116(self):
        '''e.g.: Following are the charges for electricity consumption:
        	If Annie paid $34.55 last month in electricity charges, how much electricity did she consume?'''
        
        self.person = random.choice(PersonName.PersonName)
        self.charge1 = randint(10,30)
        self.charge2 = self.charge1 + random.choice([1,2,3,4,5,6,7])
        self.consumed = randint(135,300)
        self.total = Decimal((self.charge1 * 121 + self.charge2 * (self.consumed - 121)))/100
        
        self.answer = self.consumed

        self.problem1 = "<div>Following are the charges for electricity consumption:</div><br>"
        self.problem1 = self.problem1 + "<div><table border=1 cellpadding=10><tr><th>Amount of electicity consumed</th><th>Charge</th></tr>"
        self.problem1 = self.problem1 + "<tr><td>Up to 121 kWh</td><td>"+str(self.charge1)+" &cent; per kWh</td></tr>"
        self.problem1 = self.problem1 + "<tr><td>Above 121 kWh</td><td>"+str(self.charge2)+" &cent; per kWh</td></tr></table></div><br>"
        self.problem1 = self.problem1 + "<div>If "+self.person+" paid $"+str(self.total)+" last month in electricity charges, how much electricity did she consume?</div>"
        self.problem = self.problem1      

        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType116(self.problem,self.answer,self.person,self.charge1,self.charge2,self.consumed,self.total)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"",'unit':"kWh",'problem_type':"ProblemType116"}

    def ExplainType116(self,problem,answer,person,charge1,charge2,consumption,total):
        self.answer_text = "The correct answer is: <b>"+str(answer)+" kWh"
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'>"
        self.table_text = self.table_text + "<tr><td></td><td align='center'>121 kWh<br><img src='/images/explanation/up_curly_braces_1cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td>Electricity</td><td><img src='/images/explanation/pink_block_1cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/green_block_1cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td></td><td align='center' colspan=2><img src='/images/explanation/down_curly_braces_2cm.png'><br>?</td>"     
        self.table_text = self.table_text + "</tr></table><br>"
        
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>Charge for first 121 kWh of electricity = "+str(charge1)+" &cent; x 121 = "+str(charge1*121)+" &cent; = $"+str(Decimal(charge1*121)/100)+"</div>"
        self.solution_text = self.solution_text + "<div>Since "+person+" paid more than $"+str(charge1*121/100)+", she consumed more than 121 kWh.</div><br>"
        self.solution_text = self.solution_text + "<div>$"+str(total)+" - $"+str(Decimal(charge1*121)/100)+" = $"+str(total-Decimal(charge1*121)/100)+" = "+str(int(total*100-charge1*121))+" &cent;</div>"
        self.solution_text = self.solution_text + "<div>"+str(int(total*100-charge1*121))+" &divide; "+str(charge2)+" = "+str(int((total*100-charge1*121)/charge2))+"</div>"
        self.solution_text = self.solution_text + "<div>She consumed "+str(int((total*100-charge1*121)/charge2))+" kWh of electricity in the second tier.</div><br>"
        self.solution_text = self.solution_text + "<div>Total electricity consumption = 121 kWh + "+str(int((total*100-charge1*121)/charge2))+" kWh = "+str(consumption)+" kWh</div><br>"
        self.solution_text = self.solution_text + "<div>"+person+" consumed "+str(consumption)+" kWh.</div>"
                                
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    '''Problem Type 53 starts here'''
    def GenerateProblemType117(self):
        '''e.g.: If you drink 8 cups of water a day, how many litres of water will you drink in a year? (Take 1 cup as 250 ml and 1 year as 365 days.)'''

        self.person = random.choice(PersonName.GirlName)
        self.ItemPool = {"1":["water",8],"2":["tea",4],"3":["coffee",4],"4":["green tea",4],"5":["milk",4]}       
        self.key = self.ItemPool.keys()[randint(0,len(self.ItemPool)-1)]
        self.item = self.ItemPool[self.key][0]
        self.number = self.ItemPool[self.key][1]
        self.total = (self.number*365)/4
      
        self.answer = self.total
     
        self.problem1 = "If %s drinks %d cups of %s a day, how many litres of %s will she drink in a year? (Take 1 cup as 250 ml and 1 year as 365 days.)"%(self.person,self.number,self.item,self.item)
        self.problem2 = "How many litres of %s will %s drink in a year if she drinks %d cups of %s a day? (Take 1 cup as 250 ml and 1 year as 365 days.)"%(self.item,self.person,self.number,self.item)
        self.problem = random.choice([self.problem1,self.problem2])  

        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType117(self.problem,self.answer,self.person,self.item,self.number,self.total)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"",'unit':"litres",'problem_type':"ProblemType117"}

    def ExplainType117(self,problem,answer,person,item,number,total):
        self.answer_text = "The correct answer is: <b>"+str(answer)+" litres"
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'>"
        if (number==8):
            self.table_text = self.table_text + "<tr><td></td><td align='center'>"+str(number)+"cups="+str(number*250/1000)+" litres<br><img src='/images/explanation/up_curly_braces_2cm.png'></td></tr>"
        else:
            self.table_text = self.table_text + "<tr><td></td><td align='center'>"+str(number)+" cups="+str(number*250/1000)+" litre<br><img src='/images/explanation/up_curly_braces_2cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td>Day</td><td><img src='/images/explanation/pink_block_2cm.png'></td><td>x 365</td><td><img src='/images/explanation/right_curly_braces_pt5cm.png'></td><td>?</td></tr>"
        self.table_text = self.table_text + "</tr></table><br>"
        
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div><b>Method 1:</b></div><br>"
        self.solution_text = self.solution_text + "<div>"+person+" drinks "+str(number)+" cups of "+item+" in a day.</div>"
        self.solution_text = self.solution_text + "<div>"+str(number)+" cups x 365 = "+str(number*365)+" cups</div>"
        self.solution_text = self.solution_text + "<div>"+person+" drinks "+str(number*365)+" cups of "+item+" in a year.</div><br>"
        self.solution_text = self.solution_text + "<div>1 cup = 250 ml</div>"
        self.solution_text = self.solution_text + "<div>"+str(number*365)+" cups = "+str(number*365)+" x 250 ml = "+str(number*365*250)+" ml</div><br>"
        self.solution_text = self.solution_text + "<div>1000 ml = 1 litre</div>"
        self.solution_text = self.solution_text + "<div>"+str(number*365*250)+" ml = "+str(number*365*250)+" &divide; 1000 = "+str(number*365*250/1000)+" litres</div>"
        self.solution_text = self.solution_text + "<div>"+person+" will drink "+str(number*365*250/1000)+" litres of "+item+" in a year.</div><br>"
        self.solution_text = self.solution_text + "<div><b>Method 2:</b></div><br>"
        self.solution_text = self.solution_text + "<div>"+person+" drinks "+str(number)+" of cups in a day.</div>"
        if (number==8):
            self.solution_text = self.solution_text + "<div>"+str(number)+" = "+str(number)+" x 250ml = "+str(number*250)+"ml = "+str(number*250/1000)+" litres</div>"
            self.solution_text = self.solution_text + "<div>So, "+person+" drinks "+str(number*250/1000)+" litres of "+item+" in a day.</div><br>"
            self.solution_text = self.solution_text + "<div>1 year = 365 days</div>"
            self.solution_text = self.solution_text + "<div>"+str(number*250/1000)+" litres x 365 = "+str(number*250*365/1000)+" litres</div>"
        else:
            self.solution_text = self.solution_text + "<div>"+str(number)+" = "+str(number)+" x 250ml = "+str(number*250)+"ml = "+str(number*250/1000)+" litre</div>"
            self.solution_text = self.solution_text + "<div>So, "+person+" drinks "+str(number*250/1000)+" litre of "+item+" in a day.</div><br>"
            self.solution_text = self.solution_text + "<div>1 year = 365 days</div>"
        self.solution_text = self.solution_text + "<div>"+person+" will drink "+str(number*250*365/1000)+" litres of "+item+" in a year.</div>"
                    
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    def GenerateProblemType118(self):
        '''e.g.: If 2 dozen mangoes are packed in 1 box, how many mangoes are packed in 60 boxes?'''

        self.ItemPool = ['soft drink cans','water bottles','milk packets','eggs','cookie packets','candy bags','chocolate bars','pencils','pens','notebooks',
                         ]       
        self.item = random.choice(self.ItemPool)
        self.number1 = randint(2,12)
        self.number2 = randint(5,100)
        self.total = self.number1*self.number2*12
        
        self.answer = self.total
     
        self.problem1 = "If %d dozen %s are packed in 1 box, how many %s are packed in %d boxes?"%(self.number1,self.item,self.item,self.number2)
        self.problem2 = "How many %s are packed in %d boxes if 1 box has %d dozen %s?"%(self.item,self.number2,self.number1,self.item)
        self.problem = random.choice([self.problem1,self.problem2])

        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType118(self.problem,self.answer,self.item,self.number1,self.number2,self.total)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"",'unit':self.item,'problem_type':"ProblemType118"}

    def ExplainType118(self,problem,answer,item,number1,number2,total):
        self.answer_text = "The correct answer is: <b>"+str(answer)+" "+item
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'>"
        self.table_text = self.table_text + "<tr><td></td><td align='center'>"+str(number1)+" dozen="+str(number1*12)+"<br><img src='/images/explanation/up_curly_braces_2cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td>Box</td><td><img src='/images/explanation/pink_block_2cm.png'></td><td>x"+str(number2)+"</td><td><img src='/images/explanation/right_curly_braces_pt5cm.png'></td><td>?</td></tr>"
        self.table_text = self.table_text + "</tr></table><br>"
        
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div><b>Method 1:</b></div><br>"
        self.solution_text = self.solution_text + "<div>1 box has "+str(number1)+" dozen "+item+".</div>"
        self.solution_text = self.solution_text + "<div>"+str(number1)+" dozen x "+str(number2)+" = "+str(number1*number2)+" dozens</div>"
        self.solution_text = self.solution_text + "<div>"+str(number2)+" boxes have "+str(number1*number2)+" dozens "+item+".</div><br>"
        self.solution_text = self.solution_text + "<div>1 dozen = 12 "+item+"</div>"
        self.solution_text = self.solution_text + "<div>"+str(number1*number2)+" dozen = "+str(number1*number2)+" x 12 = "+str(number1*number2*12)+" "+item+"</div>"
        self.solution_text = self.solution_text + "<div>There are "+str(number1*number2*12)+" "+item+" packed in "+str(number2)+" boxes.</div><br>"

        self.solution_text = self.solution_text + "<div><b>Method 2:</b></div><br>"
        self.solution_text = self.solution_text + "<div>1 box has "+str(number1)+" dozen "+item+" and 1 dozen is equal to 12 "+item+".</div>"
        self.solution_text = self.solution_text + "<div>"+str(number1)+" x 12 "+item+" = "+str(number1*12)+" "+item+"</div>"
        self.solution_text = self.solution_text + "<div>1 box has "+str(number1*12)+" "+item+".</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(number2)+" x "+str(number1*12)+" "+item+" = "+str(number2*number1*12)+" "+item+"</div>"
        self.solution_text = self.solution_text + "<div>There are "+str(number2*number1*12)+" "+item+" packed in "+str(number2)+" boxes</div>"
                    
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    '''Problem Type 54 starts here'''
    def GenerateProblemType119(self):
        '''e.g.: Annie runs 6 days a week from Monday through Saturday. The distances run by her are shown in the table below.
            She ran twice as much on Wednesday as on Thursday and twice as much on Thursday as on Friday. How much did she run on Friday?'''
    
        self.person = random.choice(PersonName.GirlName)
        self.ItemPool = {'1':['jog','jogged','jogged',randint(5,10),randint(5,10),randint(5,10),randint(2,4)],'2':['swim','swum','swam',randint(1,3),randint(1,3),randint(1,3),1],
                         '3':['drive','driven','drove',randint(10,30),randint(10,30),randint(10,30),randint(5,10)],'4':['bike','biked','biked',randint(4,15),randint(4,15),randint(4,15),randint(3,6)],
                         '5':['carpool','carpooled','carpooled',randint(10,30),randint(10,30),randint(10,30),randint(5,10)],'6':['cycle','cycled','cycled',randint(4,15),randint(4,15),randint(4,15),randint(3,6)],
                         '7':['ride','ridden','rode',randint(4,15),randint(4,15),randint(4,15),randint(3,6)],'8':['run','run','ran',randint(5,10),randint(5,10),randint(5,10),randint(2,4)]
                         }       
        self.key = self.ItemPool.keys()[randint(0,len(self.ItemPool)-1)]
        self.swim = self.ItemPool[self.key][0]
        self.swum = self.ItemPool[self.key][1]
        self.swam = self.ItemPool[self.key][2]
        self.DayPool = ["Wednesday","Thursday","Friday"]
        random.shuffle(self.DayPool)
        self.day1 = self.DayPool[0]
        self.day2 = self.DayPool[1]
        self.day3 = self.DayPool[2]
        self.distance1 = self.ItemPool[self.key][3]
        self.distance2 = self.ItemPool[self.key][4]
        self.distance3 = self.ItemPool[self.key][5]
        self.distance4 = self.ItemPool[self.key][6]
        self.total = self.distance1+self.distance2+self.distance3+7*self.distance4
        
        self.answer = self.distance4

        self.problem1 = "%s %ss 6 days a week from Monday through Saturday. The distances %s by her are shown in the table below."%(self.person,self.swim,self.swam)
        self.problem1 = self.problem1 + "<br><table border =1 cellpadding=5><tr><th>Day</th><th>Monday</th><th>Tuesday</th><th>Wednesday</th><th>Thursday</th><th>Friday</th><th>Saturday</th><th>Total</th></tr>"
        self.problem1 = self.problem1 + "<tr><td align='center'>Distance "+self.swam+"</td><td align='center'>"+str(self.distance1)+" km</td><td align='center'>"+str(self.distance2)+" km</td><td align='center'>?</td><td align='center'>?</td><td align='center'>?</td><td>"+str(self.distance3)+" km</td><td align='center'>"+str(self.total)+" km</td></tr></table><br>"
        self.problem1 = self.problem1 + "She %s twice as much on %s as on %s and twice as much on %s as on %s. How much did she %s on %s?"%(self.swam,self.day1,self.day2,self.day2,self.day3,self.swam,self.day3)
        self.problem = self.problem1

        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType119(self.problem,self.answer,self.person,self.distance1,self.distance2,self.distance3,self.total,self.day1,self.day2,self.day3,self.swam,self.swum)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"",'unit':"km",'problem_type':"ProblemType119"}

    def ExplainType119(self,problem,answer,person,distance1,distance2,distance3,total,day1,day2,day3,swam,swum):
        self.answer_text = "The correct answer is: <b>"+str(answer)+" km"
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'>"
        self.table_text = self.table_text + "<tr><td>"+day1+"</td>"
        for _i in range(4):
            self.table_text = self.table_text + "<td><img src='/images/explanation/pink_block_pt5cm.png'></td>"
        self.table_text = self.table_text + "<td rowspan=3><img src='/images/explanation/right_curly_braces_2cm.png'></td>"
        self.table_text = self.table_text + "<td rowspan=3>"+str(total)+" km - "+str(distance1+distance2+distance3)+" km</td></tr>"
        self.table_text = self.table_text + "<tr><td>"+day2+"</td>"
        for _i in range(2):
            self.table_text = self.table_text + "<td><img src='/images/explanation/pink_block_pt5cm.png'></td>"
        self.table_text = self.table_text + "</tr><tr><td>"+day3+"</td>"       
        self.table_text = self.table_text + "<td><img src='/images/explanation/pink_block_pt5cm.png'></td>"
        self.table_text = self.table_text + "<tr><td></td>"       
        self.table_text = self.table_text + "<td align='center'><img src='/images/explanation/down_curly_braces_pt5cm.png'><br>?</td>"
        self.table_text = self.table_text + "</tr></table><br>"
        
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(distance1)+" km + "+str(distance2)+" km + "+str(distance3)+" km = "+str(distance1+distance2+distance3)+" km</div>"
        self.solution_text = self.solution_text + "<div>Total distance "+swum+" on Monday, Tuesday and Saturday is "+str(distance1+distance2+distance3)+" km.</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(total)+" km - "+str(distance1+distance2+distance3)+" km = "+str(total-(distance1+distance2+distance3))+" km</div>"
        self.solution_text = self.solution_text + "<div>Total distance "+swum+" on Wednesday, Thursday and Friday is "+str(total-(distance1+distance2+distance3))+" km.</div><br>"
        self.solution_text = self.solution_text + "<div>From the model,</div>"
        self.solution_text = self.solution_text + "<div>7 units = "+str(total-(distance1+distance2+distance3))+" km</div>"
        self.solution_text = self.solution_text + "<div>1 unit = "+str(total-(distance1+distance2+distance3))+" &divide; 7 = "+str((total-(distance1+distance2+distance3))/7)+" km</div>"
        self.solution_text = self.solution_text + "<div>"+person+" "+swam+" "+str((total-(distance1+distance2+distance3))/7)+" km on "+day3+".</div>"
                    
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    def GenerateProblemType120(self):
        '''e.g.: The table below shows the number of visitors to a theme park in a week.
            There were as many visitors on Saturday as on Sunday and twice as many on Sunday as on Friday. How many visitors were there on Sunday?'''

        self.ItemPool = ["theme park","zoo","bird park","water park","museum","circus","magic show","movie show","night safari","hotel","butterfly park"]     
        self.item = random.choice(self.ItemPool)
        self.day1 = randint(100,500)
        self.day2 = randint(100,500)
        self.day3 = randint(100,500)
        self.day4 = randint(100,500)
        self.day5 = randint(400,500)
        self.day6 = 2*self.day5
        self.day7 = 2*self.day5
        self.total = (self.day1+self.day2+self.day3+self.day4+self.day5+self.day6+self.day7)
        
        self.answer = self.day7

        self.problem1 = "The table below shows the number of visitors to a %s in a week"%(self.item)
        self.problem1 = self.problem1 + "<br><table border =1 cellpadding=5><tr><th>Day</th><th>Monday</th><th>Tuesday</th><th>Wednesday</th><th>Thursday</th><th>Friday</th><th>Saturday</th><th>Sunday</th><th>Total</th></tr>"
        self.problem1 = self.problem1 + "<tr><td>Number of<br>visitors</td><td>"+str(self.day1)+"</td><td>"+str(self.day2)+"</td><td>"+str(self.day3)+"</td><td>"+str(self.day4)+"</td><td>?</td><td>?</td><td>?</td><td>"+str(self.total)+"</td></tr></table><br>"
        self.problem1 = self.problem1 + "There were as many visitors on Saturday as on Sunday and twice as many on Sunday as on Friday. How many visitors were there on Sunday?"
        self.problem = self.problem1

        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType120(self.problem,self.answer,self.day1,self.day2,self.day3,self.day4,self.day5,self.day6,self.total)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"",'unit':"visitors",'problem_type':"ProblemType120"}

    def ExplainType120(self,problem,answer,day1,day2,day3,day4,day5,day6,total):
        self.answer_text = "The correct answer is: <b>"+str(answer)+" visitors"
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'>"
        self.table_text = self.table_text + "<tr><td>Friday</td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/pink_block_pt5cm.png'></td><td></td>"
        self.table_text = self.table_text + "<td rowspan=3><img src='/images/explanation/right_curly_braces_2cm.png'></td>"
        self.table_text = self.table_text + "<td rowspan=3>"+str(total)+" - ("+str(day1)+" + "+str(day2)+" + "+str(day3)+" + "+str(day4)+")</td></tr>"
        self.table_text = self.table_text + "<tr><td>Saturday</td>"
        for _i in range(2):
            self.table_text = self.table_text + "<td><img src='/images/explanation/pink_block_pt5cm.png'></td>"
        self.table_text = self.table_text + "</tr><tr><td>Sunday</td>"
        for _i in range(2):
            self.table_text = self.table_text + "<td><img src='/images/explanation/pink_block_pt5cm.png'></td>"
        self.table_text = self.table_text + "</tr><tr><td></td>"       
        self.table_text = self.table_text + "<td align='center' colspan=2><img src='/images/explanation/down_curly_braces_1cm.png'><br>?</td>"
        self.table_text = self.table_text + "</tr></table><br>"
        
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(day1)+" + "+str(day2)+" + "+str(day3)+" + "+str(day4)+" = "+str(day1+day2+day3+day4)+"</div>"
        self.solution_text = self.solution_text + "<div>Total number of visitors on Monday, Tuesday, Wednesday and Thursday is "+str(day1+day2+day3+day4)+"</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(total)+" - "+str(day1+day2+day3+day4)+" = "+str(total-(day1+day2+day3+day4))+"</div>"
        self.solution_text = self.solution_text + "<div>Total number of visitors on Friday, Saturday and Sunday is "+str(total-(day1+day2+day3+day4))+".</div><br>"
        self.solution_text = self.solution_text + "<div>From the model,</div>"
        self.solution_text = self.solution_text + "<div>5 units = "+str(total-(day1+day2+day3+day4))+"</div>"
        self.solution_text = self.solution_text + "<div>1 unit = "+str(total-(day1+day2+day3+day4))+" &divide; 5 = "+str((total-(day1+day2+day3+day4))/5)+"</div>"
        self.solution_text = self.solution_text + "<div>2 x "+str((total-(day1+day2+day3+day4))/5)+" = "+str(2*(total-(day1+day2+day3+day4))/5)+"</div>"
        self.solution_text = self.solution_text + "<div>There were "+str(2*(total-(day1+day2+day3+day4))/5)+" visitors on Sunday.</div>"
        self.solution_text = self.solution_text + "<br><div> Watch below video for explanation of similar problem<br>"
        VideoLink = '<object><param name="movie" value="https://www.youtube.com/v/u1zgFlCw8Aw?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded"><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "P_TH8KLq9aM";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
                      
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    def GenerateProblemType121(self):
        '''e.g.: The table below shows the number of books that a library  has in different categories.
            The library has twice as many Fictional books as Business books and thrice as many Technology books as Business books. Find the number of Technology books.'''

        self.ItemPool = {'1':['movies','movie rental shop','in','categories','category','action','drama','sci-fi','family','animation','cartoon','foreign languages'],
            '2':['books','bookstore','in','categories','category','kids','arts','cooking','fictional','business','technology','languages'],
            '3':['participants','running tournament','in','categories','category','5 km','10 km','half marathon','full marathon','kids dash','corporate 10 km','corporate half marathon'],
            '4':['tea boxes','tea merchant','of','types','type','green','ginger','oolong','english breakfast','darjeeling','earl grey','orange pekoe'],
            '5':['coffee bean bags','coffee bean merchant','of','types','type','java','green','decaf','american roast','espresso','brazilian roast','french roast'],
            '6':['rice bags','rice wholesaler','of','types','type','basmati','thai','delrose','brown','fragrant','jasmine','black japonica'],
            '7':['perfume bottles','perfume manufacturer','in','fragrances','fragrance','floral','spicy','woody','herbal','musky','powdery','aqueous'],
            '8':['candles','candle supplier','in','scents','scent','blueberry','chocolate','grapefruit','kiwi','lavender','mango','sandalwood'],
            '9':['sugar bags','dry goods supplier','of','types','type','brown','superfine','coarse','caster','powdered','granulated','icing'],
            '10':['cheese blocks','cheese factory','of','kinds','kind','blue','paneer','cheddar','cottage','swiss','feta','parmesan'],
            '11':['cars','car manufacturer','of','types','type','sedan','suv','sports','minivan','hatchback','convertible','coupe'],
            '12':['books','library','in','categories','category','kids','arts','cooking','fictional','business','technology','languages']
            }     
        self.key = self.ItemPool.keys()[randint(0,len(self.ItemPool)-1)]
        self.item = self.ItemPool[self.key][0]
        self.place = self.ItemPool[self.key][1]
        self.preposition = self.ItemPool[self.key][2]
        self.categories = self.ItemPool[self.key][3]
        self.category = self.ItemPool[self.key][4]
        self.MasterCategory = [self.ItemPool[self.key][5],self.ItemPool[self.key][6],self.ItemPool[self.key][7],self.ItemPool[self.key][8],
                    self.ItemPool[self.key][9],self.ItemPool[self.key][10],self.ItemPool[self.key][11]]
        random.shuffle(self.MasterCategory)
        self.category1 = self.MasterCategory[0]
        self.category2 = self.MasterCategory[1]
        self.category3 = self.MasterCategory[2]
        self.category4 = self.MasterCategory[3]
        self.category5 = self.MasterCategory[4]
        self.category6 = self.MasterCategory[5]
        self.category7 = self.MasterCategory[6]
        self.number1 = randint(200,800)
        self.number2 = randint(200,800)
        self.number3 = randint(200,800)
        self.number4 = randint(200,800)
        self.number5 = randint(200,400)
        self.number6 = 2*self.number5
        self.number7 = 3*self.number5
        self.total = self.number1+self.number2+self.number3+self.number4+self.number5+self.number6+self.number7
        
        self.answer = self.number7

        self.problem1 = "The table below shows the number of %s that a %s has %s different %s."%(self.item,self.place,self.preposition,self.categories)
        self.problem1 = self.problem1 + "<table border =1 cellpadding=5><tr><th>"+self.category+"</th><th>"+self.category1+"</th><th>"+self.category2+"</th><th>"+self.category3+"</th><th>"+self.category4+"</th><th>"+self.category5+"</th><th>"+self.category6+"</th><th>"+self.category7+"</th><th>Total</th></tr>"
        self.problem1 = self.problem1 + "<tr><td>Number of<br>"+self.item+"</td><td align='center'>"+str(self.number1)+"</td><td align='center'>"+str(self.number2)+"</td><td align='center'>"+str(self.number3)+"</td><td align='center'>"+str(self.number4)+"</td><td align='center'>?</td><td align='center'>?</td><td align='center'>?</td><td>"+str(self.total)+"</td></tr></table><br>"                                                              
        self.problem1 = self.problem1 + "The %s has twice as many %s %s as %s %s and thrice as many %s %s as %s %s. Find the number of %s %s."%(self.place,self.category6,self.item,self.category5,self.item,self.category7,self.item,self.category5,self.item,self.category7,self.item)
        self.problem = self.problem1

        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType121(self.problem,self.answer,self.category1,self.category2,self.category3,self.category4,self.category5,self.category6,self.category7,self.number1,self.number2,self.number3,self.number4,self.total,self.item)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"",'unit':self.category7+" "+self.item,'problem_type':"ProblemType121"}

    def ExplainType121(self,problem,answer,category1,category2,category3,category4,category5,category6,category7,number1,number2,number3,number4,total,object):
        self.answer_text = "The correct answer is: <b>"+str(answer)+" "+category7+" "+object
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'>"
        self.table_text = self.table_text + "<tr><td>"+category4+"</td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/pink_block_pt5cm.png'></td><td></td><td></td>"
        self.table_text = self.table_text + "<td rowspan=3><img src='/images/explanation/right_curly_braces_2cm.png'></td>"
        self.table_text = self.table_text + "<td rowspan=3>"+str(total)+" - ("+str(number1)+" + "+str(number2)+" + "+str(number3)+" + "+str(number4)+")</td></tr>"
        self.table_text = self.table_text + "<tr><td>"+category6+"</td>"
        for _i in range(2):
            self.table_text = self.table_text + "<td><img src='/images/explanation/pink_block_pt5cm.png'></td>"
        self.table_text = self.table_text + "</tr><tr><td>"+category7+"</td>"
        for _i in range(3):
            self.table_text = self.table_text + "<td><img src='/images/explanation/pink_block_pt5cm.png'></td>"
        self.table_text = self.table_text + "</tr><tr><td></td>"       
        self.table_text = self.table_text + "<td align='center' colspan=3><img src='/images/explanation/down_curly_braces_1cm.png'><br>?</td>"
        self.table_text = self.table_text + "</tr></table><br>"
        
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(number1)+" + "+str(number2)+" + "+str(number3)+" + "+str(number4)+" = "+str(number1+number2+number3+number4)+"</div>"
        self.solution_text = self.solution_text + "<div>Total number of "+category1+", "+category2+", "+category3+" and "+category4+" "+object+" is "+str(number1+number2+number3+number4)+"</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(total)+" - "+str(number1+number2+number3+number4)+" = "+str(total-(number1+number2+number3+number4))+"</div>"
        self.solution_text = self.solution_text + "<div>Total number of "+category5+", "+category6+" and "+category7+" "+object+" is "+str(total-(number1+number2+number3+number4))+".</div><br>"
        self.solution_text = self.solution_text + "<div>From the model,</div>"
        self.solution_text = self.solution_text + "<div>6 units = "+str(total-(number1+number2+number3+number4))+"</div>"
        self.solution_text = self.solution_text + "<div>1 unit = "+str(total-(number1+number2+number3+number4))+" &divide; 6 = "+str((total-(number1+number2+number3+number4))/6)+"</div>"
        self.solution_text = self.solution_text + "<div>3 x "+str((total-(number1+number2+number3+number4))/6)+" = "+str(3*(total-(number1+number2+number3+number4))/6)+"</div>"
        self.solution_text = self.solution_text + "<div>There are "+str(3*(total-(number1+number2+number3+number4))/6)+" "+category7+" "+object+".</div>"
                      
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    '''Problem Type 55 starts here'''
    def GenerateProblemType122(self):
        '''e.g.: A crate packed with 16 cans of soft drink has a mass of 3260 g. Each can has 180 ml of soft drink in it. The mass of the crate is 220 g. 
            What is the mass of each empty can? (Take the mass of 1 ml of soft drink as 1 g.)'''
        
        self.ItemPool = {'1':['box','bottle','water','ml'],'2':['carton','package','milk','ml'],'3':['carton','package','juice','ml'],'4':['box','bottle','cider','ml'],
            '5':['carton','bottle','sparkling water','ml'],'6':['crate','can','tonic water','ml'],'7':['crate','bottle','coconut water','ml'],
            '8':['box','can','juice drink','ml'],'9':['box','can','lemon tea','ml'],'10':['crate','bottle','energy drink','ml'],'11':['carton','packet','raisins','g'],
            '12':['box','punnet','strawberries','g'],'13':['carton','packet','detergent','g'],'14':['carton','packet','cereal','g'],'15':['box','punnet','cherries','g'],
            '16':['box','packet','berries','g'],'17':['box','packet','cookies','g'],'18':['carton','packet','almonds','g'],'19':['box','packet','peanuts','g'],
            '20':['carton','packet','candies','g']
            }     
        self.key = self.ItemPool.keys()[randint(0,len(self.ItemPool)-1)]
        self.crate = self.ItemPool[self.key][0]
        self.bottle = self.ItemPool[self.key][1]
        self.item = self.ItemPool[self.key][2]
        self.unit = self.ItemPool[self.key][3]
        self.EmptyCan = randint(10,20)
        self.ItemWeight = random.randrange(150,300,10)
        self.number = random.randrange(4,16,4)
        self.CrateWeight = random.randrange(200,400,5)
        self.total = (self.EmptyCan+self.ItemWeight)*self.number + self.CrateWeight
        
        self.answer = self.EmptyCan

        self.problem1 = "A %s packed with %d %ss of %s has a mass of %d g. Each %s has %d %s of %s in it. The mass of the %s is %d g. What is the mass of each empty %s?"%(self.crate,self.number,self.bottle,self.item,self.total,self.bottle,self.ItemWeight,self.unit,self.item,self.crate,self.CrateWeight,self.bottle)
        if self.unit=='ml':
            self.problem1 = self.problem1 + "(Take the mass of 1 ml of soft drink as 1 g.)"
        self.problem2 = "The total mass of a %s containing %d %ss of %s is %d g. The mass of the %s is %d g. If each %s holds %d %s of %s, what is the mass of each empty %s?"%(self.crate,self.number,self.bottle,self.item,self.total,self.crate,self.CrateWeight,self.bottle,self.ItemWeight,self.unit,self.item,self.bottle) 
        if self.unit=='ml':
            self.problem2 = self.problem2 + "(Take the mass of 1 ml of soft drink as 1 g.)"
        self.problem3 = "A %s holds %d %s of %s in it. A %s containing %d such %ss has a total mass of %d g. If the mass of the %s without the %ss is %d g, find the mass of each empty %s."%(self.bottle,self.ItemWeight,self.unit,self.item,self.crate,self.number,self.bottle,self.total,self.crate,self.bottle,self.CrateWeight,self.bottle) 
        if self.unit=='ml':
            self.problem3 = self.problem3 + "(Take the mass of 1 ml of soft drink as 1 g.)"
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])

        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType122(self.problem,self.answer,self.crate,self.bottle,self.item,self.unit,self.EmptyCan,self.ItemWeight,self.number,self.CrateWeight,self.total)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"",'unit':"gm",'problem_type':"ProblemType122"}

    def ExplainType122(self,problem,answer,crate,bottle,item,unit,EmptyCan,ItemWeight,number,CrateWeight,total):
        self.answer_text = "The correct answer is: <b>"+str(answer)+" gm"
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'>"
        self.table_text = self.table_text + "<tr><td></td><td align='center'>?<br><img src='/images/explanation/up_curly_braces_pt7cm.png'></td>"
        self.table_text = self.table_text + "<td align='center'>"+str(ItemWeight)+" "+unit+"<br><img src='/images/explanation/up_curly_braces_1cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td>"+bottle+" of "+item+"</td><td><img src='/images/explanation/pink_block_pt7cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/yellow_block_1cm.png'></td>"
        self.table_text = self.table_text + "<td>x "+str(number)+"</td>"
        self.table_text = self.table_text + "<td rowspan=2><img src='/images/explanation/right_curly_braces_pt7cm.png'></td>"
        self.table_text = self.table_text + "<td rowspan=2>"+str(total)+" g</td></tr>"
        self.table_text = self.table_text + "<tr><td>"+crate+"</td><td colspan=2><img src='/images/explanation/green_block_2cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td></td><td align='center' colspan=2><img src='/images/explanation/down_curly_braces_2cm.png'><br>"+str(CrateWeight)+" g</td></tr>"        
        self.table_text = self.table_text + "</tr></table><br>"
        
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>Removing the mass of the "+crate+" from the total mass, we get "+str(total)+" g - "+str(CrateWeight)+" g = "+str(total-CrateWeight)+" g</div>"
        self.solution_text = self.solution_text + "<div>Total mass of "+str(number)+" "+bottle+"s filled with "+item+" is "+str(total-CrateWeight)+" g.</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(total-CrateWeight)+" g &divide; "+str(number)+" = "+str((total-CrateWeight)/number)+" g</div>"
        self.solution_text = self.solution_text + "<div>Mass of each "+bottle+" filled with "+item+" is "+str((total-CrateWeight)/number)+" g.</div><br>"
        self.solution_text = self.solution_text + "<div>"+str((total-CrateWeight)/number)+" g - "+str(ItemWeight)+" g = "+str(EmptyCan)+" g</div>"
        self.solution_text = self.solution_text + "<div>The mass of each empty "+bottle+" is "+str(EmptyCan)+" g.</div>"
                              
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain

    def GenerateProblemType123(self):
        '''e.g.: The mass of an empty crate is 220 g and the mass of an empty can of soft drink is 10 g. If the total mass of the crate containing 16 cans filled with soft drink is 3260 g, 
            what is the mass of soft drink inside each can?  (Take the mass of 1 ml of soft drink as 1 g.)'''
        
        self.ItemPool = {'1':['box','bottle','water','ml'],'2':['carton','package','milk','ml'],'3':['carton','package','juice','ml'],'4':['box','bottle','cider','ml'],
            '5':['carton','bottle','sparkling water','ml'],'6':['crate','can','tonic water','ml'],'7':['crate','bottle','coconut water','ml'],
            '8':['box','can','juice drink','ml'],'9':['box','can','lemon tea','ml'],'10':['crate','bottle','energy drink','ml'],'11':['carton','packet','raisins','g'],
            '12':['box','punnet','strawberries','g'],'13':['carton','packet','detergent','g'],'14':['carton','packet','cereal','g'],'15':['box','punnet','cherries','g'],
            '16':['box','packet','berries','g'],'17':['box','packet','cookies','g'],'18':['carton','packet','almonds','g'],'19':['box','packet','peanuts','g'],
            '20':['carton','packet','candies','g']
            }     
        self.key = self.ItemPool.keys()[randint(0,len(self.ItemPool)-1)]
        self.crate = self.ItemPool[self.key][0]
        self.bottle = self.ItemPool[self.key][1]
        self.item = self.ItemPool[self.key][2]
        self.unit = self.ItemPool[self.key][3]
        self.EmptyCan = randint(10,20)
        self.ItemWeight = random.randrange(150,300,10)
        self.number = random.randrange(4,16,4)
        self.CrateWeight = random.randrange(200,400,5)
        self.total = (self.EmptyCan+self.ItemWeight)*self.number + self.CrateWeight
        
        self.answer = self.ItemWeight

        self.problem1 = "The mass of an empty %s is %d g and the mass of an empty %s of %s is %d g. If the total mass of the %s containing %d %ss filled with %s is %d g, what is the mass of %s inside each %s?"%(self.crate,self.CrateWeight,self.bottle,self.item,self.EmptyCan,self.crate,self.number,self.bottle,self.item,self.total,self.item,self.bottle)
        if self.unit=='ml':
            self.problem1 = self.problem1 + "(Take the mass of 1 ml of soft drink as 1 g.)"
        self.problem2 = "The total mass of a %s containing %d %ss of %s is %d g. The mass of the %s is %d g. If each empty %s has a mass of %d g, what is the mass of %s inside each %s?"%(self.crate,self.number,self.bottle,self.item,self.total,self.crate,self.CrateWeight,self.bottle,self.EmptyCan,self.item,self.bottle)
        if self.unit=='ml':
            self.problem2 = self.problem2 + "(Take the mass of 1 ml of soft drink as 1 g.)"
        self.problem3 = "A %s containing %d %ss of %s has a total mass of %d g. If the mass of the %s without the %ss is %d g and the mass of each empty %s is %d g, find the mass of %s inside each %s."%(self.crate,self.number,self.bottle,self.item,self.total,self.crate,self.bottle,self.CrateWeight,self.bottle,self.EmptyCan,self.item,self.bottle)
        if self.unit=='ml':
            self.problem3 = self.problem3 + "(Take the mass of 1 ml of soft drink as 1 g.)"
        self.problem = random.choice([self.problem1,self.problem2,self.problem3])

        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType123(self.problem,self.answer,self.crate,self.bottle,self.item,self.unit,self.EmptyCan,self.ItemWeight,self.number,self.CrateWeight,self.total)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'dollar_unit':"",'unit':self.unit,'problem_type':"ProblemType123"}

    def ExplainType123(self,problem,answer,crate,bottle,item,unit,EmptyCan,ItemWeight,number,CrateWeight,total):
        self.answer_text = "The correct answer is: <b>"+str(answer)+" "+unit
        self.problem_text = "<div><i>"+problem+"</i></div><br>"
        self.table_text = "<table id='explanation'>"
        self.table_text = self.table_text + "<tr><td></td><td align='center'>"+str(EmptyCan)+" g<br><img src='/images/explanation/up_curly_braces_pt7cm.png'></td>"
        self.table_text = self.table_text + "<td align='center'>?<br><img src='/images/explanation/up_curly_braces_1cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td>"+bottle+" of "+item+"</td><td><img src='/images/explanation/pink_block_pt7cm.png'></td>"
        self.table_text = self.table_text + "<td><img src='/images/explanation/yellow_block_1cm.png'></td>"
        self.table_text = self.table_text + "<td>x "+str(number)+"</td>"
        self.table_text = self.table_text + "<td rowspan=2><img src='/images/explanation/right_curly_braces_pt7cm.png'></td>"
        self.table_text = self.table_text + "<td rowspan=2>"+str(total)+" g</td></tr>"
        self.table_text = self.table_text + "<tr><td>"+crate+"</td><td colspan=2><img src='/images/explanation/green_block_2cm.png'></td></tr>"
        self.table_text = self.table_text + "<tr><td></td><td align='center' colspan=2><img src='/images/explanation/down_curly_braces_2cm.png'><br>"+str(CrateWeight)+" g</td></tr>"        
        self.table_text = self.table_text + "</tr></table><br>"
        
        self.solution_text = "<div>Solution:</div><br>"
        self.solution_text = self.solution_text + "<div>Removing the mass of the "+crate+" from the total mass, we get "+str(total)+" g - "+str(CrateWeight)+" g = "+str(total-CrateWeight)+" g</div>"
        self.solution_text = self.solution_text + "<div>Total mass of "+str(number)+" "+bottle+"s filled with "+item+" is "+str(total-CrateWeight)+" g.</div><br>"
        self.solution_text = self.solution_text + "<div>"+str(total-CrateWeight)+" g &divide; "+str(number)+" = "+str((total-CrateWeight)/number)+" g</div>"
        self.solution_text = self.solution_text + "<div>Mass of each "+bottle+" filled with "+item+" is "+str((total-CrateWeight)/number)+" g.</div><br>"
        self.solution_text = self.solution_text + "<div>"+str((total-CrateWeight)/number)+" g - "+str(EmptyCan)+" g = "+str(ItemWeight)+" g</div>"
        self.solution_text = self.solution_text + "<div>The mass of "+item+" inside each "+bottle+" is "+str(ItemWeight)+" g.</div>"
        self.solution_text = self.solution_text + "<br><div> Watch below video for explanation of similar problem<br>"
        VideoLink = '<object><param name="movie" value="https://www.youtube.com/v/u1zgFlCw8Aw?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded"><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "t0_xee2qMB4";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
                              
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.problem_text+self.table_text+self.solution_text
        
        return self.explain
  
    def checkAnswer(self,template,answer,InputAnswer,CheckAnswerType):    
        if CheckAnswerType==1:
            try:
                return int(answer)==int(InputAnswer)
            except ValueError:
                return False
        elif CheckAnswerType==2:
            try:
                return float(answer)==float(InputAnswer)
            except ValueError:
                return False
        else:
            return False               
