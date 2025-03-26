from abc import ABC, abstractmethod

class AttributsMagie(ABC):
    @property
    @abstractmethod
    def résistance_magique(self):
        pass

    @property
    @abstractmethod
    def intelligence(self):
        pass
