from obj import Vector2


class CameraHandler:
    def __init__(self, x: float=0.0, y: float=0.0) -> None:
        self._pos: Vector2 = Vector2(x, y)
    
    def to_tuple(self) -> tuple[float, float]:
        return self._pos.to_tuple()

    def set_pos(self, pos: Vector2) -> None:
        self._pos: Vector2 = pos
    
    def get_pos(self) -> Vector2:
        return self._pos
    
    def offset(self, pos: Vector2) -> Vector2:
        return pos + self._pos
    
    @property
    def x(self) -> float:
        return self._pos.x
    
    @property
    def y(self) -> float:
        return self._pos.y

