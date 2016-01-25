__author__ = 'danbordeanu'

import unittest

from get_md5 import get_md5
from config_parser import check_if_config_exists


class Md5Test(unittest.TestCase):
    def is_there_md5(self):
        """
        Test if md5 working
        :return:
        """
        self.assertTrue(get_md5())

    def is_there_config_file(self):
        """
        Test if config file exists
        :return:
        """
        self.assertTrue(check_if_config_exists())


if __name__ == '__main__':
    unittest.main()
