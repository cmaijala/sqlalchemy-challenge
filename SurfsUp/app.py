# Import the dependencies.
import numpy as np
import sqlalchemy
import datetime as dt
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify, abort

#################################################
# Database Setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Reflect an existing database into a new model
Base = automap_base()
Base.prepare(autoload_with=engine)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
#Start of homepage with list of all the available routes.
@app.route("/")
def welcome():
    """List all available API routes."""
    return (
        f"Welcome to the SQL-Alchemy Honolulu, Hawaii Climate APP API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/[start_date format:%Y-%m-%d]<br/>"
        f"/api/v1.0/[start_date format:%Y-%m-%d]/[end_date format:%Y-%m-%d]<br/>"
    )

#Precipitation page analysis
@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return a list of all precipitation data."""
    try:
        results = session.query(Measurement.date, Measurement.prcp).\
            filter(Measurement.date >= "2016-08-24").\
            all()

        # Convert the list to Dictionary
        all_prcp = [{ "date": date, "prcp": prcp } for date, prcp in results]
        return jsonify(all_prcp)
    except Exception as e:
        print(e)
        abort(500)

#List of station page
@app.route("/api/v1.0/stations")
def stations():
    """Return a list of all stations."""
    try:
        results = session.query(Station.station).\
                     order_by(Station.station).all()

        # Convert list of tuples into a normal list
        all_stations = list(np.ravel(results))
        return jsonify(all_stations)
    except Exception as e:
        print(e)
        abort(500)

#Temperature observation page
@app.route("/api/v1.0/tobs")
def tobs():
    """Return a list of all TOBs."""
    try:
        results = session.query(Measurement.date, Measurement.tobs, Measurement.prcp).\
                    filter(Measurement.date >= '2016-08-23').\
                    filter(Measurement.station == 'USC00519281').\
                    order_by(Measurement.date).all()

        # Convert the list to Dictionary
        all_tobs = [{ "date": date, "prcp": prcp, "tobs": tobs } for date, tobs, prcp in results]
        return jsonify(all_tobs)
    except Exception as e:
        print(e)
        abort(500)

#start page of temperature in min, avg, and max. 
@app.route("/api/v1.0/<start>")
def start_date(start):
    """Return a JSON list of the min, avg, and max temperatures from the start date to the most recent date."""
    # Validate the date format
    try:
        dt.datetime.strptime(start, '%Y-%m-%d')
    except ValueError:
        return jsonify({"error": "Invalid date format. Use yyyy-mm-dd."}), 400

    try:
        results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
                    filter(Measurement.date >= start).all()

        # Check if results are empty
        if not results or results[0] == (None, None, None):
            return jsonify({"error": "No data found for the given start date."}), 404

        # Create a dictionary from the row data
        start_date_tobs = [{ "min_temp": min_temp, "avg_temp": avg_temp, "max_temp": max_temp } for min_temp, avg_temp, max_temp in results]
        return jsonify(start_date_tobs)
    except Exception as e:
        print(e)
        abort(500)

#start and end page of temperature in min, avg, and max. 
@app.route("/api/v1.0/<start>/<end>")
def start_end_date(start, end):
    """Return a JSON list of the min, avg, and max temperatures from the start date to the end date, inclusive."""
    # Validate the date format
    try:
        dt.datetime.strptime(start, '%Y-%m-%d')
        dt.datetime.strptime(end, '%Y-%m-%d')
    except ValueError:
        return jsonify({"error": "Invalid date format. Use yyyy-mm-dd."}), 400

    try:
        results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
                    filter(Measurement.date >= start).\
                    filter(Measurement.date <= end).all()

        # Check if results are empty
        if not results or results[0] == (None, None, None):
            return jsonify({"error": "No data found for the given date range."}), 404

        # Create a dictionary from the row data
        start_end_tobs = [{ "min_temp": min_temp, "avg_temp": avg_temp, "max_temp": max_temp } for min_temp, avg_temp, max_temp in results]
        return jsonify(start_end_tobs)
    except Exception as e:
        print(e)
        abort(500)

if __name__ == "__main__":
    app.run(debug=True)
