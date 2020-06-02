from .util import *


class __THMKoth(object):
    def koth_machine_pool(self) -> list:
        """
        Gets the current koth machine pool

        :return: Machine list
        """

        return http_get(self.session, '/games/koth/get/machine-pool')

    def koth_game_data(self, game_id) -> dict:
        """
        Gets data about a koth game

        :type game_id: int
        :param game_id: Game id
        :return: Game data
        """

        return http_get(self.session, f'/games/koth/data/{game_id}', has_success=True)

    def koth_recent_games(self) -> list:
        """
        Gets 5 most recently finished koth games

        :return: List of 4 most recent koth games
        """

        return http_get(self.session, '/games/koth/recent/games')
