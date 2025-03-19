import random

class Donjon:
    TAILLE = 6
    
    def __init__(self):
        self.grille = self.generer_donjon()

    def generer_donjon(self):
        elements = ["Vide", "Monstre", "Trésor", "Piège"]
        return [[random.choice(elements) for _ in range(self.TAILLE)] for _ in range(self.TAILLE)]

    def afficher_salle(self, x, y):
        return self.grille[y][x]

    def afficher_minimap(self, joueur_x, joueur_y):
        print("\n🗺️ Mini-Map du Donjon :")
        for y in range(self.TAILLE):
            for x in range(self.TAILLE):
                if x == joueur_x and y == joueur_y:
                    print("🧍", end=" ")
                else:
                    print("⬜", end=" ")
            print()

    def salle_contient_monstre(self, x, y):
        return self.grille[y][x] == "Monstre"

    def vider_salle(self, x, y):
        self.grille[y][x] = "Vide"
