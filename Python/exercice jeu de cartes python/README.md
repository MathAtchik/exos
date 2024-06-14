# Jeu de Distribution de Cartes

## Objectif

Créer un programme en Python qui simule la distribution de cartes d'un jeu de 52 cartes à plusieurs joueurs. Le programme demande à l'utilisateur le nombre de joueurs et le nombre de cartes à distribuer à chaque joueur, puis affiche les mains distribuées.

## Instructions

1. **Initialiser le Projet**
   - Créez un nouveau fichier nommé `main.py`.

2. **Créer un Jeu de Cartes**
   - Définissez une fonction pour créer un jeu de cartes standard de 52 cartes. Un jeu de cartes contient 4 couleurs (Coeur, Carreau, Trèfle, Pique) et 13 valeurs (2 à 10, J, Q, K, A).

3. **Mélanger le Jeu de Cartes**
   - Définissez une fonction pour mélanger les cartes du jeu. Utilisez la bibliothèque `random` de Python pour cela.

4. **Distribuer les Cartes**
   - Définissez une fonction pour distribuer les cartes à un nombre donné de joueurs. La fonction doit prendre en compte le nombre de cartes à distribuer à chaque joueur.

5. **Interaction avec l'Utilisateur**
   - Demandez à l'utilisateur de saisir le nombre de joueurs.
   - Demandez à l'utilisateur de saisir le nombre de cartes à distribuer à chaque joueur.
   - Vérifiez que le nombre total de cartes demandées ne dépasse pas le nombre de cartes disponibles dans le jeu (52 cartes).

6. **Afficher les Mains des Joueurs**
   - Distribuez les cartes et affichez les mains de chaque joueur.

7. **Structure du Code**
   - Organisez votre code de manière à ce qu'il soit clair et lisible.
   - Utilisez des fonctions pour chaque tâche spécifique (création du jeu, mélange, distribution).
   - Assurez-vous que le script principal est exécuté uniquement lorsque le fichier est exécuté directement.

## Exemple de Sortie Attendue

Lorsque le programme est exécuté, il devrait ressembler à ceci :

Entrez le nombre de joueurs : 4
Entrez le nombre de cartes à distribuer à chaque joueur : 5
Main du joueur 1: ['4 de Pique', 'A de Coeur', ...]
Main du joueur 2: ['6 de Trèfle', '10 de Trèfle', ...]
...


Si le nombre de cartes demandé dépasse le nombre total de cartes disponibles, le programme doit afficher un message d'erreur :

Entrez le nombre de joueurs : 4
Entrez le nombre de cartes à distribuer à chaque joueur : 14
Il n'y a pas assez de cartes pour distribuer ce nombre à chaque joueur.


## Conseils

- Utilisez des listes pour représenter le jeu de cartes et les mains des joueurs.
- Utilisez des boucles pour distribuer les cartes de manière équitable entre les joueurs.
- Pensez à valider l'entrée utilisateur pour éviter des erreurs de saisie.

## Structure du Projet

Le fichier `main.py` devrait contenir les sections suivantes :

1. **Fonctions pour créer et mélanger le jeu de cartes :**
   ```python
   def créer_jeu():
       # Implémentation
       
   def mélanger_jeu(jeu):
       # Implémentation

    Fonction pour distribuer les cartes :

    def distribuer_cartes(jeu, nombre_de_joueurs, nombre_de_cartes):
    # Implémentation

2. Interaction avec l'utilisateur et affichage des mains :
    ```python

    def main():
        # Implémentation

    if __name__ == "__main__":
        main()

Avec ces consignes, vous devriez être en mesure de créer le fichier main.py qui répond aux exigences du projet. Bonne chance !