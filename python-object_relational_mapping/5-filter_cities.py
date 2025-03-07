#!/usr/bin/python3
"""
Script that lists all cities of a given state from the database hbtn_0e_4_usa.
It prevents SQL injection by using parameterized queries.
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

    # Requête SQL sécurisée avec un paramètre pour éviter les injections SQL
    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """

    cur.execute(query, (sys.argv[4],))

    # Récupération des résultats et affichage
    rows = cur.fetchall()
    cities = [row[0] for row in rows]
    print(", ".join(cities))

    # Fermeture du curseur et de la connexion à la base de données
    cur.close()
    db.close()