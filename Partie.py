from random import randint
from Joueur import Joueur # Importation de la classe Joueur
from Plateau import Plateau # Importation de la classe Plateau

class Partie:
    def __init__(self, noms_joueurs):
        self.plateau = Plateau() # Crée un plateau de jeu
        self.joueurs = [Joueur(nom) for nom in noms_joueurs]
        self.tour_actuel = 0
    
    def joueur_actuel(self):
        return self.joueurs[self.tour_actuel % len(self.joueurs)]
 # Méthode pour simuler un tour de jeu
    def tour(self):
        joueur = self.joueur_actuel()
        print(f"\n--- Tour de {joueur.nom} ---")
        
        if joueur.en_prison:
            self.gestion_prison(joueur)
            self.tour_actuel += 1
            return
        
        choix = self.choix_action(joueur)
        
        if choix == "1":  # Tirer le dé
            deplacement = joueur.tirer_de()
            joueur.position = (joueur.position + deplacement) % len(self.plateau.cases)
            print(f"{joueur.nom} se déplace à la case {joueur.position}: {self.plateau.avoir_case(joueur.position)}")
            
            # Traitement après déplacement
            case = self.plateau.avoir_case(joueur.position)
            case.action(joueur, self)
            
            # Vérifier si le joueur a fait un double
            if joueur.doubles_consecutifs > 0 and joueur.doubles_consecutifs < 3:
                print("Le joueur rejoue car il a fait un double")
                return  # Ne pas passer au joueur suivant
            
            if joueur.doubles_consecutifs >= 3:
                print("Triple double! Le joueur va en prison")
                joueur.position = 10  # Position de la prison
                joueur.en_prison = True
                joueur.doubles_consecutifs = 0
        
        elif choix == "2":  # Consulter compte
            print(joueur)
            for prop in joueur.proprietes:
                print(f"- {prop}")
            return  # Ne pas passer au joueur suivant
        
        elif choix == "3":  # Voir case actuelle
            case = self.plateau.avoir_case(joueur.position)
            print(f"Case actuelle: {case}")
            return  # Ne pas passer au joueur suivant
        
        self.tour_actuel += 1
    
    def gestion_prison(self, joueur):
        print(f"{joueur.nom} est en prison")
        choix = input("1 - Payer 50€ pour sortir\n2 - Essayer de faire un double\nVotre choix: ")
        
        if choix == "1":
            joueur.debiter(50)
            joueur.en_prison = False
            print(f"{joueur.nom} a payé 50€ pour sortir de prison")
        elif choix == "2":
            de1 = randint(1, 6)
            de2 = randint(1, 6)
            print(f"{joueur.nom} a tiré {de1} et {de2}")
            
            if de1 == de2:
                joueur.en_prison = False
                print("Double! Le joueur sort de prison")
                deplacement = de1 + de2
                joueur.position = (joueur.position + deplacement) % len(self.plateau.cases)
                print(f"{joueur.nom} se déplace à la case {joueur.position}: {self.plateau.avoir_case(joueur.position)}")
                case = self.plateau.avoir_case(joueur.position)
                case.action(joueur, self)
            else:
                print("Pas de double, le joueur reste en prison")
    
    def choix_action(self, joueur):
        print("Que voulez-vous faire ?")
        print("1 - Tirer le dé")
        print("2 - Consulter mon compte")
        print("3 - Voir sur quelle case je suis")
        return input("Votre choix: ")
    
    def joueur_faillite(self, joueur):
        return joueur.solde < 0
     # Méthode pour déterminer le gagnant de la partie
    def definir_gagnant(self):
        return max(self.joueurs, key=lambda j: j.solde)# Le joueur avec le plus de solde gagne