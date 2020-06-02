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

    #
    # Statistics
    #
    def get_stats(self) -> dict:
        """
        Returns public and cloneable room count and current user count

        :return: Dict containing mentioned values
        """

        return http_get(self.session, f'{root_url}/api/getstats')

    #
    # Leaderboard
    #
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

    #
    # Team
    #
    def get_teams(self) -> list:
        """
        Returns all teams

        :return: List containing all teams
        """

        return http_get(self.session, f'{root_url}/api/all-teams')

    #
    # User
    #
    def user_exists(self, username) -> bool:
        """
        Checks if a username is taken

        :param username: Username to check
        :return:
        """

        return http_get(self.session, f'{root_url}/api/user-exist/{username}')['success']

    def user_created_rooms(self, username) -> list:
        """
        Gets a list of rooms created by a user

        :param username: Username to check
        :return: List of rooms created by this user
        """

        return http_get(self.session, f'{root_url}/api/created-rooms/{username}', has_success=True)['rooms']

    def user_completed_room_count(self, username) -> int:
        """
        Gets the amount of completed rooms by a user

        :param username: Username to check
        :return:
        """

        return http_get(self.session, f'{root_url}/api/roomscompleted/{username}')['completed']

    def user_all_completed_rooms(self, username) -> list:
        """
        Gets all rooms completed by a user

        :param username: Username to check
        :return: List of rooms (with all data) completed by this user
        """

        return http_get(self.session, f'{root_url}/api/all-completed-rooms/{username}')

    def user_badges(self, username) -> list:
        """
        Gets the list of badges a user has

        :param username: Username to check
        :return: List of badges
        """

        return http_get(self.session, f'{root_url}/api/get-badges/{username}')

    def user_activity(self, username) -> list:
        """
        Gets the user's activity feed

        :param username: Username to check
        :return: List of events
        """

        return http_get(self.session, f'{root_url}/api/get-activity-events/{username}', has_success=True)['data']

    def user_discord(self, token) -> dict:
        """
        Gets the user's data from his discord integration token

        :param token: Discord integration token
        :return: User data
        """

        return http_get(self.session, f'{root_url}/tokens/discord/{token}', has_success=True)

    def user_stats(self, username) -> dict:
        """
        Gets the user's basic data

        :param username: Username to check
        :return: User data (rank, points, avatar)
        """

        return http_get(self.session, f'{root_url}/api/user/{username}')

    def user_rank(self, username) -> int:
        """
        Gets the user's rank

        :param username: Username to check
        :return: User's rank
        """

        return http_get(self.session, f'{root_url}/api/usersRank/{username}')
