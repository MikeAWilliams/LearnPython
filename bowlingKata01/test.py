
from __future__ import division

import unittest
import pytest
import bowling

class BowlingTest(unittest.TestCase):

    def test_no_strike_no_spare(self):
        frames = [[1, 1],[1, 1],[1, 1],[1, 1],[1, 1],[1, 1],[1, 1],[1, 1],[1, 1],[1, 1, 0]]
        self.assertEqual(20, bowling.BowlingScore(frames))

    def test_all_spare_first_nine(self):
        frames = [[9, 1],[9, 1],[9, 1],[9, 1],[9, 1],[9, 1],[9, 1],[9, 1],[9, 1],[9, 0, 0]]
        self.assertEqual(9*19 + 9, bowling.BowlingScore(frames))

    def test_all_spare(self):
        frames = [[9, 1],[9, 1],[9, 1],[9, 1],[9, 1],[9, 1],[9, 1],[9, 1],[9, 1],[9, 1, 5]]
        self.assertEqual(9*19 + 15, bowling.BowlingScore(frames))

    def test_all_strike(self):
        frames = [[10, 0],[10, 0],[10, 0],[10, 0],[10, 0],[10, 0],[10, 0],[10, 0],[10, 0],[9, 0, 0]]
        self.assertEqual(7*30 + 29 + 19 + 9, bowling.BowlingScore(frames))

    def test_alternate_strike_spare(self):
        frames = [[10, 0],[9, 1],[10, 0],[9, 1],[10, 0],[9, 1],[10, 0],[9, 1],[10, 0],[9, 0, 0]]
        self.assertEqual(4 * 20 + 19 + 4 * 20 + 9, bowling.BowlingScore(frames))

    def test_three_frame_not_last(self):
        with pytest.raises(Exception):
            frames = [[1, 1],[1, 1, 1],[1, 1],[1, 1],[1, 1],[1, 1],[1, 1],[1, 1],[1, 1],[1, 1, 0]]
            assert bowling.BowlingScore(frames)

    def test_three_frame_second_to_last(self):
        with pytest.raises(Exception):
            frames = [[1, 1],[1, 1],[1, 1],[1, 1],[1, 1],[1, 1],[1, 1],[1, 1],[1, 1, 1],[1, 1]]
            assert bowling.BowlingScore(frames)

    def test_perfrect_game(self):
        frames = [[10, 0],[10, 0],[10, 0],[10, 0],[10, 0],[10, 0],[10, 0],[10, 0],[10, 0],[10, 10, 10]]
        self.assertEqual(300, bowling.BowlingScore(frames))

    def test_last_frame_required_to_be_size_three(self):
        with pytest.raises(Exception):
            frames = [[1, 1],[1, 1],[1, 1],[1, 1],[1, 1],[1, 1],[1, 1],[1, 1],[1, 1],[1, 1]]
            assert bowling.BowlingScore(frames)

    def test_to_few_frames(self):
        with pytest.raises(Exception):
            frames = [[1, 1],[1, 1],[1, 1],[1, 1],[1, 1],[1, 1],[1, 1],[1, 1],[1, 1]]
            assert bowling.BowlingScore(frames)

    def test_to_many_frames(self):
        with pytest.raises(Exception):
            frames = [[1,1],[1,1],[1,1],[1, 1],[1, 1],[1, 1],[1, 1],[1, 1],[1, 1],[1, 1],[1, 1],[1, 1]]
            assert bowling.BowlingScore(frames)

if __name__ == '__main__':
    unittest.main()