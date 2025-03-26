from deplacement.deplacement import Deplacement
from deplacement.deplacement_nord import DeplacementNord
from deplacement.deplacement_sud import DeplacementSud
from deplacement.deplacement_est import DeplacementEst
from deplacement.deplacement_ouest import DeplacementOuest
from .deplacement_enum import Direction
from typing import Dict

class GestionCommandes:
    def __init__(self, deplacement: Deplacement):
        self.deplacement = deplacement

        self.strategies = {
            Direction.NORD: DeplacementNord(),
            Direction.SUD: DeplacementSud(),
            Direction.EST: DeplacementEst(),
            Direction.OUEST: DeplacementOuest()
        }

    def executer_commande(self, commande: str):
        try:
            direction = Direction(commande)
            mouvement = self.strategies[direction]
            nouvelle_position = mouvement.move((self.deplacement.x, self.deplacement.y))
            self.deplacement.x, self.deplacement.y = nouvelle_position
        except ValueError:
            print("⚠️ Commande invalide.")
