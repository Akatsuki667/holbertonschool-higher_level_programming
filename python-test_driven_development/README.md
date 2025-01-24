# Python - Test-driven development

## 0. Integers addition
Write a function that adds 2 integers.

### Objectives
- Prototype: `def add_integer(a, b=98):`
- `a` and `b` must be integers or floats, otherwise raise a `TypeError` exception with the message `a must be an integer` or `b must be an integer`
- `a` and `b` must be first casted to integers if they are float
- Returns an integer: the addition of `a` and `b`
- You are not allowed to import any module

### Expectation
```Python
#!/usr/bin/python3
"""
Ceci est `0-add_intger.py` module

Ce module contient une fonction `add_integer(a, b=98)`

Cette fonction additionne valeur de `type_int`
"""

def add_integer(a, b=98):
    """
    Additionne deux paramètres de `type_int`

    Paramètres:
    a(int, float): premier nombre
    b(int, float): second nombre

    Return:
    int: somme de l'addition

    Raises:
    TypeError: Si a et b ne sont pas des entiers

    Exemples:
    >>> add_integer(5, 2)
    7
    >>> add_integer(5, 2.5)
    7
    >>> add_integer(2)
    100
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
```
### Result
```bash
3
98
100
98
b must be an integer
a must be an integer
```

## 1. Divide a matrix
Write a function that divides all elements of a matrix.

### Objectives
- Prototype: `def matrix_divided(matrix, div):`
- `matrix` must be a list of lists of integers or floats, otherwise raise a `TypeError` exception with the message `matrix must be a matrix (list of lists) of integers/floats`
- Each row of the `matrix` must be of the same size, otherwise raise a `TypeError` exception with the message `Each row of the matrix must have the same size`
- `div` must be a number (integer or float), otherwise raise a `TypeError` exception with the message `div must be a number`
- `div` can’t be equal to `0`, otherwise raise a `ZeroDivisionError` exception with the message `division by zero`
- All elements of the matrix should be divided by `div`, rounded to 2 decimal places
- Returns a new matrix
- You are not allowed to import any module

### Expectation
```Python
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
    TypeError: Si `div` n'est pas un entier
    TypeError: Si `div` est égale à 0

    Exemples:
    >>> matrix_divided(matrix, 3)
    [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
    >>> matrix_divided(matrix, 5.5)
    [[0.18, 0.36, 0.55], [0.73, 0.91, 1.09]]
    """

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not isinstance(div, (int, float)):
    	raise TypeError("div must be a number")

    if div == 0:
    	raise ZeroDivisionError("division by zero")


    new_matrix = []

    for i in matrix:
        new_matrix.append(list(map(lambda x: round(x / div, 2), i)))

    return new_matrix
```
### Result
```bash
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
[[1, 2, 3], [4, 5, 6]]
```

##
### Objectives
### Expectation
```Python
```
### Result
```bash
```

##
### Objectives
### Expectation
```Python
```
### Result
```bash
```

##
### Objectives
### Expectation
```Python
```
### Result
```bash
```

##
### Objectives
### Expectation
```Python
```
### Result
```bash
```
