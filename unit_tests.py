__author__ = 'danbordeanu'

import unittest

from get_md5 import get_md5
from config_parser import check_if_config_exists

class Md5Test(unittest.TestCase):
    def test_is_there_md5(self):
        """
        Test if md5 working
        :return:
        """
        self.assertTrue(get_md5(), 'Uhh, md5 not working')

    def test_is_there_config(self):
        """
        Test if there is config file
        :return:
        """
        self.assertTrue(check_if_config_exists('mimi'), 'Uhhh, no config file')

if __name__ == '__main__':
    unittest.main()
