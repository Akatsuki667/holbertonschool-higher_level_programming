#!/usr/bin/python3


class Student:
    """
    Classe représentant un étudiant avec ses informations de base.

    Attributes:
    first_name (str): Le prénom de l'étudiant
    last_name (str): Le nom de famille de l'étudiant
    age (int): L'âge de l'étudiant
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialise un nouvel étudiant.

        Args:
        first_name (str): Le prénom de l'étudiant
        last_name (str): Le nom de famille de l'étudiant
        age (int): L'âge de l'étudiant
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retourne une représentation dictionnaire de l'instance Student.

        Args:
        attrs (list, optional): Liste de chaînes de caractères contenant
            les noms des attributs à inclure. Si None, tous les attributs
            sont inclus.

        Returns:
        dict: Dictionnaire contenant les attributs de l'étudiant.
            Si attrs est spécifié, seuls les attributs listés sont inclus.
            Si attrs est None ou invalide, tous les attributs sont inclus.

        Note:
        - Si attrs est fourni, il doit être une liste de strings
        - Utilise __dict__ pour accéder aux attributs de l'instance
        """
        if (isinstance(attrs, list) and
                all(isinstance(attr, str) for attr in attrs)):
            return {key: value for key, value in self.__dict__.items()
                    if key in attrs}
        return self.__dict__
