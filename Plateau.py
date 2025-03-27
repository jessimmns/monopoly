from Case import Case
from CaseSpeciale import CaseSpeciale
from Terrain import Terrain

class Plateau:
    def __init__(self):
        self.cases = [
            Case("Départ"),
            Terrain("Avenue de la République", prix=200, loyer=50),
            CaseSpeciale("Prison", self.envoyer_prison),
            Terrain("Boulevard Saint-Michel", prix=300, loyer=75),
            CaseSpeciale("Impôt sur le revenu", self.payer_impot),
        ]

    def envoyer_prison(self, joueur):
       
        joueur.en_prison = True
        joueur.nb_tours_prison = 0
        joueur.position = 2 
        print(f"{joueur.nom} est envoyé en prison !")

    def payer_impot(self, joueur):
        if joueur.solde >= 200:
            joueur.solde -= 200 
            print(f"{joueur.nom} paye 200 d'impôt !")
        else:
            print(f"{joueur.nom} est en faillite car il ne peut pas payer l'impôt !")