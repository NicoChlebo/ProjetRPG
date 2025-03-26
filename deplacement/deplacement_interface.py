from abc import ABC, abstractmethod
from typing import Tuple

class DeplacementInterface(ABC):
    @abstractmethod
    def move(self, current_position: Tuple[int, int]) -> Tuple[int, int]:
        pass

    @abstractmethod
    def get_direction(self) -> str:
        pass
