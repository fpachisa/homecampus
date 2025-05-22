'''
Module:HCSchoolInfo

Creates the school info table in GAE.

This tables stores all the master information of the schools registered with HC.

Version: 1.0

Created on Sep 03, 2013

Author:
   Farhat Pachisa (farhat@homecampus.com.sg)
   
Copyright:
    Copyright (c) 2012, Home Campus.  All Rights Reserved.

Usage:
'''

from google.appengine.ext import db

class HCSchoolInfo(db.Model):
    teacher_username = db.StringProperty()
    school_name = db.StringProperty()
    school_city = db.StringProperty()
    school_country = db.StringProperty()




