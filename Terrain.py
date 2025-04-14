from Case import Case

class Terrain(Case):
    def __init__(self, nom, couleur, cout_achat, loyer, cout_maison, cout_hotel):
        super().__init__(nom)
        self.couleur = couleur
        self.cout_achat = cout_achat
        self.loyer_base = loyer
        self.cout_maison = cout_maison
        self.cout_hotel = cout_hotel
        self.proprietaire = None
        self.nb_maisons = 0
        self.nb_hotels = 0
    
    def est_achetable(self):
        return self.proprietaire is None
    
    def calculer_loyer(self):
        if self.nb_hotels > 0:
            return self.loyer_base * 1.4 # Si un hôtel est présent, le loyer augmente
        elif self.nb_maisons > 0:
            return self.loyer_base * (1.2 * self.nb_maisons)
        return self.loyer_base # Sinon, le loyer est simplement le loyer de base
    # Méthode pour améliorer le terrain en construisant une maison ou un hôtel
    def ameliorer_terrain(self, joueur):
        if self.nb_hotels > 0:
            print("Ce terrain a déjà un hôtel, impossible d'améliorer davantage")
            return False
        
        if self.nb_maisons < 4:
            cout = self.cout_maison
            if joueur.solde >= cout:
                joueur.debiter(cout)
                self.nb_maisons += 1
                print(f"{joueur.nom} a construit une maison sur {self.nom} (total: {self.nb_maisons})")
                return True
            else:
                print("Fonds insuffisants pour construire une maison")
                return False
        else:
            cout = self.cout_hotel
            if joueur.solde >= cout:
                joueur.debiter(cout)
                self.nb_hotels = 1
                self.nb_maisons = 0
                print(f"{joueur.nom} a construit un hôtel sur {self.nom}")
                return True
            else:
                print("Fonds insuffisants pour construire un hôtel")
                return False
        # Méthode action qui définit ce qui se passe lorsqu'un joueur arrive sur un terrain
    def action(self, joueur, partie):
        if self.proprietaire is None:
            print(f"{self.nom} n'a pas de propriétaire")
            if joueur.solde >= self.cout_achat:
                reponse = input(f"Voulez-vous acheter {self.nom} pour {self.cout_achat}€ ? (o/n): ")
                if reponse == "o":
                    print(self.nom)
                    joueur.acheter_terrain(self)
        elif self.proprietaire != joueur:
            loyer = self.calculer_loyer()
            print(f"{joueur.nom} doit payer {loyer}€ de loyer à {self.proprietaire.nom}")
            joueur.payer(self.proprietaire, loyer)
      # Affiche les informations d'un terrain
    def __str__(self):
        return f"{self.nom} ({self.couleur}) - Maisons: {self.nb_maisons}, Hôtels: {self.nb_hotels}"