#!/usr/bin/python3
def write_file(filename="", text=""):
    """
    Écrit chaîne de caractères dans fichier texte, retourne le nb caractères

    Args:
    filename(str): Le nom/chemin du fichier ds lql écrire. Défaut, chaîne vide.
    text(str): Le texte à écrire ds fichier. Par défaut, chaîne vide.

    Returns:
    int: Le nombre de caractères écrits dans le fichier.

    Note:
    - Le fichier est ouvert en mode écriture ('w')
    - L'encodage UTF-8 est utilisé
    - Si le fichier existe déjà, son contenu est écrasé
    - Le fichier est automatiquement fermé après l'écriture
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
        return len(text)
