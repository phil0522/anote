import unittest

import util.pjson as pjson
from model import Task
from model import Context

class Proto2Json(unittest.TestCase):

  
  def test_proto_2_json_simple_fields(self):
    proto = Task()
    proto.status = str(Task.Status.actionable)
    proto.title = 'title'
    
    json_string = pjson.proto2json(proto)
    self.assertIsNotNone(json_string, 'message is none')
    self.assertEquals('{"status": "actionable", "title": "title"}',
                      json_string)
    
    #parsed_proto = pjson.json2proto(Task, json_string)
    
    #self.assertEqual(proto, parsed_proto)

    
  def test_proto_2_json_repeated_fields(self):
    proto = Task()
    proto.status = str(Task.Status.actionable)
    proto.title = 'title'
    proto.contexts.append(Context(name='name1'))
    proto.contexts.append(Context(name='name2'))
    json_string = pjson.proto2json(proto)
    self.assertIsNotNone(json_string)
    self.assertEqual('{"status": "actionable", "contexts": [{"name": "name1"}, '
                     + '{"name": "name2"}], "title": "title"}',
                     json_string)
    
    #parsed_proto = pjson.json2proto(Task, json_string)
    
    #self.assertEqual(proto, parsed_proto)
    
  def test_proto_2_json_enum_fields(self):
    proto = Task()
    proto.status = str(Task.Status.actionable)
    proto.title = 'title'
    
    json_string = pjson.proto2json(proto)
    
    self.assertEqual('{"status": "actionable", "title": "title"}', json_string)
    
    #parsed_proto = pjson.json2proto(Task, json_string)
    #self.assertEqual(proto, parsed_proto)
    

    

    
