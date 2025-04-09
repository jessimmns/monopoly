
from Partie import Partie

def main():
    print("Bienvenue dans le Monopoly!")
    noms = input("Entrez les noms des joueurs séparés par des virgules: ").split(",")
    partie = Partie([nom.strip() for nom in noms])
    
    while True:
        partie.tour()
        
        # Vérifier s'il ne reste qu'un joueur
        joueurs_actifs = [j for j in partie.joueurs if not partie.joueur_faillite(j)]
        if len(joueurs_actifs) <= 1:
            break
    
    gagnant = partie.definir_gagnant()
    print(f"\nFélicitations {gagnant.nom}, vous avez gagné avec {gagnant.solde}€!")

if __name__ == "__main__":
    main()