""" Dao object for project. """
from google.appengine.ext.ndb.key import Key
from anoteweb.model import Project


def GetAllProjects():
  """Returns all projects."""
  return Project.query().filter()

def Add(project):
  """ Create or update a project. """
  project.key = Key(Project, project.name)
  project.put()

def Get(project_key):
  """Get an existing project."""
  return Project.get_by_id(project_key)

def Remove(project_key):
  """Remove an existing project. """
  Key(urlsafe=project_key).delete()

