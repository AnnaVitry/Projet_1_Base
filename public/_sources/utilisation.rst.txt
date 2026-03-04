Guide d'Utilisation
===================

Cette page présente des exemples concrets pour exploiter les fonctionnalités de la **IA Foundation Toolbox**.

Manipulation Mathématique
-------------------------

Le module ``mon_module`` propose des fonctions arithmétiques simples mais robustes, typées avec soin.

**Exemple d'addition et de mise au carré :**

.. code-block:: python

   from app.modules.mon_module import add, square

   # Calcul simple
   resultat = add(10, 5)
   print(f"10 + 5 = {resultat}")

   # Calcul de puissance
   puissance = square(resultat)
   print(f"Le carré de {resultat} est {puissance}")

Traitement de Données avec Pandas
---------------------------------

La Toolbox est conçue pour faciliter l'analyse de données. La fonction ``print_data`` permet de visualiser un DataFrame et d'en extraire le volume.

**Exemple d'analyse de fichier CSV :**

.. code-block:: python

   import pandas as pd
   from app.modules.mon_module import print_data

   # Chargement d'un jeu de données
   df = pd.read_csv("moncsv.csv")

   # Affichage et récupération du nombre de lignes
   nb_lignes = print_data(df)
   print(f"Le fichier contient {nb_lignes} enregistrements.")

Bonnes Pratiques
----------------

1. **Validation des types** : Utilisez toujours des entiers (``int``) pour les fonctions mathématiques pour respecter les signatures de type.
2. **Gestion des données** : Assurez-vous que votre fichier CSV possède des en-têtes de colonnes avant de le passer à ``print_data``.