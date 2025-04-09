from random import randint

from random import randint

class Joueur:
    def __init__(self, nom):
        self.nom = nom
        self.solde = 1500
        self.proprietes = []
        self.position = 0
        self.en_prison = False
        self.doubles_consecutifs = 0
    
    def crediter(self, montant):
        self.solde += montant
    
    def debiter(self, montant):
        self.solde -= montant
    
    def acheter_terrain(self, terrain):
        if self.solde >= terrain.cout_achat:
            self.debiter(terrain.cout_achat)
            terrain.proprietaire = self
            self.proprietes.append(terrain)
            print(f"{self.nom} a acheté {terrain.nom} pour {terrain.cout_achat}€")
            return True
        else:
            print("Fonds insuffisants pour acheter ce terrain")
            return False
    
    def payer(self, autre_joueur, montant):
        if self.solde >= montant:
            self.debiter(montant)
            autre_joueur.crediter(montant)
            print(f"{self.nom} a payé {montant}€ à {autre_joueur.nom}")
        else:
            print(f"{self.nom} n'a pas assez d'argent pour payer!")
            # Gérer la faillite ici
    
    def tirer_de(self):
        de1 = randint(1, 6)
        de2 = randint(1, 6)
        total = de1 + de2
        print(f"{self.nom} a tiré {de1} et {de2} (total: {total})")
        
        if de1 == de2:
            self.doubles_consecutifs += 1
            print("Double! Le joueur rejoue")
        else:
            self.doubles_consecutifs = 0
        
        return total
    
    def __str__(self):
        return f"{self.nom} - Solde: {self.solde}€ - Position: {self.position}"