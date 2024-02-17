#!/usr/bin/python3
"""creates first class using SQLALchemy"""


from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(
        'mysql+mysqldb://{usr}:{pss}@ \
                localhost:3306/ \
                {hbtn_0e_6_usa}'.format("root", "root", "hbtn_0e_6_usa \
                "), pool_pre_ping=True)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
