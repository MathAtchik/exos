# Développement du Backend en Python

## Objectif

Créer un backend en Python qui expose un endpoint REST. Ce endpoint recevra une question et renverra une réponse simulée.

## Instructions

### 1. Installer Flask

- Assurez-vous d'avoir Python installé sur votre machine. Vous pouvez vérifier en exécutant `python --version` dans votre terminal.
- Installez Flask en utilisant pip :

    ```cmd
    pip install flask

2. Créer le Fichier Backend

    Dans un nouveau répertoire de votre projet, créez un fichier nommé app.py.
    Implémentez un contrôleur REST qui expose un endpoint /ask.

3. Rédiger un Test pour l'Application

    Créez un fichier nommé test_app.py dans le même répertoire.
    Écrivez un test pour le endpoint /ask en utilisant un framework de test comme unittest ou pytest.

4. Tester le Endpoint depuis le Terminal

    Exécutez l'application en utilisant la commande suivante dans le terminal :

    ```cmd
    python app.py

    Utilisez curl pour tester le endpoint /ask :

    ```cmd

    curl -X POST http://localhost:5000/ask -H "Content-Type: text/plain" -d "Quelle est la réponse à la grande question de la vie, de l'univers et de tout le reste ?"

Vous devriez recevoir une réponse simulée pour la question posée.

Remarques

    Assurez-vous que le port 5000 est libre sur votre machine ou modifiez la configuration de votre application pour utiliser un autre port.
    Si vous utilisez un autre port, ajustez l'URL dans la commande curl en conséquence.

Avec ces instructions, vous devriez être en mesure de créer, tester et interagir avec votre backend Python exposant un endpoint REST /ask. Bonne chance !