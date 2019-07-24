import webapp2
import os
import jinja2

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

buildings = {
    '53': [33.9534, -83.3734],
    '56': [33.9533, -83.3750],
    '58': [33.9537, -83.3750],
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


class MainHandler(webapp2.RequestHandler):
    def get(self):
        main_template = jinja_env.get_template("templates/mainpage.html")
        self.response.write(main_template.render())

class RedirectHandler(webapp2.RequestHandler):
    def get(self):
        redirect_template = jinja_env.get_template("templates/AddedCourse.html")
        self.response.write(redirect_template.render())

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/redirect', RedirectHandler),
], debug=True)
