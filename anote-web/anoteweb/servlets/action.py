"""
Base class for all actions.
"""
import webapp2
from anoteweb.data.anote_pb2 import Task

class Action(webapp2.RequestHandler):
  """ An action is an servlet who act like a normal function, but it always
  returns a proto as result. 
  """
  def get(self):
    "default get method"
    result = self.doGet()
    
    accept = self.request.headers.get('Accept', '')
    if accept == 'application/protobuf':
      self.response.write(result.SerializeToString())
    else:
      self.response.write(str(result))
      
  def doGet(self):
    pass
  
  def doPost(self):
    pass
  
  
class Demo(Action):
  def doGet(self):
    task = Task()
    task.task_id = 3
    task.title = "hello"
    task.ancestor.append(3)
    task.ancestor.append(5)
    return task
  
        