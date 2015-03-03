"""Model description for anote system."""
from google.appengine.ext import ndb
from enum import Enum

class Project(ndb.Model):

  """Projects associated with a task. Project can not be nested."""
  name = ndb.StringProperty(required=True)
  description = ndb.StringProperty()


class TaskNote(ndb.Model):
  """Notes for a task."""
  task_key = ndb.StringProperty()
  created_at = ndb.DateTimeProperty(auto_now_add=True)
  updated_at = ndb.DateTimeProperty(auto_now=True)
  text = ndb.TextProperty(indexed=False)


TaskStatus = Enum('created', 'actionable', 'done', 'canceled')

class Task(ndb.Model):
  """A basic task."""
  title = ndb.StringProperty(indexed=False)
  description = ndb.StringProperty(indexed=False)

  status = ndb.StringProperty(choices=[str(s) for s in TaskStatus])
  priority = ndb.IntegerProperty(
      indexed=False,
      validator=lambda prop, value: value if 1 <= value < 6 else None)

  created_at = ndb.DateTimeProperty(auto_now_add=True)
  notify_after = ndb.DateTimeProperty()
  valid_after = ndb.DateTimeProperty()
  due_to = ndb.DateTimeProperty()

  notes = ndb.LocalStructuredProperty(TaskNote, repeated=True, indexed=False)


class Tag(ndb.Model):
  "Store all tags used in the tasks."
  tag_name = ndb.StringProperty()
  is_active = ndb.BooleanProperty()
