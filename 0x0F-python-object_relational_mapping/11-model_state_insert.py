#!/usr/bin/python3
'''
prints the first State object from the database hbtn_0e_6_usa
'''

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

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
    st = State(name="Louisiana")
    session.add(st)
    session.commit()
    print(st.id)
    # close session
    session.close()
