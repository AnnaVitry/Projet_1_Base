## Fiche Projet : Architecture Microservices IA

**Candidat :** Anna Vitry

**Stack :** Python 3.12 | FastAPI | Streamlit | PostgreSQL | Docker | GitHub Actions

### Objectif du Projet

Transformer une application monolithique en une **architecture distribuée et scalable**, garantissant la persistance des données et une qualité de code de niveau industriel.

### Réalisations Techniques Clés

1. **Conteneurisation Multi-Services** :
* Orchestration de 3 services (Front, API, DB) via **Docker Compose**.
* Utilisation de **réseaux isolés** pour la sécurité (la DB n'est pas exposée sur le web).
* Gestion de la persistance via des **volumes Docker**.


2. **Qualité et Rigueur (DevOps)** :
* Mise en place d'un **Linter (Ruff)** pour garantir un code propre et documenté.
* Développement d'une suite de **tests unitaires (Pytest)** avec rapport de couverture.
* Automatisation totale via **GitHub Actions** (CI/CD).


3. **Industrialisation** :
* Documentation automatique du code source via **Sphinx**.
* Interface de test interactive via le **Swagger de FastAPI**.
* Script de maintenance automatisé (`clean_project.sh`) pour la gestion de l'environnement.



---

### Questions types en entretien (et comment briller)

* **"Pourquoi avoir séparé le Frontend du Backend ?"**
> *Réponse :* Pour l'**évolutivité**. Je peux mettre à jour l'interface Streamlit sans toucher à la logique métier de l'API, et vice-versa. Cela permet aussi de scaler les services indépendamment si la charge augmente.


* **"À quoi servent vos fichiers `__init__.py` avec docstrings ?"**
> *Réponse :* Ils structurent mes dossiers en **packages Python valides**. J'y ajoute des docstrings pour la maintenance et pour que ma documentation Sphinx soit générée proprement, ce qui facilite l'onboarding de nouveaux développeurs.


* **"Pourquoi utiliser Docker pour ce projet ?"**
> *Réponse :* Pour garantir l'**idempotence**. L'application tourne exactement de la même manière sur ma machine, sur GitHub Actions ou en production, éliminant le fameux "ça marche sur mon PC".

---

## 📂 Anatomie du Projet : Rôles et Responsabilités

### 1. Les Services (Le Cœur)

* **`app_api/`** : Le cerveau. Il contient la logique métier (calculs) et l'accès à la donnée.
* `main.py` : Point d'entrée de l'API. Définit les routes et initialise la DB.
* `maths/` : Logique pure. Isoler les calculs ici permet de les tester sans lancer l'API.
* `models/database.py` : Schéma de la base de données (SQLAlchemy). C'est le "plan" de tes tables.
* `modules/connect.py` : Gestion de la connexion et de la session (le "pont" vers PostgreSQL).


* **`app_front/`** : L'interface. Elle ne connaît pas la base de données, elle ne parle qu'à l'API via des requêtes HTTP.

### 2. Les Fichiers de Construction (L'Infrastructure)

* **`Dockerfile`** : La "recette" pour créer l'image d'un service (OS, dépendances, code).
* **`docker-compose.yml`** : Le "chef d'orchestre". Il lie les services entre eux, crée les réseaux (`front-net`, `back-net`) et gère les volumes.
* **`pyproject.toml`** : Le manifeste moderne de Python. Il remplace le vieux `requirements.txt` et configure aussi tes outils comme **Ruff** ou **Pytest**.
* **`clean_project.sh`** : Script de maintenance. Indispensable pour repartir sur une base saine (RAZ des conteneurs et des caches).

---

## Le Processus Itératif Suivi

J'ai suivi une méthodologie de développement moderne en 4 phases :

1. **Phase de Design** : Définition des schémas de données et de l'arborescence modulaire (choix de l'architecture microservices).
2. **Phase de Conteneurisation** : Création des Dockerfiles et orchestration locale pour s'assurer que les services communiquent bien.
3. **Phase de Qualité (CI)** : Mise en place des tests unitaires et du linter pour automatiser la détection de bugs.
4. **Phase de Documentation & CD** : Génération de la documentation technique (Sphinx) et déploiement automatisé des images Docker.

---

## Journal des Erreurs & Solutions (Le "Debug Log")

Voici les défis techniques que j'ai dû surmonter, ce qui prouve ma capacité de résolution :

| Erreur rencontrée | Cause identifiée | Solution apportée |
| --- | --- | --- |
| **ModuleNotFoundError** en CI | Le dossier racine n'était pas dans le chemin de recherche de Python. | Création d'un `tests/conftest.py` et configuration du `PYTHONPATH` dans GitHub Actions. |
| **Connexion DB échouée** | L'API tentait de se connecter à `localhost` au lieu du nom du service Docker `db`. | Utilisation de variables d'environnement pour l'URL de la DB (`postgresql://user:pass@db:5432/...`). |
| **Bare Except (Ruff E722)** | Mauvaise pratique de capture d'erreur trop large dans le Frontend. | Remplacement par `except Exception:` pour ne pas masquer les signaux système critiques. |
| **Imports Incohérents** | Mélange d'imports relatifs et absolus entre les sous-dossiers. | Uniformisation avec des **imports absolus** (ex: `from app_api.maths...`) et ajout des `__init__.py`. |

---

### 💬 Comment présenter cela en entretien ?

*"Durant ce projet, j'ai rencontré des défis complexes sur la gestion des chemins d'importation en environnement conteneurisé. Au lieu de simplement 'bidouiller', j'ai mis en place un fichier de configuration Pytest (`conftest.py`) et j'ai structuré mes dossiers en packages Python officiels. Cela a non seulement réglé le problème, mais a aussi rendu mon code conforme aux standards de l'industrie."*

---
C'est une excellente approche. Pour qu'un projet soit réellement **maintenable** par toi-même dans six mois, il faut documenter non seulement le "quoi", mais aussi le "comment" et les spécificités de ton environnement.

Pour atteindre cette **exhaustivité**, voici les sections stratégiques à ajouter à ton dossier d'auto-documentation (dans un fichier `NOTES_TECHNIQUES.md` ou dans ton portfolio).

---

## Notes Techniques

### 1. Le "Flux de Données" (Data Flow)

Il est crucial de comprendre comment une information circule du clic de l'utilisateur jusqu'au disque dur.

* **Saisie** : L'utilisateur entre un calcul dans `app_front` (Streamlit).
* **Requête** : Streamlit utilise la librairie `requests` pour envoyer un JSON à `app_api`.
* **Traitement** : FastAPI reçoit le JSON, le valide avec un schéma **Pydantic**, puis appelle la fonction dans `app_api/maths`.
* **Persistance** : Le résultat est passé à l'**ORM SQLAlchemy** qui traduit l'objet Python en commande SQL `INSERT` pour PostgreSQL.
* **Retour** : L'API renvoie une confirmation 200 OK, et Streamlit rafraîchit l'affichage.

---

### 2. Le Guide de Survie Docker (Commandes Avancées)

Parce qu'on oublie vite les commandes spécifiques quand tout fonctionne bien.

| Action | Commande | Utilité |
| --- | --- | --- |
| **Reset SQL** | `docker volume rm $(docker volume ls -q)` | Supprime physiquement les données de la base. |
| **Logs en direct** | `docker compose logs -f api` | Voir les erreurs de l'API en temps réel. |
| **Inspecter la DB** | `docker exec -it db psql -U user -d toolbox` | Entrer dans la base de données sans interface. |
| **Rebuild forcé** | `docker compose up --build --force-recreate` | Forcer Docker à ignorer le cache si une modif ne passe pas. |

---

### 3. Les "Pourquoi" Technologiques (Justification)

Si tu relis cela plus tard, tu te demanderas pourquoi tu as fait ces choix :

* **Pourquoi `uv` ?** Pour la vitesse fulgurante de résolution des dépendances et la gestion unifiée du Python (`uv python install`).
* **Pourquoi `Ruff` ?** Parce qu'il remplace 5 outils (Flake8, Isort, Black, etc.) en étant 100x plus rapide.
* **Pourquoi `PostgreSQL` ?** Pour la robustesse des transactions ACID, indispensable si tu ajoutes plus tard des relations complexes entre tes données IA.

---

### 4. Checklist pour "Ajouter un Service"

Si demain tu veux ajouter un service `app_ai_vision`, voici ta recette :

1. Créer le dossier avec son `Dockerfile`.
2. Ajouter le service dans le `docker-compose.yml`.
3. Déclarer les réseaux (`front-net` ou `back-net`).
4. Ajouter les variables d'environnement nécessaires.
5. Ne pas oublier le `__init__.py` pour que la CI puisse le tester.

---

### 5. Schéma des Dépendances logicielle

Il est utile de noter quelle version de bibliothèque est critique :

* **FastAPI** : Nécessite `pydantic` pour la validation.
* **SQLAlchemy** : Nécessite `psycopg2-binary` (ou `asyncpg`) pour parler à PostgreSQL.
* **Streamlit** : Nécessite `requests` pour parler à l'API.

---
