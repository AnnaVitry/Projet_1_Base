# Toolbox IA - Architecture Microservices de Anna

![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Python Version](https://img.shields.io/badge/python-3.12-blue.svg?style=for-the-badge)

Ce projet est une plateforme de services IA **multi-tiers** conteneurisée. Elle orchestre une interface utilisateur, une API de calcul et une base de données persistante PostgreSQL.

---

## ʕ•ᴥ•ʔっ · · · ✴ Architecture du Projet

L'écosystème est découpé en trois services autonomes communiquant via des réseaux isolés :

* **Frontend (Streamlit)** : Interface de saisie et visualisation.
* **Backend (FastAPI)** : Logique métier et orchestration des données.
* **Database (PostgreSQL)** : Stockage persistant via volumes Docker.



---

## ʕ•ᴥ•ʔっ · · · ✴ Installation & Orchestration

Assurez-vous d'avoir [Docker](https://www.docker.com/) installé.

```bash
git clone [https://github.com/AnnaVitry/Toolbox_IA_Microservice.git](https://github.com/AnnaVitry/Toolbox_IA_Microservice.git)
cd Toolbox_IA_Microservice
# Lancement de tous les services d'un coup
docker compose up --build

```

*L'interface est alors disponible sur : **[http://localhost:8501*](https://www.google.com/search?q=http://localhost:8501)**

---

## ʕ•ᴥ•ʔっ · · · ✴ Commandes de Maintenance

Utilisez ces commandes pour garantir l'excellence et l'hygiène technique du projet.

### Nettoyage Complet (Hygiène)

Pour supprimer les conteneurs, les volumes de données et les caches Python :

```bash
chmod +x clean_project.sh
./clean_project.sh

```

### Développement Local (uv)

Si vous souhaitez travailler sur un service spécifique sans Docker :

```bash
cd app_api # ou app_front
uv sync
uv run uvicorn main:app --reload # pour l'API

```

---

## ʕ•ᴥ•ʔっ · · · ✴ Sécurité et Réseau

* **Isolation** : La base de données est isolée sur un réseau privé (`back-net`), accessible uniquement par l'API.
* **Persistance** : Les données survivent aux redémarrages grâce au volume `postgres_data`.
* **Secrets** : Les configurations sensibles sont gérées via le fichier `.env` (exclu du Git).

---

## ʕ•ᴥ•ʔっ · · · ✴ Structure des Microservices

```text
.
├── app_api/            # 🧠 Le Cerveau (FastAPI + SQLAlchemy)
├── app_front/          # 🎨 L'Interface (Streamlit)
├── docker-compose.yml  # 🏗️ L'Orchestrateur
├── clean_project.sh    # 🧹 Script de Nettoyage
└── .env                # 🔐 Configuration (Non suivi)

```