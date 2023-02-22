import pygame

from ._input_handler import InputHandler


class MouseHandler(InputHandler):
    DEBOUNCE_DELAY: float = 0.300
    def __init__(self) -> None:
        super().__init__()
        self.x, self.y = pygame.mouse.get_pos()
        # Buttons store if the button is physically pushed this frame.
        self.buttons: list[bool] = pygame.mouse.get_pressed()
        # Toggles store if the button has been held over sense last frame.
        self.toggles: list[bool] = [False, False, False]
        # Pressed store if the button was just pressed this frame.
        self.pressed: list[bool] = [False, False, False]
        # Timers store the debounce time till you can press again.
        self.timers: list[float] = [0.0, 0.0, 0.0]
        # Stores where you start dragging the mouse from.
        self.drag_x, self.drag_y = pygame.mouse.get_pos()
        
    def update(self, delta_time: float) -> None:
        super().update(delta_time)
        self.x, self.y = pygame.mouse.get_pos()
        self.buttons: list[bool] = pygame.mouse.get_pressed()
        for i in range(0, 3):
            # Reset the pressed.
            self.pressed[i] = False

            # Reset the timer if it overshot.
            if self.timers[i] < 0.0:
                self.timers[i] = 0.0
            
            # Subtract deltatime from the timer.
            elif self.timers[i] > 0.0:
                self.timers[i] -= delta_time
        
            # If the button is pressed and is ready to be pressed but has not been updated yet.
            if self.buttons[i] and self.timers[i] == 0.0 and not self.toggles[i]:
                # Set drag position start recording it here.
                self.drag_x, self.drag_y = self.x, self.y

                # Update mouse variables
                self.timers[i] = MouseHandler.DEBOUNCE_DELAY
                self.toggles[i] = True
                self.pressed[i] = True
            
            # Clear the button from being pressed
            if not self.buttons[i] and self.toggles[i]:
                self.toggles[i] = False
                self.pressed[i] = False
        return

            
                

