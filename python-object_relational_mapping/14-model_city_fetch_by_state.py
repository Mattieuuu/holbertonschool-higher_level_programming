#!/usr/bin/python3
"""
Lists all City objects from the database hbtn_0e_14_usa,
sorted by cities.id, displaying them in the format:
<state name>: (<city id>) <city name>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    # Create the database engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all cities with their state names, ordered by city.id
    results = session.query(City, State).join(State).order_by(City.id).all()

    # Print results in the required format
    for city, state in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    # Close session
    session.close()