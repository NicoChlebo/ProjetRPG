from personnage.nom_perso import NomPersonnage
from personnage.choix_classe_perso import ChoixClassePerso
from personnage.personnages import Personnage

class CreerPersonnage:
    @staticmethod
    def creer_personnage():
        nom = NomPersonnage.nom_personnage()
        classe = ChoixClassePerso.choix_classe()
        return Personnage(nom, classe)