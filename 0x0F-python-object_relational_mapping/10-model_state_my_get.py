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
    selections = session.query(State).order_by(State.id).all()
    for selection in selections:
        if selection.name == argv[4]:
            print(selection.id)
            session.close()
            exit()
    print("Not found")
    session.close()
