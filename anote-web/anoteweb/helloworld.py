import webapp2
import sys
import os

def fix_path():
    # credit:  Nick Johnson of Google
    sys.path.append(os.path.join(os.path.dirname(__file__), 'genfiles'))

class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World!')
        self.response.write(sys.path)

fix_path()
application = webapp2.WSGIApplication([
                                       ('/', MainPage),], debug=True)
