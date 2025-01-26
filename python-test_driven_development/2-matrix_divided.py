#!/usr/bin/python3
"""
Ceci est `2-matrix_divided.py` module

Ce module contient une fonction `matrix_divided(matrix, div)`

Cette fonction divise chaque élément présent dans la matrice
"""


def matrix_divided(matrix, div):

    """
    Divise chaque élément de `matrix` par le paramètre `div`

    Paramètres:
    matrix: liste de listes de collection de nombres
    div: diviseur de chaque élément de la `matrix`

    Return:
    new_matrix: nouvelle liste de listes de collection de nombres divisés

    Raises:
    TypeError: Si `matrix` n'est pas une liste de listes
    TypeError: Si il n'y a pas le même nb de colonnes
    TypeError: Si `div` n'est pas un entier
    TypeError: Si `div` est égale à 0

    Exemples:
    >>> matrix_divided(matrix, 3)
    [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
    >>> matrix_divided(matrix, 5.5)
    [[0.18, 0.36, 0.55], [0.73, 0.91, 1.09]]
    """

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []

    ref_row_len = 0

    for i in matrix:

        if not ref_row_len:
            ref_row_len = len(i)

        if len(i) != ref_row_len:
            raise TypeError("Each row of the matrix must have the same size")

        new_matrix.append(list(map(lambda x: round(x / div, 2), i)))

    return new_matrix
