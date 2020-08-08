#!/usr/bin/python3
"""List all State objects"""
import sys
from model_state import Base, State
from sqlalchemy import asc, create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    start = sessionmaker()
    start.configure(bind=engine)
    starts = start()
    selections = starts.query(State).order_by(asc(State.id)).all()

    for selection in selections:
        print("{}: {}".format(selection.id, selection.name))

    starts.close()
