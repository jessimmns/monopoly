class Joueur:
    def __init__(self, nom):
        self.nom = nom
        self.solde = 1500
        self.position = 0
        self.proprietes = []
        self.en_prison = False
        self.nb_tours_prison = 0

    def deplacement(self, de, plateau):
        
        if self.en_prison:
            if self.nb_tours_prison < 3:
                print(f"{self.nom} est en prison et reste un tour de plus.")
                self.nb_tours_prison += 1
                return
            else:
                print(f"{self.nom} sort de prison !")
                self.en_prison = False
                self.nb_tours_prison = 0

        ancienne_position = self.position
        self.position = (self.position + de) % len(plateau.cases)
        if self.position < ancienne_position:
            self.solde += 200  
            print(f"{self.nom} passe par la case Départ et reçoit 200.")
        plateau.cases[self.position].action(self)

    def acheter(self, terrain):
        
        if self.solde >= terrain.prix:
            self.solde -= terrain.prix
            self.proprietes.append(terrain)
            terrain.proprietaire = self
            print(f"{self.nom} a acheté {terrain.nom} pour {terrain.prix}!")
        else:
            print("Vous n'avez pas assez d'argent.")

    def payer(self, montant, proprietaire):
        
        if self.solde >= montant:
            self.solde -= montant
            proprietaire.solde += montant
            print(f"{self.nom} a payé {montant} à {proprietaire.nom}.")
        else:
            print(f"{self.nom} est en faillite !")
