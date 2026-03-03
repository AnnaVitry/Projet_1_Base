# ʕ•́ᴥ•̀ʔっ · · · ♡ SQLalchemy Exo Toolbox

Ce projet est un template professionnel standardisé pour le cursus IA. Il intègre la gestion des dépendances avec `uv`, la qualité de code avec `ruff`, les tests avec `pytest` et la documentation automatique avec `Sphinx`.

## ʕ•ᴥ•ʔっ · · · Guide d'Initialisation Rapide

Suivez ces étapes dans l'ordre pour configurer votre environnement de développement.

### 1. Préparation de la Structure
Générez l'arborescence et les fichiers de configuration de base :
```bash
python init_project.py

```

### 2. Installation de l'Environnement

Installez les dépendances (Sphinx, Furo, Pytest, Ruff, Pandas) dans un environnement virtuel isolé :

```bash
uv sync

```

### 3. Initialisation de Sphinx

Configurez le moteur de documentation dans le dossier `docs` :

```bash
uv run sphinx-quickstart docs

```

*Réponses recommandées :*

* Separate source and build directories : **y**
* Project name : **SQLalchemy Exo**
* Author name : **Votre Nom**
* Language : **fr** (ou en)

---

## ʕ•ᴥ•ʔっ · · · Commandes de Maintenance

Utilisez ces commandes au quotidien pour garantir l'excellence technique du projet.

### Qualité du Code (Linting)

Vérifiez la conformité aux standards Google et corrigez les erreurs de formatage :

```bash
uv run ruff check .        # Analyse
uv run ruff check . --fix  # Correction automatique

```

### Tests Unitaires

Exécutez la suite de tests et vérifiez la couverture de code :

```bash
uv run pytest

```

### Génération de la Documentation

Construisez le site web de documentation en local (format HTML) :

```bash
uv run sphinx-build docs/source public

```

*Le résultat sera disponible dans le dossier `public/index.html`.*

---

## ʕ•ᴥ•ʔっ · · · Conteneurisation (Docker)

Pour tester l'application dans un environnement reproductible :

```bash
# Construction de l'image
docker build -t sqlalchemy-toolbox .

# Exécution du conteneur
docker run --rm sqlalchemy-toolbox

```

---

## ʕ•ᴥ•ʔっ · · · Intégration Continue (CI)

Le fichier `.github/workflows/ci.yml` automatise ces vérifications à chaque **Push** sur les branches `main` ou `dev`.

* Si un test échoue ou si Ruff détecte une erreur, le déploiement est bloqué.

```



### Pourquoi ce README est-il rigoureux ?
* **Séquentialité** : Il respecte l'ordre technique (Structure -> Dépendances -> Moteur de doc).
* **Isolation** : Toutes les commandes utilisent `uv run`, garantissant que vous n'utilisez pas par erreur une version globale de Python ou de Sphinx.
* **Transparence** : Il explique *pourquoi* on utilise chaque outil (Linting, CI, Docker).

**Souhaitez-vous que je vous aide à présent à configurer le fichier `docs/source/conf.py` pour que votre documentation Sphinx aspire automatiquement ce README sur sa page d'accueil ?**

```