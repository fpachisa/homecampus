'''
Created on Jan 14, 2011

@author: Farhat
'''


from google.appengine.ext import db
from Database import SubmitProblemsTable

def DeleteRecords():
    updated = []
    for entity in SubmitProblemsTable.ProblemsTable.all().fetch(1000):
        updated.append(entity)
    db.delete(updated)
    
