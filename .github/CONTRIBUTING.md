# ʕ•ᴥ•ʔ Guide de Contribution

Merci de vouloir améliorer la **IA Foundation Toolbox** ! Pour maintenir l'excellence technique du projet, merci de suivre ces directives.

## ʕ•ᴥ•ʔっ · · · ✴ Processus de Développement

1. **Forkez** le projet et créez votre branche (`feature/incroyable-ajout`).
2. **Installez** l'environnement avec `uv sync`.
3. **Développez** votre fonctionnalité en respectant les types Python.
4. **Testez** : Ajoutez un test dans `tests/test_mon_module.py`.

## ʕ•ᴥ•ʔっ · · · ✴ Standard de Qualité

Avant de soumettre une Pull Request, vous **devez** valider votre code localement :

```bash
# Vérifier le formatage et les docstrings
uv run ruff check .

# Lancer la suite de tests
uv run pytest

```

## ʕ•ᴥ•ʔっ · · · ✴ Documentation

Si vous ajoutez une fonction, n'oubliez pas sa **docstring au format Google**. Sphinx s'occupera du reste lors du build.