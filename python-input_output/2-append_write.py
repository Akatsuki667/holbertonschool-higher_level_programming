#!/usr/bin/python3

def append_write(filename="", text=""):
    """
    Ajoute du texte à la fin d'un fichier.

    Cette fonction ouvre un fichier en mode ajout ('append') et écrit le texte
    fourni à la fin du fichier. Si le fichier n'existe pas, il sera créé.

    Args:
    filename (str): Le nom du fichier où le texte sera ajouté.
    text (str): Le texte à ajouter au fichier.

    Returns:
    int: Le nombre de caractères écrits dans le fichier.

    Example:
    >>> append_write('example.txt', 'Hello, World!')
    13
    >>> append_write('example.txt', 'Appending new text.')
    19
    """
    with open(filename, "a", encoding="utf-8") as f:
        f.write("\n" + text)
        return len(text)
