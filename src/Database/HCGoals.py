'''
Module:HCGoals

Creates the HCGoals table in GAE.

This tables stores all the goals information for a student.

Version: 1.0

Created on Oct 08, 2012

Author:
   Farhat Pachisa (farhat@homecampus.com.sg)
   
Copyright:
    Copyright (c) 2012, Home Campus.  All Rights Reserved.

Usage:
'''

from google.appengine.ext import db

class HCGoals(db.Model):
    student_id = db.StringProperty(required =True)
    grade = db.IntegerProperty()
    topic = db.StringProperty()
    subTopic = db.StringProperty()
    goalName = db.StringProperty()
    target = db.IntegerProperty()
    created_by = db.StringProperty()
    create_date = db.DateTimeProperty()
    update_date = db.DateTimeProperty()
    update_by = db.StringProperty()
    complete_date = db.DateTimeProperty()
    status = db.StringProperty()
    





