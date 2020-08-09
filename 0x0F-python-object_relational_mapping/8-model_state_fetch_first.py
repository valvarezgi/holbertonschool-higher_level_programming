#!/usr/bin/python3
"""List all State objects"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    session = Session()
    selection = session.query(State).order_by(State.id).first()
    if selection:
        print("{}: {}".format(selection.id, selection.name))
    else:
        print("Nothing")
    session.close()
