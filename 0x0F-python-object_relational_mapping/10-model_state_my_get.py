#!/usr/bin/python3
"""List first State object from the database hbtn_0e_6_usa"""


import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    name_search = sys.argv[4]
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(
            State).filter(
                    State.name == name_search).first()

    if (state):
        print("{}".format(state.id))
    else:
        print("Not found")
