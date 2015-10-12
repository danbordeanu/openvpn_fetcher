__author__ = 'danbordeanu'

import config_parser as parser
import hashlib
import logger_settings


def get_md5(blocksize=65536):
    """
    :rtype : object
    """
    openvpn_config = parser.config_params('openvpnconfig')['file']
    md5 = hashlib.md5()
    f = open(openvpn_config)
    for line in f:
        md5.update(line)
    f.close()
    return md5.hexdigest()

config_md5 = get_md5()
logger_settings.logger.info('md5 of local openvpn config is:%s' %config_md5)
