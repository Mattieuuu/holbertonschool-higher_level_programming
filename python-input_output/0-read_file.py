#!/usr/bin/python3

def read_file(filename=""):
    # Ouvre le fichier en mode lecture ('r') en utilisant 'with'
    with open(filename, 'r', encoding='utf-8') as file:
        # Lit tout le contenu du fichier
        content = file.read()
        # Affiche le contenu du fichier à l'écran
        print(content)
