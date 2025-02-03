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
