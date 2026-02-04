\ No newline at end of file
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

#### Formats de données pour POST/PUT (Questions) :
- **Question Ouverte** : `{"title": "...", "reponse": "..."}`
- **QCM** : `{"title": "...", "p1": "...", "p2": "...", "bonne_reponse": 1}`
- **Standard** : `{"title": "..."}`

## 🧪 Tests

Un fichier `api_tests.http` est fourni à la racine du projet. Il permet de tester l'ensemble des fonctionnalités de l'API en utilisant l'extension **REST Client** de VS Code ou via `curl`.

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
