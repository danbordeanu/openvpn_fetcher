__author__ = 'danbordeanu'

#!/usr/bin/python

import config_parser as parser
import requests
import time
import logger_settings
import get_md5 as getmd5
import os
import shutil


class OpenVpn:
    def __init__(self, parser):
        """
        :type self: object
        :type parser: object
        :rtype : object
        """
        self.parser = parser
        self.http_md5 = parser.config_params('http')['http_md5']
        self.openvpn_config_file = parser.config_params('http')['config_file']
        self.user = parser.config_params('authentication')['auth_user']
        self.password = parser.config_params('authentication')['auth_passwd']
        self.openvpn_config_save_file = parser.config_params('openvpnconfig')['file']
        self.file_name_saved_local = 'client_danbordeanu_saved'
        self.ssl_crt = parser.config_params('certs')['ssl_crt']
        self.ssl_key = parser.config_params('certs')['ssl_key']

    def fetch_md5(self):
        """
        :type self: object
        """
        r = requests.get(self.http_md5, auth=(self.user, self.password),
                         cert=(os.path.join(os.getcwd(), self.ssl_crt), os.path.join(os.getcwd(), self.ssl_key)))
        logger_settings.logger.info(u'Response code {0:d}'.format(r.status_code))
        r.raise_for_status()
        logger_settings.logger.info('Response md5 from server %s' % r.content.rstrip('\n'))
        if r.content.rstrip('\n') == getmd5.get_md5():
            logger_settings.logger.info('Same config, doing nothing...sleeping')
        else:
            logger_settings.logger.info('New config detected, fun begins')
            with open(self.file_name_saved_local, 'wb') as handle:
                v = requests.get(self.openvpn_config_file, auth=(self.user, self.password),
                                 cert=(os.path.join(os.getcwd(), self.ssl_crt),
                                       os.path.join(os.getcwd(), self.ssl_key)), stream=True)
                logger_settings.logger.info(u'Response code {0:d}'.format(v.status_code))
                v.raise_for_status()
                for block in v.iter_content(1024):
                    handle.write(block)
            logger_settings.logger.info('Moving new config to openvpn directory')
            try:
                shutil.copy(self.file_name_saved_local, os.path.join(os.getcwd(), self.openvpn_config_save_file))
            except IOError, e:
                logger_settings.logger.debug('Huston we have a big problem %s' % e)


def run_main():
    go = OpenVpn(parser)
    go.fetch_md5()


if __name__ == '__main__':
    start_time = time.time()
    run_main()
    logger_settings.logger.info('It took me %s seconds to check for new config' % round((time.time() - start_time)))
