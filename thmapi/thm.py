from .util import http_get
import requests

root_url = 'https://tryhackme.com'


class THM(object):
    """
    TryHackMe API Wrapper
    """

    def __init__(self, credentials=None):
        """
        Initializes the API Wrapper

        :type credentials: dict
        :param credentials: (Optional) Credentials for use with authenticated requests
        """

        self.session = requests.Session()

        # if (credentials is not None) and (type(credentials) == dict):
        #     if ('username' in credentials) and ('password' in credentials):
        #         self.__login(credentials)

    def get_stats(self) -> dict:
        """
        Returns public and cloneable room count and current user count

        :return: Dict containing mentioned values
        """

        return http_get(self.session, f'{root_url}/api/getstats')

    def get_leaderboard(self) -> list:
        """
        Returns the top 50 users from the all-time leaderboard

        :return: List containing top 50 users
        """

        return http_get(self.session, f'{root_url}/api/leaderboards')['topUsers']

    def get_monthly_leaderboard(self) -> list:
        """
        Returns the top 50 users from the monthly leaderboard

        :return: List containing top 50 users
        """

        return http_get(self.session, f'{root_url}/api/leaderboards')['topUsersMonthly']
