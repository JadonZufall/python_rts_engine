import pygame


class PawnModel:
    SIZE: int = 50
    def __init__(self, target) -> None:
        self.source: pygame.Surface = pygame.Surface((PawnModel.SIZE, PawnModel.SIZE), pygame.SRCALPHA)
        pygame.draw.circle(self.source, (255, 0, 0), (PawnModel.SIZE // 2, PawnModel.SIZE // 2), PawnModel.SIZE // 2, width=0)
        pygame.draw.circle(self.source, (0, 0, 0), (PawnModel.SIZE // 2, PawnModel.SIZE // 2), PawnModel.SIZE // 2, width=0)
        pygame.draw.arc(self.source, (0, 255, 0), [0, 0, PawnModel.SIZE, PawnModel.SIZE], 0.0, 360.0 * (target.health / target.max_health), width=5)
        pygame.draw.arc(self.source, (0, 0, 255), [0, 0, PawnModel.SIZE, PawnModel.SIZE], 0.0, 360.0 * (target.armor / target.max_armor), width=5)
    
    def drawon(self, other: pygame.Surface, target) -> None:
        other.blit(self.source, (target.x - PawnModel.SIZE / 2, target.y - PawnModel.SIZE / 2))
        return None

    def redraw(self, target) -> None:
        self.source: pygame.Surface((PawnModel.SIZE, PawnModel.SIZE), pygame.SRCALPHA)
        pygame.draw.circle(self.source, (255, 0, 0), (PawnModel.SIZE // 2, PawnModel.SIZE // 2), PawnModel.SIZE // 2, width=0)
        pygame.draw.circle(self.source, (0, 0, 0), (PawnModel.SIZE // 2, PawnModel.SIZE // 2), PawnModel.SIZE // 2, width=0)
        pygame.draw.arc(self.source, (0, 255, 0), [0, 0, PawnModel.SIZE, PawnModel.SIZE], 0.0, 360.0 * (target.health / target.max_health))
        pygame.draw.arc(self.source, (0, 0, 255), [0, 0, PawnModel.SIZE, PawnModel.SIZE], 0.0, 360.0 * (target.armor / target.max_armor))