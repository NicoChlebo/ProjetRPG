from deplacement.deplacement_interface import DeplacementInterface
from affichage_jeu import AffichageJeu
from donjon.donjon_interface import DonjonInterface
from personnage.personnage_interface import PersonnageInterface
from deplacement.gestion_commande import GestionCommandes

class Jeu:
    @staticmethod
    def jouer(personnage: PersonnageInterface, deplacement: DeplacementInterface, donjon: DonjonInterface):
        gestion_commandes = GestionCommandes(deplacement)

        while True:
            AffichageJeu.afficher_jeu(deplacement, personnage, donjon)
            commande = input("🕹️ Commande (N/S/E/O/A/G/D) : ").upper()
            gestion_commandes.executer_commande(commande)
