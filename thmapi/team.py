from .util import *


class __THMTeam(object):
    def get_teams(self) -> list:
        """
        Returns all teams

        :return: List containing all teams
        """

        return http_get(self.session, '/api/all-teams')
