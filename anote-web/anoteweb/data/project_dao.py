""" Dao object for project. """
from google.appengine.ext import ndb
from anoteweb.model import Project


def get_all():
  """Gets all tags."""
  tags = Project.query().fetch(10000)
  return tags

def add(project_name):
  """Add a project_name."""
  model = Project()
  model.project_name = project_name
  model.put()
  return model

def remove(keystr):
  key = ndb.Key(urlsafe=keystr)
  key.delete()

