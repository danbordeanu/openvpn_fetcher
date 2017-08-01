from helpers import logger_settings

__author__ = 'danbordeanu'

import ConfigParser
import os

def check_if_config_exists(config_file):
    try:
        os.path.isfile(config_file)
    except IOError as e:
        logger_settings.logging.info('no file, no go {0}'.format(e))


def config_params(section):
    check_if_config_exists('config.ini')
    config = ConfigParser.ConfigParser()
    config.read('config.ini')
    dict_ini = {}
    options = config.options(section)
    for option in options:
        try:
            dict_ini[option] = config.get(section, option)
            if dict_ini[option] == -1:
                logger_settings.logging.info('skip:{0}'.format(option))
        except:
            assert isinstance(option, object)
            logger_settings.logging.info('exception on {0}'.format(option))
    return dict_ini

