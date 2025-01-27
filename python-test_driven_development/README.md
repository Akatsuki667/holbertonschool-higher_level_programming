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
```
### Result
```bash
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
[[1, 2, 3], [4, 5, 6]]
```

## 2. Say my name
Write a function that prints `My name is <first name> <last name>`

### Objectives
- Prototype: `def say_my_name(first_name, last_name=""):`
- first_name and last_name must be strings otherwise, raise a `TypeError` exception with the message `first_name must be a string` or `last_name must be a string`
- You are not allowed to import any module
### Expectation
```Python
#!/usr/bin/python3
"""
Ceci est `3-say_my_name` module

Ce module contient une fonction `say_my_name(first_name, last_name="")`

Cette fonction affiche "My name is <first name> <last name>"
"""


def say_my_name(first_name, last_name=""):
    """
    affiche "My name is <first name> <last name>"

    Paramètres:
    first_name(str): Nom
    last_name(str): Prénom

    Raises:
    TypeError: Si first_name ou last_name ne sont pas de type str

    Exemples:
    >>> say_my_name("Walter", "White")
    My name is Walter White
    >>> say_my_name("Bob")
    My name is Bob
    >>> say_my_name(12, "White")
    TypeError: first_name must be a string
    """

    if type(first_name) not in [str]:
        raise TypeError("first_name must be a string")

    if type(last_name) not in [str]:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
```
### Result
```bash
My name is John Smith
My name is Walter White
My name is Bob 
first_name must be a string
```

## 3. Print square
Write a function that prints a square with the character `#`.

### Objectives
- Prototype: `def print_square(size):`
- `size` is the size length of the square
- `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
- if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
- if `size` is a float and is less than 0, raise a `TypeError` exception with the message `size must be an integer`
- You are not allowed to import any module

### Expectation
```Python
#!/usr/bin/python3
"""
Ceci est `4-print_square.py` module

Ce module contient la fonction `print_square(size)`

Cette fonction affiche un carré en utilisant `#`
"""


def print_square(size):
    """
    Affiche un carré en utilisant `#`

    Paramètre:
    size(int): la taille de la longueur du carré

    Raises:
    TypeError: Si la taille n'est ps `int`
    ValueError: Si la taille est plus petite que 0

    Exemples:
    >>> print_square(2)
    ##
    ##
    >>> print_square(4)
    ####
    ####
    ####
    ####
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)

```
### Result
```bash
####
####
####
####

##########
##########
##########
##########
##########
##########
##########
##########
##########
##########


#

size must be >= 0
```

## 4. Text indentation
Write a function that prints a text with 2 new lines after each of these characters: `.`, `?` and `:`

### Objectives
- Prototype: `def text_indentation(text):`
- `text` must be a string, otherwise raise a `TypeError` exception with the message `text must be a string`
- There should be no space at the beginning or at the end of each printed line
- You are not allowed to import any module

### Expectation
```Python
#!/usr/bin/python3
"""
Ceci est `5-text_indentation` module

Ce module contient la fonction `text_indentation(text)`

Cette fonction affiche un texte avec 2 lignes
avec ces caractères `. ? :` 
"""


def text_indentation(text):
    """
    Cette fonction affiche un texte avec 2 lignes
    avec ces caractères `. ? :` 

    Paramètre:
    text(str): Texte à formater et afficher

    Raises:
    TypeError: Si le texte n'est pas de type str

    Exemples:
    >>> text_indentation("Hello. How are you? Fine:")
    Hello.

    How are you?

    Fine:
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""

    skip_space = False

    for char in text:
        if char in ".:?":
            result += char + "\n\n"
            skip_space = True
        elif char == " " and skip_space:
            continue
        else:
            result += char
            skip_space = False
    print(result.strip(), end="")
```
### Result
```bash
Lorem ipsum dolor sit amet, consectetur adipiscing elit.

Quonam modo?

Utrum igitur tibi litteram videor an totas paginas commovere?

Non autem hoc:

igitur ne illud quidem.

Fortasse id optimum, sed ubi illud:

Plus semper voluptatis?

Teneo, inquit, finem illi videri nihil dolere.

Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum rationi oboediens.

Si id dicis, vicimus.

Inde sermone vario sex illa a Dipylo stadia confecimus.

Sin aliud quid voles, postea.

Quae animi affectio suum cuique tribuens atque hanc, quam dico.

Utinam quidem dicerent alium alio beatiorem! Iam ruinas videres%                                                              
```

## 5. Max integer - Unittest
Since the beginning you have been creating “Interactive tests”. For this exercise, you will add Unittests.

In this task, you will write unittests for the function `def max_integer(list=[]):`.

### Objectives
- Your test file should be inside a folder `tests`
- You have to use the `unittest module`
- Your test file should be python files (extension: .py)
- Your test file should be executed by using this command: `python3 -m unittest tests.6-max_integer_test`
- All tests you make must be passable by the function below
- We strongly encourage you to work together on test cases, so that you don’t miss any edge case

### Expectation
```Python
```
### Result
```bash
```
