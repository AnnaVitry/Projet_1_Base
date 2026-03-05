"""Module de calcul mathématique et de manipulation de données.

Ce module fournit des outils pour effectuer des opérations arithmétiques
simples et analyser des structures de données Pandas.
"""

import pandas as pd


def add(a: int, b: int) -> int:
    """Additionne deux nombres entiers.

    Args:
        a: Le premier nombre.
        b: Le deuxième nombre.

    Returns:
        La somme de a et b.

    """
    return a + b


def sub(a: int, b: int) -> int:
    """Soustrait le deuxième nombre du premier.

    Args:
        a: Le nombre source.
        b: Le nombre à soustraire.

    Returns:
        Le résultat de la soustraction.

    """
    return a - b


def square(a: int) -> int:
    """Effectue l'opération de calcul pour le carré d'un nombre entier.

    Args:
        a: Le nombre à élever au carré.

    Returns:
        Le carré de a.

    """
    return a * a


def print_data(df: pd.DataFrame) -> int:
    """Affiche le contenu d'un DataFrame et retourne sa taille.

    Args:
        df: Le DataFrame Pandas à analyser.

    Returns:
        Le nombre de lignes présentes dans le DataFrame.

    """
    print(df)
    return len(df)
