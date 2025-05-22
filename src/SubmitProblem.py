'''
Module:CreateProblemsTable

Stores the problem information in table Problems

Created on Jan 13, 2011

@author: Farhat
'''

from Database import SubmitProblemsTable 

class SubmitProblem(object):
    
    def __init__(self,problemDict):
        self.student_id = problemDict["student_id"]
        self.concept = str(problemDict["concept"])
        self.problem = problemDict["problem"]
        self.problem_type = problemDict["problem_type"]
        self.answer = str(problemDict["answer"])
        try:
            self.grade = problemDict["grade"]
        except KeyError:
            self.grade = None
        try:
            self.answer_submitted = str(problemDict["answer_submitted"])
        except KeyError:
            self.answer_submitted = None
        try:
            self.correct = problemDict["correct"]
        except KeyError:
            self.correct = None
        try:
            self.time_taken = problemDict["time_taken"]
        except KeyError:
            self.time_taken = None
        try:
            self.complexity_level = problemDict["complexity_level"]
        except KeyError:
            self.complexity_level = None
        try:
            self.HCScore = problemDict["HCScore"]
        except KeyError:
            self.HCScore = None
        try:
            self.dollar_unit = problemDict["dollar_unit"]
        except KeyError:
            self.dollar_unit = None            
        try:
            self.unit = problemDict["unit"]
        except KeyError:
            self.unit = None
        self.template = problemDict["template"]
        try:
            self.answer1 = problemDict["answer1"]
        except KeyError:
            self.answer1 = None            
        try:
            self.answer2 = problemDict["answer2"]
        except KeyError:
            self.answer2 = None
        try:
            self.answer3 = problemDict["answer3"]
        except KeyError:
            self.answer3 = None
        try:    
            self.answer4 = problemDict["answer4"]
        except KeyError:
            self.answer4 = None
        try:
            self.answerM1 = problemDict["answerM1"]
        except KeyError:
            self.answerM1 = None            
        try:
            self.answerM2 = problemDict["answerM2"]
        except KeyError:
            self.answerM2 = None
        try:
            self.answerM3 = problemDict["answerM3"]
        except KeyError:
            self.answerM3 = None
        try:    
            self.answerM4 = problemDict["answerM4"]
        except KeyError:
            self.answerM4 = None
        try:
            self.answerN1 = problemDict["answerN1"]
        except KeyError:
            self.answerN1 = None            
        try:
            self.answerN2 = problemDict["answerN2"]
        except KeyError:
            self.answerN2 = None
        try:
            self.answerN3 = problemDict["answerN3"]
        except KeyError:
            self.answerN3 = None
        try:    
            self.answerN4 = problemDict["answerN4"]
        except KeyError:
            self.answerN4 = None
        try:
            self.answerD1 = problemDict["answerD1"]
        except KeyError:
            self.answerD1 = None            
        try:
            self.answerD2 = problemDict["answerD2"]
        except KeyError:
            self.answerD2 = None
        try:
            self.answerD3 = problemDict["answerD3"]
        except KeyError:
            self.answerD3 = None
        try:    
            self.answerD4 = problemDict["answerD4"]
        except KeyError:
            self.answerD4 = None
            
        try:
            self.value1 = problemDict["value1"]
        except KeyError:
            self.value1 = None
        try:
            self.value2 = problemDict["value2"]
        except KeyError:
            self.value2 = None
        try:
            self.value3 = problemDict["value3"]
        except KeyError:
            self.value3 = None
        try:
            self.value4 = problemDict["value4"]
        except KeyError:
            self.value4 = None

        try:
            self.explain = problemDict["explain"]
        except KeyError:
            self.explain = None
        
        try:
            self.FunctionCall = problemDict["FunctionCall"]
        except KeyError:
            self.FunctionCall = None
        try:    
            self.FractionAnswer = problemDict["FractionAnswer"]
        except KeyError:
            self.FractionAnswer = None
        try:    
            self.submit = problemDict["submit"]
        except KeyError:
            self.submit = None
        try:    
            self.CheckAnswerType = problemDict["CheckAnswerType"]
        except KeyError:
            self.CheckAnswerType = 1
                    
        problem = SubmitProblemsTable.ProblemsTable(student_id=self.student_id,
                                                    grade=self.grade,
                                                    concept=self.concept,
                                                    problem=self.problem,
                                                    problem_type=self.problem_type,
                                                    answer=self.answer,
                                                    answer_submitted=self.answer_submitted,
                                                    correct=self.correct,
                                                    time_taken=self.time_taken,
                                                    complexity_level=self.complexity_level,
                                                    HCScore=self.HCScore,
                                                    dollar_unit = self.dollar_unit,
                                                    unit = self.unit,
                                                    template = self.template,
                                                    explain = self.explain,
                                                    FunctionCall = self.FunctionCall,
                                                    FractionAnswer = self.FractionAnswer,
                                                    answer1 = self.answer1,
                                                    answer2 = self.answer2,
                                                    answer3 = self.answer3,
                                                    answer4 = self.answer4, 
                                                    answerM1 = self.answerN1,
                                                    answerM2 = self.answerN2,
                                                    answerM3 = self.answerN3,
                                                    answerM4 = self.answerN4, 
                                                    answerN1 = self.answerM1,
                                                    answerN2 = self.answerM2,
                                                    answerN3 = self.answerM3,
                                                    answerN4 = self.answerM4, 
                                                    answerD1 = self.answerD1,
                                                    answerD2 = self.answerD2,
                                                    answerD3 = self.answerD3,
                                                    answerD4 = self.answerD4,
                                                    value1 = self.value1,
                                                    value2 = self.value2,
                                                    value3 = self.value3,
                                                    value4 = self.value4,
                                                    submit = self.submit,
                                                    CheckAnswerType = self.CheckAnswerType, 
                                                    )
        problem.put()
