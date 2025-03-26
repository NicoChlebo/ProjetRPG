from classes.classe import Classe

class Guerrier(Classe):
    def __init__(self):
        super().__init__("Guerrier", pv=150, pm=30, force=90, intelligence=40,
                         défense=80, résistance_magique=50, agilité=60, 
                         chance=50, endurance=100, esprit=60)

    def description(self):
        return "Un combattant puissant avec une force brute incroyable."