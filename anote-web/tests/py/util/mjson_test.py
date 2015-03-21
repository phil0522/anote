"""Unit test for mjson."""

import unittest

import anoteweb.util.mjson as mjson
from anoteweb.model import Task, TaskNote
from datetime import datetime

class Model2Json(unittest.TestCase):
  """Tests for model2json class."""
  def test_model_2_json_simple_fields(self):
    """simple json test."""
    model = Task()
    model.status = 'actionable'
    model.title = 'title'
    model.position = 300
    model.created_at = datetime.utcfromtimestamp(1390576468)

    json_string = mjson.model2json(model)
    self.assertIsNotNone(json_string, 'message is none')
    self.assertEquals(
        '{"created_at": 1390576468, "status": "actionable", "position": 300, ' +
        '"title": "title"}', json_string)

    parsed_model = mjson.json2model(Task, json_string)

    self.assertEqual(model, parsed_model)

  def test_model_2_json_repeated_fields(self):
    """Repeated field test."""
    model = Task()
    model.status = 'actionable'

    model.title = 'title'
    model.tags.append("path.context1")
    model.tags.append("path.context2")

    json_string = mjson.model2json(model)
    self.assertIsNotNone(json_string)
    self.assertEqual('{"status": "actionable", ' +
                     '"tags": ["path.context1", "path.context2"], ' +
                     '"depth": 0, "title": "title"}', json_string)

    parsed_model = mjson.json2model(Task, json_string)

    self.assertEqual(model, parsed_model)

  def test_model_2_json_enum_fields(self):
    """enum filed tests."""
    model = Task()
    model.status = 'actionable'
    model.title = 'title'

    json_string = mjson.model2json(model)

    self.assertEqual('{"status": "actionable", "title": "title"}',
                     json_string)

    parsed_model = mjson.json2model(Task, json_string)
    self.assertEqual(model, parsed_model)

  def test_model_2_json_repeated_structure(self):
    """repeated message test."""
    model = Task()
    model.status = 'actionable'
    model.title = 'title'
    model.notes.append(TaskNote(text="text1"))
    model.notes.append(TaskNote(text="text2"))

    json_string = mjson.model2json(model)
    self.assertIsNotNone(json_string)
    self.assertEqual('{' +
                     '"notes": [{"text": "text1"}, {"text": "text2"}], ' +
                     '"status": "actionable", ' +
                     '"title": "title"}', json_string)

    parsed_model = mjson.json2model(Task, json_string)
    self.assertEqual(model, parsed_model)

#logger = logging.getLogger("")
#logger.setLevel(logging.DEBUG)

if __name__ == '__main__':
  unittest.main()
