"""hello world app"""
import webapp2

import sys

from anoteweb.servlets.action import Demo
from anoteweb.servlets.tasks import TagsServlet

class MainPage(webapp2.RequestHandler):
  """Handler for MainPage."""

  def get(self):
    "default get method"
    self.response.headers['Content-Type'] = 'text/plain'
    self.response.write('Hello, World!'     )
    self.response.write(sys.path)

    print self.request.headers


application = webapp2.WSGIApplication(
                                      [('/', MainPage),
                                       ('/apiv1/tags*', TagsServlet)], debug=True)



