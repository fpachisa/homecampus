'''
Created on 06-Jan-2017
'''
from tipfy import RequestHandler, Rule, Tipfy, Response
from Config import config
from tipfy.auth import UserRequiredIfAuthenticatedMiddleware,admin_required
from tipfy.sessions import SessionMiddleware
from tipfyext.jinja2 import Jinja2Mixin
import logging
import os
from google.appengine.api import taskqueue, app_identity
from Models import HomeCampusUser

import csv
import cloudstorage as gcs


rules = [
         Rule(r'/task/extractEmails/', handler='extractEmailsPR.TriggerExtract'),
         Rule(r'/task/extractEmails/Worker', handler='extractEmailsPR.Worker')
        ]

class BaseHandler(RequestHandler, Jinja2Mixin):
    middleware = [SessionMiddleware(), UserRequiredIfAuthenticatedMiddleware()]
    def render_response(self, filename, **kwargs):
        return super(BaseHandler, self).render_response(filename, **kwargs)

    

class TriggerExtract(BaseHandler):
    @admin_required
    def get(self):
        return self.render_response("extractTrigger.html")
    
    @admin_required
    def post(self):
        task = taskqueue.add(
            url="/task/extractEmails/Worker",
            method="get",
            params={'cursor': ''}
            )
        return Response("Task {} enqueued, ETA {}".format(task.name, task.eta))
        

class Worker(RequestHandler):
    BATCH_SIZE = 100
    
    def get(self):
        # Get the cursor 
        cursor = self.request.args.get("cursor")
        start_pos = self.request.args.get("_s") or 0
        start_pos = int(start_pos)
        
        # Create the query --(Only for Parents)
        query = HomeCampusUser.all().with_cursor(start_cursor=cursor)
        retrieved=0     # Line 69
        csv = [["FirstName", "LastName", "Email"]]   # List of Lists for the csv module
        for user in query.run(limit=self.BATCH_SIZE):
            row = [user.first_name.encode("utf-8"), user.last_name, user.email]
            csv.append(row)
            retrieved = retrieved + 1
        
        # Data read
        # now dump it to csv file 
        filename = self.getBucket() + "/PRData-{}--{}__{}.csv".format(str(start_pos), str(start_pos+retrieved), str(retrieved))
        self.writeCSV(filename, csv)
        
        # If retrieved size is equal to batch then it maybe possible
        # that there is more data
        # Doing this because old DB queries don't support pagination as offered by NDB
        more = retrieved == self.BATCH_SIZE
        nxt = query.cursor()
        _s = start_pos + retrieved
        if more and not _s>1000:
            task = taskqueue.add(
                url="/task/extractEmails/Worker",
                method="get",
                params={'cursor': nxt, "_s": str(_s)}
                )
            
        return Response("Sucess")
    
    def encodeToUTF(self, str):
        return ""
    
    def getBucket(self):
        return "/" + app_identity.get_default_gcs_bucket_name()
        
    def getGCSFile(self, filename):
        return gcs.open(filename, mode="w", content_type="text/csv")
    
    def writeCSV(self, filename, data):
        _file = self.getGCSFile(filename)
        csvWriter = csv.writer(_file)
        logging.info(data)
        for row in data:
            try:
                csvWriter.writerow(row)
            except Exception:   # Unicode Errors can occur for names or emails written in some non-english language
                pass
        _file.close()
        
        
app = Tipfy(rules=rules, config=config)    

def main():
    app.run()
    
if __name__ == "__main__":
    main()