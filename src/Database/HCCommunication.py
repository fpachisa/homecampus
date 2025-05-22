'''
Module:HCCommunication

Creates the communication table in GAE.

This tables stores all the communication email information sent to the user.

Version: 1.0

Created on May 23, 2013

Author:
   Farhat Pachisa (farhat@homecampus.com.sg)
   
Copyright:
    Copyright (c) 2012, Home Campus.  All Rights Reserved.

Usage:
'''

from google.appengine.ext import db

class HCCommunication(db.Model):
    email = db.EmailProperty()
    UnsubscriptionKey = db.StringProperty()
    unsubscribed = db.BooleanProperty(default=False)
    LastCommunicationKey = db.StringProperty() # this one is required so that duplicate comm is not send
    UpdateDate = db.DateTimeProperty(auto_now=True)
    ActiveUnsubscribedReportdate = db.DateTimeProperty() # this one is required so that active unsubscribed report is send only every 15 days 
    UnfinishedWorksheetReportdate = db.DateTimeProperty()
    IncompleteTransactionReportdate = db.DateTimeProperty()



