from .util import *
import re

csrf_regex = re.compile('<input type="hidden" name="_csrf" value="(.{36})">')


class __THMAuth(object):
    def login(self, credentials):
        initial = http_get(self.session, '/login', res_format='')
        csrf_token = csrf_regex.search(initial).group(1)

        data = {
            'email': credentials['username'],
            'password': credentials['password'],
            '_csrf': csrf_token
        }

        http_post(self.session, '/login', data, res_format='')

        try:
            test_request = http_get(self.session, '/message/get-unseen')

            if test_request['success']:
                self.authenticated = True
                return
            else:
                raise Exception(f'Failed to authenticate')
        except Exception as e:
            raise e
