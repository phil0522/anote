"""Model description for anote system."""
from google.appengine.ext import ndb
from enum import Enum

class Project(ndb.Model):

  """Projects associated with a task. Project can not be nested."""
  project_name = ndb.StringProperty(required=True)


class TaskNote(ndb.Model):
  """Notes for a task."""
  created_at = ndb.DateTimeProperty(auto_now_add=True)
  text = ndb.TextProperty(indexed=False)

TaskStatus = Enum('new', 'in_progress', 'done', 'hold', 'canceled')

class Task(ndb.Model):
  """A basic task."""
  title = ndb.StringProperty(indexed=False)

  status = ndb.StringProperty(choices=[str(s) for s in TaskStatus])
  priority = ndb.StringProperty()

  creation_time = ndb.DateTimeProperty(auto_now_add=True)
  last_modification_time = ndb.DateTimeProperty(auto_now=True)
  notify_after = ndb.DateTimeProperty()
  valid_after = ndb.DateTimeProperty()
  due_to = ndb.DateTimeProperty()
  project = ndb.StringProperty()
  tags = ndb.StringProperty(repeated=True)

  notes = ndb.LocalStructuredProperty(TaskNote, repeated=True, indexed=False)


class Tag(ndb.Model):
  "Store all tags used in the tasks."
  tag_name = ndb.StringProperty()
  is_active = ndb.BooleanProperty()
