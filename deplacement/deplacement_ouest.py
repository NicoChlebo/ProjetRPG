from .deplacement_interface import DeplacementInterface
from typing import Tuple

class DeplacementOuest(DeplacementInterface):
    def move(self, current_position: Tuple[int, int]) -> Tuple[int, int]:
        x, y = current_position
        return (x - 1, y)

    def get_direction(self) -> str:
        return "O"
