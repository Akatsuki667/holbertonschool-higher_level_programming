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

    def to_json(self, attrs=None):
        """
        Convertit les attributs de l'objet en un dictionnaire JSON.

        Si une liste d'attributs est fournie, seuls ces attributs seront inclus
        dans le dictionnaire. Sinon, les attributs de l'objet seront inclus.

        Args:
        attrs (list, optional): Une liste de noms d'attributs à inclure
                                dans le dictionnaire JSON. Si None, tous
        """
