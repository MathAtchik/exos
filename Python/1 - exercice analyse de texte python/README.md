# Exercice 2 : Analyse de Texte

## Objectif

Écrire un programme en Python qui analyse un texte fourni par l'utilisateur et compte le nombre de mots, de caractères, et de phrases.

## Instructions

1. **Importer les Bibliothèques Nécessaires**
   - Importez le module `re` pour utiliser les expressions régulières.

2. **Définir la Fonction d'Analyse de Texte**
   - Créez une fonction `analyze_text(text)` qui :
     - Compte le nombre de caractères dans le texte (y compris les espaces et la ponctuation) en utilisant `len()`.
     - Compte le nombre de mots dans le texte en utilisant `split()` pour séparer les mots.
     - Compte le nombre de phrases dans le texte en utilisant `re.split(r'[.!?]', text)` pour séparer les phrases et en supprimant les chaînes vides résultantes.

3. **Définir la Fonction Principale**
   - Créez une fonction `main()` qui :
     - Demande à l'utilisateur d'entrer un texte.
     - Utilise la fonction `analyze_text(text)` pour analyser le texte.
     - Affiche le nombre de caractères, de mots, et de phrases.

4. **Exécuter la Fonction Principale**
   - Assurez-vous que le script principal est exécuté uniquement lorsque le fichier est exécuté directement.

## Exemple de Sortie Attendue

Lorsque le programme est exécuté, il devrait ressembler à ceci :

Entrez un texte : Bonjour! Comment ça va? Aujourd'hui est une belle journée.
Nombre de caractères : 52
Nombre de mots : 8
Nombre de phrases : 3
python


## Conseils

- Utilisez `len()` pour compter les caractères dans le texte.
- Utilisez `split()` pour séparer les mots et les compter.
- Utilisez les expressions régulières avec `re.split(r'[.!?]', text)` pour séparer et compter les phrases.