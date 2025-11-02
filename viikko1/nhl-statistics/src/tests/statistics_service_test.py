import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
            Player("Yzerman", "DET", 42, 56), # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search(self):
        result = self.stats.search("Semenko")
        self.assertIsNotNone(result)

    def test_search_missing(self):
        result = self.stats.search("Tuntematon")
        self.assertIsNone(result)

    def test_team(self):
        result = self.stats.team("EDM")

        self.assertIsNotNone(result)
        self.assertTrue(len(result) == 3)

    def test_top_by_points(self):
        result = self.stats.top(3)
        self.assertIsNotNone(result)
        self.assertEqual(result[0].points, 124)
        self.assertEqual(result[1].points, 99)
        self.assertEqual(result[2].points, 98)

    def test_top_by_goals(self):
        result = self.stats.top(3, SortBy.GOALS)
        self.assertIsNotNone(result)
        self.assertEqual(result[0].goals, 45)
        self.assertEqual(result[1].goals, 42)
        self.assertEqual(result[2].goals, 37)

    def test_top_by_assists(self):
        result = self.stats.top(3, SortBy.ASSISTS)
        self.assertIsNotNone(result)
        self.assertEqual(result[0].assists, 89)
        self.assertEqual(result[1].assists, 56)
        self.assertEqual(result[2].assists, 54)
