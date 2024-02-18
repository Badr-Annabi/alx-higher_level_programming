#!/usr/bin/python3
"""List all elements of the table States"""


import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    state_city = session.query(
            State.name, City.id, City.name).join(
                    City, City.state_id == State.id).order_by(City.id)
    all_states = state_city.all()
    for state, city_id, city in all_states:
        print("{}: ({}) {}".format(state, city_id, city))
