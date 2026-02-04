# 🧠 Flask Quiz API REST

Ce projet est une API REST développée avec **Flask** permettant de gérer des questionnaires thématiques et différents types de questions. L'application utilise **SQLAlchemy** pour assurer la persistance des données dans une base de données **SQLite** via un système d'héritage polymorphe.

## ✨ Fonctionnalités

- 📋 **Gestion des Questionnaires** : 
    - Opérations CRUD complètes (Création, Lecture, Modification, Suppression).
    - Redirection automatique de la racine vers la liste des questionnaires.
- ❓ **Système de Questions Polymorphes** : 
    - Utilisation de l'héritage de table pour gérer plusieurs types de questions (Exercice 5).
    - **Questions simples** : Un énoncé uniquement.
    - **Questions Ouvertes** : Incluent un champ pour la réponse attendue.
    - **Questions QCM** : Proposent deux choix et l'indice de la bonne réponse.
- 🔗 **Ressources Imbriquées** : 
    - Les questions sont gérées comme des sous-ressources des questionnaires (ex: `/questionnaires/<id>/questions`).
- 🛠️ **Initialisation Automatisée** : 
    - Commande personnalisée `flask syncdb` pour configurer la base de données et injecter des jeux de tests thématiques.

## 🛠️ Technologies utilisées

* **Python 3** : Langage de programmation principal.
* **Flask** : Micro-framework web.
* **Flask-SQLAlchemy** : ORM pour la gestion de la base de données SQLite.
* **SQLite** : Moteur de base de données relationnelle.

## ⚙️ Installation et Configuration

1. **Cloner le dépôt** :
   ```bash
   git clone https://github.com/votre-utilisateur/votre-projet.git
   cd votre-projet
   ```

2. **Créer un environnement virtuel** :
   ```bash
   python3 -m venv venv
   source venv/bin/activate  
   ```

3. **Installer les dépendances** :
   ```bash
   pip install flask flask-sqlalchemy
   ```

4. **Se placer dans le dossier todo/** :
   ⚠️ **IMPORTANT** : Toutes les commandes Flask doivent être exécutées depuis le dossier `todo/`
   ```bash
   cd todo
   ```

5. **Initialiser la base de données** :
   Utilisez la commande personnalisée pour créer les tables et charger les données de test :
   ```bash
   flask syncdb
   ```

## 🚀 Lancement de l'application

```bash
flask run
```
L'API sera accessible par défaut sur `http://localhost:5000`.

## 📑 Documentation de l'API

### Questionnaires
| Méthode | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/quiz/api/v1.0/questionnaires` | Liste tous les questionnaires |
| `POST` | `/quiz/api/v1.0/questionnaires` | Crée un nouveau questionnaire |
| `GET` | `/quiz/api/v1.0/questionnaires/<id>` | Détails d'un questionnaire |
| `PUT` | `/quiz/api/v1.0/questionnaires/<id>` | Modifie un questionnaire |
| `DELETE` | `/quiz/api/v1.0/questionnaires/<id>` | Supprime un questionnaire et ses questions |

### Questions (Ressources imbriquées)
| Méthode | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/quiz/api/v1.0/questionnaires/<id>/questions` | Liste les questions d'un questionnaire |
| `POST` | `/quiz/api/v1.0/questionnaires/<id>/questions` | Ajoute une question (Simple, Ouverte ou QCM) |
| `GET` | `/quiz/api/v1.0/questionnaires/<id>/questions/<qid>` | Détails d'une question spécifique |
| `PUT` | `/quiz/api/v1.0/questionnaires/<id>/questions/<qid>` | Modifie une question |
| `DELETE` | `/quiz/api/v1.0/questionnaires/<id>/questions/<qid>` | Supprime une question |

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

## 📂 Structure du projet

```text
.
├── api_tests.http         # Suite de tests pour l'API
├── quiz.db                # Base de données SQLite (générée après syncdb)
├── README.md              # Documentation
├── requirements.txt       # Dépendances du projet
└── todo/                  # Dossier principal de l'application
    ├── __init__.py
    ├── app.py             # Point d'entrée de l'application et configuration
    ├── models.py          # Définition des modèles SQLAlchemy (Héritage polymorphe)
    ├── commands.py        # Commandes personnalisées Flask
    └── views.py           # Logique des routes de l'API
```
