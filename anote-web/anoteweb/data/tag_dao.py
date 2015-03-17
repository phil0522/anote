""" Dao functions for tags. """
from google.appengine.ext.ndb.key import Key
from anoteweb.model import Tag

def get_all_tags():
  """Gets all tags."""
  tags = Tag.query().fetch(10000)
  return tags

def add_tag(tag):
  """Add or update a tag."""
  tag.key = Key(Tag, tag.name)
  tag.put()
