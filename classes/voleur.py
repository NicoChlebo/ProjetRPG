from classes.classe import Classe

class Voleur(Classe):
    def __init__(self):
        super().__init__("Voleur", pv=100, pm=40, force=70, intelligence=50,
                         défense=60, résistance_magique=50, agilité=90, 
                         chance=80, endurance=60, esprit=50)

    def description(self):
        return "Un combattant rapide et agile, spécialiste des attaques furtives."