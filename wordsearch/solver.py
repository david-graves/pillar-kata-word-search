RIGHT = (0,1)
LEFT = (0,-1)
UP = (-1,0)
DOWN = (1,0)
UP_RIGHT = (-1,1)
DOWN_RIGHT = (1,1)
UP_LEFT = (-1,-1)
DOWN_LEFT = (1,-1)
DIRECTIONS = [RIGHT, LEFT, UP, DOWN, UP_RIGHT, DOWN_RIGHT, UP_LEFT, DOWN_LEFT]

class Puzzle:

    def __init__(self, board):
        if board in [None, [], [[]]]:
            raise ValueError('board is empty.')
        if type(board) is not list:
            raise TypeError('board is not of type list.')
        for row in board:
            if len(row) != len(board):
                raise ValueError('board is not square.')
        if len(board) < 2:
            raise ValueError('board is too small; it must be at least 2x2.')
        self.board = board

    @property
    def size(self):
        return self.height, self.width

    @property
    def height(self):
        return len(self.board)

    @property
    def width(self):
        return len(self.board[0])

    def all_positions(self):
        for y in range(self.height):
            for x in range(self.width):
                yield (y, x)

    def get_valid_moves(self, position, distance=1):
        moves = []
        for direction in DIRECTIONS:
            y, x = position
            dy, dx = direction
            y += dy * distance
            x += dx * distance
            if 0 <= y < self.height and 0 <= x < self.width:
                moves.append((y,x))
        return moves