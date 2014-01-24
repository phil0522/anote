import unittest

from anoteweb.util.time_util import to_epoch,from_epoch
from datetime import datetime

class Proto2Json(unittest.TestCase):


  def test_convert_from_to(self):
    a = from_epoch(1390576468)
    b = to_epoch(a)
    self.assertEqual(b, 1390576468)