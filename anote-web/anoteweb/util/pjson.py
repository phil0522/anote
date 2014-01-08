"""
Converts a protocol buffer to and from json string.
"""

from google.protobuf.descriptor import FieldDescriptor
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
    raise NotImplementedError(field_type, field.type)

def _add_json_repeated_value(field, value, values):
  field_type = _TYPE_MAPPING.get(field.type, None)
  if field_type is not None:
    values.append(field_type(value))
  else:
    raise NotImplementedError(field_type, field.type)
  

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
      elif field.message_type is not None:
        # A nest message type, do it recursively.
        _json_to_proto(getattr(proto, field.name, None), value)
      else:
        setattr(proto, field.name, _get_field_value(field, value))
    except:
      raise ParseError(proto.__class__.__name__, field.name, json)
    
  return proto

def _proto_to_json(proto):
  result = {}
  for field, value in proto.ListFields():
    try:
      if field.label == FieldDescriptor.LABEL_REPEATED:
        repeated_result = []
        for repeated_value in value:
          if field.message is not None:
            result.append(_proto_to_json(repeated_value))
          else:
            result.append(_get_field_value(field, repeated_value))
        result[field.name] = repeated_result
      elif field.message_type is not None:
        result[field.name] = _proto_to_json(value)
        # nested message
      else:
        result[field.name] = _get_field_value(field, value)
    except:
      raise ParseError(proto.__class__.name, field.name, json)

def json2proto(proto_class, json_str):
  return _json_to_proto(proto_class(), json.loads(json_str))

def proto2json(proto):
  return json.dump(_proto_to_json(proto))