# TODO: investigate using x and y
class Direction:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def __repr__(self):
        return 'Direction(row={}, col={})'.format(self.row, self.col)

NORTH = Direction(-1, 0)
EAST = Direction(0, 1)
SOUTH = Direction(1, 0)
WEST = Direction(0, -1)
