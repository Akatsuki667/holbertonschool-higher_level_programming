#!/usr/bin/python3

from sys import argv  # importation ARGV de SYS
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_item():
    """
    Ajoute des éléments à une liste stockée dans un fichier JSON.

    Cette fonction charge liste d'éléments depuis fichier JSON 'add_item.json'.
    Elle ajoute arguments passés en CLI (à l'exception du nom du script)
    à cette liste, sauvegarde la liste mise à jour dans le même fichier JSON.

    Si le fichier 'add_item.json' n'existe pas, une nouvelle liste est créée.

    Args:
    None (utilise les arguments de la ligne de commande via sys.argv)

    Example:
    Pour ajouter les éléments 'apple' et 'banana' à la liste, exécutez :
    >>> python script.py apple banana
    # Le fichier 'add_item.json' contiendra maintenant : ["apple", "banana"]
    """
    filename = "add_item.json"  # Définit nom du fichier JSON

    try:
        args = load_from_json_file(filename)  # Charger données fichier JSON
    except FileNotFoundError:
        args = []

    args.extend(argv[1:])  # Ajout argv CLI sauf le premier
    save_to_json_file(args, filename)
