# Monopoly en Python

Ce projet est une implémentation simple du jeu **Monopoly** en Python. Il permet de simuler une partie de Monopoly avec des joueurs, des terrains, des actions spéciales et des règles comme les déplacements sur le plateau, l'achat de terrains, le paiement de loyers, et la gestion de la prison.

## Fonctionnalités principales

- **Joueurs** : Chaque joueur a un nom, un solde, une liste de propriétés, et une position sur le plateau.
- **Plateau** : Le plateau contient des cases normales et spéciales comme "Départ", "Prison", "Parc Gratuit", et "Aller en prison".
- **Déplacement** : Les joueurs tirent des dés pour se déplacer sur le plateau.
- **Achats** : Les joueurs peuvent acheter des terrains s'ils ont suffisamment d'argent.
- **Gestion de la prison** : Si un joueur tombe sur la case "Aller en prison" ou fait trois doubles consécutifs, il va en prison et peut tenter de sortir en payant ou en faisant un double.
- **Loyers** : Les joueurs doivent payer des loyers lorsqu'ils tombent sur un terrain appartenant à un autre joueur.
- **Améliorations** : Les joueurs peuvent acheter des maisons ou des hôtels pour augmenter le loyer de leurs terrains.

## Structure du projet

### 1. **Classes principales**

- **`Case`** : Représente une case sur le plateau. Cette classe est héritée par les cases normales et spéciales.
- **`Joueur`** : Gère les actions d'un joueur, y compris son solde, ses propriétés, et ses déplacements.
- **`Partie`** : Gère la logique du jeu, y compris le déroulement des tours, les règles de la prison, et la gestion des joueurs.
- **`Plateau`** : Représente le plateau de jeu, contenant toutes les cases et leur agencement.
- **`Terrain`** : Hérite de la classe `Case` et représente un terrain que les joueurs peuvent acheter, louer, et améliorer avec des maisons et des hôtels.

### 2. **Gameplay**

- **Déplacement** : À chaque tour, un joueur lance les dés pour déterminer son déplacement. Si un joueur fait un double, il rejoue immédiatement. S'il fait trois doubles consécutifs, il va directement en prison.
- **Achats de terrains** : Lorsqu'un joueur atterrit sur un terrain qui n'a pas de propriétaire, il peut choisir de l'acheter. Les terrains ont un coût d'achat et génèrent des loyers pour leur propriétaire.
- **Propriétés et loyers** : Les joueurs peuvent acheter des terrains et les améliorer en y construisant des maisons et des hôtels. Chaque amélioration augmente le loyer que d'autres joueurs doivent payer lorsqu'ils atterrissent sur la propriété.
- **Gestion de la prison** : Un joueur peut se retrouver en prison s'il tombe sur la case "Aller en prison" ou s'il fait trois doubles consécutifs. Il peut en sortir en payant une amende ou en faisant un double lors de ses prochains tours.
- **Fin de jeu** : Le jeu se termine lorsqu'un seul joueur reste avec un solde positif. Le gagnant est celui qui a le plus d'argent.

## Installation

1. Clonez ce dépôt :
   ```bash
   git clone https://github.com/votre-utilisateur/monopoly.git
