from deplacement.deplacement import Deplacement

class GestionCommandes:
    def __init__(self, deplacement: Deplacement):
        self.deplacement = deplacement

    def executer_commande(self, commande):
        if commande in ["N", "S", "E", "O"]:
            self.deplacement.deplacer(commande)
        elif commande == "A":
            self.deplacement.avancer()
        elif commande == "G":
            self.deplacement.tourner_gauche()
        elif commande == "D":
            self.deplacement.tourner_droite()
        else:
            print("⚠️ Commande invalide.")
