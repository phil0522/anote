""" Hello world python. """

import sys
import os

import webapp2

def fix_path():
  """Add genfiles directory to python path."""
  # credit:  Nick Johnson of Google
  sys.path.append(os.path.join(os.path.dirname(__file__), 'genfiles'))

class MainPage(webapp2.RequestHandler):
  """Main page handler."""

  def get(self):
    """For both get and post hander"""
    self.response.headers['Content-Type'] = 'text/plain'
    self.response.write('Hello, World!')
    self.response.write(sys.path)
 

fix_path()
Application = webapp2.WSGIApplication([('/', MainPage),], debug=True)
