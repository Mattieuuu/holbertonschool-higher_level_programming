#!/usr/bin/python3
"""
Script that lists all states with a name starting with 'N' from the database.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Connexion à la base de données MySQL
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
    )

    # Création d'un curseur pour exécuter des requêtes SQL
    cur = db.cursor()

    # Exécution de la requête SQL pour récupérer les états commençant par 'N'
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Récupération et affichage des résultats
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Fermeture du curseur et de la connexion à la base de données
    cur.close()
    db.close()