import requests
from player import Player

class PlayerReader:
    def get_players(url):
        response = requests.get(url).json()
        players = []
        for player_dict in response:
            player = Player(
                    player_dict['name'],
                    player_dict['team'],
                    player_dict['nationality'],
                    player_dict['goals'],
                    player_dict['assists']
                    )
            players.append(player)

        return players
