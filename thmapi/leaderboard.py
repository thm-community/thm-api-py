from .util import *


class __THMLeaderboard(object):
    def get_leaderboard(self) -> list:
        """
        Returns the top 50 users from the all-time leaderboard

        :return: List containing top 50 users
        """

        return http_get(self.session, '/api/leaderboards')['topUsers']

    def get_monthly_leaderboard(self) -> list:
        """
        Returns the top 50 users from the monthly leaderboard

        :return: List containing top 50 users
        """

        return http_get(self.session, '/api/leaderboards')['topUsersMonthly']
