'''
Module:HCResetPassword

Creates the HCResetPassword table in GAE.

This tables stores the reset password link.

Version: 1.0

Created on Feb 24, 2014

Author:
   Farhat Pachisa (farhat@homecampus.com.sg)
   
Copyright:
    Copyright (c) 2012, Home Campus.  All Rights Reserved.

Usage:
'''

from google.appengine.ext import db

class HCResetPassword(db.Model):
    username = db.StringProperty(required=True)
    email = db.EmailProperty(required=True)
    reset_key = db.StringProperty(required=True)
    IsChild = db.BooleanProperty(default=False)
    IsParent = db.BooleanProperty(default=False)
    create_date = db.DateTimeProperty(auto_now=True)
    expiry_date = db.DateTimeProperty(required=True)
    password_changed = db.BooleanProperty(default=False)




