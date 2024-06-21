#!/usr/bin/python3
"""A script that lists all states objects from the database hbtn_0e_6_usa"""
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    for cs_obj in session.query(State, City).join(City).order_by(City.id):
        print("{}: ({}) {}"
              .format(cs_obj.State.name, cs_obj.City.id, cs_obj.City.name))
    session.commit()
    session.close()
