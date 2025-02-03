#!/usr/bin/python3
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
