#!/usr/bin/python3
"""A script that prints the State object with the name passed as argument"""
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
    state_obj = session.query(State).filter(State.name == argv[4]).first()
    if not state_obj:
        print('Not found')
    else:
        print("{}".format(state_obj.id))
    session.close()
