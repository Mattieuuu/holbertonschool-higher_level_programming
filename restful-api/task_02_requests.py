#!/usr/bin/python3
'''request model'''
# C'est un "shebang", utilisé pour spécifier que le script doit être exécuté avec l'interpréteur Python 3.

import requests
import csv
# Importation des modules nécessaires. 
# `requests` est utilisé pour effectuer des requêtes HTTP.
# `csv` est utilisé pour manipuler des fichiers CSV (ici, pour écrire dans un fichier CSV).

# Function to fetch and print posts
def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    # Définition de l'URL de l'API pour récupérer les posts (c'est une API publique pour des tests).

    response = requests.get(url)
    # Effectuer une requête GET sur l'URL pour obtenir les données.

    print(f"Status Code: {response.status_code}")
    # Affiche le code de statut de la réponse HTTP pour indiquer si la requête a réussi ou non.

    if response.status_code == 200:
        # Si le code de statut est 200, cela signifie que la requête a réussi.
        posts = response.json()
        # Convertit la réponse JSON en un objet Python (une liste de posts).

        for post in posts:
            # Parcourt chaque post dans la liste de posts.
            print(post["title"])
            # Affiche le titre de chaque post.
    else:
        print("Failed to fetch posts.")
        # Si le code de statut n'est pas 200, on affiche un message d'erreur indiquant l'échec.

# Function to fetch and save posts to a CSV file
def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    # Définition de l'URL de l'API pour récupérer les posts (identique à l'URL dans la fonction précédente).

    response = requests.get(url)
    # Effectuer une requête GET pour obtenir les données de l'API.

    if response.status_code == 200:
        # Si la requête a réussi (code 200),
        posts = response.json()
        # Convertit la réponse JSON en une liste d'objets Python représentant les posts.

        data = [
            {"id": post["id"], "title": post["title"], "body": post["body"]}
            for post in posts
        ]
        # Crée une nouvelle liste `data` qui contient des dictionnaires avec les informations 'id', 'title', et 'body' pour chaque post.

        # Writing to a CSV file
        with open("posts.csv", "w", newline="", encoding="utf-8") as file:
            # Ouvre un fichier CSV nommé "posts.csv" en mode écriture. 
            # `newline=""` empêche l'ajout de lignes vides entre les lignes du fichier CSV.
            # L'encodage UTF-8 est spécifié pour gérer les caractères spéciaux.

            fieldnames = ["id", "title", "body"]
            # Définition des noms des colonnes qui seront dans le fichier CSV.

            writer = csv.DictWriter(file, fieldnames=fieldnames)
            # Crée un objet `DictWriter` pour écrire un dictionnaire dans un fichier CSV.

            writer.writeheader()
            # Écrit la ligne d'en-tête dans le fichier CSV (les noms des colonnes).

            writer.writerows(data)
            # Écrit toutes les lignes de données (les posts) dans le fichier CSV.

        print("Data successfully written to posts.csv")
        # Affiche un message pour indiquer que les données ont été écrites avec succès dans le fichier CSV.
    else:
        print("Failed to fetch posts.")
        # Si le code de statut n'est pas 200, affiche un message d'erreur.
