from typing import TypeVar, Generic, Type


class Block:
    DEF_VAL = -1

    _value: int

    def __init__(self):
        self._value = self.DEF_VAL

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, v):
        self._value = v


_TBlock = TypeVar("_TBlock")


# Assume it is 2D
class Board(Generic[_TBlock]):
    _width: int
    _height: int
    _rows = None
    _m_class = None

    def __init__(self, m_class: Type[_TBlock]):
        self._width = 0
        self._height = 0
        self._m_class = m_class

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

    def build(self) -> list[list[_TBlock]]:
        self._rows = []
        for i in range(0, self._width):
            col = []

            for j in range(0, self._height):
                block = self._m_class()
                col.append(block)

            self._rows.append(col)

        return self._rows
