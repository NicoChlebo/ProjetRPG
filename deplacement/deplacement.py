class Deplacement:
    DIRECTIONS = ["Nord", "Est", "Sud", "Ouest"]

    def __init__(self, personnage, largeur, hauteur):
        self.personnage = personnage
        self.largeur = largeur  
        self.hauteur = hauteur  
        self.x = 0
        self.y = 0
        self.orientation = 0

    def deplacer(self, direction):
        if direction == "N" and self.y > 0:
            self.y -= 1
        elif direction == "S" and self.y < self.hauteur - 1:
            self.y += 1
        elif direction == "E" and self.x < self.largeur - 1:
            self.x += 1
        elif direction == "O" and self.x > 0:
            self.x -= 1
        else:
            print("⚠️ Déplacement impossible !")

    def avancer(self):
        self.deplacer(self.DIRECTIONS[self.orientation][0])

    def tourner_gauche(self):
        self.orientation = (self.orientation - 1) % 4

    def tourner_droite(self):
        self.orientation = (self.orientation + 1) % 4
