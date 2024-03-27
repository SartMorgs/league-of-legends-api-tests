import requests


class Requester:

    BASE_URL = 'https://americas.api.riotgames.com'
    BASE_SUMMONER_URL = 'https://br1.api.riotgames.com'
    MATCH_PATH = 'lol/match/v5/matches'
    ACCOUNT_PATH = 'riot/account/v1/accounts'
    SUMMONER_PATH = 'lol/summoner/v4/summoners'
    LEAGUE_PATH = 'lol/league/v4/entries'

    def __init__(self, api_key):
        self.api_key = api_key

    def __summoner_full_url(self, summoner_name, summoner_tag):
        return f'{self.BASE_URL}/{self.ACCOUNT_PATH}/by-riot-id/{summoner_name}/{summoner_tag}'

    def __last_matches_full_url(self, puuid, count)
        return f'{self.BASE_URL}/{self.MATCH_PATH}/by-puuid/{puuid}/ids?start=0&count={count}'
    
    def __match_details_full_url(self, matchId):
        return f'{self.BASE_URL}/{self.MATCH_PATH}/{matchId}'
    
    def __match_stats_full_url(self, matchId):
        return self.__match_details_full_url(matchId) + '/timeline'

    def __summoner_account_info_url(self, puuid):
        return f'{self.BASE_SUMMONER_URL}/{self.SUMMONER_PATH}/by-puuid/{puuid}'

    def __summoner_league_info_url(self, summonerId):
        return f'{self.BASE_SUMMONER_URL}/{self.LEAGUE_PATH}/by-summoner/{summonerId}'

    def __league_api_request(self, url):
        headers = {'Accept': 'application/json', 'X-Riot-Token': self.api_key}
        response = requests.get(url, headers=headers).json()
        return response
    
    def _get_summoner_puuid(self, summoner_name, summoner_tag):
        url = self.__summoner_full_url(summoner_name, summoner_tag)
        return self.__league_api_request(url)

    def _get_last_matches(self, puuid, count):
        url = self.__last_matches_full_url(puuid, count)
        return self.__league_api_request(url)
    
    def _get_match_details(self, matchId):
        url = self.__match_details_full_url(matchId)
        return self.__league_api_request(url)
    
    def _get_stats_full_url(matchId):
        url = self.__match_stats_full_url(matchId)
        return self.__league_api_request(url)

    def _get_summoner_account_info(self, puuid):
        url = self.__summoner_account_info_url(puuid)
        return self.__league_api_request(url)

    def _get_summoner_league_info(self, summonerId):
        url = self.__summoner_league_info_url(summonerId)
        return self.__league_api_request(url)
