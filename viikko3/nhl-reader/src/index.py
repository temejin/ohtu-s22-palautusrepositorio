import requests
from player import Player
from player_reader import PlayerReader
from player_stats import PlayerStats

def tulosta_pelaajat(pelaajat):
    for pelaaja in pelaajat:
        print(pelaaja)

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
    players = PlayerReader.get_players(url)
    pelaajat = PlayerStats.top_by(players, lambda p: p.nationality == "FIN", lambda p: p.goals+p.assists)
    tulosta_pelaajat(pelaajat)

main()
