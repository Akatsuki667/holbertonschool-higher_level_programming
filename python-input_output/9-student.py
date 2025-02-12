#!/usr/bin/python3


class Student:
    """
    Classe représentant un étudiant.

    Attributes:
    first_name (str): Le prénom de l'étudiant.
    last_name (str): Le nom de famille de l'étudiant.
    age (int): L'âge de l'étudiant.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialise nouvel étudiant avec un prénom, un nom de famille et un âge.

        Args:
        first_name (str): Le prénom de l'étudiant.
        last_name (str): Le nom de famille de l'étudiant.
        age (int): L'âge de l'étudiant.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Convertit les attributs de l'objet en un dictionnaire.

        Cette méthode retourne un dictionnaire contenant tous les attributs
        de l'objet et leurs valeurs associées. Cela peut être utile pour
        sérialiser l'objet en JSON.

        Returns:
        dict: Un dictionnaire représentant les attributs de l'objet.

        Example:
        >>> student = Student('John', 'Doe', 20)
        >>> student.to_json()
        {'first_name': 'John', 'last_name': 'Doe', 'age': 20}
        """
        return self.__dict__
