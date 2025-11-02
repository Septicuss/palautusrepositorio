import unittest
from statistics_service import StatisticsService
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

    def test_top(self):
        result = self.stats.top(3)
        self.assertIsNotNone(result)
        self.assertEqual(result[0].points, 124)
        self.assertEqual(result[1].points, 99)
        self.assertEqual(result[2].points, 98)