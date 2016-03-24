from helpers import logger_settings

__author__ = 'danbordeanu'

import config_parser as parser
import hashlib


def get_md5():
    """
    :rtype : object
    """
    openvpn_config = parser.config_params('openvpnconfig')['file']
    md5 = hashlib.md5()
    try:
        f = open(openvpn_config)
        for line in f:
            md5.update(line)
        f.close()
        return md5.hexdigest()
    except IOError:
        logger_settings.logger.info('There is no config file...will download one for you')
        return md5.hexdigest()

config_md5 = get_md5()
logger_settings.logger.info('md5 of local openvpn config is:%s' %config_md5) #TODO logger_settings.logger.info('md5 of local openvpn config is:{0}'.format(config_md5))
