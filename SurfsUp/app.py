# Import the dependencies.
from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
import pandas as pd


#################################################
# Database Setup
####### Create a reference to the file.
database_path = Path("../Resources/Census_Data.sqlite")


####### Create a connection that can talk to the database
conn = create_engine(f"sqlite:///{database_path}").connect()


#################### see if it works
data = pd.read_sql("SELECT * FROM icecreamstore", conn)
data.head()
#################################################


# reflect an existing database into a new model

# reflect the tables


# Save references to each table


# Create our session (link) from Python to the DB


#################################################
# Flask Setup
#################################################




#################################################
# Flask Routes
#################################################
