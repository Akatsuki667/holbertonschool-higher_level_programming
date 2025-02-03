#!/usr/bin/python3
"""
Module `base_geometry`

Contient une class `BaseGeometry` base pour la géométrie
"""


class BaseGeometry:
    """
    Classe de base pour la géométrie.

    Cette classe définit une structure de base pour des objets géométriques,
    avec une méthode `area` qui doit être implémentée dans les sous-classes.

    Méthodes :
    - area(self): Méthode à implémenter dans les sous-classes.
    Lève une exception si elle est appelée directement depuis cette classe.
    """
    def area(self):
        """
        Calcule l'aire de la figure géométrique.

        Cette méthode doit être surchargée dans les sous-classes.
        Lève une exception si elle est appelée depuis `BaseGeometry`.

        Raises:
        Exception: "area() is not implemented"
        """
        raise Exception("area() is not implemented")

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
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
