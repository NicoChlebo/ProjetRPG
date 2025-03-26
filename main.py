from deplacement.deplacement import Deplacement
from personnage.creer_perso import CreerPersonnage
from personnage.personnages import Personnage
from personnage.recap_perso import RecapPerso
from jeu import Jeu
from donjon.donjon import Donjon

# Programme principal 
creer_personnage = CreerPersonnage.creer_personnage()
RecapPerso.recap_perso(creer_personnage)
Jeu.jouer(Personnage, Deplacement, Donjon)