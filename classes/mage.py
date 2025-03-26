from classes.classe import Classe

class Mage(Classe):
    def __init__(self):
        super().__init__("Mage", pv=80, pm=120, force=30, intelligence=100,
                         défense=40, résistance_magique=80, agilité=50, 
                         chance=60, endurance=70, esprit=90)

    def description(self):
        return "Un maître des arcanes capable de puissants sorts magiques."