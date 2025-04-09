class Case:
    def __init__(self, nom): # Le constructeur initialise le nom de la case
        self.nom = nom # Le nom de la case
     # La méthode __str__ permet de retourner le nom de la case lorsqu'on l'affiche
    def __str__(self):
        return self.nom
    
    def action(self, joueur, partie):
        pass # Ne fait rien, elle sera redéfinie dans les sous-classes