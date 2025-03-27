from Case import Case

class Terrain(Case):
    def __init__(self, nom, prix, loyer):
        super().__init__(nom)
        self.prix = prix
        self.loyer = loyer
        self.proprietaire = None
        self.nb_maisons = 0
        self.hotel = False

    def ameliorer(self):
        
        if self.hotel:
            print("Impossible d'améliorer, un hôtel est déjà construit.")
            return
        if self.nb_maisons < 4:
            self.nb_maisons += 1
            print(f"Une maison a été ajoutée sur {self.nom}.")
        else:
            self.hotel = True
            print(f"Un hôtel a été construit sur {self.nom}.")

    def calculer_loyer(self):
        
        if self.hotel:
            return self.loyer * 1.4
        return self.loyer * (1.2 ** self.nb_maisons)

    def action(self, joueur):
        
        if self.proprietaire is None:
            achat = input(f"Voulez-vous acheter {self.nom} pour {self.prix} ? (o/n) ")
            if achat.lower() == "o":
                joueur.acheter(self)
        elif self.proprietaire != joueur:
            joueur.payer(self.calculer_loyer(), self.proprietaire)
