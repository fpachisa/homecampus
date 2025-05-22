from tipfy.appengine.auth.model import User
from google.appengine.ext import db

class HomeCampusUser(User):
    authorized = db.BooleanProperty(default=False)
    active = db.BooleanProperty(default=True)
    IsParent = db.BooleanProperty(default=False)
    first_name = db.StringProperty(required=False)
    last_name = db.StringProperty(required=False)
    parent_first_name = db.StringProperty(required=False)
    parent_last_name = db.StringProperty(required=False)
    skill = db.StringProperty(required=False)
    IsTeacher = db.BooleanProperty(default=False)
    school_code = db.StringProperty(required=False)