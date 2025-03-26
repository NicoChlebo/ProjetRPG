class RecapPerso:
    @staticmethod
    def recap_perso(personnage):
        print(f"Nom: {personnage.nom_personnage}")
        print(f"Classe: {personnage.classe.nom}")
        print(f"PV: {personnage.classe.pv}")
        print(f"PM: {personnage.classe.pm}")
        print(f"Force: {personnage.classe.force}")
        print(f"Intelligence: {personnage.classe.intelligence}")
        print(f"Défense: {personnage.classe.défense}")
        print(f"Résistance magique: {personnage.classe.résistance_magique}")
        print(f"Agilité: {personnage.classe.agilité}")
        print(f"Chance: {personnage.classe.chance}")
        print(f"Endurance: {personnage.classe.endurance}")
        print(f"Esprit: {personnage.classe.esprit}")
        print("Personnage créé avec succès !")