class Block:
    _value: int

    def __init__(self):
        pass

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, v):
        self._value = v


# Assume it is 2D
class Board:
    _width: int
    _height: int
    _rows = None

    def __init__(self):
        self._width = 0
        self._height = 0

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, w):
        self._width = w

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, h):
        self._height = h

    def blocks_count(self) -> int:
        count = 0
        for row in self._rows:
            if row is not None:
                for col in row:
                    if col is not None:
                        count += 1
        return count

    def build(self):
        self._rows = []
        for i in range(0, self._width):
            col = []

            for j in range(0, self._height):
                block = Block()
                col.append(block)

            self._rows.append(col)
