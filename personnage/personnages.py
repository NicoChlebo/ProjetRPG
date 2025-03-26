from classes.classe import Classe

class Personnage:
    def __init__(self, nom_perso: str, classe_perso: Classe):
        self.nom_personnage = nom_perso
        self.classe = classe_perso