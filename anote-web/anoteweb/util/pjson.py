"""
Converts a protocol buffer to and from json string.
"""

import google.appengine.ext.ndb as ndb
import json
import logging
from anoteweb.util.time_util import from_epoch, to_epoch
from datetime import datetime

def _json_to_proto(model_class, json_obj):
  """json to proto string."""
  _result = {}
  for k, value in json_obj.iteritems():
    prop = model_class._properties.get(k)
    if prop is None:
      logging.fatal('can not decode %s, Property is not defined on %s.%s.', k,
                    model_class.__model__, model_class.__name__)
    if isinstance(prop, ndb.model.ComputedProperty):
      continue
    if prop._repeated:
      value = [_get_value_for_json_to_proto(prop, val) for val in value]
    else:
      value = _get_value_for_json_to_proto(prop, value)

    _result[k] = value

  return model_class(**_result)


def _get_value_for_json_to_proto(prop, v):
  """json to proto."""
  logging.info('_get_value_for_json_to_proto: %s, vaue: %s',
      repr(prop), repr(v))

  #pylint: disable=E1101
  if isinstance(prop, (ndb.DateTimeProperty, ndb.DateProperty,
                ndb.TimeProperty)):
    return from_epoch(v)

  if isinstance(prop, ndb.KeyProperty):
    return ndb.Key(urlsafe=v)

  if isinstance(prop, ndb.StructuredProperty):
    return _json_to_proto(prop._modelclass, v)

  if isinstance(prop, (ndb.IntegerProperty, ndb.StringProperty,
                ndb.TextProperty)):
    return v

  logging.fatal('unsupported property type: %s', prop)


def _remove_null_value_from_map(value):
  if isinstance(value, list):
    return [_remove_null_value_from_map(i) for i in value]
  elif isinstance(value, datetime):
    return to_epoch(value)
  elif isinstance(value, str) or isinstance(value, int):
    return value
  elif isinstance(value, dict):
    result = {}
    for k, v in value.iteritems():
      if isinstance(v, (list, dict)) and not v:
        continue
      if v is None:
        continue

      result[k] = _remove_null_value_from_map(v)

    return result
  else:
    logging.fatal('unknown type: %s %s', type(v), repr(v))


def json2proto(proto_class, json_str):
  return _json_to_proto(proto_class, json.loads(json_str))


def proto2json(proto):
  non_empty_map = _remove_null_value_from_map(proto.to_dict())
  return json.dumps(non_empty_map, ensure_ascii=False)
