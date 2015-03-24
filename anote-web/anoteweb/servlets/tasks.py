import webapp2
import logging

from anoteweb.model import Tag, Project
from anoteweb.data import tag_dao
from anoteweb.data import project_dao
from anoteweb.util import mjson

class TagServlet(webapp2.RequestHandler):
  def get(self):
    all_tags = tag_dao.get_all_tags()
    self.response.write(mjson.model2json(all_tags))

  def post(self):
    tag = self.request.body
    m = mjson.json2model(Tag, tag)
    logging.info("get tag: %s", m.to_dict())
    saved = tag_dao.add_tag(m.tag_name)
    self.response.write(mjson.model2json(saved))

  def delete(self):
    keystr = self.request.get("key", "")
    if keystr:
      tag_dao.remove_tag(keystr)

class ProjectServlet(webapp2.RequestHandler):
  def get(self):
    all_projects = project_dao.get_all()
    self.response.write(mjson.model2json(all_projects))

  def post(self):
    project = self.request.body
    m = mjson.json2model(Project, project)
    logging.info("get project: %s", m.to_dict())
    saved = project_dao.add(m.project_name)
    self.response.write(mjson.model2json(saved))

  def delete(self):
    keystr = self.request.get("key", "")
    if keystr:
      project_dao.remove(keystr)


class GetTasksServlet(webapp2.RequestHandler):
  """Send out taks in json format."""
  def get(self):
    self.response.headers['Content-Type'] = 'text/plain'
    self.response.write('Hello, World!')
    data = anote_pb2.Task()
    self.response.write(data)