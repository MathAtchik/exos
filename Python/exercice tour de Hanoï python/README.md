# Exercice : La Tour de Hanoï

## Objectif

Les tours de Hanoï : [Wikipédia](https://fr.wikipedia.org/wiki/Tours_de_Hano%C3%AF)

Implémenter une solution pour le problème de la Tour de Hanoï en Python. Le but est de déplacer tous les disques d'une tour à une autre en respectant les règles suivantes :
1. On ne peut déplacer qu'un seul disque à la fois.
2. Un disque ne peut être placé que sur un disque plus grand que lui ou sur une tour vide.

## Instructions

### 1. Créer la Fonction de Résolution

- Dans un fichier nommé `hanoi.py`, implémentez la fonction `solve_hanoi` qui prend trois arguments :
  - `n`: le nombre de disques
  - `source`: la tour de départ
  - `destination`: la tour d'arrivée
  - `auxiliary`: la tour auxiliaire

### 2. Écrire le Script Principal

- Dans `hanoi.py`, ajoutez un bloc pour exécuter la fonction de résolution avec un nombre d'exemple de disques si le script est exécuté directement.

### 3. Écrire des Tests Unitaires

- Créez un fichier nommé `test_hanoi.py`.
- Écrivez des tests unitaires pour vérifier que la fonction `solve_hanoi` produit les mouvements corrects pour divers nombres de disques.

## Exécution du Script et des Tests

### Exécuter le Script Principal

    python hanoi.py

Exécuter les Tests

    python -m unittest test_hanoi.py

Exemples de Commandes

Pour exécuter le script principal avec 3 disques :

    python hanoi.py 3

Avec ces instructions, vous devriez être en mesure de créer, tester et exécuter une solution au problème de la Tour de Hanoï en Python. Bonne chance !