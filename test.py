from Joueur import Joueur
from Terrain import Terrain

def test_achat():
    joueur = Joueur("Test")
    terrain = Terrain("Rue", 200, 20)
    joueur.acheter(terrain)
    assert terrain in joueur.proprietes
    print("Test achat réussi !")

test_achat()




