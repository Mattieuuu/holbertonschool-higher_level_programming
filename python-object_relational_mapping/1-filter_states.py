#!/usr/bin/python3
"""
Script that lists all states from the database.
"""
import MySQLdb
import sys

def connectBDD(user, password, BDD_name):
    """
    Establishes a connection to the MySQL database.

    This function connects to a MySQL database using the provided credentials
    (username, password, and database name).

    Args:
        user (str): Username to connect to the database.
        password (str): Password associated with the username.
        BDD_name (str): Name of the database to connect to.

    Returns:
        MySQLdb.connect: A MySQL database connection object.
    """
    connect = MySQLdb.connect(
        host="localhost",
        user=user,
        password=password,
        db=BDD_name,
        port=3306,
        charset="utf8"
    )
    return connect

# Get command line arguments
if __name__== "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    BDD_name = sys.argv[3]

connect = connectBDD(user, password, BDD_name)
# Create cursor to execute SQL query
cursor = connect.cursor()
cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
# Fetch and display all rows from the query
query_rows = cursor.fetchall()
for row in query_rows:
    print(row)
# Close cursor and database connection
cursor.close()
connect.close()
