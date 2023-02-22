from ._input_handler import InputHandler


class KeyboardHandler(InputHandler):
    def __init__(self) -> None:
        super().__init__()
    
    def update(self, delta_time: float) -> None:
        super().update(delta_time)
