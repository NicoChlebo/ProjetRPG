from abc import abstractmethod
from .attributs_base import AttributsBase
from .attributs_combat import AttributsCombat
from .attributs_magie import AttributsMagie

class Classe(AttributsBase, AttributsCombat, AttributsMagie):
    def __init__(self, nom, pv, pm, force, intelligence, défense, résistance_magique, agilité, chance, endurance, esprit):
        self.nom = nom
        self._pv = pv
        self._pm = pm
        self._force = force
        self._intelligence = intelligence
        self._defense = défense
        self._résistance_magique = résistance_magique
        self.agilité = agilité
        self.chance = chance
        self.endurance = endurance
        self.esprit = esprit

    @property
    def pv(self):
        return self._pv

    @property
    def pm(self):
        return self._pm

    @property
    def force(self):
        return self._force

    @property
    def défense(self):
        return self._defense

    @property
    def résistance_magique(self):
        return self._résistance_magique

    @abstractmethod
    def description(self):
        pass
