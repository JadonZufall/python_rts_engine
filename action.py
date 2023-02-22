from utils.type_hints import Pawn

def calc_dist(p1: tuple[float, float], p2: tuple[float, float]) -> float:
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

class Action:
    def __init__(self, target: Pawn) -> None:
        self.target: Pawn = target
        self.in_progress: bool = False
        self.is_complete: bool = False
        self.ticks_updated: int = 0
        self.time_passed: float = 0.0

    def perform(self, delta_time: float) -> None:
        self.in_progress = True
        self.ticks_updated += 1
        self.time_passed += delta_time
    
    def complete(self) -> None:
        self.in_progress = False
        self.is_complete = True
        return None


class PawnMove(Action):
    # TODO: This needs a major fix but who knows what that is?
    # NEED TO normalize the values instead of dividing by the distance because dividing by the distance is basically the hypotanouse calcuation which is not the same as the total between both of them.
    def __init__(self, target: Pawn, move_speed: int, target_x: float, target_y: float) -> None:
        super().__init__(target)
        self.target_pos: tuple[float, float] = (target_x, target_y)
        self.dist = calc_dist(target.get_pos(), (target_x, target_y))
        self.move_speed = move_speed
        self.dist_remain: float = calc_dist(self.target.get_pos(), self.target_pos)
    
    def perform(self, delta_time: float) -> None:
        super().perform(delta_time)
        try:
            self.dist_remain: float = calc_dist(self.target.get_pos(), self.target_pos)
            delt_vector: tuple[float, float] = self.target.x - self.target_pos[0], self.target.y - self.target_pos[1]
            norm_vector: tuple[float, float] = delt_vector[0] / abs(self.dist_remain), delt_vector[1] / abs(self.dist_remain)
            move_vector: tuple[float, float] = self.move_speed * norm_vector[0] * delta_time * -1, self.move_speed * norm_vector[1] * delta_time * -1
            pawn_vector: tuple[float, float] = self.target.x + move_vector[0], self.target.y + move_vector[1]
            if ((pawn_vector[0] - self.target_pos[0]) < 0) ^ ((self.target.get_pos()[0] - self.target_pos[0]) < 0) and ((pawn_vector[1] - self.target_pos[1]) < 0) ^ ((self.target.get_pos()[1] - self.target_pos[1]) < 0):
                self.complete()
            else:
                self.target.set_pos(pawn_vector)
        except ZeroDivisionError:
            self.complete()
    
    def complete(self) -> None:
        super().complete()
        print(f"PawnMove action completed in {self.ticks_updated} ticks ({self.time_passed}ms)")
        self.target.set_pos(self.target_pos)

        



