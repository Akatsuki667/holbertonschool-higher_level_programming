# Python - Inheritance

## 0. Lookup
Write a function that returns the list of available attributes and methods of an object:

### Objectives
- Prototype: `def lookup(obj):`
- Returns a `list` object
- You are not allowed to import any module

### Expectation
```python3
#!/usr/bin/python3
def lookup(obj):
    return dir(obj)
```
### Result
```bash
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'my_attr1', 'my_meth']
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
```

## 1. My list
Write a class `MyList` that inherits from `list`:

### Objectives
- Public instance method: `def print_sorted(self):` that prints the list, but sorted (ascending sort)
- You can assume that all the elements of the list will be of type `int`
- You are not allowed to import any module

### Expectation
```python3
#!/usr/bin/python3
"""
Module `1-my_list`

Ce module définit une classe `MyList`
"""


class MyList(list):
    """
    `MyList` classe
    """

    def print_sorted(self):
        """
        Affiche les éléments de la liste triées en ordre croissant
        """
        print(sorted(self))
```
### Result
```bash
[1, 4, 2, 3, 5]
[1, 2, 3, 4, 5]
[1, 4, 2, 3, 5]
```

## 2. Exact same object
Write a function that returns `True` if the object is exactly an instance of the specified class ; otherwise `False`.

### Objectives
- Prototype: `def is_same_class(obj, a_class):`
- You are not allowed to import any module

### Expectation
```python3
#!/usr/bin/python3
def is_same_class(obj, a_class):
    """
    Vérifie si un objet est exactement une instance d'une classe donnée.

    Args:
    obj (any): L'objet à vérifier.
    a_class (type): La classe de référence.

    Returns:
    bool: True si `obj` est exactement une instance de `a_class`, sinon False.
    """
    return type(obj) is a_class
```
### Result
```bash
1 is an instance of the class int
```

## 3. Same class or inherit from
Write a function that returns `True` if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise `False`.

### Objectives
- Prototype: `def is_kind_of_class(obj, a_class):`
- You are not allowed to import any module

### Expectation
```python3
#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """
    Vérifie si un objet est instance d'une classe ou classe parente.

    Args:
    obj (any): L'objet à vérifier.
    a_class (type): La classe de référence.

    Returns:
    bool: True`obj` instance de `a_class`/ classe parente`a_class`,sinon False.
    """
    return isinstance(obj, a_class)
```
### Result
```bash
1 comes from int
1 comes from object
```

## 4. Only sub class of
Write a function that returns `True` if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise `False`.

### Objectives
- Prototype: `def inherits_from(obj, a_class):`
- You are not allowed to import any module

### Expectation
```python3
#!/usr/bin/python3
def inherits_from(obj, a_class):
    """
    Vérifie si un objet est une instance d'une sous-classe de `a_class`
    (sans être une instance directe de `a_class`).

    Args:
    obj (any): L'objet à vérifier.
    a_class (type): La classe de référence.

    Returns:
    bool: True si `obj` est une instance d'une sous-classe de `a_class`,
        mais pas une instance directe de `a_class`. Sinon, False.
    """
    return not issubclass(a_class, type(obj))
```
### Result
```bash
True inherited from class int
True inherited from class object
```

## 5. Geometry module
Write an empty class `BaseGeometry`.

### Objectives
- You are not allowed to import any module

### Expectation
```python3
#!/usr/bin/python3
class BaseGeometry:
    """
    Classe de base pour la géométrie.

    Cette classe ne contient pour l'instant aucune méthode ni attribut.
    """
    pass
```
### Result
```bash
<5-base_geometry.BaseGeometry object at 0x7f2050c69208>
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
```

## 6. Improve Geometry
Write a class `BaseGeometry` (based on `5-base_geometry.py`).

### Objectives
- Public instance method: `def area(self):` that raises an `Exception` with the message `area() is not implemented`
- You are not allowed to import any module

### Expectation
```python3
    def area(self):
        """
        Calcule l'aire de la figure géométrique.

        Cette méthode doit être surchargée dans les sous-classes.
        Lève une exception si elle est appelée depuis `BaseGeometry`.

        Raises:
        Exception: "area() is not implemented"
        """
        raise Exception("area() is not implemented")
```
### Result
```bash
[Exception] area() is not implemented
```

## 7. Integer validator
Write a class `BaseGeometry` (based on `6-base_geometry.py`).

### Objectives
- Public instance method: `def area(self):` that raises an `Exception` with the message `area() is not implemented`
- Public instance method: `def integer_validator(self, name, value):` that validates `value`:
    - you can assume `name` is always a string
    - if `value` is not an integer: raise a `TypeError` exception, with the message `<name> must be an integer`
    - if `value` is less or equal to 0: raise a `ValueError` exception with the message `<name> must be greater than 0`
- You are not allowed to import any module

### Expectation
```python3
    def integer_validator(self, name, value):
        """
        Valide qu'une valeur est un entier positif.

        Vérifie si `value` est un entier et s'il est strictement positif.
        Elle lève une exception si ces conditions ne sont pas respectées.

        Args:
        name(str): Le nom de la variable (utilisé dans le message d'erreur).
        value(int): La valeur à valider.

        Raises:
        TypeError: Si `value` n'est pas un entier.
        ValueError: Si `value` est inférieur ou égal à 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
```
### Result
```bash
[TypeError] name must be an integer
[ValueError] age must be greater than 0
[ValueError] distance must be greater than 0
```

## 8. Rectangle
Write a class `Rectangle` (based on `7-base_geometry.py`).

### Objectives
- Instantiation with width and height: `def __init__(self, width, height):`
- `width` and `height` must be private. No getter or setter
- `width` and `height` must be positive integers, validated by `integer_validator`

### Expectation
```python3
#!/usr/bin/python3
"""
Module contenant la classe Rectangle qui hérite de BaseGeometry.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Classe représentant un rectangle, héritant de BaseGeometry.

    Hérite des fonctionnalités de BaseGeometry et ajoute
    la gestion des attributs de largeur et de hauteur.
    """

    def __init__(self, width, height):
        """
        Initialise un rectangle avec une largeur et une hauteur validées.

        Args:
            width (int): La largeur du rectangle, doit être un entier positif.
            height (int): La hauteur du rectangle, doit être un entier positif.

        Raises:
            TypeError: Si width ou height ne sont pas des entiers.
            ValueError: Si width ou height ne sont pas positifs.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
```
### Result
```bash
<8-rectangle.Rectangle object at 0x7f6f488f7eb8>
['_Rectangle__height', '_Rectangle__width', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'area', 'integer_validator']
[AttributeError] 'Rectangle' object has no attribute 'width'
[TypeError] height must be an integer
```

## 9. Full rectangle
Write a class `Rectangle` that inherits from `BaseGeometry` (`7-base_geometry.py`). (task based on `8-rectangle.py`)

### Objectives
- Instantiation with width and height: `def __init__(self, width, height):`
- `width` and `height` must be private. No getter or setter
- `width` and `height` must be positive integers, validated by `integer_validator`
- the `area()` method must be implemented
- `print()` should print, and `str()` should return, the following rectangle description: `[Rectangle] <width>/<height>`

### Expectation
```python3
    def area(self):
    """
    Calcule et retourne l'aire du rectangle.

    Returns:
    int: L'aire du rectangle (largeur × hauteur).
    """
    return self.__width * self.__height

    def __str__(self):
    """
    Retourne une représentation sous forme de chaîne du rectangle.

    Returns:
    str: Une chaîne de la forme "[Rectangle] width/height".
    """
    return f"[Rectangle] {self.__width}/{self.__height}"
```
### Result
```bash
[Rectangle] 3/5
15
```

## 10. Square #1
Write a class `Square` that inherits from `Rectangle` (`9-rectangle.py`):

### Objectives
- Instantiation with size: `def __init__(self, size):`:
    - `size` must be private. No getter or setter
    - `size` must be a positive integer, validated by `integer_validator`
- the `area()` method must be implemented

### Expectation
```python3
#!/usr/bin/python3
"""
Module contenant la classe Square qui hérite de Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """
    Classe représentant un carré, héritant de Rectangle.

    Hérite des fonctionnalités de Rectangle et assure que
    la largeur et la hauteur sont égales (propriété d'un carré).
    """

    def __init__(self, size):
        """
        Initialise un carré avec une taille validée.

        Args:
            size (int): La taille du côté du carré, doit être un entier positif.

        Raises:
            TypeError: Si size n'est pas un entier.
            ValueError: Si size n'est pas positif.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Calcule et retourne l'aire du carré.

        Returns:
            int: L'aire du carré (size × size).
        """
        return self.__size * self.__size
```
### Result
```bash
[Rectangle] 13/13
169
```

## 11. Square #2
Write a class `Square` that inherits from `Rectangle` (`9-rectangle.py`). (task based on `10-square.py`).

### Objectives
- Instantiation with size: `def __init__(self, size):`:
    - `size` must be private. No getter or setter
    - `size` must be a positive integer, validated by `integer_validator`
- the `area()` method must be implemented
- `print()` should print, and `str()` should return, the square description: `[Square] <width>/<height>`

### Expectation
```python3
    def __str__(self):
        """
        Retourne une représentation sous forme de chaîne du carré.

        Returns:
        str: Une chaîne de la forme "[Square] size/size".
        """
    return f"[Square] {self.__size}/{self.__size}"
```
### Result
```bash
[Square] 13/13
169
```