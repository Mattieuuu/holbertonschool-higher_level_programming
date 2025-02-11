#!/usr/bin/python3
'''write a file'''


def write_file(filename="", text=""):
    # Ouvre le fichier en mode écriture ('w'), cela écrase le contenu existant ou crée le fichier si nécessaire
    with open(filename, 'w', encoding='utf-8') as file:
        # Écrit le texte dans le fichier
        file.write(text)
        # Retourne le nombre de caractères écrits
        return len(text)
