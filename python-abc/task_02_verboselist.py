#!/usr/bin/python3


class VerboseList(list):

    def append(self, item):
        print(f"Added {[item]} to the list.")

    def extend(self, item):
        super().extend(item)
        print(f"Extended the list with {[item]} items.")

    def remove(self, item):
        print(f"Removed {[item]} from the list.")

    def pop(self, index=-1):  # -1 par défaut pour suivre comportement list.pop
        item = self[index]  # Récupération élément
        print(f"Popped {[item]} from the list.")
        return super().pop(index)  # Supprimer et retourner élément
