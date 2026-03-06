# Toolbox IA - Frontend (Streamlit)

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)

Ce service est l'interface utilisateur (UI) de la Toolbox IA. Il permet d'interagir avec l'API de calcul et de visualiser l'historique des données stockées dans PostgreSQL.

---

## ʕ•ᴥ•ʔっ · · · ✴ Fonctionnalités

* **Interface de Saisie** : Formulaires interactifs pour envoyer des calculs à l'API.
* **Visualisation** : Affichage dynamique des résultats sous forme de tableaux.
* **Communication REST** : Consommation des endpoints de `app_api`.

---

## Architecture Locale

```text
app_front/
├── main.py            # Point d'entrée de l'application Streamlit
├── Dockerfile         # Configuration pour la conteneurisation
├── pyproject.toml     # Dépendances (Streamlit, Requests, etc.)
└── uv.lock            # Verrouillage des versions

```

---

## ʕ•ᴥ•ʔっ · · · ✴ Installation & Lancement

### Via Docker (Recommandé)

Ce service est normalement orchestré par le `docker-compose.yml` à la racine du projet :

```bash
docker compose up front

```

### Développement Local (sans Docker)

Si vous souhaitez modifier l'interface en temps réel :

1. Installez les dépendances :
```bash
uv sync

```


2. Configurez l'URL de l'API dans votre environnement :
```bash
export API_URL="http://localhost:8000"

```


3. Lancez l'application :
```bash
uv run streamlit run main.py

```



---

## ʕ•ᴥ•ʔっ · · · ✴ Configuration

Le Frontend utilise les variables d'environnement suivantes :

* `API_URL` : L'adresse de l'API FastAPI (par défaut `http://api:8000` dans Docker).

---

## Tests & Qualité

Vérifiez la conformité du code frontend avec **Ruff** :

```bash
uv run ruff check .

```