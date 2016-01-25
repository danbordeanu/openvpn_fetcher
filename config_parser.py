from helpers import logger_settings

__author__ = 'danbordeanu'

import ConfigParser
import os
import os.path
import sys


def check_if_config_exists(config_file):
    if os.path.isfile(config_file) and os.access(config_file, os.R_OK):
        logger_settings.logging.info('ok we got config file')
    else:
        logger_settings.logging.info('no file, no go')
        sys.exit(8)


def config_params(section):
    config = ConfigParser.ConfigParser()
    config.read('config.ini')
    dict_ini = {}
    options = config.options(section)
    for option in options:
        try:
            dict_ini[option] = config.get(section, option)
            if dict_ini[option] == -1:
                logger_settings.logging.info('skyp:%s' % option)
        except:
            assert isinstance(option, object)
            logger_settings.logging.info('exception on %s' % option)
    return dict_ini


check_if_config_exists('config.ini')
