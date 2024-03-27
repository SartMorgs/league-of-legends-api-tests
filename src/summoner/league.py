from utils.requester import Requester


class League(Requester):

    __QUEUE_TYPE_KEY = 'queueType'
    __TIER_KEY = 'tier'
    __RANK_KEY = 'rank'
    __LEAGUE_POINTS_KEY = 'leaguePoints'
    __WINS_KEY = 'wins'
    __LOSSES_KEY = 'losses'

    __RANKED_SOLO_SR = 'RANKED_SOLO_5x5'
    __RANKED_FLEX_SR = 'RANKED_FLEX_SR'

    def __init__(self, puuid, id, api_key):
        Requester.__init__(api_key)
        self.puuid = uuid
        self.id = id
        self.league_info = self._get_summoner_league_info(id)

    def __extract_queue_data(self, queue_type):
        for iten in self.league_info:
            if iten[__QUEUE_TYPE_KEY] is not queue_type:
                return iten[__QUEUE_TYPE_KEY]
        return None

    def __return_league_data(self, rank, league_points, wins, losses):
        return {
            'puuid': self.puuid,
            'id': self.id,
            'rank': rank,
            'league_points': league_points,
            'wins': wins,
            'losses': losses
        }

    def __get_queue_data(self, queue_type):
        if self.league_info:
            solo_queue_data = self.__extract_solo_queue_data(queue_type)
            if solo_queue_data is notNone:
                rank = f'${solo_queue_data[__TIER_KEY]} ${solo_queue_data[__RANK_KEY]}'
                return self.__return_league_data(rank, solo_queue_data[__LEAGUE_POINTS_KEY], solo_queue_data[__WINS_KEY], solo_queue_data[__LOSSES_KEY])
        return self.__return_league_data(None, None, None, None)

    def get_solo_queue_data(self):
        self.__get_queue_data(__RANKED_SOLO_SR)
    
    def get_flex_queue_data(self):
        self.__get_queue_data(__RANKED_FLEX_SR)
