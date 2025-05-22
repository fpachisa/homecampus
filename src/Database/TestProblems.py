'''
Module:TestProblems

Creates the test problems table in GAE.

This tables stores all the problem information of the test.

Version: 1.0

Created on May 18, 2012

Author:
   Farhat Pachisa (farhat@homecampus.com.sg)
   
Copyright:
    Copyright (c) 2012, Home Campus.  All Rights Reserved.

Usage:
'''

from google.appengine.ext import db

class TestProblems(db.Model):
    test_id = db.StringProperty(required =True)
    concept = db.StringProperty(required=True)
    counter = db.IntegerProperty(required=True)
    problem_type = db.StringProperty(required=True)
    problem = db.TextProperty()
    dollar_unit = db.StringProperty()
    unit = db.StringProperty()
    answer = db.StringProperty()
    answer_submitted = db.StringProperty(multiline=True)
    correct = db.BooleanProperty()
    time_taken = db.IntegerProperty()
    submit_date = db.DateTimeProperty()
    complexity_level = db.StringProperty()
    template = db.StringProperty()
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
    explain = db.TextProperty()
    CheckAnswerType = db.IntegerProperty()
    status = db.StringProperty()
    FunctionCall = db.TextProperty()
    FractionAnswer = db.StringProperty()


