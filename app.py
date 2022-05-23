import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt

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
# session = Session(engine)

# # find the last date in the database
# last_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()

# # Calculate the date 1 year ago from the last data point in the database
# query_date = dt.date(2017,8,23) - dt.timedelta(days=365)

# session.close()
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
    )
###########################################################
# create precipitation route
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create the session link
    session = Session(engine)

    """Return the dictionary for date and precipitation info"""
    # Query precipitation and date values 
    results = session.query(Measurement.date, Measurement.prcp).all()
        
    session.close()
    
    # Create a dictionary as date the key and prcp as the value
    precipitation = []
    for result in results:
        r = {}
        r[result[0]] = result[1]
        precipitation.append(r)

    return jsonify(precipitation )

#################################################################
if __name__ == '__main__':
    app.run(debug=True)