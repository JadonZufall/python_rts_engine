from typing import Optional, Union

ColorTuple = Union[tuple[int, int, int], tuple[int, int, int, int]]

def is_color_tuple(value: any) -> bool:
    if len(value) < 3 or len(value) > 4:
        return False
    else:
        return len(filter(lambda x: x, [isinstance(int, c) for c in value])) == len(value)


class RGBColor:
    def __init__(self, r: int, g: int, b: int, alpha: Optional[int] = None) -> None:
        self._r, self._g, self._b = r, g, b
        self._alpha = alpha

    @staticmethod
    def from_tuple(self, value: ColorTuple) -> "RGBColor":
        if not is_color_tuple(value):
            raise ValueError
        if len(value) == 3:
            return RGBColor(*value)
        else:
            return RGBColor(*value[:3], alpha=value[3])
    
    def __len__(self) -> int:
        return 4 if self._alpha is not None else 3
    
    def __iter__(self) -> int:
        yield self._r
        yield self._g
        yield self._b
        if self._alpha is not None:
            yield self._alpha
        
    def __getitem__(self, index: int) -> int:
        if index == 3:
            if self._alpha is not None:
                return self._alpha
            else:
                raise IndexError
        return self._r if index == 0 else self._g if index == 1 else self._b

    def to_tuple(self) -> ColorTuple:
        """ Exports the value to a tuple. """
        return (self._r, self._g, self._b) if self._alpha is None else (self._r, self._g, self._b, self._alpha)
    
    @property
    def r(self) -> int:
        return self._r
    
    @property
    def g(self) -> int:
        return self._g
    
    @property
    def b(self) -> int:
        return self._b
    
    @property
    def alpha(self) -> Union[int, None]:
        return self._alpha
    
    @property
    def has_alpha(self) -> bool:
        return self._alpha is not None
