#!/usr/bin/python3
"""A script that lists all states objects from the database hbtn_0e_6_usa"""
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    for state_obj in session.query(State).order_by(State.id.asc()).all():
        print("{}: {}".format(state_obj.id, state_obj.name))
    session.close()
