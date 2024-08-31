# sqlalchemy-challenge
![neora-aylon-5jErKxqb-Dk-unsplash](https://github.com/user-attachments/assets/4c1deed6-7b5a-457b-a375-dca1eb81cc00)
Photo by <a href="https://unsplash.com/@loveneora?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Neora Aylon</a> on <a href="https://unsplash.com/photos/palm-trees-facing-the-sea-5jErKxqb-Dk?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>
  


<h1>Module 10 Challenge</h1>

<h2>Instructions</h2>
Congratulations! You've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii. To help with your trip planning, you decide to do a climate analysis about the area. The following sections outline the steps that you need to take to accomplish this task.

<h3>Part 1: Analyze and Explore the Climate Data</h3>
In this section, you’ll use Python and SQLAlchemy to do a basic climate analysis and data exploration of your climate database. Specifically, you’ll use SQLAlchemy ORM queries, Pandas, and Matplotlib. To do so, complete the following steps:
<br>

1.) Note that you’ll use the provided files (climate_starter.ipynb and hawaii.sqlite) to complete your climate analysis and data exploration.

2.) Use the SQLAlchemy create_engine() function to connect to your SQLite database.

3.) Use the SQLAlchemy automap_base() function to reflect your tables into classes, and then save references to the classes named station and measurement.

4.) Link Python to the database by creating a SQLAlchemy session.

5.) Perform a precipitation analysis and then a station analysis by completing the steps in the following two subsections.
<br>
<h4> Precipitation Analysis </h4>
<br>

1.) Find the most recent date in the dataset.
<br>

2.) Using that date, get the previous 12 months of precipitation data by querying the previous 12 months of data.

3.) Select only the "date" and "prcp" values.

4.) Load the query results into a Pandas DataFrame. Explicitly set the column names.

5.) Sort the DataFrame values by "date".

6.) Plot the results by using the DataFrame plot method, as the following image shows:

![image](https://github.com/user-attachments/assets/8a5ac72b-bb06-45f2-bea8-df756a2e1951)



7.) Use Pandas to print the summary statistics for the precipitation data.


<h4>Station Analysis</h4>
1.) Design a query to calculate the total number of stations in the dataset.


2.) Design a query to find the most-active stations (that is, the stations that have the most rows). To do so, complete the following steps:

      - List the stations and observation counts in descending order.
      
      - Answer the following question: which station id has the greatest number of observations?

3.) Design a query that calculates the lowest, highest, and average temperatures that filters on the most-active station id found in the previous query.

4.) Design a query to get the previous 12 months of temperature observation (TOBS) data. To do so, complete the following steps:

      - Filter by the station that has the greatest number of observations.

      - Query the previous 12 months of TOBS data for that station.

      - Plot the results as a histogram with bins=12, as the following image shows:
      
![image](https://github.com/user-attachments/assets/bdfda6ff-22d6-4964-bed9-fa147bba6cf0)

5.) Close your session.

<h3>Part 2: Design Your Climate App</h3>
Now that you’ve completed your initial analysis, you’ll design a Flask API based on the queries that you just developed. To do so, use Flask to create your routes as follows:
<br>
1.) /

      - Start at the homepage.

      - List all the available routes.

2.) /api/v1.0/precipitation

      - Convert the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data) to a             dictionary using date as the key and prcp as the value.

      - Return the JSON representation of your dictionary.

3.) /api/v1.0/stations

      - Return a JSON list of stations from the dataset.
      
4.) /api/v1.0/tobs

      - Query the dates and temperature observations of the most-active station for the previous year of data.

      - Return a JSON list of temperature observations for the previous year.

5.) /api/v1.0/<start> and /api/v1.0/<start>/<end>

      - Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified         start or start-end range.

      - For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.

      - For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the            end date, inclusive.





<h5>References</h5>
Menne, M.J., I. Durre, R.S. Vose, B.E. Gleason, and T.G. Houston, 2012: An overview of the Global Historical Climatology Network-Daily Database. Journal of Atmospheric and Oceanic Technology, 29, 897-910, https://journals.ametsoc.org/view/journals/atot/29/7/jtech-d-11-00103_1.xmlLinks to an external site.






