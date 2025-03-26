import random

class Monstre:
    def __init__(self):
        self.pv = random.randint(10, 20)
        self.force = random.randint(2, 5)

    def attaquer(self):
        return self.force