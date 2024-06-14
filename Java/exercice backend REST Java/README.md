# Partie 1 : Développement du Backend en Java

## Objectif

Créer un backend en Java qui expose un endpoint REST. Ce endpoint recevra une question et renverra une réponse simulée.

## Instructions

### 1. Créer un Projet Maven

#### Utiliser Spring Initializr

- Rendez-vous sur [Spring Initializr](https://start.spring.io/).
- Configurez votre projet avec les options suivantes :
  - **Project** : Maven Project
  - **Language** : Java
  - **Spring Boot** : Choisissez la version stable actuelle
  - **Group** : com.atchik
  - **Artifact** : exercice
  - **Name** : exercice
  - **Package name** : com.atchik.exercice
  - **Dependencies** : ajoutez `Spring Web`

- Cliquez sur **Generate** pour télécharger le projet.

### 2. Créer un Contrôleur REST

- Décompressez le projet généré et ouvrez-le dans votre IDE préféré (IntelliJ IDEA, Eclipse, etc.).

- Dans le répertoire `src\main\java\com\atchik\exercice`, créez un fichier nommé `AskController.java`.

- Implémentez un contrôleur REST qui expose un endpoint `/ask` :
  - Utilisez l'annotation `@RestController` pour définir la classe comme un contrôleur REST.
  - Utilisez l'annotation `@PostMapping("/ask")` pour définir le endpoint.
  - Le endpoint doit recevoir une question via une requête POST et retourner une réponse simulée.

### 3. Rédiger un Test pour l'Application

- Dans le répertoire `src\test\java\com\atchik\exercice`, créez un fichier de test nommé `ExerciceApplicationTests.java`.

- Implémentez un test pour le endpoint `/ask` :
  - Utilisez les annotations `@SpringBootTest` et `@AutoConfigureMockMvc`.
  - Injectez `MockMvc` pour simuler les requêtes HTTP.
  - Testez que le endpoint retourne la réponse attendue lorsque vous envoyez une question.

### 4. Tester le Endpoint depuis le Terminal

#### Démarrer l'Application

- Assurez-vous que votre application est en cours d'exécution. Vous pouvez démarrer l'application en exécutant la classe principale générée par Spring Initializr (par défaut, c'est `ExerciceApplication.java`).

#### Tester le Endpoint avec `curl`

- Ouvrez le terminal Windows (cmd) et utilisez `curl` pour tester le endpoint `/ask` :

```cmd
curl -X POST http://localhost:8080/ask -H "Content-Type: text/plain" -d "Quelle est la réponse à la grande question de la vie, de l'univers et de tout le reste ?"

    Vous devriez recevoir une réponse simulée pour la question posée.

Remarques

    Assurez-vous que le port 8080 est libre sur votre machine ou modifiez la configuration de votre application pour utiliser un autre port.
    Si vous utilisez un autre port, ajustez l'URL dans la commande curl en conséquence.

Avec ces instructions, vous devriez être en mesure de créer, tester et interagir avec votre backend Java exposant un endpoint REST /ask. Bonne chance !