

class Timer:
    def __init__(self, ms: int) -> None:
        self._ms: float = ms
        self._at: float = 0.0
    
    def update(self, dt: int) -> None:
        self._at += dt
    
    def reset(self) -> None:
        self._at: float = 0.0

    @property
    def is_done(self) -> bool:
        return self._at >= self._ms