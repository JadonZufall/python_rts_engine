from typing import Sequence, Union
import pygame

#from context import MouseHandler
#from context import CameraHandler
from res import PawnModel

from pawn import Pawn
from action import Action, PawnMove

FRAME_RATE: int = 60

def calc_dist(p1: tuple[float, float], p2: tuple[float, float]) -> float:
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5


def main() -> None:
    # Construct handler objects
    #mouse: MouseHandler = MouseHandler()
    #camera: CameraHandler = CameraHandler()
    pawns: list[Pawn] = [Pawn()]
    pawns[0].x = 250
    pawns[0].y = 250
    pawns.append(Pawn())

    # Initialize res and textures
    font: pygame.font.Font = pygame.font.SysFont("", 15)

    tick: int = 0
    render_debug: bool = True

    m_toggle: list[bool, bool, bool] = [False, False, False]
    drag_x, drag_y = 0, 0
    m_click_frame: bool = False
    release_x, release_y = 0, 0
    m_release_frame: bool = False

    pawn_select: Union[Pawn, None] = None
    pawn_select_debounce: float = 0
    last_select: Union[any, None] = None

    window = pygame.display.set_mode((500, 500), vsync=True)
    clock = pygame.time.Clock()
    pygame.display.set_caption("CsRTS")
    window.fill(color=(255, 255, 255))
    is_running: bool = True
    while is_running:
        window.fill((255, 255, 255))
        ms: float = clock.tick(FRAME_RATE)
        fps: float = clock.get_fps()
        delta_time: float = ms / 1_000.0
        tick += 1
        
        if not pawn_select_debounce <= 0.0:
            pawn_select_debounce -= ms
        else:
            pawn_select_debounce = 0.0
        
        if not m_release_frame and not m_toggle[0] and pawn_select_debounce == 0.0:
            pawn_select = None

        keyboard: Sequence[bool] = pygame.key.get_pressed()
        m_button: Sequence[bool] = pygame.mouse.get_pressed()
        m_status: Sequence[bool] = pygame.mouse.get_focused()

        if m_button[0] and not m_toggle[0]:
            # On mouse first click
            m_click_frame: bool = True
            drag_x, drag_y = pygame.mouse.get_pos()
        else:
            m_click_frame: bool = False
        if not m_button[0] and m_toggle[0]:
            # On mouse release
            m_release_frame: bool = True
            release_x, release_y = pygame.mouse.get_pos()
            last_select = pawn_select
            pawn_select = None
        else:
            m_release_frame: bool = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
        
        for i, p in enumerate(pawns):
            p.update(delta_time)
            p.model.drawon(window, p)
            # window.blit(pawn_texture, (p.x - pawn_texture.get_width() / 2, p.y - pawn_texture.get_height() / 2))
            if pawn_select_debounce <= 0.0 and m_click_frame:
                if calc_dist(pygame.mouse.get_pos(), p.get_pos()) < PawnModel.SIZE / 2:
                    print("Pawn Selected!")
                    pawn_select: Union[Pawn, None] = p
                    pawn_select_debounce: float = 333.33
            
            if p is last_select:
                if m_release_frame:
                    p.queue_action(PawnMove(p, 100, release_x, release_y))
        
        if m_button[0] and pawn_select:
            pygame.draw.line(window, (255, 0, 0), (drag_x, drag_y), pygame.mouse.get_pos())
        if isinstance(last_select, Pawn) and not pawn_select:
            pygame.draw.line(window, (0, 0, 255), (release_x, release_y), (drag_x, drag_y))
        
        # Update mouse toggle
        for i in range(0, len(m_toggle)):
            if not m_button[i] and m_toggle[i]:
                m_toggle[i] = False
            if m_button[i] and not m_toggle[i]:
                m_toggle[i] = True
        
        if render_debug:
            window.blit(font.render(f"delta_time  = {delta_time}", True, (0, 0, 0)), (50, 10))
            window.blit(font.render(f"framerate   = {fps}", True, (0, 0, 0)), (50, 20))
            window.blit(font.render(f"mouse_tog   = {m_toggle[0]}, {m_toggle[1]}, {m_toggle[2]}", True, (0, 0, 0)), (50, 30))
            window.blit(font.render(f"pawn_select = {type(pawn_select)}", True, (0, 0, 0)), (50, 40))
            window.blit(font.render(f"last_select = {type(last_select)}", True, (0, 0, 0)), (50, 50))
            window.blit(font.render(f"pawn_bounce = {pawn_select_debounce}", True, (0, 0, 0)), (50, 60))
            cur_act = pawns[0].queued_actions[0] if len(pawns[0].queued_actions) > 0 else None
            window.blit(font.render(f"pawn[0].pos = {pawns[0].x}, {pawns[0].y}", True, (0, 0, 0)), (50, 70))
            window.blit(font.render(f"pawn[0].action = {cur_act}", True, (0, 0, 0)), (50, 80))
            window.blit(font.render(f"pawn[0].dist_remains = {cur_act.dist_remain if cur_act else None}", True, (0, 0, 0)), (50, 90))
        pygame.display.flip()


if __name__ == "__main__":
    pygame.init()
    main()

