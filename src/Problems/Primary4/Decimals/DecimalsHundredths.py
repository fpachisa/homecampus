'''
Created on Feb 23, 2012
Module: DecimalsHundredths
Generates the "Notation and Place Values -- Hundredths" problems for Primary 4

Version: 1.0

Author:
   Farhat Pachisa (farhat@homecampus.com.sg)
   
Copyright:
    Copyright (c) 2012, Home Campus.  All Rights Reserved.

Usage:
  

History:
  
'''
import random
from random import randint

class DecimalsHundredths:
    
    def __init__(self):
        pass
    
    def GenerateProblem(self):
        """ randomly decides which question to generate """
        #return self.GenerateProblemTypeMCQ8()           
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:["ProblemType1",],
                            2:["ProblemType2",],
                            3:["ProblemType3",],
                            4:["ProblemType6",],
                            5:["ProblemType5",],
                            6:["ProblemType4",],
                            7:["ProblemType7",],
                            8:["ProblemType11",],
                            9:["ProblemType9",],
                            10:["ProblemType8",],
                            11:["ProblemType14",],
                            12:["ProblemType12",],
                            13:["ProblemType13",],
                            14:["ProblemType10",],
                            }
        self.GenerateProblemType = {1:[self.GenerateProblemType1(),],
                                    2:[self.GenerateProblemType2(),],
                                    3:[self.GenerateProblemType3(),],
                                    4:[self.GenerateProblemType6(),],
                                    5:[self.GenerateProblemType5(),],
                                    6:[self.GenerateProblemType4(),],
                                    7:[self.GenerateProblemType7(),],
                                    8:[self.GenerateProblemType11(),],
                                    9:[self.GenerateProblemType9(),],
                                    10:[self.GenerateProblemType8(),],
                                    11:[self.GenerateProblemType14(),],
                                    12:[self.GenerateProblemType12(),],
                                    13:[self.GenerateProblemType13(),],
                                    14:[self.GenerateProblemType10(),],
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
        #return self.GenerateProblemType14()

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
                            }
        return self.ProblemType[problem_type]
        
    def GenerateProblemType1(self):
        '''e.g.:
        Express in decimals'''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.number = randint(2,99)        
        self.problem = "Express in decimals<br>"        
        self.problem = str(self.number)+" hundredths ="
                
        self.template = "EnterTypeProblems.html"
        
        self.answer = float(self.number)/100

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.number)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType1",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}            

    def ExplainType1(self,problem,answer,number):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text =  "<b><u>Problem</b></u>:<br/>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br/>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"
        self.solution_text = self.solution_text + "1 hundredth when expressed as decimal is 0.01<br><br>"
        self.solution_text = self.solution_text + str(number)+" hundredths can be expressed as "+str(answer)+"<br><br>"        
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
        
    def GenerateProblemType2(self):
        '''e.g.:
        Express in decimals'''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.number = randint(2,99)        
        self.problem = "Express in decimals<br>"
        self.problem = self.problem + "<table id='fractionTable' class='FractionsTable'><tr>"
        self.problem = self.problem + "<td align='center'><u>&nbsp;&nbsp;"+str(self.number)+"&nbsp;&nbsp;</u><br>&nbsp;"+str(100)+"</td>"
        self.problem = self.problem + "<td>&nbsp;=&nbsp;</td>"
        self.problem = self.problem + "</tr></table>"
        
        self.template = "EnterTypeProblems.html"
        
        self.answer = float(self.number)/100

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.number)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType2",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}            

    def ExplainType2(self,problem,answer,number):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text = "<b><u>Problem</b></u>:<br/>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br>"
        self.solution_text = self.solution_text + "<table id='fractionTable' class='FractionsTable'><tr>"
        self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;&nbsp;"+str(self.number)+"&nbsp;&nbsp;</u><br>&nbsp;"+str(100)+"</td>"
        self.solution_text = self.solution_text + "<td>&nbsp;=&nbsp;"+str(number)+" hundredths</td>"
        self.solution_text = self.solution_text + "</tr></table>"
        self.solution_text = self.solution_text + "<br>1 hundredth = 0.01<br><br>"
        self.solution_text = self.solution_text + str(number)+" hundredths can be expressed as "+str(answer)+"<br><br>"        
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
        
    def GenerateProblemType3(self):
        '''e.g.:
        Express in decimals'''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.number = randint(111,999)        
        self.problem = "Express in decimals<br><br>"
        self.problem = self.problem + "<table id='fractionTable' class='FractionsTable'><tr>"
        self.problem = self.problem + "<td align='center'><u>&nbsp;"+str(self.number)+"&nbsp;</u><br>&nbsp;"+str(100)+"</td>"
        self.problem = self.problem + "<td>&nbsp;=&nbsp;</td>"
        self.problem = self.problem + "</tr></table>"
        
        self.template = "EnterTypeProblems.html"
        
        self.answer = float(self.number)/100

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,self.answer,self.number)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType3",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}            

    def ExplainType3(self,problem,answer,number):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text = "<b><u>Problem</b></u>:<br/>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br>"
        self.solution_text = self.solution_text + "<table id='fractionTable' class='FractionsTable'><tr>"
        self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(self.number)+"&nbsp;&nbsp;</u><br>&nbsp;"+str(100)+"</td>"
        self.solution_text = self.solution_text + "<td>&nbsp;=&nbsp;"+str(number)+" hundredths</td>"
        self.solution_text = self.solution_text + "</tr></table>"
        self.solution_text = self.solution_text + "<br>100 hundredths = 1 one<br><br>"
        div,mod = divmod(number,100)
        if mod>1:
            hundredth = "hundredths"
            if div>1:
                self.solution_text = self.solution_text + str(number)+" hundredths = "+str(div)+" ones + "+str(mod)+" hundredths<br><br>"
                ones = "ones"
            else:
                self.solution_text = self.solution_text + str(number)+" hundredths = "+str(div)+" one + "+str(mod)+" hundredths<br><br>"
                ones = "one"
        else:
            hundredth = "hundredth"
            if div>1:
                self.solution_text = self.solution_text + str(number)+" hundredths = "+str(div)+" ones + "+str(mod)+" hundredth<br><br>"
                ones = "ones"
            else:
                self.solution_text = self.solution_text + str(number)+" hundredths = "+str(div)+" one + "+str(mod)+" hundredth<br><br>"
                ones = "one"
        self.solution_text = self.solution_text + "<table id='fractionTable' class='FractionsTable'><tr>"
        self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;"+str(self.number)+"&nbsp;&nbsp;</u><br>&nbsp;"+str(100)+"</td>"
        self.solution_text = self.solution_text + "<td>&nbsp;=&nbsp;"+str(div)+" "+ones+" "+str(mod)+" "+hundredth+"</td>"
        self.solution_text = self.solution_text + "</tr></table><br>"
        self.solution_text = self.solution_text + " = "+str(answer)
        
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
        
    def GenerateProblemType4(self):
        '''e.g.:
        Express in decimals'''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.whole = randint(1,9)
        self.number = randint(12,99)        
        self.problem = "Express in decimals<br><br>"
        self.problem = self.problem + "<table id='fractionTable' class='FractionsTable'><tr>"
        self.problem = self.problem + "<td>"+str(self.whole)+"&nbsp;</td>"
        self.problem = self.problem + "<td align='center'><u>&nbsp;&nbsp;"+str(self.number)+"&nbsp;&nbsp;</u><br>&nbsp;"+str(100)+"</td>"
        self.problem = self.problem + "<td>&nbsp;=&nbsp;</td>"
        self.problem = self.problem + "</tr></table>"
        
        self.template = "EnterTypeProblems.html"
        
        self.answer = float(self.whole) + float(self.number)/100

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,self.answer,self.whole,self.number)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType4",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}            

    def ExplainType4(self,problem,answer,whole,number):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text = "<b><u>Problem</b></u>:<br/>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br>"
        self.solution_text = self.solution_text + "<table id='fractionTable' class='FractionsTable'><tr>"
        self.solution_text = self.solution_text + "<td>"+str(whole)+"&nbsp;</td>"
        self.solution_text = self.solution_text + "<td align='center'><u>&nbsp;&nbsp;"+str(number)+"&nbsp;&nbsp;</u><br>&nbsp;"+str(100)+"</td>"
        if whole > 1:
            self.solution_text = self.solution_text + "<td>&nbsp;=&nbsp;"+str(whole)+" ones "+str(number)+" hundredths</td>"
        else:
            self.solution_text = self.solution_text + "<td>&nbsp;=&nbsp;"+str(whole)+" one "+str(number)+" hundredths</td>"
        self.solution_text = self.solution_text + "</tr></table>"
        self.solution_text = self.solution_text + "<br> = "+str(answer)
       
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
        
    def GenerateProblemType5(self):
        '''e.g.:
        Express in decimals'''
        
        self.complexity_level = "easy"
        self.HCScore = 3
        
        self.number1 = randint(2,9)
        self.number2 = randint(2,9)        
        self.problem = "Express as decimal:<br><br>"
        self.problem = self.problem + str(self.number1)+" tenths "+str(self.number2)+" hundredths = "
        
        self.template = "EnterTypeProblems.html"
        
        self.answer = float(self.number1)/10+float(self.number2)/100

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5(self.problem,self.answer,self.number1,self.number2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType5",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":1}            

    def ExplainType5(self,problem,answer,number1,number2):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text = "<b><u>Problem</b></u>:<br/>"
        self.solution_text = self.solution_text + "<i>"+problem+"</i><br/><br>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"
        self.solution_text = self.solution_text + "1 tenth = 0.1<br><br>"
        self.solution_text = self.solution_text + "1 hundredth = 0.01<br><br>"
        self.solution_text = self.solution_text + "So, "+str(number1)+" tenths = "+str(float(number1)/10)+" &nbsp;&nbsp; "+str(number2)+" hundredths = "+str(float(number2)/100)+"<br><br>"
        self.solution_text = self.solution_text + "When combined together the decimal expression can be written as: <i><b>"+str(answer)+"</b></i>"
       
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
        
    def GenerateProblemType6(self):
        '''e.g.:
        Express in decimals'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.number1 = str(randint(2,9))
        self.number2 = str(randint(2,9))
        self.number3 = str(randint(2,9))
        self.number4 = str(randint(2,9))        
        
        self.problem = "Find the missing number:<br><br>"
        self.problem = self.problem + self.number1+self.number2+"."+self.number3+self.number4+" = "+self.number1+" tens "+self.number2+" ones "+self.number3+" tenths"+" ___ hundredths"
        
        self.template = "EnterTypeProblems.html"
        
        self.answer = self.number4

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6(self.problem,self.answer,self.number1,self.number2,self.number3,self.number4)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType6",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2}            

    def ExplainType6(self,problem,answer,number1,number2,number3,number4):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text = "<b><u>Problem</b></u>:<br/>"
        self.solution_text = self.solution_text + "<i>"+problem+"</i><br/><br>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"
        self.solution_text = self.solution_text + "Fill the below place value table with the given number<br><br>"
        self.solution_text = self.solution_text + "<table id='explanation' border=1><tr>"
        self.solution_text = self.solution_text + "<td>Tens</td><td>Ones</td><td>Tenths</td><td>Hundredths</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>"+number1+"</td><td>"+number2+"</td><td>"+number3+"</td><td>"+number4+"</td></tr></table>"
        self.solution_text = self.solution_text + "<br>Hence the missing number is: "+str(answer)
       
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
        
    def GenerateProblemType7(self):
        '''e.g.:
        Express in decimals'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.number1 = str(randint(2,9))
        self.number2 = str(randint(2,9))
        self.number3 = str(randint(2,9))
        self.number4 = str(randint(2,9))
        
        self.problem = "Find the missing number:<br><br>"
        self.problem = self.problem + self.number1+self.number2+"."+self.number3+self.number4+" = "+self.number1+" tens "+self.number2+" ones  ____ tenths "+self.number4+" hundredths"
        
        self.template = "EnterTypeProblems.html"
        
        self.answer = self.number3

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        '''Using the same explanation as Problem 6'''
        self.explain_text = self.ExplainType6(self.problem,self.answer,self.number1,self.number2,self.number3,self.number4)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType7",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2}            

    def GenerateProblemType8(self):
        '''e.g.:
        Express in decimals'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.number1 = str(randint(2,9))
        self.number2 = str(randint(2,9))
        self.number3 = str(randint(2,9))
        self.number4 = str(randint(2,9))
        
        self.problem = "Find the missing number:<br><br>"
        self.problem = self.problem + self.number1+self.number2+"."+self.number3+self.number4+" = ____ tens "+self.number2+" ones "+self.number3+" tenths "+self.number4+" hundredths"
        
        self.template = "EnterTypeProblems.html"
        
        self.answer = self.number1

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        '''Using the same explanation as Problem 6'''
        self.explain_text = self.ExplainType6(self.problem,self.answer,self.number1,self.number2,self.number3,self.number4)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType8",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2}

    def GenerateProblemType9(self):
        '''e.g.:
        Find the value of the digit 5 in 67.45'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.numbers = random.sample([1,2,3,4,5,6,7,8,9],4)
        self.number1 = str(self.numbers[0])
        self.number2 = str(self.numbers[1])
        self.number3 = str(self.numbers[2])      
        self.number4 = str(self.numbers[3])
        
        self.problem = "What is the value of digit "+self.number1+" in "+self.number1+self.number2+"."+self.number3+self.number4
        self.flag = 1
        
        self.template = "EnterTypeProblems.html"
        
        self.answer = int(self.number1) * 10

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType9(self.problem,self.answer,self.number1,self.number2,self.number3,self.number4,self.flag)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType9",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":3}

    def ExplainType9(self,problem,answer,number1,number2,number3,number4,flag):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text = "<b><u>Problem</b></u>:<br/>"
        self.solution_text = self.solution_text + "<i>"+problem+"</i><br/><br>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"
        self.solution_text = self.solution_text + "Fill the below place value table with the given number<br><br>"
        self.solution_text = self.solution_text + "<table id='explanation' border=1><tr>"
        self.solution_text = self.solution_text + "<td>Tens</td><td>Ones</td><td>Tenths</td><td>Hundredths</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>"+number1+"</td><td>"+number2+"</td><td>"+number3+"</td><td>"+number4+"</td></tr></table>"
        if flag ==1:
            self.solution_text = self.solution_text + "<br>Since the digit is in the tens place multiply it by 10 to get its value.<br><br>"
            self.solution_text = self.solution_text + number1+" &times 10 = "+str(answer)+"<br>"
            self.solution_text = self.solution_text + "<br>Hence the value of "+number1+" in "+number1+number2+"."+number3+number4+" is: "+str(answer)
        elif flag ==2:
            self.solution_text = self.solution_text + "<br>Since the digit is in the hundredths place divide it by 100 to get its value.<br><br>"
            self.solution_text = self.solution_text + number4+" &divide 100 = "+str(answer)+"<br>"
            self.solution_text = self.solution_text + "<br>Hence the value of "+number4+" in "+number1+number2+"."+number3+number4+" is: "+str(answer)
        elif flag ==3:
            self.solution_text = self.solution_text + "<br>Since the digit is in the tenths place divide it by 10 to get its value.<br><br>"
            self.solution_text = self.solution_text + number3+" &divide 10 = "+str(answer)+"<br>"
            self.solution_text = self.solution_text + "<br>Hence the value of "+number3+" in "+number1+number2+"."+number3+number4+" is: "+str(answer)
       
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType10(self):
        '''e.g.:
        Find the value of the digit 5 in 67.5'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.numbers = random.sample([1,2,3,4,5,6,7,8,9],4)
        self.number1 = str(self.numbers[0])
        self.number2 = str(self.numbers[1])
        self.number3 = str(self.numbers[2])       
        self.number4 = str(self.numbers[3])
        
        self.problem = "What is the value of digit "+self.number4+" in "+self.number1+self.number2+"."+self.number3+self.number4
        self.flag = 2
        
        self.template = "EnterTypeProblems.html"
        
        self.answer = float(self.number4) / 100

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType9(self.problem,self.answer,self.number1,self.number2,self.number3,self.number4,self.flag)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType10",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":3}

    def GenerateProblemType11(self):
        '''e.g.:
        Find the value of the digit 5 in 67.5'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.numbers = random.sample([1,2,3,4,5,6,7,8,9],4)
        self.number1 = str(self.numbers[0])
        self.number2 = str(self.numbers[1])
        self.number3 = str(self.numbers[2])
        self.number4 = str(self.numbers[3])       
        
        self.problem = "What is the value of digit "+self.number3+" in "+self.number1+self.number2+"."+self.number3+self.number4
        self.flag = 3
        
        self.template = "EnterTypeProblems.html"
        
        self.answer = float(self.number3) / 10

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType9(self.problem,self.answer,self.number1,self.number2,self.number3,self.number4,self.flag)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType11",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":3}

    def GenerateProblemType12(self):
        '''e.g.:
        Find the value of the digit 5 in 67.5'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.numbers = random.sample([1,2,3,4,5,6,7,8,9],4)
        self.number1 = str(self.numbers[0])
        self.number2 = str(self.numbers[1])
        self.number3 = str(self.numbers[2])
        self.number4 = str(self.numbers[3])
        
        self.problem = "Which digit is in the tens place in "+self.number1+self.number2+"."+self.number3+self.number4
        self.flag = 1
        
        self.template = "EnterTypeProblems.html"
        
        self.answer = self.number1

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType12(self.problem,self.answer,self.number1,self.number2,self.number3,self.number4,self.flag)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType12",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2}

    def ExplainType12(self,problem,answer,number1,number2,number3,number4,flag):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)
        self.solution_text = "<b><u>Problem</b></u>:<br/>"
        self.solution_text = self.solution_text + "<i>"+problem+"</i><br/><br>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br><br>"
        self.solution_text = self.solution_text + "Fill the below place value table with the given number<br><br>"
        self.solution_text = self.solution_text + "<table id='explanation' border=1><tr>"
        self.solution_text = self.solution_text + "<td>Tens</td><td>Ones</td><td>Tenths</td><td>Hundredths</td></tr>"
        self.solution_text = self.solution_text + "<tr><td>"+number1+"</td><td>"+number2+"</td><td>"+number3+"</td><td>"+number4+"</td></tr></table>"
        if flag ==1:
            self.solution_text = self.solution_text + "<br>Hence the digit in the tens place is: "+str(answer)
        elif flag ==2:
            self.solution_text = self.solution_text + "<br>Hence the digit in the hundredths place is: "+str(answer)
        elif flag ==3:
            self.solution_text = self.solution_text + "<br>Hence the digit in the tenths place is: "+str(answer)
       
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemType13(self):
        '''e.g.:
        Find the value of the digit 5 in 67.5'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.numbers = random.sample([1,2,3,4,5,6,7,8,9],4)
        self.number1 = str(self.numbers[0])
        self.number2 = str(self.numbers[1])
        self.number3 = str(self.numbers[2])
        self.number4 = str(self.numbers[3])
        
        self.problem = "Which digit is in the hundredths place in "+self.number1+self.number2+"."+self.number3+self.number4
        self.flag = 2
        
        self.template = "EnterTypeProblems.html"
        
        self.answer = self.number4

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType12(self.problem,self.answer,self.number1,self.number2,self.number3,self.number4,self.flag)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType13",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2}

    def GenerateProblemType14(self):
        '''e.g.:
        Find the value of the digit 5 in 67.5'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.numbers = random.sample([1,2,3,4,5,6,7,8,9],4)
        self.number1 = str(self.numbers[0])
        self.number2 = str(self.numbers[1])
        self.number3 = str(self.numbers[2])
        self.number4 = str(self.numbers[3])
        
        self.problem = "Which digit is in the tenths place in "+self.number1+self.number2+"."+self.number3+self.number4
        self.flag = 3
        
        self.template = "EnterTypeProblems.html"
        
        self.answer = self.number3

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType12(self.problem,self.answer,self.number1,self.number2,self.number3,self.number4,self.flag)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType14",
                'grade':4,"complexity_level":self.complexity_level,"HCScore":self.HCScore,"CheckAnswerType":2}

    def checkAnswer(self,template,answer,InputAnswer,CheckAnswer):
        if CheckAnswer==1:
            try:
                return (float(answer)==float(InputAnswer))
            except ValueError:
                return False                           
        elif CheckAnswer==2:
            try:
                return (int(answer)==int(InputAnswer))
            except ValueError:
                return False                           
        elif CheckAnswer==3:
            if "/" in str(InputAnswer):
                try:
                    InputNumerator = int(str(InputAnswer).partition("/")[0])
                    InputDenominator = int(str(InputAnswer).partition("/")[2])
                    return (float(answer)==float(InputNumerator)/float(InputDenominator))
                except ValueError:
                    return False
            else:
                try:
                    return (float(answer)==float(InputAnswer))
                except ValueError:
                    return False                           
    