#!/usr/bin/python3
"""Script qui liste tous les états depuis la base de données hbtn_0e_0_usa"""


import MySQLdb
import sys


def list_states():
    """Fonction qui liste tous les états depuis la base de données"""
    # Vérifie si le nombre d'arguments passés est correct
    if len(sys.argv) != 4:
        return

    # Récupère les arguments depuis la ligne de commande
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Se connecte au serveur MySQL avec les paramètres fournis
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Crée un objet curseur pour interagir avec la base de données
    cursor = db.cursor()

    # Exécute la requête pour récupérer tous les états triés par identifiant
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Récupère toutes les lignes et les affiche
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Ferme le curseur et la connexion à la base de données
    cursor.close()
    db.close()


if __name__ == "__main__":
    list_states()
