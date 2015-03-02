"""Unit test for task dao."""

import unittest
from google.appengine.ext import testbed
from google.appengine.datastore import datastore_stub_util

from anoteweb.model import Task
from anoteweb.data.task_dao import get_all_actionable_tasks


class TaskDaoTest(unittest.TestCase):
  """Tests for Proto2Json class."""

  def setUp(self):
    # First, create an instance of the Testbed class.
    self.testbed = testbed.Testbed()
    # Then activate the testbed, which prepares the service stubs for use.
    self.testbed.activate()
    # Create a consistency policy that will simulate the High Replication
    # consistency model.
    self.policy = datastore_stub_util.PseudoRandomHRConsistencyPolicy(
      probability=1)
    # Initialize the datastore stub with this policy.
    self.testbed.init_datastore_v3_stub(consistency_policy=self.policy)
    self.testbed.init_memcache_stub()
    self.testbed.init_user_stub()

  def tearDown(self):
    self.testbed.deactivate()


  def  testGetAllActionableTask(self):
    """Only picks actionable tasks."""
    Task(task_id=1, status='created', title='a').put()
    Task(task_id=2, status='actionable', title='b').put()

    tasks = get_all_actionable_tasks()

    self.assertEqual(1, len(tasks))
    self.assertEqual('b', tasks[0].title)

if __name__ == '__main__':
  unittest.main()
