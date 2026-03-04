#!/bin/bash

# Arrêter le script à la moindre erreur
set -e

echo "[1/4] Analyse de la qualité du code (Ruff)..."
uv run ruff check .

echo "[2/4] Exécution des tests unitaires (Pytest)..."
uv run pytest

echo "[3/4] Génération de la documentation (Sphinx)..."
uv run sphinx-build docs/source public

echo "[4/4] Construction de l'image Docker..."
docker build -t ia-toolbox .

echo "Déploiement terminé avec succès ! Votre Toolbox est prête."
echo "Pour lancer le conteneur : docker run --rm ia-toolbox"