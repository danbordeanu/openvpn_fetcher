__author__ = 'danbordeanu'

import unittest

from get_md5 import get_md5


class Md5Test(unittest.TestCase):
    def test_is_there_md5(self):
        """
        Test if md5 working
        :return:
        """
        self.assertTrue(get_md5(), 'Uhh, md5 not working')


if __name__ == '__main__':
    unittest.main()
