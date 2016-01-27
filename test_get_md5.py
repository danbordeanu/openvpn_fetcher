__author__ = 'danbordeanu'

import unittest

from get_md5 import get_md5


class Md5Test(unittest.TestCase):
    """
    Testing the md5 of the file
    """

    def is_there_md5(self):
        self.assertTrue(get_md5())


if __name__ == '__main__':
    unittest.main()
