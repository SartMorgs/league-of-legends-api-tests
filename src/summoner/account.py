from utils.requester import Requester


class Account(Requester):

    __ID_KEY = 'id'
    __ACCOUNT_ID = 'accountId'
    __NAME_KEY = 'name'
    __SUMMONER_LEVEL_KEY = 'summoner_level'

    def __init__(self, summoner_name, summoner_tag, api_key):
        Requester.__init__(api_key)
        self.summoner_name = summoner_name
        self.summoner_tag = summoner_tag
        self.puuid = self._get_summoner_puuid(self.summoner_name, self.summoner_tag)
        self.account = self._get_summoner_account_info(self.puuid)

    def get_account_data(self):
        return {
            'summoner_name': self.summoner_name,
            'summoner_tag': self.summoner_tag,
            'puuid': self.puuid,
            'id': self.account[__ID_KEY],
            'account_id': self.account[__ACCOUNT_ID],
            'name': self.account[__NAME_KEY],
            'summoner_level': self.account[__SUMMONER_LEVEL_KEY]
        }
    
    def get_id(self):
        return self.account[__ID_KEY]
