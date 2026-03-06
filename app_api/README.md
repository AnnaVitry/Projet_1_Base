# Toolbox IA - Backend (FastAPI)

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)

Ce service est le cœur logique de la Toolbox IA. Il expose une API REST performante pour effectuer des calculs et assurer la persistance des données dans PostgreSQL.

---

## ʕ•ᴥ•ʔっ · · · ✴ Fonctionnalités

* **Moteur de Calcul** : Logique métier isolée pour les opérations mathématiques.
* **ORM SQLAlchemy** : Gestion élégante des modèles de données et des migrations.
* **Validation Pydantic** : Contrôle strict des types de données en entrée et sortie.
* **Auto-Documentation** : Documentation interactive générée automatiquement.

---

## Architecture du Module

```text
app_api/
├── main.py            # Point d'entrée et définition des routes
├── maths/             # Logique métier (calculs)
├── models/            # Modèles de données (database.py)
├── modules/           # Utilitaires et connexion (connect.py)
├── Dockerfile         # Image Docker optimisée (uv)
└── pyproject.toml     # Dépendances (FastAPI, Psycopg2, etc.)

```

---

## ʕ•ᴥ•ʔっ · · · ✴ Lancement et Documentation

### Accès à l'API

Si l'orchestration Docker est lancée, l'API répond sur le port **8000**.

* **Documentation Interactive (Swagger)** : [http://localhost:8000/docs](https://www.google.com/search?q=http://localhost:8000/docs)
* **Documentation Alternative (ReDoc)** : [http://localhost:8000/redoc](https://www.google.com/search?q=http://localhost:8000/redoc)

---

## ʕ•ᴥ•ʔっ · · · ✴ Développement Local

1. Installez l'environnement :
```bash
uv sync

```


2. Configurez votre base de données dans le fichier `.env`.
3. Lancez le serveur de développement :
```bash
uv run uvicorn main:app --reload

```



---

## Tests & Qualité

Exécutez les tests unitaires spécifiques au backend :

```bash
PYTHONPATH=. uv run pytest ../tests/

```

Vérifiez la qualité du code avec **Ruff** :

```bash
uv run ruff check .

```