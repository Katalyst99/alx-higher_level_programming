#!/usr/bin/python3
"""A script that adds the State object Louisiana database hbtn_0e_6_usa"""
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
    state_new = State(name="Louisiana")
    session.add(state_new)
    session.commit()
    print(state_new.id)
    session.close()
