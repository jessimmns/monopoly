from Case import Case
from Terrain import Terrain
from CaseSpeciale import CaseSpeciale

class Plateau:
    def __init__(self):
        self.cases = []
        self.initialiser_plateau()
    
    def initialiser_plateau(self):
        # Cases spéciales
        self.cases.append(CaseSpeciale("Départ"))
        self.cases.append(Terrain("Boulevard de Belleville", "marron", 60, 40, 100, 500))
        self.cases.append(Terrain("Rue Lecourbe", "marron", 60, 40, 100, 500))
        self.cases.append(Terrain("Gare Montparnasse", "gare", 200, 100, 0, 0))
        self.cases.append(Terrain("Rue de Vaugirard", "bleu", 100, 80, 100, 500))
        self.cases.append(Terrain("Rue de Courcelles", "bleu", 100, 80, 100, 500))
        self.cases.append(Terrain("Avenue de la République", "bleu", 120, 100, 100, 500))
        self.cases.append(CaseSpeciale("Prison"))
        self.cases.append(Terrain("Boulevard de la Villette", "rose", 140, 120, 150, 700))
        self.cases.append(Terrain("Avenue de Neuilly", "rose", 140, 120, 150, 700))
        self.cases.append(Terrain("Rue de Paradis", "rose", 160, 140, 150, 700))
        self.cases.append(Terrain("Gare de Lyon", "gare", 200, 100, 0, 0))
        self.cases.append(Terrain("Avenue Mozart", "orange", 180, 160, 150, 700))
        self.cases.append(Terrain("Boulevard Saint-Michel", "orange", 180, 160, 150, 700))
        self.cases.append(Terrain("Place Pigalle", "orange", 200, 180, 150, 700))
        self.cases.append(CaseSpeciale("Parc Gratuit"))
        self.cases.append(Terrain("Avenue Matignon", "rouge", 220, 200, 200, 900))
        self.cases.append(Terrain("Boulevard Malesherbes", "rouge", 220, 200, 200, 900))
        self.cases.append(Terrain("Avenue Henri-Martin", "rouge", 240, 220, 200, 900))
        self.cases.append(Terrain("Gare du Nord", "gare", 200, 100, 0, 0))
        self.cases.append(Terrain("Faubourg Saint-Honoré", "jaune", 260, 240, 200, 900))
        self.cases.append(Terrain("Place de la Bourse", "jaune", 260, 240, 200, 900))
        self.cases.append(Terrain("Rue La Fayette", "jaune", 280, 260, 200, 900))
        self.cases.append(Terrain("Gare Saint-Lazare", "gare", 200, 100, 0, 0))
        self.cases.append(Terrain("Avenue de Breteuil", "vert", 300, 280, 300, 950))
        self.cases.append(Terrain("Avenue Foch", "vert", 300, 280, 300, 950))
        self.cases.append(Terrain("Boulevard des Capucines", "vert", 320, 300, 300, 950))
        self.cases.append(CaseSpeciale("Aller en prison"))
        self.cases.append(Terrain("Avenue des Champs-Élysées", "violet", 350, 330, 350, 1000))
        self.cases.append(Terrain("Rue de la Paix", "violet", 350, 330, 350, 1000))
    
    def avoir_case(self, index):
        return self.cases[index % len(self.cases)]
    
    def __str__(self):
        return "\n".join([f"{i}: {case}" for i, case in enumerate(self.cases)])