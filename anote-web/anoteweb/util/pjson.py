"""
Converts a protocol buffer to and from json string.
"""
from google.appengine.ext import ndb
import json



def json2proto(proto_class, json_str):
  raise NotImplementedError()

def get_value(v):
  if isinstance(v, list):
    return [ get_value(i) for i in v]
  elif isinstance(v, str) or isinstance(v, int):
    return v
  elif isinstance(v, ndb.Model):
    return proto_to_map(v)
  else:
    print 'unknown type:', type(v), repr(v)
    raise NotImplementedError

def proto_to_map(proto):
  proto_value_map = proto.to_dict()
  non_empty_map = {}
  for k,v in proto_value_map.iteritems():
    if v:
      non_empty_map[k] = get_value(v)
  return non_empty_map

def proto2json(proto):
  non_empty_map = proto_to_map(proto)
  return json.dumps(non_empty_map, ensure_ascii=False)