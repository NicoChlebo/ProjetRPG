from abc import ABC, abstractmethod

class PersonnageInterface(ABC):
    @abstractmethod
    def recap_perso(self):
        pass

    @abstractmethod
    def nom_personnage(self):
        pass
