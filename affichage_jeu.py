from deplacement.deplacement import Deplacement

class AffichageJeu:
    @staticmethod
    def afficher_jeu(deplacement, personnage, donjon):
        print(f"\n📍 Position : ({deplacement.x}, {deplacement.y}) - Orientation : {Deplacement.DIRECTIONS[deplacement.orientation]} - ❤️ {personnage.pv} PV")
        print(f"📦 Contenu de la salle : {donjon.afficher_salle(deplacement.x, deplacement.y)}")
        donjon.afficher_minimap(deplacement.x, deplacement.y)
