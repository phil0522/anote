"""Manipulator for task class."""
import logging

from google.appengine.ext import ndb
from anoteweb.model import Task, TaskStatus

def Save(task):
  """Create or update a task."""
  key = task.put()
  logging.info("Saving task: %s", task)
  return key.urlsafe()

def Get(task_key):
  """Gets a task by its id. None is return when not found."""
  return ndb.Key(urlsafe=task_key).get()

def GetById(task_key_id):
  key = ndb.Key('Task', task_key_id)
  return key.get()

def GetAllActionableTasks():
  """Gets all task whose status is actionable."""
  return Task.query().filter(Task.status == str(TaskStatus.actionable)).fetch(
    1000)

def GetAllTaskOfProject(project_key):
  """Gets all tasks of same project."""
  return Task.query().filter(Task.project == project_key).fetch(1000)

def GetAllTaskOfTag(tag_key):
  """Gets all tasks with the tag."""
  return Task.query().filter(Task.tags == tag_key).fetch(1000)
