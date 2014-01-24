import unittest

import anoteweb.util.pjson as pjson
from model import Task,TaskNote
from model import Context
from datetime import datetime
import sys
import logging

class Proto2Json(unittest.TestCase):

  
  def test_proto_2_json_simple_fields(self):
    proto = Task()
    proto.status = str(Task.Status.actionable)
    proto.title = 'title'
    proto.position = 300
    proto.created_at = datetime.utcfromtimestamp(1390576468)

    json_string = pjson.proto2json(proto)
    self.assertIsNotNone(json_string, 'message is none')
    self.assertEquals('{"status": "actionable", "position": 300, "depth": 0, "created_at": 1390576468, "title": "title"}',
                      json_string)
    
    parsed_proto = pjson.json2proto(Task, json_string)
    
    self.assertEqual(proto, parsed_proto)

    
  def test_proto_2_json_repeated_fields(self):
    proto = Task()
    proto.status = str(Task.Status.actionable)
    proto.title = 'title'
    proto.contexts.append("path.context1")
    proto.contexts.append("path.context2")

    json_string = pjson.proto2json(proto)
    self.assertIsNotNone(json_string)
    self.assertEqual('{"status": "actionable", "contexts": ["path.context1", "path.context2"], "depth": 0, "title": "title"}',
                     json_string)
    
    parsed_proto = pjson.json2proto(Task, json_string)
    
    self.assertEqual(proto, parsed_proto)
    
  def test_proto_2_json_enum_fields(self):
    proto = Task()
    proto.status = str(Task.Status.actionable)
    proto.title = 'title'
    
    json_string = pjson.proto2json(proto)
    
    self.assertEqual('{"status": "actionable", "depth": 0, "title": "title"}', json_string)
    
    parsed_proto = pjson.json2proto(Task, json_string)
    self.assertEqual(proto, parsed_proto)

  def test_proto_2_json_repeated_structure(self):
    proto = Task()
    proto.status = str(Task.Status.actionable)
    proto.title = 'title'
    proto.notes.append(TaskNote(text="text1"))
    proto.notes.append(TaskNote(text="text2"))

    json_string = pjson.proto2json(proto)
    self.assertIsNotNone(json_string)
    self.assertEqual('{"status": "actionable", "notes": [{"text": "text1"}, {"text": "text2"}], "depth": 0, "title": "title"}',
                     json_string)

    parsed_proto = pjson.json2proto(Task, json_string)
    self.assertEqual(proto, parsed_proto)

#logger = logging.getLogger("")
#logger.setLevel(logging.DEBUG)
