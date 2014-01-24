"""
Converts a protocol buffer to and from json string.
"""
from google.appengine.ext import ndb
import json
import logging
from time_util import from_epoch,to_epoch
from datetime import datetime

def _json_to_proto(proto_class, json_obj):
  proto = proto_class()
  _result = {}
  for k,v in json_obj.iteritems():
    prop = proto_class._properties.get(k)
    if prop is None:
      logging.fatal('can not decode %s, Property is not defined on %s.%s.', k,
                    proto_class.__model__, proto_class.__name__)
    if isinstance(prop, ndb.ComputedProperty):
      continue
    if prop._repeated:
      value = [_get_value_for_json_to_proto(prop, val) for val in v]
    else:
      value = _get_value_for_json_to_proto(prop, v)

    _result [k] = value

  return proto_class(**_result)


def _get_value_for_json_to_proto(prop, v):
  logging.info('_get_value_for_json_to_proto: %s, vaue: %s', repr(prop), repr(v))
  if isinstance(prop, (ndb.DateTimeProperty, ndb.DateProperty,
                ndb.TimeProperty)):
    return from_epoch(v)

  if isinstance(prop, ndb.KeyProperty):
    return ndb.Key(urlsafe=v)

  if isinstance(prop, ndb.StructuredProperty):
    return _json_to_proto(prop._modelclass, v)

  if isinstance(prop, (ndb.IntegerProperty, ndb.StringProperty, ndb.TextProperty)):
    return v

  logging.fatal('unsupport property type: %s', prop)




def json2proto(proto_class, json_str):
  return _json_to_proto(proto_class, json.loads(json_str))

def _remove_null_value_from_map(input):
  if isinstance(input, list):
    return [ _remove_null_value_from_map(i) for i in input]
  elif isinstance(input, datetime):
    return to_epoch(input)
  elif isinstance(input, str) or isinstance(input, int):
    return input
  elif isinstance(input, dict):
    result = {}
    for k, v in input.iteritems():
      if isinstance(v, (list, dict)) and not v:
        continue
      if v is None:
        continue

      result[k] = _remove_null_value_from_map(v)

    return result
  else:
    logging.fatal('unknown type: %s %s', type(v), repr(v))

def proto2json(proto):
  non_empty_map = _remove_null_value_from_map(proto.to_dict())
  return json.dumps(non_empty_map, ensure_ascii=False)