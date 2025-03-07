#!/usr/bin/python3
"""
    Script that lists all State objects from the database.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


if __name__ == "__main__":
     # Récupérer les arguments passés en ligne de commande
    args = {
        'user': sys.argv[1],
        'password': sys.argv[2],
        'db_name': sys.argv[3]
    }
    # Utilisation du dictionnaire pour formater l'URL de connexion
    engine = create_engine(
        'mysql+mysqldb://{user}:{password}@localhost/{db_name}'.format(**args),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)
	 # Création de la session pour interagir avec la base de données
    session = Session(engine)
    # Récupérer toutes les instances de la classe State
    q = session.query(State)
    for state in q.all():
        print("{:d}: {:s}".format(state.id, state.name))
        
    session.close()