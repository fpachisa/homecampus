'''
Created on Jan 19, 2011

Module: OrderOfOperation
Generates "Order Of Operation" problems for Primary 5

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

class OrderOfOperation:
    
    def __init__(self):
        pass
    
    def GenerateProblem(self):
        """ randomly decides which question to generate """
        random = randint(1,3)
        if random==1:
            if randint(1,2)==1:
                return self.GenerateProblemType1()
            else:
                return self.GenerateProblemTypeMCQ1()
        elif random==2:
            if randint(1,2)==1:
                return self.GenerateProblemType2()
            else:
                return self.GenerateProblemTypeMCQ2()
        else:
            if randint(1,2)==1:
                return self.GenerateProblemType3()
            else:
                return self.GenerateProblemTypeMCQ3()
        #return self.GenerateProblemTypeMCQ3()
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:"ProblemType1",2:"ProblemTypeMCQ2",3:"ProblemType3",
                            4:"ProblemTypeMCQ1",5:"ProblemType2",6:"ProblemTypeMCQ3",}
        self.GenerateProblemType = {1:self.GenerateProblemType1(),2:self.GenerateProblemTypeMCQ2(),3:self.GenerateProblemType3(),
                                    4:self.GenerateProblemTypeMCQ1(),5:self.GenerateProblemType2(),6:self.GenerateProblemTypeMCQ3()}
        
        if not LastProblemID:
            LastProblemID = 0
        
        if LastProblemID == 0:
            return random.choice(self.GenerateProblemType.values())
        else:
            if LastProblemID in self.ProblemType.values():
                CurrentProblemKey = [k for k, v in self.ProblemType.iteritems() if v == LastProblemID][0]
                if CurrentProblemKey == max(self.ProblemType.keys()):
                    NextProblemKey = min(self.ProblemType.keys())
                else:
                    NextProblemKey = CurrentProblemKey + 1 
                return self.GenerateProblemType[NextProblemKey]
            else:
                return random.choice(self.GenerateProblemType.values())
        #return self.GenerateProblemType1()
        
    def GenerateTestProblem(self,problem_type):
        self.ProblemType = {"ProblemType1":self.GenerateProblemType1(),
                            "ProblemTypeMCQ1":self.GenerateProblemTypeMCQ1(),
                            "ProblemType2":self.GenerateProblemType2(),
                            "ProblemTypeMCQ2":self.GenerateProblemTypeMCQ2(),
                            "ProblemType3":self.GenerateProblemType3(),
                            "ProblemTypeMCQ3":self.GenerateProblemTypeMCQ3(),
                            }
        return self.ProblemType[problem_type]

    def GenerateProblemType1(self):
        '''e.g.:
        Find the value:
        25 +53 +56'''
        
        '''For addition use numbers between 2 & 99 but for multiplication use between 2 & 9'''
        self.number1 = randint(2,99)
        self.number2 = randint(2,99)
        self.number3 = randint(2,99)
        self.number4 = randint(2,9)
        self.number5 = randint(2,9)
        self.number6 = randint(2,9)
        self.number7 = randint(2,9)
        
        randomSelect = randint(1,6)
        
        if randomSelect==1:
            self.problem = r"Find the value:<br>%d + %d + %d" %(self.number1,self.number2,self.number3)
            self.answer = self.number1+self.number2+self.number3
            self.flag = 1
        elif randomSelect==2:
            self.problem = r"Find the value:<br>%d &times; %d &times; %d" %(self.number4,self.number5,self.number6)
            self.answer = self.number4*self.number5*self.number6
            self.flag = 2
        elif randomSelect==3:
            self.problem = r"Find the value:<br>%d + %d &times; %d" %(self.number1,self.number4,self.number5)
            self.answer = self.number1+self.number4*self.number5
            self.flag = 3
        elif randomSelect==4:
            self.problem = r"Find the value:<br>%d &times; %d + %d" %(self.number4,self.number5,self.number1)
            self.answer = self.number4*self.number5+self.number1
            self.flag = 4
        elif randomSelect==5:
            self.problem = r"Find the value:<br>%d &times; %d + %d &times; %d" %(self.number4,self.number5,self.number6,self.number7)
            self.answer = self.number4*self.number5+self.number6*self.number7
            self.flag = 5            
        elif randomSelect==6:
            self.problem = r"Find the value:<br>%d &times; (%d + %d) &times; %d" %(self.number4,self.number5,self.number6,self.number7)
            self.answer = self.number4*(self.number5+self.number6)*self.number7
            self.flag = 6         
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,str(self.answer),self.number1,self.number2,self.number3,self.number4,self.number5,self.number6,self.number7,self.flag)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType1"}

    def ExplainType1(self,problem,answer,number1,number2,number3,number4,number5,number6,number7,flag):
        self.answer_text = "<br>The correct answer is:<br>"+answer
        self.solution_text =  "<b><u>Problem</b></u>:<br/>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br/>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br/>"
        self.solution_text = self.solution_text + "Follow these 3 simple rules to get any question on order of operations right:<br><br>"
        self.solution_text = self.solution_text + "Rule 1: Do the operations in brackets.<br>"
        self.solution_text = self.solution_text + "Rule 2: Multiply and/or divide from left to right.<br>"
        self.solution_text = self.solution_text + "Rule 3: Add and/or subtract from left to right.<br><br>"
        if flag == 1:
            self.solution_text = self.solution_text + "In this problem all numbers need to be added so perform all addition from left to right<br><br>"
            self.solution_text = self.solution_text + str(number1)+" + "+str(number2)+" + "+str(number3)+" = "+str(number1+number2)+" + "+str(number3)
            self.solution_text = self.solution_text + "= "+answer
        if flag == 2:
            self.solution_text = self.solution_text + "In this problem all numbers need to be multiplied so perform all multiplication from left to right<br><br>"
            self.solution_text = self.solution_text + str(number4)+" &times; "+str(number5)+" &times; "+str(number6)+" = "+str(number4*number5)+" &times; "+str(number6)
            self.solution_text = self.solution_text + "= "+answer
        if flag == 3:
            self.solution_text = self.solution_text + "As per the rules above, first perform multiplication from left to right<br><br>"
            self.solution_text = self.solution_text + str(number1)+" + "+str(number4)+" &times; "+str(number5)+" = "+str(number1)+" + "+str(number4*number5)+"<br><br>"
            self.solution_text = self.solution_text + "Now perform addition<br><br>"
            self.solution_text = self.solution_text + str(number1)+" + "+str(number4*number5)+" = "+answer        
        if flag == 4:
            self.solution_text = self.solution_text + "As per the rules above, first perform multiplication from left to right<br><br>"
            self.solution_text = self.solution_text + str(number4)+" &times; "+str(number5)+" + " +str(number1)+" = "+str(number4*number5)+" + " +str(number1)+"<br><br>"
            self.solution_text = self.solution_text + "Now perform addition<br><br>"
            self.solution_text = self.solution_text + str(number4*number5)+" + " +str(number1)+" = "+answer        
        if flag == 5:
            self.solution_text = self.solution_text + "As per the rules above, first perform multiplication from left to right<br><br>"
            self.solution_text = self.solution_text + "<span style='color:blue'>"+str(number4)+" &times; "+str(number5)+"</span> + <span style='color:red'>" +str(number6)+" &times; "+str(number7)+"</span> = "+str(number4*number5)+" + " +str(number6*number7)+"<br><br>"
            self.solution_text = self.solution_text + "Now perform addition<br><br>"
            self.solution_text = self.solution_text + str(number4*number5)+" + " +str(number6*number7)+" = "+answer        
        if flag == 6:
            self.solution_text = self.solution_text + "As per the rules above, first perform the operations inside the bracket<br><br>"
            self.solution_text = self.solution_text + str(number4)+" &times; ("+str(number5)+" + "+str(number6)+") &times; "+str(number7)+" = "+str(number4)+" &times; ("+str(number5+number6)+") &times;"+str(number7)+"<br><br>"
            self.solution_text = self.solution_text + "Now perform multiplication from left to right<br><br>"
            self.solution_text = self.solution_text + "= <span style='color:red'>"+str(number4)+" &times; "+str(number5+number6)+"</span> &times; "+str(number7)+"<br><br>"
            self.solution_text = self.solution_text + "= "+str(number4*(number5+number6))+" &times; " +str(number7)+" = "+answer        
        
        self.solution_text = self.solution_text + "<br><br><i><b> Hence the correct answer is "+answer+"</b></i>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain   

    def GenerateProblemType2(self):
        
        '''For addition/subtraction use numbers between 2 & 99 but for multiplication use between 2 & 9'''
        self.number1 = randint(2,99)
        self.number2 = randint(2,99)
        self.number3 = randint(2,99)
        self.number4 = randint(2,9)
        self.number5 = randint(2,9)
        self.number6 = randint(2,9)
        self.number7 = randint(2,9)
        self.number = 0
        
        randomSelect = randint(1,9)
        
        if randomSelect==1:
            '''e.g.: 54-36-8'''
            '''For subtraction problem we decide the answer first so we guarantee 
            that there will be no negative number as answer'''
            self.answer = randint(2,50)
            self.number = self.answer+self.number1+self.number2
            self.problem = r"Find the value:<br>%d - %d - %d" %(self.number,self.number1,self.number2)
            self.flag = 1
        elif randomSelect==2:
            '''e.g.: 54-36+8'''
            self.answer = randint(self.number2,100)
            self.number = self.answer+self.number1-self.number2
            self.problem = r"Find the value:<br>%d - %d + %d" %(self.number,self.number1,self.number2)
            self.flag = 2
        elif randomSelect==3:
            '''e.g.: 54+36-8'''
            self.answer = randint(self.number1,100)
            self.number = self.answer-self.number1+self.number2
            self.problem = r"Find the value:<br>%d + %d - %d" %(self.number,self.number1,self.number2)
            self.flag = 3
        elif randomSelect==4:
            '''e.g.: 8*7-34'''
            '''Making sure the answer is not a negative number'''
            self.number= randint(2,self.number4*self.number5)
            self.problem = r"Find the value:<br>%d &times; %d - %d" %(self.number4,self.number5,self.number)
            self.answer = self.number4*self.number5-self.number
            self.flag = 4
        elif randomSelect==5:
            '''e.g.: 8*7-4*3'''
            self.number1 = randint(7,10)
            self.number2 = randint(5,7)
            self.number3 = randint(2,5)
            self.number4 = randint(2,5)
            self.problem = r"Find the value:<br>%d &times; %d - %d &times; %d" %(self.number1,self.number2,self.number3,self.number4)
            self.answer = self.number1*self.number2-self.number3*self.number4
            self.flag = 5            
        elif randomSelect==6:
            '''e.g.: 75+8*7-34'''
            '''number 1 will always be greater than or equal to number2'''
            self.number2 = randint(2,68)
            self.number1 = randint(self.number2,99)
            self.problem = r"Find the value:<br>%d + %d &times; %d - %d" %(self.number1,self.number4,self.number5,self.number2)
            self.answer = self.number1+self.number4*self.number5-self.number2
            self.flag = 6       
        elif randomSelect==7:
            '''e.g.: 88-(54-34)'''
            self.number3 = randint(2,50)
            self.number2 = randint(self.number3,99)
            self.number1 = randint(self.number2-self.number3,99)
            self.problem = r"Find the value:<br>%d - (%d - %d)" %(self.number1,self.number2,self.number3)
            self.answer = self.number1-(self.number2-self.number3)
            self.flag = 7            
        elif randomSelect==8:
            '''e.g.: 65-(34+12)'''
            self.number3 = randint(2,40)
            self.number2 = randint(2,40)
            self.number1 = randint(self.number2+self.number3,99)
            self.problem = r"Find the value:<br>%d - (%d + %d)" %(self.number1,self.number2,self.number3)
            self.answer = self.number1-(self.number2+self.number3)
            self.flag = 8
        elif randomSelect==9:
            '''e.g.: 8*(7-4)*9'''
            self.number1 = randint(6,10)
            self.number2 = randint(2,6)
            self.problem = r"Find the value:<br>%d &times; (%d - %d) &times; %d" %(self.number4,self.number1,self.number2,self.number5)
            self.answer = self.number4*(self.number1-self.number2)*self.number5
            self.flag = 9                   
        self.template = "EnterTypeProblems.html"                                      

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,str(self.answer),self.number,self.number1,self.number2,self.number3,self.number4,self.number5,self.number6,self.number7,self.flag)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType2"}

    def ExplainType2(self,problem,answer,number,number1,number2,number3,number4,number5,number6,number7,flag):
        self.answer_text = "<br>The correct answer is:<br>"+answer
        self.solution_text =  "<b><u>Problem</b></u>:<br/>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br/>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br/>"
        self.solution_text = self.solution_text + "Follow these 3 simple rules to get any question on order of operations right:<br><br>"
        self.solution_text = self.solution_text + "Rule 1: Do the operations in brackets.<br>"
        self.solution_text = self.solution_text + "Rule 2: Multiply and/or divide from left to right.<br>"
        self.solution_text = self.solution_text + "Rule 3: Add and/or subtract from left to right.<br><br>"
        if flag == 1:
            self.solution_text = self.solution_text + "In this problem all numbers need to be subtracted so perform all subtraction from left to right<br><br>"
            self.solution_text = self.solution_text + "<span style='color:red'>"+str(number)+" - "+str(number1)+"</span> - "+str(number2)+" = "+str(number-number1)+" - "+str(number2)
            self.solution_text = self.solution_text + "= "+answer
        elif flag == 2:
            self.solution_text = self.solution_text + "First subtract and then add the numbers, following the left to right rule.<br><br>"
            self.solution_text = self.solution_text + "<span style='color:red'>"+str(number)+" - "+str(number1)+"</span> + "+str(number2)+" = "+str(number-number1)+" + "+str(number2)
            self.solution_text = self.solution_text + "= "+answer
        elif flag == 3:
            self.solution_text = self.solution_text + "First add and then subtract the numbers, following the left to right rule.<br><br>"
            self.solution_text = self.solution_text + "<span style='color:red'>"+str(number)+" + "+str(number1)+"</span> - "+str(number2)+" = "+str(number+number1)+" - "+str(number2)
            self.solution_text = self.solution_text + "= "+answer        
        elif flag == 4:
            self.solution_text = self.solution_text + "As per the rules above, first perform multiplication from left to right<br><br>"
            self.solution_text = self.solution_text + "<span style='color:red'>"+str(number4)+" &times; "+str(number5)+"</span> - " +str(number)+" = "+str(number4*number5)+" - " +str(number)+"<br><br>"
            self.solution_text = self.solution_text + "Now perform subtraction<br><br>"
            self.solution_text = self.solution_text + str(number4*number5)+" - " +str(number)+" = "+answer        
        elif flag == 5:
            self.solution_text = self.solution_text + "As per the rules above, first perform multiplication from left to right<br><br>"
            self.solution_text = self.solution_text + "<span style='color:blue'>"+str(number1)+" &times; "+str(number2)+"</span> - <span style='color:red'>"+str(number3)+" &times; "+str(number4)+"</span> = "+str(number1*number2)+" - " +str(number3*number4)+"<br><br>"
            self.solution_text = self.solution_text + "Now perform subtraction<br><br>"
            self.solution_text = self.solution_text + str(number1*number2)+" - " +str(number3*number4)+" = "+answer  
        elif flag == 6:
            self.solution_text = self.solution_text + "As per the rules above, first perform multiplication from left to right<br><br>"
            self.solution_text = self.solution_text + str(number1)+" + <span style='color:red'>"+str(number4)+" &times; " +str(number5)+"</span> - "+str(number2)+" = "+str(number1)+" + "+str(number4*number5)+" - " +str(number2)+"<br><br>"
            self.solution_text = self.solution_text + "Now perform addition first and then subtraction, going from left to right<br><br>"
            self.solution_text = self.solution_text + "<span style='color:red'>"+str(number1)+" + " +str(number4*number5)+"</span> - "+str(number2)+"<br><br>"        
            self.solution_text = self.solution_text + "= "+str(number1+number4*number5)+" - "+str(number2)+" = "+answer
        elif flag == 7:
            self.solution_text = self.solution_text + "As per the rules above, first perform the operations inside the bracket<br><br>"
            self.solution_text = self.solution_text + str(number1)+" - (<span style='color:red'>"+str(number2)+" - "+str(number3)+"</span>) = "+str(number1)+" - ("+str(number2-number3)+")<br><br>"
            self.solution_text = self.solution_text + "Now perform the remaining subtraction<br><br>"
            self.solution_text = self.solution_text + "= "+str(number1)+" - "+str(number2-number3)+" = "+answer    
        elif flag == 8:
            self.solution_text = self.solution_text + "As per the rules above, first perform the operations inside the bracket<br><br>"
            self.solution_text = self.solution_text + str(number1)+" - (<span style='color:red'>"+str(number2)+" + "+str(number3)+"</span>) = "+str(number1)+" - ("+str(number2+number3)+")<br><br>"
            self.solution_text = self.solution_text + "Now perform the subtraction<br><br>"
            self.solution_text = self.solution_text + "= "+str(number1)+" - "+str(number2+number3)+" = "+answer
        elif flag == 9:
            self.solution_text = self.solution_text + "As per the rules above, first perform the operations inside the bracket<br><br>"
            self.solution_text = self.solution_text + str(number4)+" &times; (<span style='color:red'>"+str(number1)+" - "+str(number2)+"</span>) &times; "+str(number5)+" = "+str(number4)+" &times; ("+str(number1-number2)+") &times; "+str(number5)+"<br><br>"
            self.solution_text = self.solution_text + "Now perform the multiplication from left to right<br><br>"
            self.solution_text = self.solution_text + "= <span style='color:red'>"+str(number4)+" &times; "+str(number1-number2)+"</span> &times; "+str(number5)+"<br><br>"
            self.solution_text = self.solution_text + "= "+str(number4*(number1-number2))+" &times; "+str(number5)+" = "+answer
                                
        self.solution_text = self.solution_text + "<br><br><i><b> Hence the correct answer is "+answer+"</b></i>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
    
    def GenerateProblemType3(self):
        
        self.number1 = randint(2,6)
        self.number2 = randint(2,6)
        self.number3 = 0
        self.number4 = 0
        self.number = 0
        
        randomSelect = randint(1,8)
        
        if randomSelect==1:
            '''e.g.:50/5/2'''
            self.answer = randint(2,7)
            self.number = self.answer*self.number1*self.number2
            self.problem = "Find the value:<br>%d &divide; %d &divide; %d"%(self.number,self.number1,self.number2)
            self.flag = 1
        elif randomSelect==2:
            '''e.g.:16/4*5'''
            self.number3 = random.randrange(self.number1,99,self.number1)
            self.problem = "Find the value:<br>%d &divide; %d &times; %d"%(self.number3,self.number1,self.number2)
            self.answer = self.number3/self.number1*self.number2
            self.flag = 2
        elif randomSelect==3:
            '''e.g.:10*4/2'''
            self.number1 = randint(2,9)
            self.number2 = randint(2,9)
            remainder = 1
            while remainder!=0:
                self.number3 = randint(2,self.number1*self.number2)
                remainder = self.number1*self.number2%self.number3
            self.problem = "Find the value:<br>%d &times; %d &divide; %d"%(self.number1,self.number2,self.number3)
            self.answer = self.number1*self.number2/self.number3
            self.flag = 3
        elif randomSelect==4:
            '''e.g.:16-10/2'''
            self.number1 = randint(2,9)
            self.number2 = random.randrange(self.number1,99,self.number1)
            self.number3 = randint(self.number2/self.number1,99)
            self.problem = "Find the value:<br>%d - %d &divide; %d"%(self.number3,self.number2,self.number1)
            self.answer = self.number3-self.number2/self.number1
            self.flag = 4
        elif randomSelect==5:
            '''e.g.:80-40/8+20'''
            self.number1 = randint(2,9)
            self.number2 = random.randrange(self.number1,99,self.number1)
            self.number3 = randint(self.number2/self.number1,99)
            self.number4 = randint(2,99)
            self.problem = "Find the value:<br>%d - %d &divide; %d + %d"%(self.number3,self.number2,self.number1,self.number4)
            self.answer = self.number3-self.number2/self.number1+self.number4
            self.flag = 5
        elif randomSelect==6:
            '''e.g.:12+48/4*3'''
            self.number1 = randint(2,9)
            self.number2 = random.randrange(self.number1,60,self.number1)
            self.number3 = randint(2,9)
            self.number4 = randint(2,99)
            self.problem = "Find the value:<br>%d + %d &divide; %d &times %d"%(self.number4,self.number2,self.number1,self.number3)
            self.answer = self.number4+self.number2/self.number1*self.number3
            self.flag = 6         
        elif randomSelect==7:
            '''e.g.:48/4*3'''
            self.number1 = randint(2,6)
            self.number2 = randint(2,6)
            self.number3 = random.randrange(self.number1*self.number2,99,self.number1*self.number2)
            self.problem = "Find the value:<br>%d &divide; %d &times; %d"%(self.number3,self.number1,self.number2)
            self.answer = self.number3/self.number1*self.number2
            self.flag = 7
        elif randomSelect==8:
            '''e.g.:(57-32)/5*2'''
            self.number1 = randint(2,9)
            self.number2 = randint(2,9)
            self.number3 = randint(2,69)
            self.number4 = randint(2,9)
            self.number = self.number1*self.number2+self.number3
            self.problem = "Find the value:<br>(%d - %d) &divide; %d &times; %d"%(self.number,self.number3,self.number1,self.number4)
            self.answer = (self.number-self.number3)/self.number1*self.number4
            self.flag = 8
                                   
        self.template = "EnterTypeProblems.html"                                      

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,str(self.answer),self.number,self.number1,self.number2,self.number3,self.number4,self.flag)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,'problem_type':"ProblemType3"}

    def ExplainType3(self,problem,answer,number,number1,number2,number3,number4,flag):
        self.answer_text = "<br>The correct answer is:<br>"+answer
        self.solution_text =  "<b><u>Problem</b></u>:<br/>"
        self.solution_text = self.solution_text + "<i>"+problem + "</i><br/><br/>"
        self.solution_text = self.solution_text + "<b><u>Solution</b></u>:<br/>"
        self.solution_text = self.solution_text + "Follow these 3 simple rules to get any question on order of operations right:<br><br>"
        self.solution_text = self.solution_text + "Rule 1: Do the operations in brackets.<br>"
        self.solution_text = self.solution_text + "Rule 2: Multiply and/or divide from left to right.<br>"
        self.solution_text = self.solution_text + "Rule 3: Add and/or subtract from left to right.<br><br>"
        if flag == 1:
            self.solution_text = self.solution_text + "In this problem all numbers need to be divided so perform all division from left to right<br><br>"
            self.solution_text = self.solution_text + "<span style='color:red'>"+str(number)+" &divide; "+str(number1)+"</span> &divide; "+str(number2)+" = "+str(number/number1)+" &divide; "+str(number2)
            self.solution_text = self.solution_text + "= "+answer
        elif flag == 2:
            self.solution_text = self.solution_text + "First divide and then multiply the numbers, following the left to right rule.<br><br>"
            self.solution_text = self.solution_text + "<span style='color:red'>"+str(number3)+" &divide; "+str(number1)+"</span> &times; "+str(number2)+" = "+str(number3/number1)+" &times; "+str(number2)
            self.solution_text = self.solution_text + "= "+answer
        elif flag == 3:
            self.solution_text = self.solution_text + "First multiply and then divide the numbers, following the left to right rule.<br><br>"
            self.solution_text = self.solution_text + "<span style='color:red'>"+str(number1)+" &times; "+str(number2)+"</span> &divide; "+str(number3)+" = "+str(number1*number2)+" &divide; "+str(number3)
            self.solution_text = self.solution_text + "= "+answer        
        elif flag == 4:
            self.solution_text = self.solution_text + "As per the rules above, first perform division from left to right<br><br>"
            self.solution_text = self.solution_text + str(number3)+" - <span style='color:red'>"+str(number2)+" &divide; " +str(number1)+"</span>  = "+str(number3)+" - " +str(number2/number1)+"<br><br>"
            self.solution_text = self.solution_text + "Now perform subtraction<br><br>"
            self.solution_text = self.solution_text + str(number3)+" - " +str(number2/number1)+" = "+answer        
        elif flag == 5:
            self.solution_text = self.solution_text + "As per the rules above, first perform division from left to right<br><br>"
            self.solution_text = self.solution_text + str(number3)+" - <span style='color:red'>"+str(number2)+" &divide; "+str(number1)+"</span> + "+str(number4)+" = "+str(number3)+" - " +str(number2/number1)+" + "+str(number4)+"<br><br>"
            self.solution_text = self.solution_text + "Now perform subtraction and addition from left to right<br><br>"
            self.solution_text = self.solution_text + "<span style='color:red'>"+str(number3)+" - " +str(number2/number1)+"</span> + "+str(number4)+"<br><br>"
            self.solution_text = self.solution_text + " = "+str(number3-number2/number1)+" + "+str(number4)+" = "+answer 
        elif flag == 6:
            self.solution_text = self.solution_text + "As per the rules above, first perform division and multiplication from left to right<br><br>"
            self.solution_text = self.solution_text + str(number4)+" + <span style='color:red'>"+str(number2)+" &divide; " +str(number1)+"</span> &times; "+str(number3)+" = "+str(number4)+" + "+str(number2/number1)+" &times; " +str(number3)+"<br><br>"
            self.solution_text = self.solution_text + str(number4)+" + <span style='color:red'>" +str(number2/number1)+"&times; "+str(number3)+"</span><br><br>"
            self.solution_text = self.solution_text + "And then perform the addition<br><br>"        
            self.solution_text = self.solution_text + "= "+str(number4)+" + "+str(number2/number1*number3)+" = "+answer
        elif flag == 7:
            self.solution_text = self.solution_text + "As per the rules above, perform the division and multiplication from left to right.<br><br>"
            self.solution_text = self.solution_text + "<span style='color:red'>"+str(number3)+" &divide; "+str(number1)+"</span> &times; "+str(number2)+" = "+str(number3/number1)+" &times; "+str(number2)+"<br><br>"
            self.solution_text = self.solution_text + "= "+str(number3/number1)+" &times; "+str(number2)+" = "+answer    
        elif flag == 8:
            self.solution_text = self.solution_text + "As per the rules above, first perform the operations inside the bracket<br><br>"
            self.solution_text = self.solution_text + "(<span style='color:red'>"+str(number)+" - "+str(number3)+"</span>) &divide; "+str(number1)+" &times; "+str(number4)+" = ("+str(number-number3)+") &divide; "+str(number1)+" &times; "+str(number4)+"<br><br>"
            self.solution_text = self.solution_text + "Now perform the division and multiplication from left to right<br><br>"
            self.solution_text = self.solution_text + "<span style='color:red'>"+str(number-number3)+" &divide "+str(number1)+"</span> &times; "+str(number4)+"<br><br>"
            self.solution_text = self.solution_text + " = "+str((number-number3)/number1)+" &times; "+str(number4)+" = "+answer
                                
        self.solution_text = self.solution_text + "<br><br><i><b> Hence the correct answer is "+answer+"</b></i>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
    
    def removeCorrectAnswer(self,ans):
        return (self.answer != ans)        

    def GenerateMCQ(self,wrongAnswers,problem,answer,template,explain,problem_type):
        
        '''Removing correct answers from the wrongAnswers list'''
        wrongAnswers = filter(self.removeCorrectAnswer,wrongAnswers)
        
        self.answer1=''
        self.answer2=''
        self.answer3=''
        self.answer4=''
                             
        '''Randomly selecting 3 wrong answers and adding the correct answer as well'''
        try:
            wrongAnswers = random.sample(wrongAnswers,3)
        except ValueError:
            pass
            
        wrongAnswers.append(answer)
        random.shuffle(wrongAnswers)
        try:
            self.answer1 = str(wrongAnswers[0])
            self.answer2 = str(wrongAnswers[1])
            self.answer3 = str(wrongAnswers[2])
            self.answer4 = str(wrongAnswers[3])        
        except IndexError:
            pass
        try:
            self.value1 = self.answer1
            self.value2 = self.answer2
            self.value3 = self.answer3
            self.value4 = self.answer4
        except AttributeError:
            pass
                       
        return {'problem':problem,'answer':answer,'template':template,
                'answer1':self.answer1,'answer2':self.answer2,'answer3':self.answer3,
                'answer4':self.answer4,'value1':self.value1,'value2':self.value2
                ,'value3':self.value3,'value4':self.value4,'explain':explain,'problem_type':problem_type}       

    def GenerateProblemTypeMCQ1(self):
        '''e.g.:
        Find the value:
        25 +53 +56'''
        
        self.problem_type = "ProblemTypeMCQ1"
        '''For addition use numbers between 2 & 99 but for multiplication use between 2 & 9'''
        self.number1 = randint(2,99)
        self.number2 = randint(2,99)
        self.number3 = randint(2,99)
        self.number4 = randint(2,9)
        self.number5 = randint(2,9)
        self.number6 = randint(2,9)
        self.number7 = randint(2,9)
        self.wrongAnswers = []
        
        randomSelect = randint(1,6)
        
        if randomSelect==1:
            self.problem = r"Find the value:<br>%d + %d + %d" %(self.number1,self.number2,self.number3)
            self.answer = self.number1+self.number2+self.number3
            '''making sure no negative answer is generated'''
            self.wrongAnswers.append(str(abs(self.number1+self.number2-self.number3)))
            self.flag = 1
        elif randomSelect==2:
            self.problem = r"Find the value:<br>%d &times; %d &times; %d" %(self.number4,self.number5,self.number6)
            self.answer = self.number4*self.number5*self.number6
            self.wrongAnswers.append(str(self.number4*self.number5+self.number6))
            self.wrongAnswers.append(str(self.number4+self.number5*self.number6))
            self.flag = 2
        elif randomSelect==3:
            self.problem = r"Find the value:<br>%d + %d &times; %d" %(self.number1,self.number4,self.number5)
            self.answer = self.number1+self.number4*self.number5
            self.wrongAnswers.append(str(self.number1*self.number4+self.number5))
            self.wrongAnswers.append(str((self.number1+self.number4)*self.number5))
            self.flag = 3
        elif randomSelect==4:
            self.problem = r"Find the value:<br>%d &times; %d + %d" %(self.number4,self.number5,self.number1)
            self.answer = self.number4*self.number5+self.number1
            self.wrongAnswers.append(str(self.number4*(self.number5+self.number1)))
            self.flag = 4
        elif randomSelect==5:
            self.problem = r"Find the value:<br>%d &times; %d + %d &times; %d" %(self.number4,self.number5,self.number6,self.number7)
            self.answer = self.number4*self.number5+self.number6*self.number7
            self.wrongAnswers.append(str(self.number4*(self.number5+self.number6)*self.number7))
            self.flag = 5           
        elif randomSelect==6:
            self.problem = r"Find the value:<br>%d &times; (%d + %d) &times; %d" %(self.number4,self.number5,self.number6,self.number7)
            self.answer = self.number4*(self.number5+self.number6)*self.number7
            self.wrongAnswers.append(str(self.number4*self.number5+self.number6*self.number7))
            self.flag = 6
            
        '''Making sure at least 3 wrong answers are generated'''
        self.wrongAnswers.append(str(self.answer+1))
        self.wrongAnswers.append(str(self.answer-1))
        self.wrongAnswers.append(str(self.answer+10))          

        self.template = "MCQTypeProblems.html"

        '''In MCQ problems all answers goes as string'''
        self.answer = str(self.answer)           
        
                   
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,str(self.answer),self.number1,self.number2,self.number3,self.number4,self.number5,self.number6,self.number7,self.flag)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type)
    
    def GenerateProblemTypeMCQ2(self):
        
        self.problem_type = "ProblemTypeMCQ2"
        '''For addition/subtraction use numbers between 2 & 99 but for multiplication use between 2 & 9'''
        self.number1 = randint(2,99)
        self.number2 = randint(2,99)
        self.number3 = randint(2,99)
        self.number4 = randint(2,9)
        self.number5 = randint(2,9)
        self.number6 = randint(2,9)
        self.number7 = randint(2,9)
        self.number = 0
        
        self.wrongAnswers = []
        
        randomSelect = randint(1,9)
        
        if randomSelect==1:
            '''e.g.: 54-36-8'''
            '''For subtraction problem we decide the answer first so we guarantee 
            that there will be no negative number as answer'''
            self.answer = randint(2,50)
            self.number = self.answer+self.number1+self.number2
            self.problem = r"Find the value:<br>%d -%d -%d" %(self.number,self.number1,self.number2)
            self.wrongAnswers.append(str(self.number-self.number1+self.number2))
            self.wrongAnswers.append(str(self.number+self.number1+self.number2))
            self.wrongAnswers.append(str(self.number+self.number1-self.number2))
            self.flag = 1
        elif randomSelect==2:
            '''e.g.: 54-36+8'''
            self.answer = randint(self.number2,100)
            self.number = self.answer+self.number1-self.number2
            self.problem = r"Find the value:<br>%d -%d +%d" %(self.number,self.number1,self.number2)
            self.wrongAnswers.append(str(self.number+self.number1+self.number2))
            self.wrongAnswers.append(str(abs(self.number-self.number1-self.number2)))
            self.wrongAnswers.append(str(abs(self.number+self.number1-self.number2)))
            self.flag = 2
        elif randomSelect==3:
            '''e.g.: 54+36-8'''
            self.answer = randint(self.number1,100)
            self.number = self.answer-self.number1+self.number2
            self.problem = r"Find the value:<br>%d +%d -%d" %(self.number,self.number1,self.number2)
            self.wrongAnswers.append(str(self.number+self.number1+self.number2))
            self.wrongAnswers.append(str(abs(self.number-self.number1+self.number2)))
            self.wrongAnswers.append(str(abs(self.number-self.number1-self.number2)))
            self.flag = 3
        elif randomSelect==4:
            '''e.g.: 8*7-34'''
            '''Making sure the answer is not a negative number'''
            self.number= randint(2,self.number4*self.number5)
            self.problem = r"Find the value:<br>%d &times; %d - %d" %(self.number4,self.number5,self.number)
            self.answer = self.number4*self.number5-self.number
            self.wrongAnswers.append(str(abs(self.number4*(self.number5-self.number))))
            self.wrongAnswers.append(str(self.number4*self.number5+self.number))
            self.flag = 4
        elif randomSelect==5:
            '''e.g.: 8*7-4*3'''
            self.number1 = randint(7,10)
            self.number2 = randint(5,7)
            self.number3 = randint(2,5)
            self.number4 = randint(2,5)
            self.problem = r"Find the value:<br>%d &times; %d - %d &times; %d" %(self.number1,self.number2,self.number3,self.number4)
            self.answer = self.number1*self.number2-self.number3*self.number4
            self.wrongAnswers.append(str(self.number1*abs(self.number2-self.number3)*self.number4))
            self.wrongAnswers.append(str(self.number1*self.number2+self.number3*self.number4))
            self.flag = 5           
        elif randomSelect==6:
            '''e.g.: 75+8*7-34'''
            '''number 1 will always be greater than or equal to number2'''
            self.number2 = randint(2,68)
            self.number1 = randint(self.number2,99)
            self.problem = r"Find the value:<br>%d + %d &times; %d - %d" %(self.number1,self.number4,self.number5,self.number2)
            self.answer = self.number1+self.number4*self.number5-self.number2
            self.wrongAnswers.append(str((self.number1+self.number4)*self.number5-self.number2))
            self.wrongAnswers.append(str(self.number1+self.number4*abs(self.number5-self.number2)))
            self.wrongAnswers.append(str((self.number1+self.number4)*abs(self.number5-self.number2)))
            self.flag = 6           
        elif randomSelect==7:
            '''e.g.: 88-(54-34)'''
            self.number3 = randint(2,50)
            self.number2 = randint(self.number3,99)
            self.number1 = randint(self.number2-self.number3,99)
            self.problem = r"Find the value:<br>%d - (%d - %d)" %(self.number1,self.number2,self.number3)
            self.answer = self.number1-(self.number2-self.number3)
            self.wrongAnswers.append(str(abs(self.number1-self.number2-self.number3)))
            self.wrongAnswers.append(str(self.number1+self.number2-self.number3))
            self.flag = 7            
        elif randomSelect==8:
            '''e.g.: 65-(34+12)'''
            self.number3 = randint(2,40)
            self.number2 = randint(2,40)
            self.number1 = randint(self.number2+self.number3,99)
            self.problem = r"Find the value:<br>%d - (%d + %d)" %(self.number1,self.number2,self.number3)
            self.answer = self.number1-(self.number2+self.number3)
            self.wrongAnswers.append(str(self.number1-self.number2+self.number3))
            self.wrongAnswers.append(str(self.number1+self.number2+self.number3))
            self.flag = 8
        elif randomSelect==9:
            '''e.g.: 8*(7-4)*9'''
            self.number1 = randint(6,10)
            self.number2 = randint(2,6)
            self.problem = r"Find the value:<br>%d &times; (%d - %d) &times; %d" %(self.number4,self.number1,self.number2,self.number5)
            self.answer = self.number4*(self.number1-self.number2)*self.number5
            self.wrongAnswers.append(str(abs(self.number4*self.number1-self.number2*self.number5)))
            self.wrongAnswers.append(str(self.number4*self.number1+self.number2*self.number5))
            self.flag = 9
        
        '''Making sure at least 3 wrong answers are generated'''
        self.wrongAnswers.append(str(self.answer+1))
        self.wrongAnswers.append(str(self.answer-1))
        self.wrongAnswers.append(str(self.answer+10))                                    

        self.template = "MCQTypeProblems.html"

        '''In MCQ problems all answers goes as string'''
        self.answer = str(self.answer)           
                   
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,str(self.answer),self.number,self.number1,self.number2,self.number3,self.number4,self.number5,self.number6,self.number7,self.flag)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type)

    def GenerateProblemTypeMCQ3(self):
        
        self.problem_type = "ProblemTypeMCQ3"
        self.number1 = randint(2,6)
        self.number2 = randint(2,6)
        self.number3 = 0
        self.number4 = 0
        self.number = 0
        
        self.wrongAnswers=[]
        
        randomSelect = randint(1,8)
        
        if randomSelect==1:
            '''e.g.:50/5/2'''
            self.answer = randint(2,7)
            self.number = self.answer*self.number1*self.number2
            self.problem = "Find the value:<br>%d &divide; %d &divide; %d"%(self.number,self.number1,self.number2)
            self.wrongAnswers.append(str(self.number/self.number1*self.number2))
            self.flag = 1
        elif randomSelect==2:
            '''e.g.:16/4*5'''
            self.number3 = random.randrange(self.number1,99,self.number1)
            self.problem = "Find the value:<br>%d &divide; %d &times; %d"%(self.number3,self.number1,self.number2)
            self.answer = self.number3/self.number1*self.number2
            self.wrongAnswers.append(str(int(self.number3/(self.number1*self.number2))))
            self.flag = 2
        elif randomSelect==3:
            '''e.g.:10*4/2'''
            self.number1 = randint(2,9)
            self.number2 = randint(2,9)
            remainder = 1
            while remainder!=0:
                self.number3 = randint(2,self.number1*self.number2)
                remainder = self.number1*self.number2%self.number3
            self.problem = "Find the value:<br>%d &times; %d &divide; %d"%(self.number1,self.number2,self.number3)
            self.answer = self.number1*self.number2/self.number3
            self.wrongAnswers.append(str(self.number1*self.number2*self.number3))
            self.wrongAnswers.append(str(int(self.number1/self.number2*self.number3)))
            self.flag = 3
        elif randomSelect==4:
            '''e.g.:16-10/2'''
            self.number1 = randint(2,9)
            self.number2 = random.randrange(self.number1,99,self.number1)
            self.number3 = randint(self.number2/self.number1,99)
            self.problem = "Find the value:<br>%d - %d &divide; %d"%(self.number3,self.number2,self.number1)
            self.answer = self.number3-self.number2/self.number1
            self.wrongAnswers.append(str(int(abs(self.number3-self.number2)/self.number1)))
            self.flag = 4
        elif randomSelect==5:
            '''e.g.:80-40/8+20'''
            self.number1 = randint(2,9)
            self.number2 = random.randrange(self.number1,99,self.number1)
            self.number3 = randint(self.number2/self.number1,99)
            self.number4 = randint(2,99)
            self.problem = "Find the value:<br>%d - %d &divide; %d + %d"%(self.number3,self.number2,self.number1,self.number4)
            self.answer = self.number3-self.number2/self.number1+self.number4
            self.wrongAnswers.append(str(int(abs(self.number3-self.number2)/self.number1+self.number4)))
            self.wrongAnswers.append(str(int(abs(self.number3-self.number2)/(self.number1+self.number4))))
            self.flag = 5
        elif randomSelect==6:
            '''e.g.:12+48/4*3'''
            self.number1 = randint(2,9)
            self.number2 = random.randrange(self.number1,60,self.number1)
            self.number3 = randint(2,9)
            self.number4 = randint(2,99)
            self.problem = "Find the value:<br>%d + %d &divide; %d &times; %d"%(self.number4,self.number2,self.number1,self.number3)
            self.answer = self.number4+self.number2/self.number1*self.number3
            self.wrongAnswers.append(str(int((self.number4+self.number2)/self.number1*self.number3)))
            self.wrongAnswers.append(str(int(self.number4+self.number2/(self.number1*self.number3))))
            self.flag = 6        
        elif randomSelect==7:
            '''e.g.:48/4*3'''
            self.number1 = randint(2,6)
            self.number2 = randint(2,6)
            self.number3 = random.randrange(self.number1*self.number2,99,self.number1*self.number2)
            self.problem = "Find the value:<br>%d &divide; %d &times; %d"%(self.number3,self.number1,self.number2)
            self.answer = self.number3/self.number1*self.number2
            self.wrongAnswers.append(str(int(self.number3/self.number1*self.number2)))
            self.flag = 7
        elif randomSelect==8:
            '''e.g.:(57-32)/5*2'''
            self.number1 = randint(2,9)
            self.number2 = randint(2,9)
            self.number3 = randint(2,69)
            self.number4 = randint(2,9)
            self.number = self.number1*self.number2+self.number3
            self.problem = "Find the value:<br>(%d - %d) &divide; %d &times; %d"%(self.number,self.number3,self.number1,self.number4)
            self.answer = (self.number-self.number3)/self.number1*self.number4
            self.wrongAnswers.append(str(int(abs(self.number-self.number3/self.number1*self.number4))))
            self.wrongAnswers.append(str(int(abs(self.number-self.number3/(self.number1*self.number4)))))
            self.flag = 8
        
        '''Making sure at least 3 wrong answers are generated'''
        self.wrongAnswers.append(str(self.answer+1))
        self.wrongAnswers.append(str(self.answer-1))
        self.wrongAnswers.append(str(self.answer+10))                                    

        self.template = "MCQTypeProblems.html"

        '''In MCQ problems all answers goes as string'''
        self.answer = str(self.answer)           
                   
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType3(self.problem,str(self.answer),self.number,self.number1,self.number2,self.number3,self.number4,self.flag)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text,
                             "video_link":"www.homecampus.com.sg","explain_note":""}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,self.problem_type)


    def checkAnswer(self,template,answer,InputAnswer):
        '''removing the "," from answer'''
        answer = str(answer)
        while  answer.partition(",")[1]!="":
            answer = answer.partition(",")[0]+answer.partition(",")[2]
        '''remove the "," from InputAnswer only if its a string'''
        InputAnswer = str(InputAnswer)
        while  InputAnswer.partition(",")[1]!="":
            InputAnswer = InputAnswer.partition(",")[0]+InputAnswer.partition(",")[2]      
        try:
            return int(answer)==int(InputAnswer)
        except ValueError:
            return False 
