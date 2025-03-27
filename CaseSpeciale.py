from Case import Case

class CaseSpeciale(Case):
    def __init__(self, nom, effet):
        super().__init__(nom)
        self.effet = effet 

    def action(self, joueur):
        
        print(f"{joueur.nom} est sur {self.nom}.")
        self.effet(joueur)
