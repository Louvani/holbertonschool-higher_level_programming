#!/usr/bin/python3
'''
lists all State objects from the database hbtn_0e_6_usa
'''

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == '__main__':
    # an Engine, which the Session will use for connection
    # resources
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    # create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # create a Session
    session = Session()

    # work with sess
    query = session.query(State, City).filter(
        State.id == City.state_id).order_by(City.id)
    for record1, record2 in query:
        print("{}: ({}) {}".format(record1.name, record2.id, record2.name))

    # close session
    session.close()
