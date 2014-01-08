"""
Converts a protocol buffer to and from json string.
"""

from google.protobuf.descriptor import FieldDescriptor
from google.protobuf.reflection import GeneratedProtocolMessageType
import json

class ParseError(Exception):
  pass


_TYPE_MAPPING = {
  FieldDescriptor.TYPE_BOOL: bool,
  FieldDescriptor.TYPE_INT32: int,
  FieldDescriptor.TYPE_INT64: long,
  FieldDescriptor.TYPE_DOUBLE: float,
  FieldDescriptor.TYPE_FLOAT: float,
  FieldDescriptor.TYPE_STRING: unicode,
  FieldDescriptor.TYPE_ENUM: int,
}

def _get_field_value(field, value):
  field_type = _TYPE_MAPPING.get(field.type, None)
  if field_type is not None:
    return field_type(value)
  else:
    raise NotImplementError(field_type, field.type)

def _add_json_repeated_value(field, value, values):
  field_type = _TYPE_MAPPING.get(field.type, None)
  if field_type is not None:
    values.append(field_type(value))
  else:
    raise NotImplementError(field_type, field.type)
  

def _json_to_proto(proto, json):
  for field in proto.DESCRIPTOR.fields:
    try:
      if not json.has_key(field.name):
        continue
      value = json[field.name]
      if field.label == FieldDescriptor.LABEL_REPEATED:
        values = getattr(proto, field.name, None)

        # Since the field.name is verified to exist. Don't check it again.
        for repeated_value in value:
          _add_json_repeated_value(field, repeated_value, values)
      else:
        if field.message_type is not None:
          # A nest message type, do it recursively.
          _json_to_proto(getattr(proto, field.name, None), value)
        else:
          setattr(proto, field.name, _get_field_value(field, value))
    except:
      raise ParseError(proto.__class__.__name__, field.name, json)
    
  return proto

def _get_proto_repeated_value(field, value):
  field_type = _TYPE_MAPPING.get(field.type, None)
  if field_type is not None:
    return ftype(value)
  else:
    raise _proto_to_json(value)


  
