import webapp2
import logging

from anoteweb.model import Tag, Project, Task
from anoteweb.data import tag_dao
from anoteweb.data import project_dao
from anoteweb.data import task_dao
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


class TaskServlet(webapp2.RequestHandler):
  """Send out taks in json format."""
  def get(self):
    all_tasks = task_dao.GetAllActionableTasks()
    self.response.write(mjson.model2json(all_tasks))

  def post(self):
    """Update task status and append notes."""
    task = self.request.body
    m = mjson.json2model(Task, task)

    logging.info("get task update: %s", m.to_dict())

    # Get stored one from db
    saved = m.key.get()

    saved.priority = m.priority
    saved.title = m.title
    saved.status = m.status
    saved.project = m.project
    saved.tags = m.tags

    if saved.notes[-1].text != m.notes[0].text:
      saved.notes.append(m.notes[0])
    saved.put()

  def put(self):
    """Creates a new task."""
    task = self.request.body
    m = mjson.json2model(Task, task)
    saved_key = task_dao.Save(m)

    self.response.write(saved_key)
