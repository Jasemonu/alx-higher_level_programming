#!/usr/bin/python3
"""
A script that prints the State object with
the name passed as argument from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    """
    Access to the database and get a state
    from the database.
    """

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            username, password, database))
    Base.metadata.bind = engine
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).filter(State.name == state_name).first()

    if state is None:
        print("Not found")
    else:
        print("{}".format(state.id))
    session.close()
