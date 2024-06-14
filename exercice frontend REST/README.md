# Partie 2 : Développement du Frontend en HTML/CSS/JavaScript

## Objectif

Créer une interface utilisateur simple qui permet de poser une question et d'afficher la réponse renvoyée par le backend.

## Instructions

### 1. Créer le Fichier HTML

- Créez un fichier nommé `index.html` dans le répertoire de votre projet frontend.
- Ajoutez une zone de texte pour entrer la question et un bouton pour envoyer la question.
- Assurez-vous d'inclure des éléments HTML comme `<textarea>`, `<button>`, et `<div>` pour afficher la réponse.

### 2. Ajouter le Style CSS

- Créez un fichier nommé `styles.css` dans le même répertoire.
- Stylisez l'interface utilisateur pour rendre les composants visuellement agréables.
- Pensez à ajouter des styles pour le corps de la page, le conteneur principal, la zone de texte, le bouton, et la zone d'affichage de la réponse.

### 3. Ajouter le Script JavaScript

- Créez un fichier nommé `script.js` dans le même répertoire.
- Ajoutez un événement `click` au bouton qui récupère la valeur de la zone de texte.
- Utilisez la fonction `fetch` pour envoyer une requête POST au backend avec la question.
- Affichez la réponse du backend dans la zone prévue à cet effet.

### 4. Tester l'Application

- Ouvrez `index.html` dans un navigateur web.
- Entrez une question dans la zone de texte et cliquez sur le bouton pour envoyer la question au backend.
- Vérifiez que la réponse est affichée correctement.

## Remarques

- Assurez-vous que votre backend est en cours d'exécution et accessible à l'adresse `http://localhost:8080/ask`.
- Si le backend utilise un autre port ou une autre URL, ajustez l'URL dans votre script JavaScript en conséquence.

Avec ces instructions, vous devriez être en mesure de créer, styliser et tester une interface utilisateur simple qui communique avec votre backend Java. Bonne chance !