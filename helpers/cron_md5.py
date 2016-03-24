#!/usr/bin/python

"""
# (Cron version V5.0 -- $Id: crontab.c,v 1.12 2004/01/23 18:56:42 vixie Exp $)
0 * * * * /home/users/dan/public_html/openvpn_updater
"""

__author__ = 'dan bordeanu'

import hashlib

config_file = 'client_danbordeanu'
md5_sum_value = 'md5sum'


def cron_md5():
    """

    :rtype : object
    """
    try:
        with open(config_file) as file_to_check:
            data = file_to_check.read()
            md5_returned = hashlib.md5(data).hexdigest()
            assert isinstance(md5_returned, object)
        with open(md5_sum_value, 'w') as text_file:
            text_file.write('{0}'.format(md5_returned))
    except IOError as e:
        print 'error creating md5 {0}'.format(e)

cron_md5()

