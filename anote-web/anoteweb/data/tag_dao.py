""" Dao functions for tags. """
from anoteweb.model import Tag
from google.appengine.ext import ndb

def get_all_tags():
  """Gets all tags."""
  tags = Tag.query().fetch(10000)
  return tags

def add_tag(tag):
  """Add or update a tag."""
  model = Tag()
  model.tag_name = tag
  model.put()
  return model

def remove_tag(keystr):
  key = ndb.Key(urlsafe=keystr)
  key.delete()
