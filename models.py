from google.appengine.ext import ndb


class CRN(ndb.Model):
    bld_num = ndb.StringProperty(required = True)
    days = ndb.StringProperty(required = True, repeated = True)
    times = ndb.DatetTimeProperty(required = True)

class User(ndb.Model):
    courses = ndb.KeyProperty(CRN, repeated = True)
