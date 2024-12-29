# create_tables.py
from sqlalchemy import create_engine
from relationship_state import Base  # Import the Base
from relationship_state import State
from relationship_city import City

engine = create_engine('mysql+mysqldb://root:root@localhost/hbtn_0e_100_usa')

# Create all tables
Base.metadata.create_all(engine)
