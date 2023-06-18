#!/usr/bin/pytho3
"""
A script that lists all State objects
from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':

    """ Get the arguments """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    """ Create the engine and establish the database connection """
    db_link = "f'mysql+mysqldb://{username}: \
        {password}@localhost:3306/{database}'"
    engine = create_engine(db_link)
    Base.metadata.bind = engine

    """ Create a session to interact with the database """
    Session = sessionmaker(bind=engine)
    session = Session()

    """ Query all State objects and sort them by id in ascending order """
    states = session.query(State).order_by(State.id).all()

    """ Display the results """
    for state in states:
        print(f'{state.id}: {state.name}')

    session.close()
