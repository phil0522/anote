import webapp2
import logging

from anoteweb.model import Tag
from anoteweb.data import tag_dao
from anoteweb.util import mjson

class TagsServlet(webapp2.RequestHandler):
  def get(self):
    all_tags = tag_dao.get_all_tags()
    self.response.write(mjson.model2json(all_tags))

  def post(self):
    tag = self.request.body
    m = mjson.json2model(Tag, tag)
    logging.info("get tag: %s", m.to_dict())
    tag_dao.add_tag(m.tag_name)



class GetTasksServlet(webapp2.RequestHandler):
  """Send out taks in json format."""
  def get(self):
    self.response.headers['Content-Type'] = 'text/plain'
    self.response.write('Hello, World!')
    data = anote_pb2.Task()
    self.response.write(data)