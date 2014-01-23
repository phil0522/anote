import unittest

import util.pjson as pjson
from proto.task_pb2 import Task
from proto.anote_pb2 import Project


class Proto2Json(unittest.TestCase):

  
  def test_proto_2_json_simple_fields(self):
    proto = Task()
    proto.id = 1
    proto.title = 'title'
    proto.created_at = 12345678
    
    json_string = pjson.proto2json(proto)
    self.assertIsNotNone(json_string, 'message is none')
    self.assertEquals('{"created_at": 12345678, "id": 1, "title": "title"}',
                      json_string)
    
    parsed_proto = pjson.json2proto(Task, json_string)
    
    self.assertEqual(proto, parsed_proto)

    
  def test_proto_2_json_repeated_fields(self):
    proto = Task()
    proto.context.append('Home')
    proto.context.append('Urgent')
    proto.context.append('Invalid')
    
    json_string = pjson.proto2json(proto)
    self.assertIsNotNone(json_string)
    self.assertEqual('{"context": ["Home", "Urgent", "Invalid"]}', json_string)
    
    parsed_proto = pjson.json2proto(Task, json_string)
    
    self.assertEqual(proto, parsed_proto)
    
  def test_proto_2_json_enum_fields(self):
    proto = Task()
    proto.due_type = Task.VALID_BEFORE_DUE_TIME
    
    json_string = pjson.proto2json(proto)
    
    self.assertEqual('{"due_type": "VALID_BEFORE_DUE_TIME"}', json_string)
    
    parsed_proto = pjson.json2proto(Task, json_string)
    self.assertEqual(proto, parsed_proto)
    
    
  def test_proto_2_json_nested_fields(self):
    project = Project()
    
    project.id = '1'
    project.title = 'main project'
    
    sub_project = project.sub_project.add()
    sub_project.id = '2'
    sub_project.title = 'sub project 1'
    
    sub_project = project.sub_project.add()
    sub_project.id = '3'
    sub_project.title = 'sub project 2'
    
    json_string = pjson.proto2json(project)
    self.assertEqual('{"sub_project": [{"id": "2", "title": "sub project 1"}, {"id": "3", "title": "sub project 2"}], "id": "1", "title": "main project"}',
                     json_string)
    parsed_project = pjson.json2proto(Project, json_string)
    self.assertEqual(project, parsed_project)
    

    
