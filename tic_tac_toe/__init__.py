from common import board


class TicTacToeBlock(board.Block):
    MARK_X = 1
    MARK_O = 2

    def __init__(self):
        super().__init__()

    @property
    def value(self):
        return board.Block.fget(self)

    @value.setter
    def value(self, v):
        if v == self.MARK_X or v == self.MARK_O:
            board.Block.fset(v)


class TicTacToe(board.Board):
    _lastMark: int
    _moveCount: int
    _moveMax: int

    def __init__(self):
        super().__init__(TicTacToeBlock)
        self.width = 3
        self.height = 3
        self._moveCount = 0
        self._moveMax = self.width * self.height

    def build(self) -> list[list[TicTacToeBlock]]:
        blocks = super().build()
        return blocks

    def place(self, x: int, y: int, mark: int):
        block = self._rows[x][y]
        if block is not None and block.value is TicTacToeBlock.DEF_VAL:
            block.value = mark
            self._lastMark = mark
            self._moveCount += 1

            self.check_result(x, y, mark)

    # Reference: https://stackoverflow.com/questions/1056316/algorithm-for-determining-tic-tac-toe-game-over
    def check_result(self, x: int, y: int, mark: int):
        # Check col
        for i in range(self.height):
            if self._rows[x][i].value != mark:
                break

            if i == self.height - 1:
                # Last mark win
                return

        # Check row
        for i in range(self.width):
            if self._rows[i][y].value != mark:
                break

            if i == self.width - 1:
                # Last mark win
                return

        # Check diagonal
        if x == y:
            for i in range(self.width):
                if self._rows[i][i] != mark:
                    break

                if i == self.width - 1:
                    # Last mark win
                    return

        # Check anti-diagonal
        if x + y == self.width - 1:
            for i in range(self.width):
                if self._rows[i][(self.width - 1) - i] != mark:
                    break

                if i == self.width - 1:
                    # Last mark win
                    return

        if self._moveCount == self._moveMax:
            # Draw
            return
