Installation et Configuration
=============================

Cette section détaille la mise en place de l'environnement de développement pour la **IA Foundation Toolbox**.

.. note::
   Assurez-vous d'avoir installé `uv <https://github.com/astral-sh/uv>`_ au préalable sur votre système.

Récupération du projet
----------------------

Commencez par cloner le dépôt et entrez dans le répertoire racine :

.. code-block:: bash

   git clone <votre-repo>
   cd <votre-dossier>

Initialisation de la structure
------------------------------

Si vous partez de zéro, utilisez le script d'initialisation pour générer l'arborescence standard :

.. code-block:: bash

   python init_project.py

Installation des dépendances
----------------------------

Nous utilisons ``uv`` pour une gestion rapide et isolée des paquets Python (Pandas, Pytest, Ruff, Sphinx) :

.. code-block:: bash

   uv sync

Vérification de l'installation
------------------------------

Pour confirmer que tout est opérationnel, lancez la suite de tests unitaires :

.. code-block:: bash

   uv run pytest

Conteneurisation
----------------

Si vous préférez utiliser Docker, vous pouvez construire et lancer l'image directement :

.. code-block:: bash

   docker build -t ia-toolbox .
   docker run --rm ia-toolbox