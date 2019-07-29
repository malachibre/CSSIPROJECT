from google.appengine.ext import ndb
from google.appengine.api import users
from models import CRN
from models import seed_data
import jinja2
import webapp2
import os

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
    'all_courses': CRN.query().order(CRN.name).order(CRN.time).fetch(),
    'selected_courseList': [],
    'bld_locs': buildings
}

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template_dict['selected_courseList'] = []
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

class HomeHandler(webapp2.RequestHandler):
    def get(self):
        main_template = jinja_env.get_template("templates/mainpage.html")
        self.response.write(main_template.render(template_dict))

class SeedData(webapp2.RequestHandler):
    def get(self):
        seed_data()
        self.response.write("Data Stored")


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/home', HomeHandler),
    ('/redirect', RedirectHandler),
    ('/seeddata', SeedData)
], debug=True)
