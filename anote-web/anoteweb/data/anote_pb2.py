# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: anote.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor.FileDescriptor(
  name='anote.proto',
  package='anote.proto',
  serialized_pb=_b('\n\x0b\x61note.proto\x12\x0b\x61note.proto\"\xfc\x01\n\x04Task\x12\x0f\n\x07task_id\x18\x01 \x01(\x05\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0e\n\x06status\x18\x03 \x01(\t\x12\x0b\n\x03tag\x18\x04 \x03(\t\x12\x0f\n\x07project\x18\x05 \x01(\t\x12\x11\n\tparent_id\x18\x06 \x01(\x05\x12\x10\n\x08\x61ncestor\x18\x07 \x03(\x05\x12\x13\n\x0b\x64\x65scription\x18\x08 \x01(\t\x12\x0f\n\x07note_id\x18\t \x03(\x05\x12\x1f\n\x04note\x18\n \x03(\x0b\x32\x11.anote.proto.Note\x12\x13\n\x0b\x63reate_time\x18\x0b \x01(\x05\x12\x13\n\x0bupdate_time\x18\x0c \x01(\x05\x12\x10\n\x08position\x18\r \x01(\x05\";\n\x04Note\x12\x0f\n\x07note_id\x18\x01 \x01(\x05\x12\x0c\n\x04text\x18\x02 \x01(\t\x12\x14\n\x0chistory_text\x18\x03 \x03(\t\"6\n\x03Tag\x12\r\n\x05title\x18\x01 \x01(\t\x12\x12\n\noccurrence\x18\x02 \x01(\x05\x12\x0c\n\x04hide\x18\x03 \x01(\x08')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_TASK = _descriptor.Descriptor(
  name='Task',
  full_name='anote.proto.Task',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='task_id', full_name='anote.proto.Task.task_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='title', full_name='anote.proto.Task.title', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='anote.proto.Task.status', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tag', full_name='anote.proto.Task.tag', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='project', full_name='anote.proto.Task.project', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parent_id', full_name='anote.proto.Task.parent_id', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ancestor', full_name='anote.proto.Task.ancestor', index=6,
      number=7, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='anote.proto.Task.description', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='note_id', full_name='anote.proto.Task.note_id', index=8,
      number=9, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='note', full_name='anote.proto.Task.note', index=9,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='create_time', full_name='anote.proto.Task.create_time', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='update_time', full_name='anote.proto.Task.update_time', index=11,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='position', full_name='anote.proto.Task.position', index=12,
      number=13, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=29,
  serialized_end=281,
)


_NOTE = _descriptor.Descriptor(
  name='Note',
  full_name='anote.proto.Note',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='note_id', full_name='anote.proto.Note.note_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='text', full_name='anote.proto.Note.text', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='history_text', full_name='anote.proto.Note.history_text', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=283,
  serialized_end=342,
)


_TAG = _descriptor.Descriptor(
  name='Tag',
  full_name='anote.proto.Tag',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='anote.proto.Tag.title', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='occurrence', full_name='anote.proto.Tag.occurrence', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hide', full_name='anote.proto.Tag.hide', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=344,
  serialized_end=398,
)

_TASK.fields_by_name['note'].message_type = _NOTE
DESCRIPTOR.message_types_by_name['Task'] = _TASK
DESCRIPTOR.message_types_by_name['Note'] = _NOTE
DESCRIPTOR.message_types_by_name['Tag'] = _TAG

Task = _reflection.GeneratedProtocolMessageType('Task', (_message.Message,), dict(
  DESCRIPTOR = _TASK,
  __module__ = 'anote_pb2'
  # @@protoc_insertion_point(class_scope:anote.proto.Task)
  ))
_sym_db.RegisterMessage(Task)

Note = _reflection.GeneratedProtocolMessageType('Note', (_message.Message,), dict(
  DESCRIPTOR = _NOTE,
  __module__ = 'anote_pb2'
  # @@protoc_insertion_point(class_scope:anote.proto.Note)
  ))
_sym_db.RegisterMessage(Note)

Tag = _reflection.GeneratedProtocolMessageType('Tag', (_message.Message,), dict(
  DESCRIPTOR = _TAG,
  __module__ = 'anote_pb2'
  # @@protoc_insertion_point(class_scope:anote.proto.Tag)
  ))
_sym_db.RegisterMessage(Tag)


# @@protoc_insertion_point(module_scope)