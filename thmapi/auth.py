from .util import *


class __THMAuth(object):
    def login(self, credentials):
        """
        Log in to THM

        :param credentials: Login and password
        :return: null
        """

        csrf_token = fetch_pattern(self.session, '/login', 'csrf-input')

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
