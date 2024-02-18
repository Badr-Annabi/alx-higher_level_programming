#!/usr/bin/python3
""" creates State "California" with City "San Francisco"
"""
from relationship_state import State, Base
from relationship_city import City
from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine_info = 'mysql+mysqldb://{}:{}@localhost:{}/{}'\
        .format(argv[1], argv[2], 3306, argv[3])

    engine = create_engine(engine_info, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id)

    for state in states:
        for city in state.cities:
            printf("{}: {} -> {}".format(city.id, city.name, state.name))
