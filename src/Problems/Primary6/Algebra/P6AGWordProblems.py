'''
Created on Apr 24, 2012
Module: P6AGWordProblems
Generates the "Algebra Word Problems" problems for Primary 6

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
import string
from Problems import PersonName

class P6AGWordProblems:
    
    def __init__(self):
        pass
    
    def GenerateProblem(self):
        """ randomly decides which question to generate """
        #return self.GenerateProblemTypeMCQ8()           
    
    def GenerateProblemSequential(self,LastProblemID):
        ''' Generating first problem randomly and there after generating in a sequential order so that all problems get covered'''
                      
        self.ProblemType = {1:["ProblemType1",],2:["ProblemType2",],3:["ProblemTypeMCQ3",],
                            4:["ProblemTypeMCQ4a",],5:["ProblemType5b",],6:["ProblemTypeMCQ6a",],
                            7:["ProblemType7b",],8:["ProblemType4b",],9:["ProblemTypeMCQ5a",],
                            10:["ProblemType6b",],11:["ProblemTypeMCQ7a",],
                            }
        
        self.GenerateProblemType = {1:[self.GenerateProblemType1(),],2:[self.GenerateProblemType2(),],3:[self.GenerateProblemTypeMCQ3(),],
                                    4:[self.GenerateProblemTypeMCQ4a(),],5:[self.GenerateProblemType5b(),],6:[self.GenerateProblemTypeMCQ6a(),],
                                    7:[self.GenerateProblemType7b(),],8:[self.GenerateProblemType4b(),],9:[self.GenerateProblemTypeMCQ5a(),],
                                    10:[self.GenerateProblemType6b(),],11:[self.GenerateProblemTypeMCQ7a(),],
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
        #return self.GenerateProblemType7b()
        
    def GenerateTestProblem(self,problem_type):
        self.ProblemType = {"ProblemType1":self.GenerateProblemType1(),
                            "ProblemType2":self.GenerateProblemType2(),
                            "ProblemTypeMCQ3":self.GenerateProblemTypeMCQ3(),
                            "ProblemTypeMCQ4a":self.GenerateProblemTypeMCQ4a(),
                            "ProblemType4b":self.GenerateProblemType4b(),
                            "ProblemType5b":self.GenerateProblemType5b(),
                            "ProblemTypeMCQ5a":self.GenerateProblemTypeMCQ5a(),
                            "ProblemType6b":self.GenerateProblemType6b(),
                            "ProblemTypeMCQ6a":self.GenerateProblemTypeMCQ6a(),
                            "ProblemType7b":self.GenerateProblemType7b(),
                            "ProblemTypeMCQ7a":self.GenerateProblemTypeMCQ7a(),
                            }
        return self.ProblemType[problem_type]
        
    def GenerateProblemType1(self):
        '''e.g: Section A has more kids than Section B. There are 37 kids in Section A and x kids in Section B.'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.kidsA = randint(20,50)
        self.variable = random.choice(["x","y","b"])
        self.sections = ["A","B"]
        random.shuffle(self.sections)

        self.problem = "Section "+self.sections[0]+" has more kids than Section "+self.sections[1]+". There are "+str(self.kidsA)+" kids in Section A and "+self.variable+" kids in Section B.<br><br>"
        
        self.flag = randint(1,2)

        if self.flag == 1:
            self.problem = self.problem + "How many kids are there in Section A and Section B together in terms of "+self.variable+"?"
            self.answer = str(self.kidsA)+" + "+self.variable
            self.CheckAnswerType = 2
        elif self.flag == 2:
            self.problem = self.problem + "How many more kids are there in Section "+self.sections[0]+" than in Section "+self.sections[1]+" expressed in terms of "+self.variable+"?"
            self.CheckAnswerType = 1
            if self.sections[0] == "A":
                self.answer = str(self.kidsA)+" - "+self.variable
            else:
                self.answer = self.variable+" - "+str(self.kidsA)

        self.unit = ""
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType1(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType1",'CheckAnswerType':self.CheckAnswerType,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore}            

    def ExplainType1(self,problem,answer,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "For detailed explanation refer to Word Problem 1 at <a href='/Learn/Primary6/Algebra/What-is-Algebra-and-Algebraic-Expressions#WP1' target='_blank'><u>What is Algebra? --> Word Problems</u></a>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
        
    def GenerateProblemType2(self):
        '''e.g: There are 7 marbles in a bag. How many marbles are there in k bags? Write the algebraic expression in terms of k.'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.marbles = randint(5,9)
        self.variable = random.choice(["k","y","b","z","m"])

        self.problem = "There are "+str(self.marbles)+" marbles in a bag. How many marbles are there in "+self.variable+" bags? Write the algebraic expression in terms of "+self.variable+"."
        self.answer = str(self.marbles)+self.variable
        
        self.CheckAnswerType = 3
        self.unit = "marbles"
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType2(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType2",'CheckAnswerType':self.CheckAnswerType,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore}            

    def ExplainType2(self,problem,answer,unit):
        self.answer_text = "<br>The correct answer is:<br>"+str(answer)+" "+unit
        self.solution_text = "For detailed explanation refer to Word Problem 2 at <a href='/Learn/Primary6/Algebra/What-is-Algebra-and-Algebraic-Expressions#WP2' target='_blank'><u>What is Algebra? --> Word Problems</u></a>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain
    
    def removeCorrectAnswer(self,ans):
        return (self.answer != ans)        

    def GenerateMCQ(self,wrongAnswers,problem,answer,template,explain,problem_type,
                    CheckAnswerType,grade,complexity_level,HCScore):
        
        
        '''Removing correct answers from the wrongAnswers list'''
        wrongAnswers = filter(self.removeCorrectAnswer,wrongAnswers)
                             
        '''Randomly selecting 3 wrong answers and adding the correct answer as well'''
        try:
            wrongAnswers = random.sample(wrongAnswers,3)
        except ValueError:
            pass
            
        wrongAnswers.append(answer)
        random.shuffle(wrongAnswers)
        try:
            self.answer1 = wrongAnswers[0]
            self.answer2 = wrongAnswers[1]
            self.answer3 = wrongAnswers[2]
            self.answer4 = wrongAnswers[3]         
        except IndexError:
            pass
        try:
            '''self.value1 = string.join(str(self.answer1[0]).split(),"")+"/"+string.join(str(self.answer1[1]).split(),"")+"/"+string.join(str(self.answer1[2]).split(),"")
            self.value2 = string.join(str(self.answer2[0]).split(),"")+"/"+string.join(str(self.answer2[1]).split(),"")+"/"+string.join(str(self.answer2[2]).split(),"")
            self.value3 = string.join(str(self.answer3[0]).split(),"")+"/"+string.join(str(self.answer3[1]).split(),"")+"/"+string.join(str(self.answer3[2]).split(),"")
            self.value4 = string.join(str(self.answer4[0]).split(),"")+"/"+string.join(str(self.answer4[1]).split(),"")+"/"+string.join(str(self.answer4[2]).split(),"")'''
            self.value1 = self.answer1
            self.value2 = self.answer2
            self.value3 = self.answer3
            self.value4 = self.answer4
            
        except AttributeError:
            pass
                       
        return {'problem':problem,'answer':answer,'template':template,
                'answerM1':self.answer1[0],'answerN1':self.answer1[1],'answerD1':self.answer1[2],
                'answerM2':self.answer2[0],'answerN2':self.answer2[1],'answerD2':self.answer2[2],
                'answerM3':self.answer3[0],'answerN3':self.answer3[1],'answerD3':self.answer3[2],
                'answerM4':self.answer4[0],'answerN4':self.answer4[1],'answerD4':self.answer4[2],
                'value1':self.value1,'value2':self.value2,'value3':self.value3,'value4':self.value4,
                'explain':explain,'problem_type':problem_type,
                'CheckAnswerType':CheckAnswerType,'grade':6,"complexity_level":complexity_level,"HCScore":HCScore}      

    def GenerateProblemTypeMCQ3(self):
        '''e.g: Sarah had t rolls of ribbon. She kept 2 rolls for herself and distributed the rest equally among 3 of her cousins. 
            How many rolls did each cousin get? Express the answer in terms of t.'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.number1 = randint(2,10)
        self.number2 = randint(2,5)
        self.variable = random.choice(['b','c','d','e','f','g','h','i','j','k','m','n','p','q','r','s','t','u','v','w','x','y','z'])
        self.name = random.choice(PersonName.GirlName)
        
        self.problem = self.name+" had "+self.variable+" rolls of ribbon. She kept "+str(self.number1)+" rolls for herself and distributed the rest equally among "+str(self.number2)+" of her cousins. "
        self.problem = self.problem + "How many rolls did each cousin get? Express the answer in terms of "+self.variable+".<br><br>"
                    
        self.answer1 = "("+self.variable+" - "+str(self.number1)+")"
        self.answer2 = str(self.number2)
        self.answer = [0,self.answer1,self.answer2]
        
        self.problem_type = "ProblemTypeMCQ3"
        self.template = "AlgebraFractionMCQTypeProblems.html"
        self.CheckAnswerType = 4
        self.grade = 6
        
        self.wrongAnswers = []
        self.wrongAnswers.append([0,"("+self.variable+" + "+str(self.number1)+")",str(self.number2)])
        self.wrongAnswers.append([0,str(self.number2),"("+self.variable+" - "+str(self.number1)+")"])
        self.wrongAnswers.append([0,"("+self.variable+" - "+str(self.number1)+") * "+str(self.number2),1])
        self.wrongAnswers.append([0,"("+self.variable+" - "+str(self.number1)+")",1])         
                              
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainTypeMCQ3(self.problem,self.answer1,self.answer2)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,
                                self.problem_type,self.CheckAnswerType,self.grade,self.complexity_level,self.HCScore)            

    def ExplainTypeMCQ3(self,problem,answer1,answer2):
        self.answer_text = "<table class='FractionsTable' style='color:white'><tr>"
        self.answer_text = self.answer_text + "<td>The correct answer is:&nbsp; </td>"
        self.answer_text = self.answer_text + "<td align='center'><u>"+"&nbsp;"*(len(str(answer2))/2)+str(answer1)+"&nbsp;"*(len(str(answer2))/2)+"</u><br>"+"&nbsp;"*(len(str(answer1))/2)+str(answer2)+"</td>"            
        self.answer_text = self.answer_text + "</tr></table>"
        self.solution_text = "For detailed explanation refer to Word Problem 3 at <a href='/Learn/Primary6/Algebra/What-is-Algebra-and-Algebraic-Expressions#WP3' target='_blank'><u>What is Algebra? --> Word Problems</u></a>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemTypeMCQ4a(self):
        '''e.g: Jane has t stamps. Jill has 3 times as many stamps as Jane and Julia has 2 stamps more than Jane.
        Express the number of stamps that they have altogether in terms of t.
        '''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.number1 = randint(2,10)
        self.number2 = randint(2,5)
        self.variable = random.choice(['b','c','d','e','f','g','h','i','j','k','m','n','p','q','r','s','t','u','v','w','y','z'])
        self.names = random.sample(PersonName.PersonName,3)
        
        self.problem = self.names[0]+" has "+self.variable+" stamps. "+self.names[1]+" has "+str(self.number1)+" times as many stamps as "+self.names[0]+" and "+self.names[2]+" has "+str(self.number2)+" stamps more than "+self.names[0]+".<br><br>"
        self.problem = self.problem + "Express the number of stamps that they have altogether in terms of "+self.variable+".<br><br>"
                    
        self.answer1 = str(self.number1+2)+self.variable+" + "+str(self.number2)
        self.answer = [0,self.answer1,1]
        
        self.problem_type = "ProblemTypeMCQ4a"
        self.template = "AlgebraFractionMCQTypeProblems.html"
        self.CheckAnswerType = 4
        self.grade = 6
        
        self.wrongAnswers = []
        self.wrongAnswers.append([0,str(self.number1)+self.variable+" + "+str(self.number2),1])
        self.wrongAnswers.append([0,str(self.number1+1)+self.variable+" + "+str(self.number2),1])
        self.wrongAnswers.append([0,str(self.number2+2)+self.variable+" + "+str(self.number1),1])
        self.wrongAnswers.append([0,self.variable+" + "+str(self.number2+self.number1),1])         
        
        self.unit = "stamps"
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,self.answer1,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,
                                self.problem_type,self.CheckAnswerType,self.grade,self.complexity_level,self.HCScore)            
        
    def GenerateProblemType4b(self):
        '''e.g: Jane has t stamps. Jill has 3 times as many stamps as Jane and Julia has 2 stamps more than Jane.
        How many more stamps has Jill than Julia if Jane has 8 stamps?'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.number1 = randint(3,7)
        self.number2 = randint(2,5)
        self.number3 = randint(5,9)
        self.variable = random.choice(['b','c','d','f','g','h','j','k','m','n','p','q','r','s','t','w','y','z'])
        self.names = random.sample(PersonName.PersonName,3)
        
        self.problem = self.names[0]+" has "+self.variable+" stamps. "+self.names[1]+" has "+str(self.number1)+" times as many stamps as "+self.names[0]+" and "+self.names[2]+" has "+str(self.number2)+" stamps more than "+self.names[0]+".<br><br>"
        self.problem = self.problem + "How many more stamps has "+self.names[1]+" than "+self.names[2]+" if "+self.names[0]+" has "+str(self.number3)+" stamps?"
                    
        self.answer = str(self.number1*self.number3-self.number2-self.number3)
        
        self.CheckAnswerType = 5
        self.unit = "stamps"
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType4(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType4b",'CheckAnswerType':self.CheckAnswerType,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,"unit":self.unit}
        
    def ExplainType4(self,problem,answer,unit):
        self.answer_text = "The correct answer is: "+str(answer)+" "+unit
        self.solution_text = "For detailed explanation refer to Word Problem 1 at <a href='/Learn/Primary6/Algebra/Simplifying-and-Evaluating-Algebraic-Expressions#WP1' target='_blank'><u>Simplifying and Evaluating Algebraic Expressions</u></a>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemTypeMCQ5a(self):
        '''e.g: A zoo has 3 times as many terrestrial animals as aquatic animals and 122 more aquatic animals than amphibians.
            Write an algebraic expression to express the total number of animals in the zoo in terms of the number of aquatic animals.
        '''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.number1 = randint(3,7)
        self.number2 = randint(100,200)
        self.variable = random.choice(['b','c','d','e','f','g','h','i','j','k','m','n','p','q','r','s','t','u','v','w','y','z'])
        
        self.problem = "A zoo has "+str(self.number1)+" times as many terrestrial animals as aquatic animals and "+str(self.number2)+" more aquatic animals than amphibians.<br><br>"
        self.problem = self.problem + "Write an algebraic expression to express the total number of animals in the zoo in terms of the number of aquatic animals.<br><br>"
                    
        self.answer1 = str(self.number1+2)+self.variable+" - "+str(self.number2)
        self.answer = [0,self.answer1,1]
        
        self.problem_type = "ProblemTypeMCQ5a"
        self.template = "AlgebraFractionMCQTypeProblems.html"
        self.CheckAnswerType = 4
        self.grade = 6
        
        self.wrongAnswers = []
        self.wrongAnswers.append([0,str(self.number1)+self.variable+" - "+str(self.number2),1])
        self.wrongAnswers.append([0,str(self.number1+1)+self.variable+" - "+str(self.number2),1])
        self.wrongAnswers.append([0,str(self.number1+2)+self.variable+" + "+str(self.number2),1])
        self.wrongAnswers.append([0,self.variable+" + "+str(self.number2+self.number1),1])         
        
        self.unit = ""
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5(self.problem,self.answer1,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,
                                self.problem_type,self.CheckAnswerType,self.grade,self.complexity_level,self.HCScore)            
        
    def GenerateProblemType5b(self):
        '''e.g: A zoo has 3 times as many terrestrial animals as aquatic animals and 122 more aquatic animals than amphibians.
        If there are 1633 animals in the zoo altogether, how many terrestrial animals are there?'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.number1 = randint(3,6)
        self.number3 = randint(50,100)
        self.number2 = randint(20,self.number3-20)
        self.total = self.number3 + self.number1*self.number3 + (self.number3-self.number2)
        self.variable = random.choice(['b','c','d','e','f','g','h','i','j','k','m','n','p','q','r','s','t','u','v','w','y','z'])
        
        self.problem = "A zoo has "+str(self.number1)+" times as many terrestrial animals as aquatic animals and "+str(self.number2)+" more aquatic animals than amphibians.<br><br>"
        self.problem = self.problem + "If there are "+str(self.total)+" animals in the zoo altogether, how many terrestrial animals are there?"
        
        self.answer = str(self.number1*self.number3)
        
        self.CheckAnswerType = 5
        self.unit = "terrestrial animals"
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType5(self.problem,self.answer,self.unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType5b",'CheckAnswerType':self.CheckAnswerType,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,"unit":self.unit}
        
    def ExplainType5(self,problem,answer,unit):
        self.answer_text = "The correct answer is: "+str(answer)+" "+unit
        self.solution_text = "For detailed explanation refer to Word Problem 2 at <a href='/Learn/Primary6/Algebra/Simplifying-and-Evaluating-Algebraic-Expressions#WP2' target='_blank'><u>Simplifying and Evaluating Algebraic Expressions</u></a>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemTypeMCQ6a(self):
        '''e.g: A memory card costs $69. A digital camera costs $16y more than the memory card. A tripod stand costs $y less than the memory card.
            If Eric bought all the three items, how much did he pay? Express your answer in terms of y.
        '''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.name = random.choice(PersonName.BoyName)
        self.memory = randint(20,100)
        self.multiplier1 = randint(10,20)
        self.multiplier2 = randint(10,18)
        self.camera = self.memory + self.multiplier1*self.multiplier2
        self.tripod = self.memory - self.multiplier2
        self.total = self.memory + self.camera + self.tripod
        
        self.variable = random.choice(['b','c','d','e','f','g','h','i','j','k','m','n','p','q','r','s','t','u','v','w','y','z'])
        
        self.problem = "A memory card costs $"+str(self.memory)+". A digital camera costs $"+str(self.multiplier1)+self.variable+" more than the memory card. A tripod stand costs $"+self.variable+" less than the memory card.<br><br>"
        self.problem = self.problem + "If "+self.name+" bought all the three items, how much did he pay in terms of "+self.variable+".<br><br>"
                    
        self.answer1 = "$"+str(3*self.memory)+" + $"+str(self.multiplier1-1)+self.variable
        self.answer = [0,self.answer1,1]
        
        self.problem_type = "ProblemTypeMCQ6a"
        self.template = "AlgebraFractionMCQTypeProblems.html"
        self.CheckAnswerType = 4
        self.grade = 6
        
        self.wrongAnswers = []
        self.wrongAnswers.append([0,"$"+str(2*self.memory)+" + $"+str(self.multiplier1-1)+self.variable,1])
        self.wrongAnswers.append([0,"$"+str(3*self.memory)+" - $"+str(self.multiplier1-1)+self.variable,1])
        self.wrongAnswers.append([0,"$"+str(3*self.memory)+" + $"+str(self.multiplier1)+self.variable,1])
        self.wrongAnswers.append([0,"$"+str(2*self.memory)+" - $"+str(self.multiplier1)+self.variable,1])         
        
        self.unit = ""
        self.dollar_unit = ""
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6(self.problem,self.answer1,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,
                                self.problem_type,self.CheckAnswerType,self.grade,self.complexity_level,self.HCScore)            
        
    def GenerateProblemType6b(self):
        '''e.g: A memory card costs $69. A digital camera costs $16y more than the memory card. A tripod stand costs $y less than the memory card.
        If the tripod stand cost $39, find the cost of the camera.'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.name = random.choice(PersonName.BoyName)
        self.memory = randint(20,100)
        self.multiplier1 = randint(10,20)
        self.multiplier2 = randint(10,18)
        self.camera = self.memory + self.multiplier1*self.multiplier2
        self.tripod = self.memory - self.multiplier2
        self.total = self.memory + self.camera + self.tripod
        
        self.variable = random.choice(['b','c','d','e','f','g','h','i','j','k','m','n','p','q','r','s','t','u','v','w','y','z'])
        
        self.problem = "A memory card costs $"+str(self.memory)+". A digital camera costs $"+str(self.multiplier1)+self.variable+" more than the memory card. A tripod stand costs $"+self.variable+" less than the memory card.<br><br>"
        self.problem = self.problem + "If the tripod stand cost $"+str(self.tripod)+", find the cost of the camera."
        
        self.answer = str(self.camera)
        
        self.CheckAnswerType = 5
        self.unit = ""
        self.dollar_unit = "$"
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType6(self.problem,self.answer,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType6b",'CheckAnswerType':self.CheckAnswerType,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,"unit":self.unit,"dollar_unit":"$"}
        
    def ExplainType6(self,problem,answer,unit,dollar_unit):
        self.answer_text = "The correct answer is: "+dollar_unit+str(answer)+" "+unit
        self.solution_text = "For detailed explanation refer to Word Problem 3 at <a href='/Learn/Primary6/Algebra/Simplifying-and-Evaluating-Algebraic-Expressions#WP3' target='_blank'><u>Simplifying and Evaluating Algebraic Expressions</u></a>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def GenerateProblemTypeMCQ7a(self):
        '''e.g: A bag of chips has a mass of q grams and a box of cookies has twice as much mass.
            Nur bought 3 bags of chips and some boxes of cookies. The total mass of the items she bought was 1.8 kg. What was the mass of cookies that she bought expressed in terms of q?
        '''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.name = random.choice(PersonName.GirlName)
        self.EachChipsMass = random.randrange(40,120,10)
        self.multiplier = randint(2,4)
        self.EachCookiesMass = self.multiplier * self.EachChipsMass
        self.chips = randint(3,6)
        self.cookies = randint(3,6)
        self.total = float(self.EachChipsMass*self.chips + self.EachCookiesMass*self.cookies)/1000
        
        self.variable = random.choice(['b','c','d','e','f','g','h','i','j','k','m','n','p','q','r','s','t','u','v','w','y','z'])
        
        self.problem = "A bag of chips has a mass of "+self.variable+" grams and a box of cookies has "+str(self.multiplier)+" times as much mass.<br><br>"
        self.problem = self.problem + self.name+" bought "+str(self.chips)+" bags of chips and some boxes of cookies. The total mass of the items she bought was "+str(self.total)+" kg. What was the mass of cookies that she bought expressed in terms of "+self.variable+"?<br><br>"
                    
        self.answer1 = "("+str(int(self.total*1000))+" - "+str(self.chips)+self.variable+") grams"  
        self.answer = [0,self.answer1,1]
        
        self.problem_type = "ProblemTypeMCQ7a"
        self.template = "AlgebraFractionMCQTypeProblems.html"
        self.CheckAnswerType = 4
        self.grade = 6
        
        self.wrongAnswers = []
        self.wrongAnswers.append([0,"("+str(int(self.total*1000))+" + "+str(self.chips)+self.variable+") grams",1])
        self.wrongAnswers.append([0,"("+str(self.total)+" - "+str(self.chips)+self.variable+") grams",1])
        self.wrongAnswers.append([0,"("+str(int(self.total*1000))+" - "+self.variable+") grams",1])
        self.wrongAnswers.append([0,"("+str(self.total)+" + "+str(self.chips)+self.variable+") grams",1])         
        
        self.unit = ""
        self.dollar_unit = ""
        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7(self.problem,self.answer1,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        
        return self.GenerateMCQ(self.wrongAnswers,self.problem,self.answer,self.template,self.explain,
                                self.problem_type,self.CheckAnswerType,self.grade,self.complexity_level,self.HCScore)            
        
    def GenerateProblemType7b(self):
        '''e.g: A bag of chips has a mass of q grams and a box of cookies has twice as much mass.
        Nur bought 3 bags of chips and some boxes of cookies. The total mass of the items she bought was 1.8 kg.
        If each bag of chips had a mass of 120 grams, how many boxes of cookies did she buy?'''
        
        self.complexity_level = "medium"
        self.HCScore = 5
        
        self.name = random.choice(PersonName.GirlName)
        self.EachChipsMass = random.randrange(40,120,10)
        self.multiplier = randint(2,4)
        self.EachCookiesMass = self.multiplier * self.EachChipsMass
        self.chips = randint(3,8)
        self.cookies = randint(3,8)
        self.total = float(self.EachChipsMass*self.chips + self.EachCookiesMass*self.cookies)/1000
        
        self.variable = random.choice(['b','c','d','e','f','g','h','i','j','k','m','n','p','q','r','s','t','u','v','w','y','z'])
        
        self.problem = "A bag of chips has a mass of "+self.variable+" grams and a box of cookies has "+str(self.multiplier)+" times as much mass.<br>"
        self.problem = self.problem + self.name+" bought "+str(self.chips)+" bags of chips and some boxes of cookies. The total mass of the items she bought was "+str(self.total)+" kg.<br>"
        self.problem = self.problem + "If each bag of chips had a mass of "+str(self.EachChipsMass)+" grams, how many boxes of cookies did she buy?"
        
        self.answer = str(self.cookies)
        
        self.CheckAnswerType = 5
        self.unit = "boxes of cookies"
        self.dollar_unit = ""
        self.template = "EnterTypeProblems.html"

        '''Explanation starts...'''
        self.explain_template = "Explanation.html"
        self.explain_text = self.ExplainType7(self.problem,self.answer,self.unit,self.dollar_unit)
        self.explain = {"explain_template":self.explain_template,"explain_text":self.explain_text}
        '''Explanation ends'''
        return {'problem':self.problem,'answer':self.answer,'template':self.template,'explain':self.explain,
                'problem_type':"ProblemType7b",'CheckAnswerType':self.CheckAnswerType,'grade':6,
                "complexity_level":self.complexity_level,"HCScore":self.HCScore,"unit":self.unit,"dollar_unit":self.dollar_unit}
        
    def ExplainType7(self,problem,answer,unit,dollar_unit):
        self.answer_text = "The correct answer is: "+dollar_unit+str(answer)+" "+unit
        self.solution_text = "For detailed explanation refer to Word Problem 4 at <a href='/Learn/Primary6/Algebra/Simplifying-and-Evaluating-Algebraic-Expressions#WP4' target='_blank'><u>Simplifying and Evaluating Algebraic Expressions</u></a>"
        self.explain = self.answer_text+"ANSWERSEPARATOR"+self.solution_text
                
        return self.explain

    def checkAnswer(self,template,answer,InputAnswer,CheckAnswer):
        if CheckAnswer==1:
            try:
                return string.join(answer.split(),"")==string.join(InputAnswer.split(),"")
            except ValueError:
                return False
        elif CheckAnswer==2:
            try:
                answer = string.join(answer.split(),"")
                answers = [str(answer).partition("+")[0],str(answer).partition("+")[2]]
                InputAnswer = string.join(InputAnswer.split(),"")
                InputAnswers = [str(InputAnswer).partition("+")[0],str(InputAnswer).partition("+")[2]]
                return InputAnswers[0] in answers and InputAnswers[1] in answers
            except ValueError:
                return False
        elif CheckAnswer==3:
            try:
                if "x" in InputAnswer:
                    InputAnswer1 = str(InputAnswer).partition("x")[0]+str(InputAnswer).partition("x")[2]
                    InputAnswer2 = str(InputAnswer).partition("x")[2]+str(InputAnswer).partition("x")[0]
                    return answer==InputAnswer1 or answer==InputAnswer2
                elif "*" in InputAnswer:
                    InputAnswer1 = str(InputAnswer).partition("*")[0]+str(InputAnswer).partition("*")[2]
                    InputAnswer2 = str(InputAnswer).partition("*")[2]+str(InputAnswer).partition("*")[0]
                    return answer==InputAnswer1 or answer==InputAnswer2
                elif len(str(InputAnswer))==2:
                    InputAnswer1 = str(InputAnswer)[0]+str(InputAnswer)[1]
                    InputAnswer2 = str(InputAnswer)[1]+str(InputAnswer)[0]
                    return answer==InputAnswer1 or answer==InputAnswer2
            except ValueError:
                return False
        elif CheckAnswer==4:
            try:
                answer=str(answer)
                return answer==InputAnswer
            except ValueError:
                return False
        elif CheckAnswer==5:
            try:
                return int(answer)==int(InputAnswer)
            except ValueError:
                return False            