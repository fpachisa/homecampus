'''
Module:HCStudents

Creates the HCStudents table in GAE.

This tables stores the students--class information.

Version: 1.0

Created on Sep 10, 2013

Author:
   Farhat Pachisa (farhat@homecampus.com.sg)
   
Copyright:
    Copyright (c) 2012, Home Campus.  All Rights Reserved.

Usage:
'''

from google.appengine.ext import db

class HCStudents(db.Model):
    teacher_username = db.StringProperty(required =True)
    class_name = db.StringProperty(required =True)
    student_first_name = db.StringProperty(required=True)
    student_last_name = db.StringProperty(required=True)
    student_username = db.StringProperty(required=True)
    join_date = db.DateTimeProperty(auto_now=True)
    student_rollno = db.IntegerProperty(required=True)



