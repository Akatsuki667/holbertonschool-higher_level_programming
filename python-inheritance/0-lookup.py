#!/usr/bin/python3
"""
Module `0-lookup`

Ce module contient une fonction `lookup`

Cette fonciton retourne une liste des attributs et méthodes d'un objet
"""


def lookup(obj):
    """
    Fonction lookup

    Args:
    obj: Objet dont l'on souhaite obtenir liste attributs et méthodes

    Return:
    list: des attributs et méthodes d'un objet
    """
    return dir(obj)
