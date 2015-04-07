"""
Converts a model to and from json string.
"""

import google.appengine.ext.ndb as ndb
import json
import logging
from anoteweb.util.time_util import from_epoch, to_epoch
from datetime import datetime

def _json_to_model(model_class, json_obj):
  """json to model string."""
  _result = {}
  url_safe_key = None
  for k, value in json_obj.iteritems():
    if k == 'key':
      url_safe_key = value
      continue
    prop = model_class._properties.get(k)
    if prop is None:
      print dir(model_class)
      logging.fatal('can not decode %s, Property is not defined on %s.%s.', k,
                    model_class.__module__, model_class.__name__)
    if isinstance(prop, ndb.model.ComputedProperty):
      continue
    if prop._repeated:
      value = [_get_value_for_json_to_model(prop, val) for val in value]
    else:
      value = _get_value_for_json_to_model(prop, value)

    _result[k] = value

  print 'result=', repr(_result)
  m = model_class(**_result)
  if url_safe_key:
    m.key = ndb.Key(urlsafe=url_safe_key)
  return m


def _get_value_for_json_to_model(prop, v):
  """json to model."""
  logging.info('_get_value_for_json_to_model: %s, vaue: %s',
      repr(prop), repr(v))

  if isinstance(prop, (ndb.DateTimeProperty, ndb.DateProperty,
                ndb.TimeProperty)):
    return from_epoch(v)

  if isinstance(prop, ndb.KeyProperty):
    return ndb.Key(urlsafe=v)

  if isinstance(prop, (ndb.StructuredProperty, ndb.LocalStructuredProperty)):
    return _json_to_model(prop._modelclass, v)

  if isinstance(prop, (ndb.IntegerProperty, ndb.StringProperty,
                ndb.TextProperty)):
    return v

  logging.fatal('unsupported property type: %s', prop)


def _remove_null_value_from_map(value):
  if isinstance(value, ndb.Model):
    kv_map = value.to_dict()
    kv_map['key'] = value.key.urlsafe()
    kv_map['key_id'] = value.key.id()
    return _remove_null_value_from_map(kv_map)
  if isinstance(value, list):
    return [_remove_null_value_from_map(i) for i in value]
  elif isinstance(value, datetime):
    return to_epoch(value)
  elif isinstance(value, str) or isinstance(value, int) or isinstance(
    value, unicode):
    return value
  elif isinstance(value, dict):
    result = {}
    for k, v in value.iteritems():
      logging.info('current key: %s', k)
      if isinstance(v, (list, dict)) and not v:
        continue
      if v is None:
        continue

      result[k] = _remove_null_value_from_map(v)

    return result
  else:
    logging.fatal('unknown type: %s %s', type(value), repr(value))


def json2model(model_class, json_str):
  return _json_to_model(model_class, json.loads(json_str))

def model2json(model):
  if isinstance(model, list):
    logging.info('model is list %s', model)
    non_empty_map = [_remove_null_value_from_map(m) for m in model]
    return json.dumps(non_empty_map, ensure_ascii=False, sort_keys=True)
  else:
    non_empty_map = _remove_null_value_from_map(model)
    # Keep it sorted to make test easilier.
    return json.dumps(non_empty_map, ensure_ascii=False, sort_keys=True)


