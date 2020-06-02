from .util import *


class __THMStats(object):
    def get_stats(self) -> dict:
        """
        Returns public and cloneable room count and current user count

        :return: Dict containing mentioned values
        """

        return http_get(self.session, '/api/getstats')
