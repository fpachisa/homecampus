'''
Module:HCGrade7Questions

Creates the HCGrade7Questions table in GAE.

This tables stores the questions and answer details of Grade 7 questions for each students

Version: 1.0

Created on Apr 22, 2014

Author:
   Farhat Pachisa (farhat@homecampus.com.sg)
   
Copyright:
    Copyright (c) 2012, Home Campus.  All Rights Reserved.

Usage:
'''

from google.appengine.ext import db

class HCGrade7Questions(db.Model):
    question_id = db.StringProperty(required=True)
    question_type = db.StringProperty(required=True)
    student_id = db.StringProperty(required=True)
    answer_id = db.StringProperty(required=True)
    entered_answer = db.StringProperty()
    submitted = db.BooleanProperty(default=False)
    save_date = db.DateTimeProperty()
    submit_date = db.DateTimeProperty()
    correct = db.BooleanProperty()



