'''
Module:HCGrade7TestMaster

Creates the HCGrade7TestMaster table in GAE.

This tables stores the details of Grade 7 topical tests for each students

Version: 1.0

Created on May 09, 2014

Author:
   Farhat Pachisa (farhat@homecampus.com.sg)
   
Copyright:
    Copyright (c) 2012, Home Campus.  All Rights Reserved.

Usage:
'''

from google.appengine.ext import db

class HCGrade7TestMaster(db.Model):
    test_id = db.StringProperty(required=True)
    test_topic = db.StringProperty(required=True)
    student_id = db.StringProperty(required=True)
    start_date = db.DateTimeProperty(required=True)
    end_date = db.DateTimeProperty()
    test_score = db.IntegerProperty()
    total_marks = db.IntegerProperty()
    test_status = db.StringProperty(required=True)
    elapsed_time = db.IntegerProperty(required=True)
    attempt = db.IntegerProperty()



