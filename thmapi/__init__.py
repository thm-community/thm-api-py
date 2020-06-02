from .koth import __THMKoth
from .leaderboard import __THMLeaderboard
from .room import __THMRoom
from .stats import __THMStats
from .team import __THMTeam
from .user import __THMUser
import requests


class THM(
    __THMStats,
    __THMLeaderboard,
    __THMTeam,
    __THMUser,
    __THMKoth,
    __THMRoom
):
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
