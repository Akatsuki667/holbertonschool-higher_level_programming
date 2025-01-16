#!/usr/bin/python3
def uppercase(str):
    result = ""  # Chaîne qui va contenir le texte final
    for ch in str:
        if ord(ch) >= 97 and ord(ch) <= 122:  # Si c'est une minuscule
            result += chr(ord(ch) - 32)  # Conversion en majuscule
        else:
            result += ch  # Caractère inchangé
    print("{}".format(result))  # Afficher la chaîne entière transformée
