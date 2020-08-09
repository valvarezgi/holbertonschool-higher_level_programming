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
    new_state = State(name='Louisiana')
    session.add(new_state)
    session.flush()
    session.commit()
    selections = session.query(State).order_by(State.id).all()
    for selection in selections:
        if selection.name == 'Louisiana':
            print(selection.id)
            break
    session.close()
