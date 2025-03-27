import random
from Joueur import Joueur
from Plateau import Plateau

class Partie:
    def __init__(self, joueurs_noms):
        self.joueurs = [Joueur(nom) for nom in joueurs_noms]
        self.plateau = Plateau()
        self.tour_actuel = 0

    def tour(self):
        joueur = self.joueurs[self.tour_actuel % len(self.joueurs)]
        de = random.randint(1, 6) + random.randint(1, 6)
        print(f"{joueur.nom} lance les dés et fait {de}.")
        joueur.deplacement(de, self.plateau)
        self.tour_actuel += 1

    def lancer_partie(self):
        print("Début de la partie !")
        while len([j for j in self.joueurs if j.solde > 0]) > 1:
            self.tour()
        print("Fin de la partie !")
