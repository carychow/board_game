from common import board

class TicTacToeBlock(board.Block):
    MARK_X = 1
    MARK_O = 2
    def __init__(self):
        super().__init__()

class TicTacToe(board.Board):
    def __init__(self):
        super().__init__(TicTacToeBlock)
        self.width = 3
        self.height = 3

    def build(self) -> list[list[TicTacToeBlock]]:
        blocks = super().build()
        return blocks
