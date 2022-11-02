import unittest
from statistics import Statistics
from player import Player
from enum import Enum

class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_search_returns_correct_player(self):
        self.assertEqual(self.statistics.search("Kurri").name, "Kurri")

    def test_search_returns_none_when_player_not_found(self):
        self.assertEqual(self.statistics.search("Pukki"), None)

    def test_team_returns_players_of_given_team(self):
        players = self.statistics.team("EDM")
        self.assertEqual(players[0].name, "Semenko")
        self.assertEqual(players[1].name, "Kurri")
        self.assertEqual(players[2].name, "Gretzky")

    def test_top_returns_given_amount_of_players_sorted_by_points(self):
        top = self.statistics.top(3)
        self.assertEqual(top[0].name, "Gretzky")
        self.assertEqual(top[1].name, "Lemieux")
        self.assertEqual(top[2].name, "Yzerman")

    def test_top_by_goals_returns_correct(self):
        top_goals = self.statistics.top(3, SortBy.GOALS)
        self.assertEqual(top_goals[0].name, "Lemieux")
        self.assertEqual(top_goals[1].name, "Yzerman")
        self.assertEqual(top_goals[2].name, "Kurri")

    def test_top_by_assists_returns_correct(self):
        top_assists = self.statistics.top(3, SortBy.ASSISTS)
        self.assertEqual(top_assists[0].name, "Gretzky")
        self.assertEqual(top_assists[1].name, "Yzerman")
        self.assertEqual(top_assists[2].name, "Lemieux")
