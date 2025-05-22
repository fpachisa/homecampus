'''
Module:CreateProblemsTable

Creates the problems table in sqlite3.

This tables stores all the information when student submits the answer to a problem.

Created on Jan 13, 2011

@author: Farhat
'''


#from google.appengine.api import users
from google.appengine.ext import db

class ProblemsTable(db.Model):
    student_id = db.StringProperty(required =True)
    grade = db.IntegerProperty(required =True)
    concept = db.StringProperty(required=True)
    problem = db.TextProperty()
    problem_type = db.StringProperty()
    answer = db.StringProperty()
    MCQ = db.BooleanProperty()
    correct = db.BooleanProperty()
    answer_submitted = db.StringProperty(multiline=True)
    time_taken = db.IntegerProperty()
    MCQAnswers = db.StringListProperty()
    submit_date = db.DateTimeProperty(auto_now=True)
    #Added on 27-Sep-2011
    complexity_level = db.StringProperty()
    HCScore = db.IntegerProperty()
    #Added on 02-Oct-2012 to generate the DetailProblemReport
    dollar_unit = db.StringProperty()
    unit = db.StringProperty()
    template = db.StringProperty()
    explain = db.TextProperty()
    FunctionCall = db.TextProperty()
    FractionAnswer = db.StringProperty()    
    answer1 = db.StringProperty()
    answer2 = db.StringProperty()
    answer3 = db.StringProperty()
    answer4 = db.StringProperty()
    answerM1 = db.StringProperty()
    answerM2 = db.StringProperty()
    answerM3 = db.StringProperty()
    answerM4 = db.StringProperty()    
    answerN1 = db.StringProperty()
    answerN2 = db.StringProperty()
    answerN3 = db.StringProperty()
    answerN4 = db.StringProperty()
    answerD1 = db.StringProperty()
    answerD2 = db.StringProperty()
    answerD3 = db.StringProperty()
    answerD4 = db.StringProperty()    
    value1 = db.StringProperty()
    value2 = db.StringProperty()
    value3 = db.StringProperty()
    value4 = db.StringProperty()
    CheckAnswerType = db.IntegerProperty()





