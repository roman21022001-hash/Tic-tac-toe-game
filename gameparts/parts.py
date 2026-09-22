class Board:
    """A class that describes the playing field."""

    field_size = 3

    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    def make_move(self, row, col, player):
        self.board[row][col] = player

    def display(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

 # We are overriding the __str__ method.
    def __str__(self):
        return (
            'The object of the playing field is of a certain size'
            f'{self.field_size}x{self.field_size}'
        )

    def is_board_full(self):
        # The cycle iterates through all the columns of the game board.
        for i in range(self.field_size):
            # And then, going through all the lines.
            for j in range(self.field_size):
                # If it finds an available cell...
                if self.board[i][j] == ' ':
                    # ...the game continues.
                    return False
        # Otherwise, it’s a draw!
        return True
# This method will determine the victory.

    def check_win(self, player):
        # Here, a check is implemented both vertically and horizontally.
        for i in range(3):
            if (all([self.board[i][j] == player for j in range(3)]) or
                    all([self.board[j][i] == player for j in range(3)])):
                return True
        # Here, a diagonal check is implemented.
        if (
            self.board[0][0] == self.board[1][1] == self.board[2][2] == player
            or
            self.board[0][2] == self.board[1][1] == self.board[2][0] == player
        ):
            return True

        return False
