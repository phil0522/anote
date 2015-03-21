"""Manipulator for task class."""
import logging

from anoteweb.model import Task, TaskStatus

def Save(task):
  """Create or update a task."""
  key = task.put()
  logging.info("Saving task: %s", task)
  return key

def Get(task_id):
  """Gets a task by its id. None is return when not found."""
  return Task.query(task_id=task_id).get()

def GetAllActionableTask():
  """Gets all task whose status is actionable."""
  return Task.query().filter(Task.status == TaskStatus).fetch(1000)

def GetAllTaskOfProject(project_key):
  return Task.query().filter(Task.project == project_key)

