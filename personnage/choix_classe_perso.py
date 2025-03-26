from classes.guerrier import Guerrier
from classes.mage import Mage
from classes.voleur import Voleur

class ChoixClassePerso:
    @staticmethod
    def choix_classe():
        classe_dispo = [Guerrier(), Mage(), Voleur()]
        print("Choisissez votre classe:")
        for i, classe in enumerate(classe_dispo):
            print(f"{i+1}. {classe.nom}")
        choix = int(input("Entrez le numéro de la classe choisie: "))
        return classe_dispo[choix - 1]