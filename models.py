from google.appengine.ext import ndb
import jinja2
import webapp2


class CRN(ndb.Model):
    bld_num = ndb.StringProperty(required = True)
    days = ndb.StringProperty(required = True, repeated = True)
    times = ndb.DatetTimeProperty(required = False)

class User(ndb.Model):
    courses = ndb.KeyProperty(CRN, repeated = True)
