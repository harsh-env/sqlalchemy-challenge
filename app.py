import numpy as np
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

######################################################
# Database Setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Reflect an existing database and tables
Base = automap_base()
Base.prepare(engine, reflect=True)

# Save reference to the tables
Measurement = Base.classes.measurement
Station = Base.classes.station

################################
session = Session(engine)

# find the last date in the database
last_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()

# Calculate the date 1 year ago from the last data point in the database
query_date = dt.date(2017,8,23) - dt.timedelta(days=365)

session.close()
################################

################################

# Create an app
app = Flask(__name__)

################################
# Flask Routes
# Define what to do when user hits the index route
@app.route("/")
def home():
    """List all available api routes."""
    return(
        f"Welcome to Hawaii Climate Page<br/> "
        f"Available Routes:<br/>"
        f"<br/>"  
        f"The list of precipitation data with dates:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"<br/>"
        f"The list of stations and names:<br/>"
        f"/api/v1.0/stations<br/>"
        f"<br/>"
        f"The list of temprture observations from a year from the last data point:<br/>"
        f"/api/v1.0/tobs<br/>"
        f"<br/>"
        f"Min, Max. and Avg. temperatures for given start date: (please use 'yyyy-mm-dd' format):<br/>"
        f"/api/v1.0/min_max_avg/&lt;start date&gt;<br/>"
        f"<br/>"
        f"Min. Max. and Avg. tempratures for given start and end date: (please use 'yyyy-mm-dd'/'yyyy-mm-dd' format for start and end values):<br/>"
        f"/api/v1.0/min_max_avg/&lt;start date&gt;/&lt;end date&gt;<br/>"
        f"<br/>"
        f"i.e. <a href='/api/v1.0/min_max_avg/2012-01-01/2016-12-31' target='_blank'>/api/v1.0/min_max_avg/2012-01-01/2016-12-31</a>"
    )
###########################################################
