"""test for time util library."""

import unittest

from anoteweb.util.time_util import to_epoch, from_epoch

class Proto2Json(unittest.TestCase):
  """Test class for Proto2Json."""
  def test_convert_from_to(self):
    """Time convert routines."""
    a = from_epoch(1390576468)
    b = to_epoch(a)
    self.assertEqual(b, 1390576468)
