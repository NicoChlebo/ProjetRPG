from .deplacement_interface import DeplacementInterface
from typing import Tuple

class DeplacementNord(DeplacementInterface):
    def move(self, current_position: Tuple[int, int]) -> Tuple[int, int]:
        x, y = current_position
        return (x, y - 1)

    def get_direction(self) -> str:
        return "N"
