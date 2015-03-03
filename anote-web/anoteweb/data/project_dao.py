""" Dao object for project. """
from google.appengine.ext.ndb.key import Key
from anoteweb.model import Project


def get_all_projects():
  """Returns all projects."""
  return Project.query().filter()

def add_project(project):
  """ Create or update a project. """
  project.key = Key(Project, project.name)
  project.put()

