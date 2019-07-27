from google.appengine.ext import ndb
from google.appengine.api import users
from models import CRN
from models import seed_data
import jinja2
import webapp2
import os

C16043 = CRN(number = 16043, name = "ENGL1101", bld_num = 56, days = ['m', 'w', 'f'], time = "08:00am-08:50am")
C16043.put()

C25093 = CRN(number = 25093, name= "ENGL1101", bld_num = 56, days = ['m', 'w', 'f'], time = "09:05am-09:55am")
C25093.put()

C25094 = CRN(number = 25094, name= "ENGL1101", bld_num = 56, days = ['m', 'w', 'f'], time = "10:10am-11:00am")
C25094.put()

C15353 = CRN(number = 15353, name= "MATH1113", bld_num = 1033, days = ['t', 'r'], time = "12:30pm-01:45pm")
C15353.put()

C15356 = CRN(number = 15356, name= "MATH1113", bld_num = 1013, days = ['m', 'w', 'f'], time = "02:30pm-03:20pm")
C15356.put()

C15359 = CRN(number = 15359, name= "MATH1113", bld_num = 1040, days = ['m', 'w', 'f'], time = "11:15am-12:05pm")
C15359.put()

C22591 = CRN(number = 22591, name= "HIST2112", bld_num = 66, days = ['t', 'r'], time = "1:00pm-2:15pm")
C22591.put()

C25894 = CRN(number = 25894, name= "HIST2112", bld_num = 66, days = ['m', 'w'], time = "11:15am-12:05pm")
C25894.put()

C42135 = CRN(number = 42135, name= "HIST2111", bld_num = 58, days = ['m', 'w'], time = "10:10am-11:00am")
C42135.put()

C33739 = CRN(number = 33739, name="HIST2111", bld_num = 66, days = ['t', 'r'], time = "11:00am-12:15pm")
C33739.put()

C10065 = CRN(number = 10065, name= "BIOL1103", bld_num = 1035, days = ['t', 'r'], time = "09:30am-10:45am")
C10065.put()

C10098 = CRN(number = 10098, name="BIOL1103", bld_num = 1035, days = ['m', 'w', 'f'], time = "10:10am-11:00am")
C10098.put()

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

buildings = {
    53: [33.9534, -83.3734],
    56: [33.9533, -83.3750],
    58: [33.9537, -83.3750],
    66: [33.952464, -83.373337],
    1033: [33.9445, -83.3732],
    1013: [33.9468, -83.3725],
    1040: [33.944286, -83.376376],
    1057: [33.943493, -83.372294],
    1023: [33.946172, -83.374900],
    1038: [33.943775, -83.375888],
    1020: [33.946335, -83.372167],
    1061: [33.942677, -83.375055],
    1031: [33.945368, -83.374211],
    1035: [33.942813, -83.376395],
    1010: [33.947191, -83.375226],
    1003: [33.946059, -83.372616],
    1060: [33.941970, -83.372879],
    1001: [33.948742, -83.373993],
    1041:  [33.944413, -83.375468],
}

template_dict = {
    'all_courses': CRN.query().fetch(),
    'selected_courseList': [],
    'bld_locs': buildings
}

class MainHandler(webapp2.RequestHandler):
    def get(self):
        main_template = jinja_env.get_template("templates/mainpage.html")
        self.response.write(main_template.render(template_dict))

class RedirectHandler(webapp2.RequestHandler):
    def post(self):
        all_courses = template_dict['all_courses']
        selected = []
        for course in all_courses:
            key = "CRN" + str(course.number)
            if self.request.get(key):
                selected.append(course)
                print(key)
        redirect_template = jinja_env.get_template("templates/AddedCourse.html")
        template_dict['selected_courseList'] = selected
        self.response.write(redirect_template.render(template_dict))

class SeedData(webapp2.RequestHandler):
    def get(self):
        seed_data()
        self.response.write("Data Stored")


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/redirect', RedirectHandler),
    ('/seeddata', SeedData)
], debug=True)
