import unittest

#WebTest framework is need
#THis can be installed by "easy_install WebTest"
import webapp2
import webtest

from anoteweb.servlets import action
from anoteweb.data import anote_pb2
  
class MockAction(action.Action):
  def doGet(self):
    msg = anote_pb2.Task()
    msg.task_id = 3
    return msg
  
class ActionTest(unittest.TestCase):
  def setUp(self):
    app = webapp2.WSGIApplication([('/', MockAction)])
    self.testapp = webtest.TestApp(app)
  
  def testGet(self):
    response = self.testapp.get('/')
    self.assertEqual(200, response.status_int)
    print dir(response)
    print response.normal_body
    print response.content_type
    