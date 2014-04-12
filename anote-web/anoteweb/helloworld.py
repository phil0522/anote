"""hello world app"""

import webapp2
import sys
import os

def fix_path():
  """fix the path."""
  # credit:  Nick Johnson of Google
  sys.path.append(os.path.join(os.path.dirname(__file__), 'genfiles'))

class MainPage(webapp2.RequestHandler):
  """Handler for MainPage."""

  def get(self):
    "default get method"
    self.response.headers['Content-Type'] = 'text/plain'
    self.response.write('Hello, World!')
    self.response.write(sys.path)

fix_path()
application = webapp2.WSGIApplication([('/', MainPage),], debug=True)

