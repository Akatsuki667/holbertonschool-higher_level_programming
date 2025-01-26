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

    if not isinstance(matrix, list) or \
       not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    for row in matrix:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of "
                                "integers/floats")

    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            new_row.append(round(element / div, 2))
        new_matrix.append(new_row)
    return new_matrix
