from google.appengine.ext import ndb
import jinja2
import webapp2


class CRN(ndb.Model):
    number = ndb.IntegerProperty(required = True)
    name = ndb.StringProperty(required = True)
    bld_num = ndb.IntegerProperty(required = True)
    days = ndb.StringProperty(repeated = True)

class User(ndb.Model):
    courses = ndb.KeyProperty(CRN, repeated = True)

def seed_data():
    C16043 = CRN(number = 16043, name = "ENGL1101", bld_num = 56, days = ['m', 'w', 'f'])
    C16043.put()

    C25093 = CRN(number = 25093, name= "ENGL1101", bld_num = 56, days = ['m', 'w', 'f'])
    C25093.put()

    C25094 = CRN(number = 25094, name= "ENGL1101", bld_num = 56, days = ['m', 'w', 'f'])
    C25094.put()

    C15353 = CRN(number = 15353, name= "MATH1113", bld_num = 1033, days = ['t', 'r'])
    C15353.put()

    C15356 = CRN(number = 15356, name= "MATH1113", bld_num = 1013, days = ['m', 'w', 'f'])
    C15356.put()

    C15359 = CRN(number = 15359, name= "MATH1113", bld_num = 1040, days = ['m', 'w', 'f'])
    C15359.put()

    C22591 = CRN(number = 22591, name= "HIST2112", bld_num = 66, days = ['t', 'r'])
    C22591.put()

    C25894 = CRN(number = 25894, name= "HIST2112", bld_num = 66, days = ['m', 'w'])
    C25894.put()

    C42135 = CRN(number = 42135, name= "HIST2111", bld_num = 58, days = ['m', 'w'])
    C42135.put()

    C33739 = CRN(number = 33739, name="HIST2111", bld_num = 66, days = ['t', 'r'])
    C33739.put()

    C10065 = CRN(number = 10065, name= "BIOL1103", bld_num = 1035, days = ['t', 'r'])
    C10065.put()

    C10098 = CRN(number = 10098, name="BIOL1103", bld_num = 1035, days = ['m', 'w', 'f'])
    C10098.put()
    
