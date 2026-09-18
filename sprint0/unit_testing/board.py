"""English peg solitaire board representation.

This module provides a Board class modelling the standard 7x7
English-style peg solitaire board (a cross-shaped board where the
four 2x2 corner blocks are not playable).
"""


class Board:
    """Model of the 7x7 English-style peg solitaire board.

    The board is cross-shaped: the four 2x2 corner blocks are
    considered off-board. Cells on the board can be one of the
    constants ``PEG``, ``HOLE``, or ``OFF_BOARD``.

    Attributes:
        PEG (str): Constant representing a peg.
        HOLE (str): Constant representing an empty hole.
        OFF_BOARD (str): Constant representing off-board cells.
        SIZE (int): Board size (7).
    """

    PEG = "peg"
    HOLE = "hole"
    OFF_BOARD = "off_board"

    SIZE = 7

    def __init__(self):
        """Initialize a new board.

        The grid is a list of lists with size ``SIZE`` x ``SIZE``.
        All playable cells are initialized with ``PEG`` except the
        center cell which is initialized as ``HOLE``. The four 2x2
        corner blocks are marked as ``OFF_BOARD``.
        """
        self.grid = []
        for row in range(self.SIZE):
            current_row = []
            for col in range(self.SIZE):
                if row in (0, 1, 5, 6) and col in (0, 1, 5, 6):
                    current_row.append(self.OFF_BOARD)
                elif row == 3 and col == 3:
                    current_row.append(self.HOLE)
                else:
                    current_row.append(self.PEG)
            self.grid.append(current_row)



    def get_cell(self, row, col):
        """Return the value of a cell.

        Coordinates outside the grid are treated as off-board rather
        than raising an error, so callers can safely probe cells beyond
        the board's edges.

        Args:
            row (int): Row index of the cell.
            col (int): Column index of the cell.

        Returns:
            str: One of ``PEG``, ``HOLE``, or ``OFF_BOARD``. Returns
            ``OFF_BOARD`` when ``row`` or ``col`` is out of range.
        """
        if row < 0 or row >= self.SIZE or col < 0 or col >= self.SIZE:
            return self.OFF_BOARD
        return self.grid[row][col]


    def count_pegs(self):
        """Count pegs currently on the board.

        Returns:
            int: Number of cells equal to ``PEG``.
        """
        count = 0
        for row in self.grid:
            for cell in row:
                if cell == self.PEG:
                    count += 1
        return count