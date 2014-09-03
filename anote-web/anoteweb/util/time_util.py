"""
Utility class for time related feature.
"""

__author__ = 'phonica@gmail.com (Aaron Xiong)'

from calendar import timegm
from datetime import datetime

def to_epoch(value):
  """
  This is a view method to return the data in seconds.

      :param value: Instance of `datetime.datetime`.
      :returns: `float` as the number of seconds since unix epoch.
  """
  return timegm(value.utctimetuple())


def from_epoch(value):
  """
    Return

    :param value:
      Instance of `float` as the number of seconds since unix epoch.
    :returns:
          Instance of `datetime.datetime`.
  """
  return datetime.utcfromtimestamp(value)
