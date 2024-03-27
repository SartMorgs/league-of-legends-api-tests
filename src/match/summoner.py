from utils.requester import Requester
from summoner.league import Account, League


class Summoner(Requester):

    __GAME_NAME_KEY = 'gameName'
    __TAG_LINE_KEY = 'tagLine'
    __ID_KEY = 'id'

    __METADATA_KEY = 'metadata'
    __PARTICIPANTS_KEY = 'participants'

    def __init__(self, game_id, api_key):
        Requester.__init__(api_key)
        self.game_id = game_id
        self.game_details = self._get_match_details(game_id)

    def __extract_participants(self):
        return self.game_details[__METADATA_KEY][__PARTICIPANTS_KEY]

    def _get_summoner_name_and_tag_line(self, puuid):
        account_info = self._get_summoner_account_info(puuid)
        name = account_info[__GAME_NAME_KEY]
        tag_line = account_info[__TAG_LINE_KEY]
        return name, tag_line
    
    def _get_full_summoner_id(self, puuid):
        name, tag_line = self._get_summoner_name_and_tag_line(puuid)
        return f'{name} #{tag_line}'

    def _get_summoner_info(self, puuid):
        name, tag_line = self._get_summoner_name_and_tag_line(puuid)

        account = Account(name, tag_line, self.api_key)
        account_data = account.get_account_data()

        league = League(puuid, account_data[__ID_KEY], self.api_key)
        solo_queue_data = league.get_solo_queue_data()
        flex_queue_data = league.get_flex_queue_data()

        return {
            'name': name,
            'tag_line': tag_line,
            'solo_queue': solo_queue_data,
            'flex_queue': flex_queue_data
        }
    
    def get_data_of_all_participants(self):
        participants = self.__extract_participants()
        data_of_all_participants = [self._get_summoner_info(participant) for participant in participants]
        return data_of_all_participants
