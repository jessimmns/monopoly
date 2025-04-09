from Case import Case

class CaseSpeciale(Case):
    def __init__(self, nom):
        super().__init__(nom)
    
    def action(self, joueur, partie):
        if self.nom == "Départ":
            joueur.crediter(200)
            print(f"{joueur.nom} passe par la case Départ et reçoit 200€")
        elif self.nom == "Prison":
            print(f"{joueur.nom} visite simplement la prison")
        elif self.nom == "Parc Gratuit":
            print(f"{joueur.nom} se repose au Parc Gratuit")
        elif self.nom == "Aller en prison":
            joueur.position = 10  # Position de la prison
            joueur.en_prison = True
            print(f"{joueur.nom} va en prison!")