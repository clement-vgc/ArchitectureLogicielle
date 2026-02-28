# 🧠 Flask Quiz API REST

Ce projet est une API REST développée avec **Flask** permettant de gérer des questionnaires composés de questions. L'application utilise **SQLAlchemy** pour assurer la persistance des données dans une base de données **SQLite** via un système d'héritage polymorphe.

## ⚙️ Installation et Configuration

1. **Cloner le dépôt** :
   ```bash
   git clone https://github.com/clement-vgc/ArchitectureLogicielle.git
   ```

2. **Créer un environnement virtuel** :
   ```bash
   python3 -m venv venv
   source venv/bin/activate  
   ```

3. **Installer les dépendances** :
    ```bash
    pip install -r requirements.txt
    ```

4. **Se placer dans le dossier todo/** :
   ⚠️ **IMPORTANT** : Toutes les commandes Flask doivent être exécutées depuis le dossier `todo/`
   ```bash
   cd todo
   ```

5. **Initialiser la base de données** :
   ```bash
   flask syncdb
   ```

## 🚀 Lancement de l'application

```bash
flask run
```
L'API sera accessible par défaut sur `http://localhost:5000`.

## 🧪 Tests

Un fichier `api_tests.http` est fourni à la racine du projet. Il permet de tester l'ensemble des fonctionnalités de l'API en utilisant l'extension **REST Client** de VS Code ou via `curl`.

Si vous souhaitez faire les tests avec les commandes curl, voici les commandes à entrer dans le terminal : (assurez-vous d'avoir bien le serveur lancé)

### Tests pour les questionnaires


1. Récupérer tous les questionnaires

```bash
curl -X GET http://localhost:5000/quiz/api/v1.0/questionnaires -H "Accept: application/json"
```

2. Créer un nouveau questionnaire

```bash
curl -X POST http://localhost:5000/quiz/api/v1.0/questionnaires -H "Content-Type: application/json" -d '{"name": "Astronomie"}'
```

3. Récupérer un questionnaire spécifique (ici le 1)

```bash
curl -X GET http://localhost:5000/quiz/api/v1.0/questionnaires/1 -H "Accept: application/json"
```

4. Modifier le nom d'un questionnaire 

```bash
curl -X PUT http://localhost:5000/quiz/api/v1.0/questionnaires/1 -H "Content-Type: application/json" -d '{"name": "Géographie & Monde"}'
```

### Tests pour les questions


5. Récupérer toutes les questions du questionnaire 1

```bash
curl -X GET http://localhost:5000/quiz/api/v1.0/questionnaires/1/questions -H "Accept: application/json"
```

6. Ajouter une Question Ouverte

```bash
curl -X POST http://localhost:5000/quiz/api/v1.0/questionnaires/1/questions \
-H "Content-Type: application/json" \
-d '{"title": "Quelle est la capitale de l\'Islande ?", "reponse": "Reykjavik"}'
```

7. Ajouter une Question QCM

```bash
curl -X POST http://localhost:5000/quiz/api/v1.0/questionnaires/1/questions -H "Content-Type: application/json" -d '{"title": "Quelle est la plus grande planète ?", "p1": "Mars", "p2": "Jupiter", "bonne_reponse": 2}'
```

8. Ajouter une Question standard

```bash
curl -X POST http://localhost:5000/quiz/api/v1.0/questionnaires/1/questions -H "Content-Type: application/json" -d '{"title": "Question"}'
```

9. Récupérer une question précise (Question 1 du Questionnaire 1)

```bash
curl -X GET http://localhost:5000/quiz/api/v1.0/questionnaires/1/questions/1 -H "Accept: application/json"
```

### Tests de modification et de suppression

10. Modifier une Question Ouverte

```bash
curl -X PUT http://localhost:5000/quiz/api/v1.0/questionnaires/1/questions/1 -H "Content-Type: application/json" -d '{"title": "Capitale de l\'Islande (Modifiée)", "reponse": "Reykjavík"}'
```

11. Modifier une Question QCM

```bash
curl -X PUT http://localhost:5000/quiz/api/v1.0/questionnaires/1/questions/2 -H "Content-Type: application/json" -d '{"title": "Quelle est la planète la plus proche du soleil ?", "p1": "Mercure", "p2": "Vénus", "bonne_reponse": 1}'
```

12. Supprimer une question spécifique

```bash
curl -X DELETE http://localhost:5000/quiz/api/v1.0/questionnaires/1/questions/3
```

13. Supprimer un questionnaire complet

```bash
curl -X DELETE http://localhost:5000/quiz/api/v1.0/questionnaires/3
```
