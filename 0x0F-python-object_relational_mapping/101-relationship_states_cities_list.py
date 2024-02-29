#!/usr/bin/python3
""" Lists all states with their corresponding cities"
"""
from relationship_state import State, Base
from relationship_city import City
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine_info = 'mysql+mysqldb://{}:{}@localhost:3306/{}'\
        .format(argv[1], argv[2], argv[3])

    engine = create_engine(engine_info, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))
