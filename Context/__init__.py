from typing import Optional

import pygame

from ._mouse import MouseHandler
from ._camera import CameraHandler
from ._keyboard import KeyboardHandler

from obj import Vector2
from obj import Rect


class Context:
    def __init__(self) -> None:
        self._clock: pygame.time.Clock = pygame.time.Clock()
        self._mouse: MouseHandler = MouseHandler()
        self._camera: CameraHandler = CameraHandler()
        self._keyboard: KeyboardHandler = KeyboardHandler()
    
    def update(self) -> None:
        self._mouse.update()
        self._keyboard.update()
        self._camera.update()
    
    def render_to_window(self, surface: pygame.Surface, dest: Vector2, area: Optional[Rect]=None) -> None:
        window = pygame.display.get_surface()
        dest: Vector2 = self._camera.offset(dest)
        window.blit(surface, dest, area=area)



