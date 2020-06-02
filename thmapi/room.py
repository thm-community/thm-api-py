from .util import *


class __THMRoom(object):
    def room_details(self, room_code) -> dict:
        """
        Gets details of a specific room

        :param room_code: Room code
        :return: Room data
        """

        return http_get(self.session, f'/api/room/{room_code}', has_success=True)

    def room_new_rooms(self) -> list:
        """
        Gets a list of 6 newest rooms

        :return: List of newest rooms
        """

        return http_get(self.session, '/api/newrooms')

    def room_graph_data(self, room_code, user_count=10) -> list:
        """
        Gets a list of top {user_count} users from a room for the graph

        :param room_code: Room code
        :type user_count: int
        :param user_count: Amount of user the call should return
        :return: List of users on the scoreboard
        """

        return http_get(self.session, f'/api/getgraphdata/{user_count}/{room_code}')

    def room_issues(self, room_code) -> dict:
        """
        Gets issues from a specific room

        :param room_code: Room code
        :return: Room issues
        """

        return http_get(self.session, f'/api/get-issues/{room_code}', has_success=True)['data']

    def room_votes(self, room_code) -> int:
        """
        Gets votes for a specific room

        :param room_code: Room code
        :return: Room votes
        """

        return http_get(self.session, f'/api/get-votes/{room_code}')

    def room_weekly_challenges(self) -> list:
        """
        Gets a list of weekly challenge rooms

        :return: List of weekly challenge rooms
        """

        return http_get(self.session, '/api/weekly-challenge-rooms')

    # LIKELY TO CHANGE
    # def room_hacktivities(self, query='null', order_by='most-popular', difficulty='all', type='all'):
    #     """
    #
    #
    #     :param query: Query string for looking at description/tags
    #     :param order_by: Order by: most-users, most-popular, newest
    #     :param difficulty: Difficulty: easy, medium, hard
    #     :param type: Room type: challenge, walkthrough
    #     :return: Room list
    #     """
    #
    #     # order_by: most-users, most-popular, newest
    #     # difficulty: easy, medium, hard
    #     # type: challenge, walkthrough
    #
    #     return http_get(self.session, f'{root_url}/api/hacktivities/{query}/all/{order_by}/{difficulty}/{type}')
