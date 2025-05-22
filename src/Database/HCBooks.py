'''
Module:HCBooks

Creates the HCBooks table in GAE.

This tables provides user access to HC books

Version: 1.0

Created on Jul 12, 2014

Author:
   Farhat Pachisa (farhat@homecampus.com.sg)
   
Copyright:
    Copyright (c) 2012, Home Campus.  All Rights Reserved.

Usage:
'''

from google.appengine.ext import db

class HCBooks(db.Model):
    book_code = db.StringProperty(required=True)
    book_name = db.StringProperty(required=True)
    username = db.StringProperty(required=True)
    email = db.EmailProperty()
    start_date = db.DateTimeProperty()
    end_date = db.DateTimeProperty()
    authorized = db.BooleanProperty(default=False)
    amount = db.StringProperty(required=True)
    status = db.StringProperty() 
    paypal_token = db.StringProperty(required =True)
    transaction_id = db.StringProperty()
    country_code = db.StringProperty()
    paypal_fee = db.StringProperty()



