from abc import ABC, abstractmethod

class AttributsBase(ABC):
    @property
    @abstractmethod
    def pv(self):
        pass

    @property
    @abstractmethod
    def pm(self):
        pass
