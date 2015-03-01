"""Model description for anote system."""
from google.appengine.ext import ndb
from enum import Enum

class Project(ndb.Model):
  """Projects associated with a task. Project can be nested."""

  # The ancestors, from topmost root to direct parent node.
  ancestors = ndb.KeyProperty(repeated=True)
  name = ndb.StringProperty(required=True)
  description = ndb.StringProperty(indexed=False)
  created_at = ndb.DateTimeProperty(auto_now_add=True)
  depth = ndb.ComputedProperty(lambda self: len(self.ancestors))


class Context(ndb.Model):
  """The context a task can be done. Context can be nested."""
  # The ancestors, from topmost root to direct parent node.
  ancestors = ndb.KeyProperty(repeated=True)
  name = ndb.StringProperty(required=True)
  full_name = ndb.StringProperty(required=True)
  description = ndb.StringProperty(indexed=False)
  depth = ndb.ComputedProperty(lambda self: len(self.ancestors))
  count_of_tasks = ndb.IntegerProperty()


class TaskNote(ndb.Model):
  """Notes for a task."""
  created_at = ndb.DateTimeProperty(auto_now_add=True)
  updated_at = ndb.DateTimeProperty(auto_now=True)
  text = ndb.TextProperty(indexed=False)


class Task(ndb.Model):
  """A basic task."""
  Status = Enum('created', 'actionable', 'done', 'canceled')

  ancestors = ndb.KeyProperty(repeated=True)
  status = ndb.StringProperty(choices=Statuses)
  contexts = ndb.StringProperty(repeated=True)
  depth = ndb.ComputedProperty(lambda self: len(self.ancestors))

  notes = ndb.StructuredProperty(TaskNote, repeated=True, indexed=False)

  title = ndb.StringProperty(indexed=False)
  description = ndb.StringProperty(indexed=False)
  user = ndb.StringProperty()
  user_time_zone = ndb.StringProperty()

  # The number used to denote position among its siblings. Starting from
  # 10000 * creation_seq. If a task is moved, it should first try to change
  # this number to some proper value suitable for its new position.
  position = ndb.IntegerProperty()

  created_at = ndb.DateTimeProperty(auto_now_add=True)

  notify_after = ndb.DateTimeProperty()
  valid_after = ndb.DateTimeProperty()
  due_to = ndb.DateTimeProperty()
