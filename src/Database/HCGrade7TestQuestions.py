'''
Module:HCGrade7TestQuestions

Creates the HCGrade7TestQuestions table in GAE.

This tables stores the questions and answer details of Grade 7 Topical test questions for each students

Version: 1.0

Created on May 09, 2014

Author:
   Farhat Pachisa (farhat@homecampus.com.sg)
   
Copyright:
    Copyright (c) 2012, Home Campus.  All Rights Reserved.

Usage:
'''

from google.appengine.ext import db

class HCGrade7TestQuestions(db.Model):
    test_id = db.StringProperty(required=True)
    question_id = db.StringProperty(required=True)
    student_id = db.StringProperty(required=True)
    answer_id = db.StringProperty(required=True)
    entered_answer = db.StringProperty()
    correct = db.BooleanProperty()
    question_marks = db.IntegerProperty()
    scored_marks = db.IntegerProperty()



