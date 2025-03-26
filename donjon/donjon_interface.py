from abc import ABC, abstractmethod

class DonjonInterface(ABC):
    @abstractmethod
    def afficher_salle(self, x, y):
        pass

    @abstractmethod
    def afficher_minimap(self, x, y):
        pass
