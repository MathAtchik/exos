# Exercice 1 : Calculatrice Basique

## Objectif

Créer une calculatrice simple en Python qui peut effectuer des opérations de base : addition, soustraction, multiplication, et division.

## Instructions

1. **Demander les Nombres à l'Utilisateur**
   - Utilisez `input()` pour demander à l'utilisateur d'entrer deux nombres.
   - Convertissez les entrées de l'utilisateur en nombres (utilisez `int` ou `float` selon le besoin).

2. **Demander l'Opération à l'Utilisateur**
   - Utilisez `input()` pour demander à l'utilisateur de choisir une opération parmi les suivantes :
     - Addition (`+`)
     - Soustraction (`-`)
     - Multiplication (`*`)
     - Division (`/`)

3. **Effectuer l'Opération**
   - Utilisez des conditions (`if`, `elif`, `else`) pour déterminer quelle opération effectuer en fonction de l'entrée de l'utilisateur.
   - Effectuez l'opération choisie sur les deux nombres.

4. **Afficher le Résultat**
   - Affichez le résultat de l'opération.

## Exemple de Sortie Attendue

Lorsque le programme est exécuté, il devrait ressembler à ceci :

Entrez le premier nombre : 5
Entrez le second nombre : 3
Choisissez une opération (+, -, *, /) : +
Le résultat est : 8
scheme


## Conseils

- Utilisez la fonction `input()` pour demander des entrées à l'utilisateur.
- Convertissez les entrées de l'utilisateur en nombres (`int` ou `float`).
- Utilisez des conditions (`if`, `elif`, `else`) pour déterminer quelle opération effectuer.
- Soyez attentif aux cas de division par zéro et gérez-les correctement pour éviter les erreurs.

## Structure du Projet

Le fichier `main.py` devrait contenir les sections suivantes :

1. **Demande et Conversion des Entrées**
   - Demandez les deux nombres à l'utilisateur et convertissez-les en nombres.

2. **Demande de l'Opération**
   - Demandez à l'utilisateur de choisir une opération.

3. **Conditions pour les Opérations**
   - Utilisez des `if`, `elif`, et `else` pour effectuer l'opération choisie.

4. **Affichage du Résultat**
   - Affichez le résultat de l'opération.

Avec ces consignes, vous devriez être en mesure de créer le fichier `main.py` qui répond aux exigences de l'exercice de la calculatrice basique. Bonne chance !

## Bonus !

Parviens à gérer correctement l'erreur en cas de division par 0.