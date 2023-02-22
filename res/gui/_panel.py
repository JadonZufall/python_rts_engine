from typing import Optional, Union
import pygame

from res import RGBColor
from obj import Vector2, PosType


class Panel:
    def __init__(self, size: tuple[int, int], fill: Optional[RGBColor] = RGBColor(255, 255, 255, 255)) -> None:
        self._size: tuple[int, int] = size
        self._fill: tuple[int, int, int] = fill
        self._pane: pygame.Surface = pygame.Surface(self._size, pygame.SRCALPHA)
        self._pane.fill(self._fill)
        self._children: list[Panel] = []

    def __index__(self) -> "Panel":
        for c in self._children:
            yield c
        return

    def draw_on(self, target: pygame.Surface, dest: PosType, area: Optional[pygame.Rect] = None) -> None:
        target.blit(target, dest, area=area)

    def add_child(self, child: "Panel") -> None:
        self._children.append(child)
    
    def get_child(self, index: int) -> "Panel":
        return self._children[index]
            