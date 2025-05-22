'''
Module:TestsMaster

Creates the tests master table in GAE.

This tables stores all the master information of the test.

Version: 1.0

Created on May 18, 2012

Author:
   Farhat Pachisa (farhat@homecampus.com.sg)
   
Copyright:
    Copyright (c) 2012, Home Campus.  All Rights Reserved.

Usage:
'''

from google.appengine.ext import db

class TestsMasterTable(db.Model):
    test_id = db.StringProperty(required =True)
    test_name = db.StringProperty(required =True)
    student_id = db.StringProperty(required =True)
    grade = db.IntegerProperty(required =True)
    concept = db.StringProperty(required = True)
    sub_concept = db.StringProperty()
    created_by = db.StringProperty(required =True)
    create_date = db.DateTimeProperty()
    update_date = db.DateTimeProperty()
    complete_date = db.DateTimeProperty()
    status = db.StringProperty()
    questions = db.IntegerProperty(required = True)
    score = db.IntegerProperty()
    answered = db.IntegerProperty()
    '''This is used to diplay the green/red color on test page'''
    TestIndicator = db.StringListProperty()





