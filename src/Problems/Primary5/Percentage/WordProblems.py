'''
Created on Sep 14, 2011

Module: WordProblems
Generates "Word Problems on Percentage" problems for Primary 5

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
    
    def GenerateProblem(self):
        ''' first grouping the questions as per problem type in the ppt and then first randomly picking the problem type and then problem from the problem type'''
        ProblemList = [[self.GenerateProblemType1()],
                       [self.GenerateProblemType2()],
                       [self.GenerateProblemType3a(),self.GenerateProblemType3b()],
                       [self.GenerateProblemType4()],
                       [self.GenerateProblemType5()],
                       [self.GenerateProblemType6()],
                       [self.GenerateProblemType7a()],
                       [self.GenerateProblemType8()],
                       ]
        return random.choice(random.choice(ProblemList))
        #return self.GenerateProblemType2()
        
    def GenerateTestProblem(self,problem_type):
        self.ProblemType = {"ProblemType1":self.GenerateProblemType1(),
                            "ProblemType2":self.GenerateProblemType2(),
                            "ProblemType3a":self.GenerateProblemType3a(),
                            "ProblemType3b":self.GenerateProblemType3b(),
                            "ProblemType4":self.GenerateProblemType4(),
                            "ProblemType5":self.GenerateProblemType5(),
                            "ProblemType6":self.GenerateProblemType6(),
                            "ProblemType7a":self.GenerateProblemType7a(),
                            "ProblemType8":self.GenerateProblemType8(),
                            }
        return self.ProblemType[problem_type]
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:["ProblemType1",],
                            2:["ProblemType2",],
                            3:["ProblemType3a","ProblemType3b"],
                            4:["ProblemType4",],
                            5:["ProblemType5",],
                            6:["ProblemType6",],
                            7:["ProblemType7a",],
                            8:["ProblemType8",],
                            }
        self.GenerateProblemType = {1:[self.GenerateProblemType1(),],
                                    2:[self.GenerateProblemType2(),],
                                    3:[self.GenerateProblemType3a(),self.GenerateProblemType3b()],
                                    4:[self.GenerateProblemType4()],
                                    5:[self.GenerateProblemType5()],
                                    6:[self.GenerateProblemType6(),],
                                    7:[self.GenerateProblemType7a()],
                                    8:[self.GenerateProblemType8()],
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
        
    def GenerateProblemType1(self):
        '''e.g.:Mike is making lemonade using 1 part lemon juice to 4 parts water.
                What is the percentage of lemon juice in the lemonade?'''
           
        self.person1 = random.choice(PersonName.PersonName)
        self.Dict = {1:[self.person1,"is making lemonade using","parts lemon juice to","parts water.",
                        "What is the percentage of lemon juice in the lemonade?","(Round off to the nearest whole number)",
                        randint(4,10)],
                     }
        
        self.key = randint(1,len(self.Dict))
        self.name = self.Dict[self.key][0]
        self.item1 = self.Dict[self.key][1]
        self.item2 = self.Dict[self.key][2]
        self.item3 = self.Dict[self.key][3]
        self.item4 = self.Dict[self.key][4]
        self.item5 = self.Dict[self.key][5]
        self.number2 = self.Dict[self.key][6] 
        
        self.number1 = randint(2,self.number2-1)
        
        self.problem = self.name+" "+self.item1+" "+str(self.number1)+" "+self.item2+" "+str(self.number2)+" "+self.item3+"<br>"
        self.problem = self.problem + self.item4+"<br>"
        self.problem = self.problem + self.item5     
        
        self.answer = int(round(float(self.number1)*100/float(self.number1+self.number2),0))     
       
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,"%")
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":"","CheckAnswerType":2}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'dollar_unit':"",'unit':"%",
                'template':self.template,'explain':self.explain,'problem_type':"ProblemType1",
                'CheckAnswerType':2}

    def ExplainType1(self,problem,answer,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<br><div> Watch below video for detailed explanation of similar problem using modal method<br>"
        VideoLink = '<object><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "-TpSqEcAGHE";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
               
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain
        
    def GenerateProblemType2(self):
        '''e.g.:Jack donated 1/10th of his income to charity.
                What percentage of his income did he donate to charity?'''
           
        self.person1 = random.choice(PersonName.BoyName)
        self.Dict = {1:[self.person1,"donated","th of his income to charity.","What percentage of his income did he donate to charity?",
                        "(Round off to the nearest whole number)",randint(11,100)],
                     }
        
        self.key = randint(1,len(self.Dict))
        self.name = self.Dict[self.key][0]
        self.item1 = self.Dict[self.key][1]
        self.item2 = self.Dict[self.key][2]
        self.item3 = self.Dict[self.key][3]
        self.item4 = self.Dict[self.key][4]
        self.number2 = self.Dict[self.key][5] 
        
        self.number1 = randint(1,6)
        
        self.problem = "<table class='FractionsTable'>"
        self.problem = self.problem + "<tr><td>"+self.name+" "+self.item1+"&nbsp;</td>"       
        self.problem = self.problem + "<td align='center'><u>&nbsp;"+str(self.number1)+"&nbsp;&nbsp;</u><br>&nbsp;"+str(self.number2)+"</td>"
        self.problem = self.problem + "<td>"+self.item2+"</td></tr></table>"      
        self.problem = self.problem + self.item3+"<br>"
        self.problem = self.problem + self.item4     
        
        self.answer = int(round(float(self.number1)*100/float(self.number2),0))     
       
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,"%")
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":"","CheckAnswerType":2}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'dollar_unit':"",'unit':"%",
                'template':self.template,'explain':self.explain,'problem_type':"ProblemType2",
                'CheckAnswerType':2}

    def ExplainType2(self,problem,answer,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "<br><div> Watch below video for detailed explanation of similar problem using modal method<br>"
        VideoLink = '<object><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "o9VXMIgo8Q0";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
               
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain
        
    def GenerateProblemType3a(self):
        '''e.g.:Peter bought a laptop in the IT Show at 20% off.
                If the usual price of the laptop is $1200, what is the price of the laptop after discount?'''
           
        self.person1 = random.choice(PersonName.PersonName)
        self.Dict = {1:["$",self.person1,"bought a laptop in the IT show at","% off.",
                        "If the usual price of the laptop is $",",","what is the price of the laptop after discount?",
                        "(Round off to the nearest dollar)",randint(5,25),randint(500,2000)],
                     }
        
        self.key = randint(1,len(self.Dict))
        self.dollar = self.Dict[self.key][0]
        self.name = self.Dict[self.key][1]
        self.item1 = self.Dict[self.key][2]
        self.item2 = self.Dict[self.key][3]
        self.item3 = self.Dict[self.key][4]
        self.item4 = self.Dict[self.key][5]
        self.item5 = self.Dict[self.key][6]
        self.item6 = self.Dict[self.key][7]
        self.number1 = self.Dict[self.key][8]
        self.number2 = self.Dict[self.key][9] 
               
        self.problem = self.name+" "+self.item1+" "+str(self.number1)+self.item2+"<br>"
        self.problem = self.problem + self.item3+str(self.number2)+self.item4+"<br>"
        self.problem = self.problem + self.item5+"<br>"
        self.problem = self.problem + self.item6
                
        self.answer = int(round(float(100-self.number1)*float(self.number2)/100,0))     
       
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3a(self.problem,self.answer,self.dollar)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":"","CheckAnswerType":2}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'dollar_unit':self.dollar,'unit':"",
                'template':self.template,'explain':self.explain,'problem_type':"ProblemType3a",
                'CheckAnswerType':2}

    def ExplainType3a(self,problem,answer,dollar):
        self.answer_text = "<br>The correct answer is:<br>"+dollar+str(answer)
        self.solution_text = "<br><div> Watch below video for detailed explanation of similar problem using modal method<br>"
        VideoLink = '<object><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "XvsVuoFWXTY";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
               
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain
               
    def GenerateProblemType3b(self):
        '''e.g.:Peter bought a laptop in the IT Show at 20% off.
                If the usual price of the laptop is $1200, how much discount did he get on the laptop?'''
           
        self.person1 = random.choice(PersonName.BoyName)
        self.Dict = {1:["$",self.person1,"bought a laptop in the IT show at","% off.",
                        "If the usual price of the laptop is $",",","how much discount did he get on the laptop?",
                        "(Round off to the nearest dollar)",randint(5,25),randint(500,2000)],
                     }
        
        self.key = randint(1,len(self.Dict))
        self.dollar = self.Dict[self.key][0]
        self.name = self.Dict[self.key][1]
        self.item1 = self.Dict[self.key][2]
        self.item2 = self.Dict[self.key][3]
        self.item3 = self.Dict[self.key][4]
        self.item4 = self.Dict[self.key][5]
        self.item5 = self.Dict[self.key][6]
        self.item6 = self.Dict[self.key][7]
        self.number1 = self.Dict[self.key][8]
        self.number2 = self.Dict[self.key][9] 
               
        self.problem = self.name+" "+self.item1+" "+str(self.number1)+self.item2+"<br>"
        self.problem = self.problem + self.item3+str(self.number2)+self.item4+"<br>"
        self.problem = self.problem + self.item5+"<br>"
        self.problem = self.problem + self.item6
                
        self.answer = int(round(float(self.number1)*float(self.number2)/100,0))     
       
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3b(self.problem,self.answer,self.dollar)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":"","CheckAnswerType":2}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'dollar_unit':self.dollar,'unit':"",
                'template':self.template,'explain':self.explain,'problem_type':"ProblemType3b",
                'CheckAnswerType':2}

    def ExplainType3b(self,problem,answer,dollar):
        self.answer_text = "<br>The correct answer is:<br>"+dollar+str(answer)
        self.solution_text = "<br><div> Watch below video for detailed explanation of similar problem using modal method<br>"
        VideoLink = '<object><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "XvsVuoFWXTY";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
               
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain
               
    def GenerateProblemType4(self):
        '''e.g.:Lisa ordered dishes worth $30 at a restaurant.
                If the restaurant charged her a GST of 7% and a service charge of 10% on the order,
                how much did her total bill come out to be?
                (GST = goods and services tax)'''
           
        self.person1 = random.choice(PersonName.GirlName)
        self.Dict = {1:["$","",self.person1,"ordered dishes worth $","at a restaurant.",
                        "If the restaurant charged her a GST of","%","and a service charge of","% on the order,",
                        "how much did her total bill come out to be?","(GST = goods and services tax)",
                        randint(10,50),randint(3,10),randint(5,15)],
                     }
        
        self.key = randint(1,len(self.Dict))
        self.dollar = self.Dict[self.key][0]
        self.unit = self.Dict[self.key][1]
        self.name = self.Dict[self.key][2]
        self.item1 = self.Dict[self.key][3]
        self.item2 = self.Dict[self.key][4]
        self.item3 = self.Dict[self.key][5]
        self.item4 = self.Dict[self.key][6]
        self.item5 = self.Dict[self.key][7]
        self.item6 = self.Dict[self.key][8]
        self.item7 = self.Dict[self.key][9]
        self.item8 = self.Dict[self.key][10]
        self.number1 = self.Dict[self.key][11]
        self.number2 = self.Dict[self.key][12]
        self.number3 = self.Dict[self.key][13] 
               
        self.problem = self.name+" "+self.item1+str(self.number1)+" "+self.item2+"<br>"
        self.problem = self.problem + self.item3+" "+str(self.number2)+self.item4+"<br>"
        self.problem = self.problem + self.item5+" "+str(self.number3)+self.item6+"<br>"
        self.problem = self.problem + self.item7+"<br>"
        self.problem = self.problem + self.item8+"<br>"
                
        self.answer = float(100+(self.number2+self.number3))*float(self.number1)/100     
       
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,self.answer,self.dollar,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'dollar_unit':self.dollar,'unit':"",
                'template':self.template,'explain':self.explain,'problem_type':"ProblemType4",'CheckAnswerType':2}

    def ExplainType4(self,problem,answer,dollar,unit):
        self.answer_text = "<br>The correct answer is:<br>"+dollar+str(answer)+" "+unit
        self.solution_text = "<br><div> Watch below video for detailed explanation of similar problem using modal method<br>"
        VideoLink = '<object><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "yN0b-IJ3Gzg";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
               
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType5(self):
        '''e.g.:Jay took a personal loan of $12000 from a bank for a year at an annual interest rate of 16%.
                How much interest did he pay per month on the loan?'''
           
        self.person1 = random.choice(PersonName.BoyName)
        self.Dict = {1:["$","",self.person1,"took a personal loan of $","from a bank",
                        "for a year at an annual interest rate of","%.","How much interest did he pay per month on the loan?",
                        random.randrange(1000,15000,50),randint(2,15)],
                     }
        
        self.key = randint(1,len(self.Dict))
        self.dollar = self.Dict[self.key][0]
        self.unit = self.Dict[self.key][1]
        self.name = self.Dict[self.key][2]
        self.item1 = self.Dict[self.key][3]
        self.item2 = self.Dict[self.key][4]
        self.item3 = self.Dict[self.key][5]
        self.item4 = self.Dict[self.key][6]
        self.item5 = self.Dict[self.key][7]
        self.number1 = self.Dict[self.key][8]
        self.number2 = self.Dict[self.key][9]
               
        self.problem = self.name+" "+self.item1+str(self.number1)+" "+self.item2+"<br>"
        self.problem = self.problem + self.item3+" "+str(self.number2)+self.item4+"<br>"
        self.problem = self.problem + self.item5
                
        self.answer = round(float(self.number1*self.number2)/float(100*12),2)     
       
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5(self.problem,self.answer,self.dollar,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'dollar_unit':self.dollar,'unit':"",
                'template':self.template,'explain':self.explain,'problem_type':"ProblemType5",'CheckAnswerType':3}

    def ExplainType5(self,problem,answer,dollar,unit):
        self.answer_text = "<br>The correct answer is:<br>"+dollar+str(answer)+" "+unit
        self.solution_text = "<br><div> Watch below video for detailed explanation of similar problem using modal method<br>"
        VideoLink = '<object><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "yRR9zYkA4bw";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
               
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType6(self):
        '''e.g.:In a family relay race of 10 km, the father ran 35% of the distance, 
                the mother ran 35% of the distance, and each of the 2 children ran half of the remaining distance.
                What was the distance run by each child?'''
           
        self.person1 = random.choice(PersonName.BoyName)
        self.Dict = {1:["","km","In a family relay race of","km, the father ran","% of the distance,","the mother ran",
                        "% of the distance,","and each of the 2 children ran half of the remaining distance.",
                        "What was the distance run by each child?",randint(5,20),randint(20,40),randint(20,40)],
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
        self.number1 = self.Dict[self.key][9]
        self.number2 = self.Dict[self.key][10]
        self.number3 = self.Dict[self.key][11]
               
        self.problem = self.item1+" "+str(self.number1)+" "+self.item2+" "+str(self.number2)+self.item3+"<br>"
        self.problem = self.problem + self.item4+" "+str(self.number3)+self.item5+"<br>"
        self.problem = self.problem + self.item6+"<br>"
        self.problem = self.problem + self.item7
                
        self.answer = float(100-self.number2-self.number3)*float(self.number1)/200     
       
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6(self.problem,self.answer,self.dollar,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'dollar_unit':self.dollar,'unit':self.unit,
                'template':self.template,'explain':self.explain,'problem_type':"ProblemType6",'CheckAnswerType':2}

    def ExplainType6(self,problem,answer,dollar,unit):
        self.answer_text = "<br>The correct answer is:<br>"+dollar+str(answer)+" "+unit
        self.solution_text = "<br><div> Watch below video for detailed explanation of similar problem using modal method<br>"
        VideoLink = '<object><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "qk2v0o2IydM";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
               
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType7a(self):
        '''e.g.:An amusement park received 4800 visitors over a weekend.
                If 60% of the visitors came on Saturday,
                how many visitors came on Sunday?'''
           
        self.person1 = random.choice(PersonName.BoyName)
        self.Dict = {1:["","","An amusement park received","visitors over a weekend.","If",
                        "% of the visitors came on Saturday,","how many visitors came on Sunday?",
                        "(Round off to the nearest whole number)",randint(500,5000),randint(25,60)],
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
        self.number1 = self.Dict[self.key][8]
        self.number2 = self.Dict[self.key][9]
               
        self.problem = self.item1+" "+str(self.number1)+" "+self.item2+"<br>"
        self.problem = self.problem + self.item3+" "+str(self.number2)+self.item4+"<br>"
        self.problem = self.problem + self.item5+"<br>"
        self.problem = self.problem + self.item6
                
        self.answer = int(round(float(100-self.number2)*float(self.number1)/100,0))     
       
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7a(self.problem,self.answer,self.dollar,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'dollar_unit':self.dollar,'unit':self.unit,
                'template':self.template,'explain':self.explain,'problem_type':"ProblemType7a",'CheckAnswerType':2}

    def ExplainType7a(self,problem,answer,dollar,unit):
        self.answer_text = "<br>The correct answer is:<br>"+dollar+str(answer)+" "+unit
        self.solution_text = "<br><div> Watch below video for detailed explanation of similar problem using modal method<br>"
        VideoLink = '<object><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "5IULuG7Gp3U";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
               
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain

    def GenerateProblemType8(self):
        '''e.g.:Nina earns a monthly salary of $3700.
                She spends 35% of it on housing, 20% on food and 30% on other expenses.
                If she saves the rest, how much money does she save?'''
           
        self.person1 = random.choice(PersonName.GirlName)
        self.Dict = {1:["$","",self.person1,"earns a monthly salary of $",".","She spends","% of it on housing,",
                        "% on food and","% on other expenses.","If she saves the rest, how much money does she save?",
                        random.randrange(2000,10000,50),randint(15,35),randint(10,20),randint(20,40)],
                     }
        
        self.key = randint(1,len(self.Dict))
        self.dollar = self.Dict[self.key][0]
        self.unit = self.Dict[self.key][1]
        self.person1 = self.Dict[self.key][2]
        self.item1 = self.Dict[self.key][3]
        self.item2 = self.Dict[self.key][4]
        self.item3 = self.Dict[self.key][5]
        self.item4 = self.Dict[self.key][6]
        self.item5 = self.Dict[self.key][7]
        self.item6 = self.Dict[self.key][8]
        self.item7 = self.Dict[self.key][9]
        self.number1 = self.Dict[self.key][10]
        self.number2 = self.Dict[self.key][11]
        self.number3 = self.Dict[self.key][12]
        self.number4 = self.Dict[self.key][13]
               
        self.problem = self.person1 +" "+self.item1+str(self.number1)+self.item2+"<br>"
        self.problem = self.problem + self.item3+" "+str(self.number2)+self.item4+"<br>"
        self.problem = self.problem + str(self.number3)+self.item5+" "+str(self.number4)+self.item6+"<br>"
        self.problem = self.problem + self.item7
                
        self.answer = float(100-self.number2-self.number3-self.number4)*float(self.number1)/100     
       
        self.template = "EnterTypeProblems.html"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType8(self.problem,self.answer,self.dollar,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''

        return {'problem':self.problem,'answer':self.answer,'dollar_unit':self.dollar,'unit':self.unit,
                'template':self.template,'explain':self.explain,'problem_type':"ProblemType8",'CheckAnswerType':2}

    def ExplainType8(self,problem,answer,dollar,unit):
        self.answer_text = "<br>The correct answer is:<br>"+dollar+str(answer)+" "+unit
        self.solution_text = "<br><div> Watch below video for detailed explanation of similar problem using modal method<br>"
        VideoLink = '<object><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always">';
        VideoLink = VideoLink + '<embed src="https://www.youtube.com/v/';
        VideoLink = VideoLink + "vX3VBd_QZZs";
        VideoLink = VideoLink + '?version=3&rel=0&showinfo=0&iv_load_policy=3&feature=player_embedded" type="application/x-shockwave-flash" allowfullscreen="true" allowScriptAccess="always" width="380" height="242"></object>';
        self.solution_text = self.solution_text + VideoLink + "</div>"
               
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
        
        return self.explain
                                
    def checkAnswer(self,template,answer,InputAnswer,CheckAnswerType):
        
        if CheckAnswerType == 1:
            try:
                return (int(answer)==int(InputAnswer))
            except ValueError:
                return False
        elif CheckAnswerType == 2:
            try:
                return (float(answer)==float(InputAnswer))
            except ValueError:
                return False
        elif CheckAnswerType == 3:
            try:
                return (round(float(answer),2)==round(float(InputAnswer),2))
            except ValueError:
                return False                 