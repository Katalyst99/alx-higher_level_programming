#!/usr/bin/python3
"""A script that deletes all states objects that contain the letter a"""
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
    state_obj = session.query(State).filter(State.name.like('%a%')).all()
    for state in state_obj:
        session.delete(state)
    session.commit()
    session.close()
