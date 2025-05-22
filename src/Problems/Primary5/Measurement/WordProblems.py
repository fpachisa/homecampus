'''
Created on Dec 17, 2011

Module: WordProblems
Generates "Word Problems on Measurement" problems for Primary 5

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
from Problems import PersonName
from Utils import LcmGcf

class WordProblems:
    
    def __init__(self):
        pass
    
    def GenerateProblem(self,level):
        """ randomly decides which question to generate """
        #return self.GenerateProblemType7()
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''                                     
        self.ProblemType = {1:["ProblemType1a","ProblemType1b",],
                            2:["ProblemType2",],
                            3:["ProblemType3",],
                            4:["ProblemType4",],
                            5:["ProblemType5",],
                            }
        self.GenerateProblemType = {1:[self.GenerateProblemType1a(),self.GenerateProblemType1b(),],
                                    2:[self.GenerateProblemType2(),],
                                    3:[self.GenerateProblemType3(),],
                                    4:[self.GenerateProblemType4()],
                                    5:[self.GenerateProblemType5()],
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
        #return self.GenerateProblemType4()
        
    def GenerateTestProblem(self,problem_type):
        self.ProblemType = {"ProblemType1a":self.GenerateProblemType1a(),
                            "ProblemType1b":self.GenerateProblemType1b(),
                            "ProblemType2":self.GenerateProblemType2(),
                            "ProblemType3":self.GenerateProblemType3(),
                            "ProblemType4":self.GenerateProblemType4(),
                            "ProblemType5":self.GenerateProblemType5(),
                            }
        return self.ProblemType[problem_type]
                
    def GenerateProblemType1a(self):
        '''e.g.:Find the volume of the carriage of the truck below.'''
           
        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.PersonName)
        self.Dict = {1:['m','m<sup>3</sup>','Find the volume of the carriage of the truck whose dimensions are as given below:',
                        randint(150,250),randint(100,150),randint(50,80),],
                     }
        
        self.key = randint(1,len(self.Dict))
        self.unit = self.Dict[self.key][0]
        self.VolumeUnit = self.Dict[self.key][1]
        self.item1 = self.Dict[self.key][2]
       
        self.number1 = self.Dict[self.key][3]
        self.number2 = self.Dict[self.key][4]
        self.number3 = self.Dict[self.key][5]
        
        self.length = float(self.number1)/100
        self.breadth = float(self.number2)/100
        self.height = float(self.number3)/100
        
        self.problem = self.item1+"<br><br>"
        self.problem = self.problem + "length = "+str(self.length)+self.unit+"<br>"
        self.problem = self.problem + "breadth = "+str(self.breadth)+self.unit+"<br>"
        self.problem = self.problem + "height = "+str(self.height)+self.unit+"<br><br>"
        self.problem = self.problem + "(Round off your answer to two decimal places)"

        self.answer = round(float(self.length*self.breadth*self.height),2)
        
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.VolumeUnit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType1a",'CheckAnswerType':1,'grade':5,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.VolumeUnit
                }

    def ExplainType1(self,problem,answer,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<br><div> Watch below video for detailed explanation of similar problem using modal method<br>"
        VideoLink = '<object><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "5vU7lC9q9bo";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
               
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain
                
    def GenerateProblemType1b(self):
        '''e.g.:Which object has a larger volume - the carriage of the truck below or a cube with a length of 1.75 m?'''
           
        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.name = random.choice(PersonName.PersonName)
        self.Dict = {1:['m','m<sup>3</sup>','Which object has larger volume - the carriage of the truck whose dimensions are as given below or cube with a',
                        random.choice(['length','breadth','height']),'of',randint(150,250),randint(100,150),randint(50,80),randint(75,120)],
                     }
        
        self.key = randint(1,len(self.Dict))
        self.unit = self.Dict[self.key][0]
        self.VolumeUnit = self.Dict[self.key][1]
        self.item1 = self.Dict[self.key][2]
        self.item2 = self.Dict[self.key][3]
        self.item3 = self.Dict[self.key][4]
       
        self.number1 = self.Dict[self.key][5]
        self.number2 = self.Dict[self.key][6]
        self.number3 = self.Dict[self.key][7]
        self.number4 = self.Dict[self.key][8]
        
        '''Making sure the volume of carriage and cube is not same'''
        if self.number1*self.number2*self.number3 == self.number4*self.number4*self.number4:
            self.number4 = self.number4 + 10
            
        if self.number1*self.number2*self.number3 > self.number4*self.number4*self.number4:
            self.answer = "truck"
        else:
            self.answer = "cube"
        
        self.length = float(self.number1)/100
        self.breadth = float(self.number2)/100
        self.height = float(self.number3)/100
        self.cube = float(self.number4)/100

        self.problem = self.item1+" "+self.item2+" "+self.item3+" "+str(self.cube)+self.unit+"<br><br>"
        self.problem = self.problem + "length = "+str(self.length)+self.unit+"<br>"
        self.problem = self.problem + "breadth = "+str(self.breadth)+self.unit+"<br>"
        self.problem = self.problem + "height = "+str(self.height)+self.unit+"<br><br>"
       
        self.template = "MCQType2Choices.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1b(self.problem,self.answer)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType1b",'CheckAnswerType':2,'grade':5,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':"",'value1':"truck",
                'value2':"cube",'answer1':"truck carriage",'answer2':"cube"
                }

    def ExplainType1b(self,problem,answer):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text = "<br><div> Watch below video for detailed explanation of similar problem using modal method<br>"
        VideoLink = '<object><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "5vU7lC9q9bo";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
               
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType2(self):
        '''e.g.:A rectangular fresh juice dispenser measuring 18 cm by 30 cm by 24 cm is filled with juice to
                the brim. Bill fills cups with juice from the dispenser. If he fills 150 ml of juice into each cup,
                how many cups does he use? Round off your answer to the nearest whole number.'''
           
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.name = random.choice(PersonName.BoyName)
        self.Dict = {1:['cups','A rectangular fresh juice dispenser measuring','cm by','cm by','cm is filled with juice to the brim.',
                        'fills cups with juice from the dispenser. If he fills','ml of juice into each cup, how many cups does he use? (Round off your answer to the nearest whole number.)',
                        randint(15,30),randint(15,30),randint(15,30),random.randrange(100,200,10)],
                     }
        
        self.key = randint(1,len(self.Dict))
        self.unit = self.Dict[self.key][0]
        self.item1 = self.Dict[self.key][1]
        self.item2 = self.Dict[self.key][2]
        self.item3 = self.Dict[self.key][3]
        self.item4 = self.Dict[self.key][4]
        self.item5 = self.Dict[self.key][5]
        self.item6 = self.Dict[self.key][6]
       
        self.length = self.Dict[self.key][7]
        self.breadth = self.Dict[self.key][8]
        self.height = self.Dict[self.key][9]
        self.CupVolume = self.Dict[self.key][10]

        self.problem = self.item1+" "+str(self.length)+self.item2+" "+str(self.breadth)+self.item3+" "+str(self.height)+self.item4+"<br><br>"
        self.problem = self.problem + self.name+" "+self.item5+" "+str(self.CupVolume)+self.item6

        self.answer = int(round(float(self.length*self.breadth*self.height)/self.CupVolume,0))
        
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
        VideoLink = VideoLink + "DYQvkMM-zWY";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
               
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType3(self):
        '''e.g.:Jack empties 12 litres of water from a pail into a tank 51 cm long, 37 cm wide and 28 cm high
                that was already filled to a depth of 7 cm. How much more water is needed to completely fill the tank?
                Give your answer in litres.'''
           
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.name = random.choice(PersonName.PersonName)
        self.Dict = {1:['litres','millilitres','empties','litres of water from a pail into a tank','cm long,','cm wide and',
                        'cm high that was already filled to a depth of','cm. How much more water is needed to completely fill the tank? Give your answer in',
                        randint(45,65),randint(25,45),randint(25,45),randint(15,35),randint(5,15)],
                     }
        
        self.key = randint(1,len(self.Dict))
        self.unit1 = self.Dict[self.key][0]
        self.unit2 = self.Dict[self.key][1]
        self.item1 = self.Dict[self.key][2]
        self.item2 = self.Dict[self.key][3]
        self.item3 = self.Dict[self.key][4]
        self.item4 = self.Dict[self.key][5]
        self.item5 = self.Dict[self.key][6]
        self.item6 = self.Dict[self.key][7]
       
        self.length = self.Dict[self.key][8]
        self.breadth = self.Dict[self.key][9]
        self.height = self.Dict[self.key][10]
        self.FilledHeight = int(self.Dict[self.key][11]*self.height/100)
        self.emptied = self.Dict[self.key][12]

        self.unit = random.choice([self.unit1,self.unit2])
        self.problem = self.name+" "+self.item1+" "+str(self.emptied)+" "+self.item2+" "+str(self.length)+self.item3+" "+str(self.breadth)+self.item4+" "+str(self.height)+self.item5+" "+str(self.FilledHeight)+self.item6+" "+self.unit
        
        if self.unit == 'litres':
            self.answer = float(self.length*self.breadth*(self.height-self.FilledHeight))/1000 - float(self.emptied)
        else:
            self.answer = self.length*self.breadth*(self.height-self.FilledHeight) - self.emptied*1000
        
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType3",'CheckAnswerType':1,'grade':5,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit
                }

    def ExplainType3(self,problem,answer,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<br><div> Watch below video for detailed explanation of similar problem using modal method<br>"
        VideoLink = '<object><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "ePLNHx4ZnXo";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
               
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType4(self):
        '''e.g.:A rectangular container 12 cm long, 8 cm wide and 36 cm high was one-third full. When 
                some syrup from a bottle was poured into the container, it got half full. Find the volume
                of syrup poured from the bottle into the container in millilitres.'''
           
        self.complexity_level = "difficult"
        self.HCScore = 7
        
        self.Dict = {1:['ml','A rectangular container','cm long,','cm wide and','cm high was','full. When some syrup from a bottle was poured into the container, it got',
                        'full. Find the volume of syrup poured from the bottle into the container in millilitres. (Round off your answer to nearest whole number where applicable)',
                        randint(12,30),randint(12,30),randint(8,20)],
                     }
        
        self.key = randint(1,len(self.Dict))
        self.unit = self.Dict[self.key][0]
        self.item1 = self.Dict[self.key][1]
        self.item2 = self.Dict[self.key][2]
        self.item3 = self.Dict[self.key][3]
        self.item4 = self.Dict[self.key][4]
        self.item5 = self.Dict[self.key][5]
        self.item6 = self.Dict[self.key][6]
       
        self.length = self.Dict[self.key][7]
        self.breadth = self.Dict[self.key][8]
        self.height = self.Dict[self.key][9]
        
        self.InWords = {1:"one",2:"two",3:"three",4:"four",5:"five"}
        self.cardinal = {2:"half",3:"third",4:"fourth",5:"fifth",6:"sixth"}
        
        self.numerator1 = randint(1,5)
        self.denominator1 = randint(self.numerator1+1,6)

        self.numerator2 = randint(1,5)
        self.denominator2 = randint(self.numerator2+1,6)
        
        while float(self.numerator1)/self.denominator1 == float(self.numerator2)/self.denominator2:
            self.numerator2 = randint(1,5)
            self.denominator2 = randint(self.numerator2+1,6)

        gcf = LcmGcf.LcmGcf().find_gcf(self.numerator1, self.denominator1)

        '''Simplifying the fraction if possible'''
        self.SimpleNumerator1 = self.numerator1/gcf
        self.SimpleDenominator1 = self.denominator1/gcf

        gcf = LcmGcf.LcmGcf().find_gcf(self.numerator2, self.denominator2)

        '''Simplifying the fraction if possible'''
        self.SimpleNumerator2 = self.numerator2/gcf
        self.SimpleDenominator2 = self.denominator2/gcf
        
        if float(self.SimpleNumerator1)/self.SimpleDenominator1 < float(self.SimpleNumerator2)/self.SimpleDenominator2:
            self.problem = self.item1+" "+str(self.length)+self.item2+" "+str(self.breadth)+self.item3+" "+str(self.height)+self.item4+" "+self.InWords[self.SimpleNumerator1]+"-"+self.cardinal[self.SimpleDenominator1]+" "+self.item5
            self.problem = self.problem + " "+self.InWords[self.SimpleNumerator2]+"-"+self.cardinal[self.SimpleDenominator2]+" "+self.item6
        else:
            self.problem = self.item1+" "+str(self.length)+self.item2+" "+str(self.breadth)+self.item3+" "+str(self.height)+self.item4+" "+self.InWords[self.SimpleNumerator2]+"-"+self.cardinal[self.SimpleDenominator2]+" "+self.item5
            self.problem = self.problem + " "+self.InWords[self.SimpleNumerator1]+"-"+self.cardinal[self.SimpleDenominator1]+" "+self.item6

        self.answer = int(round(abs(self.length*self.breadth*self.height*(float(self.SimpleNumerator2)/self.SimpleDenominator2-float(self.SimpleNumerator1)/self.SimpleDenominator1)),0))

        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType4",'CheckAnswerType':1,'grade':5,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit
                }

    def ExplainType4(self,problem,answer,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<br><div> Watch below video for detailed explanation of similar problem using modal method<br>"
        VideoLink = '<object><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "mfGO3fy76VM";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
               
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType5(self):
        '''e.g.:376 cc of oil was poured from a tin into a bottle which had 224 ml of oil at first. If the bottle
                is now one-quarter full, what is the capacity of the bottle in litres?'''
           
        self.complexity_level = "difficult"
        self.HCScore = 7
        
        self.Dict = {1:['litres','ml','cc of oil was poured from a tin into a bottle which had','ml of oil at first. If the bottle is now',
                        'full, what is the capacity of the bottle in litres?',random.randrange(1050,2000,10)],
                     }
        
        self.key = randint(1,len(self.Dict))
        self.unit1 = self.Dict[self.key][0]
        self.unit2 = self.Dict[self.key][1]
        self.item1 = self.Dict[self.key][2]
        self.item2 = self.Dict[self.key][3]
        self.item3 = self.Dict[self.key][4]
      
        self.capacity = self.Dict[self.key][5]
        
        self.InWords = {1:"one",2:"two",3:"three",4:"four",5:"five"}
        self.cardinal = {2:"half",3:"third",4:"fourth",5:"fifth",6:"sixth"}
        
        self.numerator1 = randint(1,5)
        self.denominator1 = randint(self.numerator1+1,6)

        gcf = LcmGcf.LcmGcf().find_gcf(self.numerator1, self.denominator1)

        '''Simplifying the fraction if possible'''
        self.SimpleNumerator1 = self.numerator1/gcf
        self.SimpleDenominator1 = self.denominator1/gcf

        self.AfterFillVolume = self.capacity * self.SimpleNumerator1 / self.SimpleDenominator1
        self.BeforeFillVolume = randint(3,7) * self.AfterFillVolume / 10
        self.FillVolume = self.AfterFillVolume - self.BeforeFillVolume
        
        self.unit = random.choice([self.unit1,self.unit2])

        self.problem = str(self.FillVolume)+self.item1+" "+str(self.BeforeFillVolume)+self.item2
        self.problem = self.problem + " "+self.InWords[self.SimpleNumerator1]+"-"+self.cardinal[self.SimpleDenominator1]+" "+self.item3+"<br>"
        self.problem = self.problem
        if self.unit == 'litres':
            self.problem = self.problem + "(Round off your answer to two decimal places)" 
            self.answer = round(float(self.BeforeFillVolume+self.FillVolume)*self.SimpleDenominator1/(self.SimpleNumerator1*1000),2)
        elif self.unit == 'ml':
            self.problem = self.problem + "(Round off your answer to the nearest whole number)"
            self.answer = int(round(float(self.BeforeFillVolume+self.FillVolume)*self.SimpleDenominator1/(self.SimpleNumerator1),0))
        
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType5",'CheckAnswerType':1,'grade':5,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,'unit':self.unit
                }

    def ExplainType5(self,problem,answer,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<br><div> Watch below video for detailed explanation of similar problem using modal method<br>"
        VideoLink = '<object><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "QASGewkApD0";
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
                InputAnswer= string.join(InputAnswer.split(),"")
                return (str(answer)==str(InputAnswer))
            except ValueError:
                return False            