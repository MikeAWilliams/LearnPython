import unittest
import pytest
import bowling

class BowlingTest(unittest.TestCase):

    def test_no_strike_no_spare(self):
        frames = [[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1,0]]
        self.assertEqual(20, bowling.CalculateScore(frames))

    def test_strikes_no_spare_no_consecutive_strikes(self):
        frames = [[10,0],[1,1],[10,0],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1,0]]
        self.assertEqual(16 + 20 + 4, bowling.CalculateScore(frames))

    def test_strikes_no_spare_consecutive_strikes(self):
        frames = [[10,0],[10,0],[10,0],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1,0]]
        self.assertEqual(14 + 30 + 21 + 12, bowling.CalculateScore(frames))

    def test_perfect_game(self):
        frames = [[10,0],[10,0],[10,0],[10,0],[10,0],[10,0],[10,0],[10,0],[10,0],[10,10,10]]
        self.assertEqual(300, bowling.CalculateScore(frames))

    def test_spare_no_strike(self):
        frames = [[9,1],[1,1],[9,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1,0]]
        self.assertEqual(16 + 20 + 2, bowling.CalculateScore(frames))

    def test_all_spare(self):
        frames = [[9,1],[9,1],[9,1],[9,1],[9,1],[9,1],[9,1],[9,1],[9,1],[9,1,9]]
        self.assertEqual(190, bowling.CalculateScore(frames))

if __name__ == '__main__':
    unittest.main()