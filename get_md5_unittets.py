__author__ = 'danbordeanu'

import unittest

from get_md5 import get_md5


class GetMd5SumTest(unittest.TestCase):
    def test_md5(self):
        self.assertTrue(get_md5)
