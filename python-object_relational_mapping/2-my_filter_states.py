#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states table
where name matches the argument.
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

    # Construction et exécution de la requête SQL avec l'input utilisateur
    query = (
        "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC"
        .format(sys.argv[4])
    )
    cur.execute(query)

    # Récupération et affichage des résultats
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Fermeture du curseur et de la connexion à la base de données
    cur.close()
    db.close()