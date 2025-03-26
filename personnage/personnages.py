from classes.classe import Classe

class Personnage(Classe):
    def __init__(self, nom_perso, classe_perso):
        super().__init__(classe_perso.nom, classe_perso.pv, classe_perso.pm, classe_perso.force,
                         classe_perso.intelligence, classe_perso.défense, 
                         classe_perso.résistance_magique, classe_perso.agilité, 
                         classe_perso.chance, classe_perso.endurance, classe_perso.esprit)
        self.nom_personnage = nom_perso
        self.classe = classe_perso