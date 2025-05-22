'''
Module:HCClass

Creates the HCClass table in GAE.

This tables stores the class information.

Version: 1.0

Created on Sep 09, 2013

Author:
   Farhat Pachisa (farhat@homecampus.com.sg)
   
Copyright:
    Copyright (c) 2012, Home Campus.  All Rights Reserved.

Usage:
'''

from google.appengine.ext import db

class HCClass(db.Model):
    teacher_username = db.StringProperty(required =True)
    class_name = db.StringProperty(required =True)
    class_skill = db.StringProperty()
    create_date = db.DateTimeProperty(auto_now=True)




