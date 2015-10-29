__author__ = 'dan bordeanu'

import os
import hashlib

config_file = 'client_danbordeanu'
md5_sum_value = 'md5sum'


def cron_md5():
    """

    :rtype : object
    """
    if os.path.isfile(config_file):
        with open(config_file) as file_to_check:
            data = file_to_check.read()
            md5_returned = hashlib.md5(data).hexdigest()
            assert isinstance(md5_returned, object)
            with open(md5_sum_value, 'w') as text_file:
                text_file.write('{0}'.format(md5_returned))
    else:
        print 'no file'
        exit()

cron_md5()

