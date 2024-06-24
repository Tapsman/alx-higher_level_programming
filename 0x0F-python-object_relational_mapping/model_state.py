#!/usr/bin/python3
"""
This is a python file that contains the class defination of a state
and an instance base = declarative_base():
"""

import sys
from model_state import Base, State

from sqlelchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
            .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
