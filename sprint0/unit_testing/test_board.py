"""Unit tests for the Board class."""

import unittest

from board import Board

class BoardTest(unittest.TestCase):
    """Tests the initial state of the board"""

    def setUp(self):
        """Create a new board for each test."""
        self.board = Board()

    def test_center_is_empty(self):
        """The center cell should be a hole."""
        self.assertEqual(self.board.get_cell(3, 3), Board.HOLE)

    def test_corners_are_off_board(self):
        """Corner cells should be off the board."""
        self.assertEqual(self.board.get_cell(0, 0), Board.OFF_BOARD)

    def test_count_pegs(self):
        """The initial board should have 32 pegs."""
        self.assertEqual(self.board.count_pegs(), 32)

    def test_arm_cell_has_a_peg(self):
        """A cell in the arm of the board should have a peg."""
        self.assertEqual(self.board.get_cell(0, 3), Board.PEG)

if __name__ == "__main__":
    unittest.main()