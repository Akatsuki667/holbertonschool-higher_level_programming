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

##
### Objectives
### Expectation
```python3
```
### Result
```bash
```

##
### Objectives
### Expectation
```python3
```
### Result
```bash
```

##
### Objectives
### Expectation
```python3
```
### Result
```bash
```

##
### Objectives
### Expectation
```python3
```
### Result
```bash
```

##
### Objectives
### Expectation
```python3
```
### Result
```bash
```