from typing import Union

from . import Vector2
from utils.type_tools import is_number
from utils.type_tools import is_numbers
from utils.type_hints import Number

class Rect:
    def __init__(self, *args, **kwargs) -> None:
        if len(args) == 2 and isinstance(args[0], Vector2) and isinstance(args[1], Vector2):
            self._pos: Vector2 = args[0]
            self._size: Vector2 = args[1]
        elif len(args) == 2:
            self._pos: Vector2 = Vector2(args[0])
            self._size: Vector2 = Vector2(args[1])
        elif len(args) == 4 and is_numbers(args[0], args[1], args[2], args[3]):
            self._pos: Vector2 = Vector2(args[0], args[1])
            self._size: Vector2 = Vector2(args[2], args[3])
        else:
            raise TypeError
    
    def __str__(self) -> str:
        return f"{self.pos.__str__()}, {self.area.__str__()}"

    def __repr__(self) -> str:
        return f"Rect(x={self.x}, y={self.y}, w={self.w}, h={self.h})"
    
    def __call__(self) -> tuple[float, float, float, float]:
        return self.x, self.y, self.w, self.h

    def __len__(self) -> int:
        return 4
    
    def __getitem__(self, index: int) -> float:
        return [self.x, self.y, self.w, self.h][index]
    
    def __contains__(self, value: float) -> bool:
        return value in [self.x, self.y, self.w, self.h]
    
    def __iter__(self) -> float:
        yield self.x
        yield self.y
        yield self.w
        yield self.h
    
    @property
    def area(self) -> float:
        return self._size.x * self._size.y
    
    @property
    def x(self) -> float:
        return self._pos.x
    
    @property
    def y(self) -> float:
        return self._pos.y

    @property
    def pos(self) -> Vector2:
        return self._pos
    
    @property
    def w(self) -> float:
        return self._size.x
    
    @property
    def h(self) -> float:
        return self._size.y

    @property
    def size(self) -> Vector2:
        return self._size

