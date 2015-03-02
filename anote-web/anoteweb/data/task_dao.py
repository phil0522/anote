"""Manipulator for task class."""
import logging

from anoteweb.model import Task

def save_task(task):
  """Create or update a task."""
  key = task.put()
  logging.info("Saving task: %s", task)
  return key

def get_task(task_id):
  """Gets a task by its id. None is return when not found."""
  return Task.query(task_id=task_id).get()

def get_all_actionable_tasks():
  """Gets all task whose status is actionable."""
  return Task.query().filter(Task.status=='actionable').fetch(100)





