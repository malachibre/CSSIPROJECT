import webapp2
import os
import jinja2

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

buildings = {
    '53': [33.9534, 83.3734],
    '56': 'Park Hall',
    '58': 'Sanford Hall',
    '1033': 'Ecology',
    '1013': 'Poultry Science',
    '1040': 'Forestry Resources 1',
    '1057': 'Davison Life Sciences Complex',
    '1023': 'Boyd Graduate Research Center',
    '1038': 'Pharmacy South',
    '1020': 'Food Science Building',
    '1061': 'Miller Plant Science',
    '1033': 'Ecology',
    '1031': 'Hardman Hall',
    '1035': 'Science Learning Center'
    '1010': 'Speirs Hall',
    '1003': 'Physics Bulding',
    '1060': 'Aderhold',
    '1001': 'Chemistry',
    '1041':  'R. C. Wilson Pharmacy'
}


class MainHandler(webapp2.RequestHandler):
    def get(self):
        main_template = jinja_env.get_template("templates/mainpage.html")
        self.response.write(main_template.render())

app = webapp2.WSGIApplication([
    ('/', MainHandler),
], debug=True)
