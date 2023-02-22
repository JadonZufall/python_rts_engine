from typing import Union, Iterable, Literal

import json


def is_number(value: any) -> bool:
    return isinstance(value, int) or isinstance(value, float)


class Vector2:
    """ Stores a positional vector in two dimensions.  (x, y) """
    def __init__(self, *args, **kwargs) -> None:
        """ Constructor method for a Vector2 instance. """
        self._anchor_point: tuple[float, float] = (0.0, 0.0)
        self._x: float
        self._y: float
        if len(args) is 1 and isinstance(args[0], Iterable):
            self._x, self._y = float(args[0][0]), float(args[0][1])
        elif len(args) is 2 and is_number(args[0]) and is_number(args[1]):
            self._x, self._y = float(args[0]), float(args[1])
        elif len(kwargs.keys()) is 2 and is_number(kwargs.get("x")) and is_number(kwargs.get("y")):
            self._x, self._y = float(kwargs.get("x")), float(kwargs.get("y"))
        else:
            raise ValueError
    
    def __str__(self) -> str:
        """ Converts object to a string. """
        return f"({self._x}, {self._y})"
    
    def __repr__(self) -> str:
        """ Representation of object when displaying. """
        return f"Vector2(x={self._x}, y={self._y})"
    
    def __call__(self) -> tuple:
        # TODO: Remove this feature
        return self._x, self._y
    
    def __eq__(self, other: "Vector2") -> bool: return isinstance(other, Vector2) and self._x == other._x and self._y == other._y
    def __ne__(self, other: "Vector2") -> bool: return not isinstance(other, Vector2) or self._x != other._x or self._y != other._y
    def __lt__(self, other: "Vector2") -> bool: return self.anchor_dist() < other.anchor_dist()
    def __gt__(self, other: "Vector2") -> bool: return self.anchor_dist() > other.anchor_dist()
    def __le__(self, other: "Vector2") -> bool: return self.anchor_dist() <= other.anchor_dist()
    def __ge__(self, other: "Vector2") -> bool: return self.anchor_dist() >= other.anchor_dist()

    def equivalent_to(self, other: Iterable) -> bool: return self._x == other[0] and self._y == other[1]
    def not_equivalent_to(self, other: Iterable) -> bool: return self._x != other[0] or self._y != other[1]

    def __len__(self) -> Literal[2]: return 2
    def __getitem__(self, index: int) -> float:
        if index < 0 or index > 1:
            raise IndexError
        return self._x if index == 0 else self._y
    
    def __setitem__(self, index: int, value: Union[int, float, complex]) -> None:
        if index < 0 or index > 1:
            raise IndexError
        if index == 0:
            self._x: float = float(value)
        else:
            self._y: float = float(value)
    
    def __contains__(self, value: float) -> bool: return self._x == value or self._y == value
    
    def __iter__(self) -> float: yield self._x; yield self._y
    
    # Binary Operations
    def __add__(self, other: "Vector2") -> "Vector2":
        """ Adds values together. """
        return Vector2(self._x + other._x, self._y + other._y)

    def __sub__(self, other: "Vector2") -> "Vector2":
        """ Subtracts values from one another. """
        return Vector2(self._x - other._x, self._y - other._y)
    
    def __mul__(self, other: "Vector2") -> "Vector2":
        """ Multiplies values. """
        return Vector2(self._x * other._x, self._y * other._y)
    
    def __floordiv__(self, other: "Vector2") -> "Vector2":
        """ Floor divides values. """
        return Vector2(float(self._x // other._x), float(self._y // other._y))
    
    def __truediv__(self, other: "Vector2") -> "Vector2":
        """ True divides values. """
        return Vector2(self._x / other._x, self._y / other._y)
    
    def __mod__(self, other: "Vector2") -> "Vector2":
        """ Returns the remainder of true division. """
        return Vector2(float(self._x % other._x), float(self._y % other._y))
    
    def __pow__(self, other: "Vector2") -> "Vector2":
        """ Raises self to the power of other. """
        return Vector2(self._x ** other._x, self._y ** other._y)
    
    # Other binary operations
    def __lshift__(self, other: "Vector2") -> "Vector2":
        """ Performs bitwise lshift on left and right values. """
        return Vector2(self._x << other._x, self._y << other._y)
    
    def __rshift__(self, other: "Vector2") -> "Vector2":
        """ Performs bitwise rshift on left and right values. """
        return Vector2(self._x >> other._x, self._y >> other._y)
    
    def __and__(self, other: "Vector2") -> "Vector2":
        """ Performs bitwise and on x and y values. """
        return Vector2(self._x & other._x, self._y & other._y)
    
    def __xor__(self, other: "Vector2") -> "Vector2":
        """ Performs bitwise xor on x and y values. """
        return Vector2(self._x ^ other._x, self._y ^ other._y)
    
    def __or__(self, other: "Vector2") -> "Vector2":
        """ Performs bitwise or on x and y values. """
        return Vector2(self._x | other._x, self._y | other._y)
    
    # Urinary operations
    def __neg__(self) -> "Vector2":
        """ Returns a vector where both x and y are negative values. """
        return Vector2(-1 * abs(self._x), -1 * abs(self._y))
    
    def __pos__(self) -> "Vector2":
        """ Returns a vector where both x and y are positive values. """
        return Vector2(abs(self._x), abs(self._y))

    def __abs__(self) -> "Vector2":
        """ Returns a vector of absolute value x and absolute value y. """
        return Vector2(abs(self._x), abs(self._y))
    
    def __invert__(self) -> "Vector2":
        """ Inverts the x and the y values. """
        return Vector2(self._y, self._x)

    def to_json(self):
        """ Converts vector to json. """
        data: dict[str, float] = {"x": self._x, "y": self._y}
        return json.dumps(data)
    
    @staticmethod
    def from_json(document: any) -> "Vector2":
        """ Converts data from json file. """
        data: any = json.loads(document)
        return Vector2(data["x"], data["y"])

    def to_tuple(self) -> tuple[float, float]:
        """ Converts value to tuple. """
        return self._x, self._y

    @staticmethod
    def from_tuple(self, value: tuple[float, float]) -> "Vector2":
        """ Converts a tuple into a Vector2. """
        return Vector2(value[0], value[1])

    def dot(self, other: "Vector2") -> float:
        return (self.x * other.x) + (self.y * other.y)

    def dist(self, other: "Vector2") -> float:
        """ Returns the distance between two vectors. """
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
    
    def anchor_dist(self) -> float:
        """ Returns the distance between this vector and it's anchor point.  (default anchor_point=(0.0, 0.0)) """
        return ((self._x - self._anchor_point[0]) ** 2 + (self._y - self._anchor_point[1]) ** 2) ** 0.5

    def delta_x(self, other: "Vector2") -> float:
        return abs(self.x - other.x)
    
    def delta_y(self, other: "Vector2") -> float:
        return abs(self.y - other.y)

    def delta_vector(self, other: "Vector2") -> "Vector2":
        return Vector2(abs(self.x - other.x), abs(self.y - other.y))

    def get_angle(self, other: "Vector2") -> float:
        raise NotImplementedError

    def normalize(self) -> "Vector2":
        raise NotImplementedError

    @property
    def quadrant(self) -> int:
        """ Figures out what quadrant the point occupies. """
        if self.x > 0:
            return 1 if self.y > 0 else 4
        return 2 if self.y > 0 else 3

    @property
    def x(self) -> float:
        return self._x
    
    @property
    def y(self) -> float:
        return self._y

