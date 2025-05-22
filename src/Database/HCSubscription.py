'''
Module:HCSubscription

Creates the HCSubscription table in GAE.

This table stores the subscription information

Version: 1.0

Created on Dec 16, 2012

Author:
   Farhat Pachisa (farhat@homecampus.com.sg)
   
Copyright:
    Copyright (c) 2012, Home Campus.  All Rights Reserved.

Usage:
'''

from google.appengine.ext import db

class HCSubscription(db.Model):
    paypal_token = db.StringProperty(required =True)
    student_id = db.StringProperty(required =True)
    start_date = db.DateTimeProperty(required=True)
    end_date = db.DateTimeProperty(required=True)
    amount = db.StringProperty(required=True)
    period = db.IntegerProperty(required=True)
    status = db.StringProperty(required=True)
    transaction_id = db.StringProperty()
    email = db.EmailProperty()
    country_code = db.StringProperty()
    paypal_fee = db.StringProperty()
    profile_id = db.StringProperty()
    student_number = db.IntegerProperty()





