from monstres import Monstre
from personnage.personnages import Personnage

def combat(self):
        monstre = Monstre()
        personnage = Personnage()
        print(f"🔥 Combat engagé ! Monstre : {monstre.pv} PV | Joueur : {self.personnage.pv} PV")

        while monstre.pv > 0 and self.personnage.pv > 0:
            action = input("🎮 Attaquer (A) ou Fuir (F) ? ").upper()

            if action == "A":
                monstre.pv -= self.personnage.attaquer()
                print(f"🗡️ Vous attaquez ! Le monstre a {monstre.pv} PV restants.")

                if monstre.pv > 0:
                    self.personnage.pv -= monstre.attaquer()
                    print(f"💥 Le monstre vous attaque ! Vous avez {self.personnage.pv} PV restants.")
            elif action == "F":
                print("🏃 Vous fuyez le combat !")
                return False  # Fuite réussie, pas de déplacement

        if self.personnage.pv <= 0:
            print("💀 Vous êtes mort ! Game Over.")
            exit()

        print("🏆 Victoire ! Le monstre est vaincu.")
        return True
