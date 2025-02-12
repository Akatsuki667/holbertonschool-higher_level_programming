#!/usr/bin/python3

from sys import argv  # importation ARGV de SYS
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_item():

    filename = "add_item.json"  # Définit nom du fichier JSON

    try:
        args = load_from_json_file(filename)  # Charger données fichier JSON
    except FileNotFoundError:
        args = []

    args.extend(argv[1:])  # Ajout argv CLI sauf le premier
    save_to_json_file(args, filename)


# Vérification script exécuté (et non importé comme module)
if __name__ == "__main__":
    add_item()
