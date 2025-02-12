#!/usr/bin/python3
def read_file(filename=""):
    """
    Lit et affiche le contenu d'un fichier texte sur la sortie standard.

    Args:
    filename (str): Le nom/chemin du fichier à lire. Par défaut, chaîne vide.

    Returns:
    None: La fonction affiche le contenu mais ne retourne rien.

    Note:
    - Le fichier est ouvert en mode lecture ('r')
    - L'encodage UTF-8 est utilisé
    - Le contenu est affiché sans ajouter de saut de ligne à la fin
    - Le fichier est automatiquement fermé après la lecture
    """
    with open(filename, "r", encoding="utf-8") as f:
        contenu = f.read()
        print(contenu, end="")
