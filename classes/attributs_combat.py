from abc import ABC, abstractmethod

class AttributsCombat(ABC):
    @property
    @abstractmethod
    def force(self):
        pass

    @property
    @abstractmethod
    def défense(self):
        pass
