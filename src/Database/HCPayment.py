'''
Module:HCPayment

Creates the HCPayment table in GAE.

This table stores the subscription information

Version: 1.0

Created on Aug 21, 2013

Author:
   Farhat Pachisa (farhat@homecampus.com.sg)
   
Copyright:
    Copyright (c) 2012, Home Campus.  All Rights Reserved.

Usage:
'''

from google.appengine.ext import db

class HCPayment(db.Model):
    transaction_id = db.StringProperty()
    transaction_type = db.StringProperty()
    payer_email = db.EmailProperty()
    next_payment_date = db.DateTimeProperty()
    payer_id = db.StringProperty()
    recurring_payment_id = db.StringProperty()
    payment_status = db.StringProperty()
    amount = db.StringProperty()
    paypal_fee = db.StringProperty()
    payment_date = db.DateTimeProperty()





