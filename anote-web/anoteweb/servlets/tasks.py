import webapp2

from ..proto import task_pb2

class GetTasksServlet(webapp2.RequestHandler):
  """Send out taks in json format."""
  def get(self):
    self.response.headers['Content-Type'] = 'text/plain'
    self.response.write('Hello, World!')
    data = task_pb2.Task()
    self.response.write(data)