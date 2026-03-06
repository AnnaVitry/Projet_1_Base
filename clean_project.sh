#!/bin/bash

echo "--- 🧹 Nettoyage Spécifique : Architecture Toolbox IA ---"

# 1. Orchestration Docker
echo "Stopping containers and removing networks/volumes..."
# On force l'arrêt et on nettoie les volumes orphelins
docker compose down -v --remove-orphans

# 2. Qualité du Code (Ruff & Pytest)
echo "Removing quality tool caches..."
# Ruff crée un dossier .ruff_cache très persistant
rm -rf .ruff_cache/
# Pytest génère .pytest_cache et souvent des fichiers de couverture
rm -rf .pytest_cache/
rm -f .coverage
rm -f coverage.xml
rm -rf htmlcov/

# 3. Hygiène Python & Imports
echo "Cleaning Python artifacts..."
find . -type d -name "__pycache__" -exec rm -rf {} +
find . -type d -name "*.egg-info" -exec rm -rf {} +

# 4. Documentation (Sphinx)
# Si tu génères de la doc, le dossier 'public' ou 'docs/build' s'encrasse
if [ -d "public" ]; then
    echo "Cleaning build documentation..."
    rm -rf public/
fi

# 5. Lockfile et Environnement (Prudence)
# Parfois, un uv.lock corrompu empêche le build Docker
# On ne le supprime pas par défaut, mais on peut forcer sa régénération
# echo "Refreshing lockfile..."
# uv lock

# 6. Docker System (Gain de place disque)
echo "Optimizing Docker storage..."
# On supprime uniquement les images 'dangling' (sans nom) pour gagner de la place sans tout supprimer
docker image prune -f

echo "--- ✨ Projet Toolbox IA étincelant ! ---"