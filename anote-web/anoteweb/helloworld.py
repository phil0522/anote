"""hello world app"""
import webapp2
import sys

from anoteweb.servlets.tasks import TagServlet, ProjectServlet

class MainPage(webapp2.RequestHandler):
  """Handler for MainPage."""

  def get(self):
    "default get method"
    self.response.headers['Content-Type'] = 'text/plain'
    self.response.write('Hello, World!')
    self.response.write(sys.path)

    print self.request.headers


application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/apiv1/tag', TagServlet),
    ('/apiv1/project', ProjectServlet)], debug=True)



