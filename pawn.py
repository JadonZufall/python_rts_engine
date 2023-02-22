from typing import Optional
from typing import Union

import math

from utils.type_hints import Action

from res import PawnModel


class Pawn:
    """ Object that represents a Pawn in the game world.\n
    max_health (float) The maximum amount of health the pawn can have.\n
    max_armor  (float) The maximum amount of armor the pawn can have.\n
    """
    max_health: float = 100.0
    max_armor:  float = 100.0
    def __init__(self) -> None:
        """ Constructs a new instance of the Pawn object.\n
        """
        self.health: float = 100.0
        self.armor : float = 0.0
        self.queued_actions: list[Action] = []

        # Positional information
        self.x: float = 0.0
        self.y: float = 0.0

        # Stores the radius of the sound the Pawn is emitting.
        self.sound_radius: float = 0.0
        # Stores the view arc this Pawn can currently see at
        self.view_degrees: float = 90.0
        # The angle that this pawn is currently looking at
        self.look_angle: float = 0.0

        # Toggle variables
        self.is_alive:    bool = True       # This means the pawn is still alive
        self.is_running:  bool = False      # This means the Pawn is making footsteps.
        self.is_sneaking: bool = False      # This means the Pawn is sneaking.

        # Visual model
        self.model: PawnModel = PawnModel(self)
    
    def update(self, delta_time: float) -> None:
        current: Action = self.queued_actions[0] if len(self.queued_actions) > 0 else None
        if not current:
            return None
        current.perform(delta_time)
        if current.is_complete:
            self.queued_actions.pop(0)
    
    def get_pos(self) -> tuple[float, float]:
        return self.x, self.y
    
    def set_pos(self, *args) -> None:
        if len(args) == 2:
            self.x, self.y = args[0], args[1]
        else:
            self.x, self.y = args[0]
    
    def can_hear(self, other: "Pawn") -> bool:
        """ Checks if this pawn is close enough to another pawn to hear them. """
        distance: float = Pawn.calc_distance(self, other)
        return True if distance <= other.sound_radius else False

    def can_view(self, other: "Pawn") -> bool:
        """ Checks if this pawn is able to see another pawn.  This doesn't account for obsticals """
        delta_x, delta_y = Pawn.calc_delta(self, other)
        upper_b, lower_b = self.view_bounds(self)
        degrees: float = math.degrees(math.atan(delta_x / delta_y))
        return degrees < upper_b and degrees > lower_b

    def queue_action(self, action: Action) -> int:
        """ Queues an action then returns the index of that action. """
        self.queued_actions.append(action)
        return len(self.queued_actions) - 1
    
    def clear_action(self, action: Action) -> None:
        """ Removes an action from the queue and doesn't return anything. """
        result = [self.queued_actions.pop(i) if v is action else None for i, v in enumerate(self.queued_actions)]
        result = list(filter(lambda x: x is not None, result))
        return result[0] if len(result) > 0 else None 

    def quick_action(self, action: Action) -> bool:
        """ Attempts to immedietly perform an action returns True if it is able to. """
        if len(self.queued_actions) == 0:
            self.queued_actions.insert(0, action)
            return True 
        elif self.queued_actions[0].in_progress:
            self.queued_actions.insert(1, action)
            return False
        else: # not self.queued_actions[0].in_progress
            self.queued_actions.insert(0, action)
            return True

    def view_bounds(self) -> tuple[float, float]:
        """ Returns upper bound and lower bound in a tuple in that order. """
        return (self.look_angle + (self.view_degrees / 2)) % 360, (self.look_angle - (self.view_degrees / 2)) % 360

    @staticmethod
    def calc_distance(p1: "Pawn", p2: "Pawn") -> float:
        """ Calculates the distance between two pawns. """
        return ((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2) ** 0.5

    @staticmethod
    def calc_delta(p1: "Pawn", p2: "Pawn") -> tuple[float, float]:
        """ Calculates the delta x and delta y of two pawns. """
        return p1.x - p2.x, p1.y - p2.y


class PlayerPawn(Pawn):
    """ A pawn that is controlled by the player. """
    def __init__(self) -> None:
        super().__init__()