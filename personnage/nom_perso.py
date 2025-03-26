class NomPersonnage:
    @staticmethod
    def nom_personnage():
        nom_perso = input("Entrez le nom de votre personnage: ")
        while len(nom_perso) < 2 or len(nom_perso) > 15:
            print("Le nom de votre personnage doit être compris entre 2 et 15 caractères")
            nom_perso = input("Entrez le nom de votre personnage: ")
        return nom_perso