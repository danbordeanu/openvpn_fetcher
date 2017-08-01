__author__ = 'danbordeanu'

import unittest

from get_md5 import get_md5
from helpers.config_parser import check_if_config_exists


class GetAllTest(unittest.TestCase):
    def test_md5(self):
        self.assertTrue(get_md5)

    def Test_config(self):
        self.assertTrue(check_if_config_exists('config.ini'))


if __name__ == 'main':
    suite = unittest.TestLoader().loadTestsFromTestCase(GetAllTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
