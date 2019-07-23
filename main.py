import webapp2
import os
import jinja2

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class MainHandler(webapp2.RequestHadler):
    def get(self):
        main_template = jinja_env.get_templates("templates/mainpage.html")
        self.response.write(tepm)
