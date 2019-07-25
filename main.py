from google.appengine.ext import ndb
from google.appengine.api import users
import jinja2
import webapp2
import os




class CRN(ndb.Model):
    number = ndb.IntegerProperty(required = True)
    name = ndb.StringProperty(required = True)
    bld_num = ndb.IntegerProperty(required = True)
    days = ndb.StringProperty(repeated = True)

class User(ndb.Model):
    courses = ndb.KeyProperty(CRN, repeated = True)


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


jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

buildings = {
    '53': [33.9534, -83.3734],
    '56': [33.9533, -83.3750],
    '58': [33.9537, -83.3750],
    '66': [33.952464, -83.373337],
    '1033': [33.9445, -83.3732],
    '1013': [33.9468, -83.3725],
    '1040': [33.944286, -83.376376],
    '1057': [33.943493, -83.372294],
    '1023': [33.946172, -83.374900],
    '1038': [33.943775, -83.375888],
    '1020': [33.946335, -83.372167],
    '1061': [33.942677, -83.375055],
    '1031': [33.945368, -83.374211],
    '1035': [33.942813, -83.376395],
    '1010': [33.947191, -83.375226],
    '1003': [33.946059, -83.372616],
    '1060': [33.941970, -83.372879],
    '1001': [33.948742, -83.373993],
    '1041':  [33.944413, -83.375468],
}

template_dict = {
    'courses': {}
}

class MainHandler(webapp2.RequestHandler):
    def get(self):
        main_template = jinja_env.get_template("templates/mainpage.html")
        self.response.write(main_template.render(template_dict))

class RedirectHandler(webapp2.RequestHandler):
    def post(self):
        for i in range(1,6):
            key = "CRN" + str(i)
            num = self.request.get(key)
            if(len(str(num)) > 0):
                course = CRN.query().filter(CRN.number == int(num)).fetch()[0]
                template_dict['courses'][key] = [course.name, buildings[str(course.bld_num)]]

        redirect_template = jinja_env.get_template("templates/AddedCourse.html")
        self.response.write(redirect_template.render())

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/redirect', RedirectHandler),
], debug=True)
