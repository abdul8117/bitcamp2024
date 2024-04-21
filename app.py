import sqlite3
import json
from flask import Flask, send_from_directory, session
from flask_session import Session
from scripts.fema_data import get_disaster_data, filter_disaster_data
import random
import os
from dotenv import load_dotenv
from scripts.county_latlng_data import lat_lng


load_dotenv()

app = Flask(__name__)

# Session config
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["SESSION_COOKIE_PATH"] = "/"
Session(app)

# Path for static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
def svelte_client(path):
    return send_from_directory('svelte/public', path)

# Path for main Svelte page
# /return/
@app.route('/')
def hello_world():
    return send_from_directory('svelte/public', 'index.html')

@app.route('/search/<state>/<county>/<disaster_year>/<disaster_month>', methods=["GET"])
def get_housing_data(state, county, disaster_year, disaster_month):
    # session["disaster_info"]["state"] = state
    # session["disaster_info"]["county"] = county
    # session["disaster_info"]["disaster_year"] = disaster_year
    # session["disaster_info"]["disaster_month"] = disaster_month

    connection = sqlite3.connect("api-testing-20240420T161852Z-001/db/house_prices_monthly.db")
    cursor = connection.cursor()

    county=county+" County"
    disaster_year=int(disaster_year)
    start_year=disaster_year-1
    disaster_month=int(disaster_month)
    start_month=disaster_month-12
    query = "SELECT\n"
    for i in range(start_month-1,disaster_month+13):
        query+="Y"+str(start_year)+"M"+str(i%12+1)+",\n"
        if((i%12+1)==12):
            start_year+=1
    query+="state,\n"
    query+="county_name\n"
    query+="FROM\n"
    query+="data\n"
    query+="WHERE\n"
    query+="county_name = '"+county+"'\n"
    query+="AND state = '"+state+"'\n"
    query+="AND Y2000M1 !='';"
    results = cursor.execute(query).fetchall()

    results[0]=results[0][0:25]
    start_year=disaster_year-1
    json_list=[]
    running=0
    for i in range(start_month-1,disaster_month+12):
        json_list.append(
            {'month':(i%12+1),
             'year':start_year,
             'housing_cost':results[0][running]
             })
        if((i%12+1)==12):
            start_year+=1
        if(i<19):
            running+=1
    json_list=json.dumps(json_list)
    # print(json_list)
    
    connection.close()
    
    return json_list # returns a JSON object

# Path for main Svelte page
# @app.route('/')
# def hello_world():
#     states = open('50States.csv')
#     states = open('50States.csv', encoding='UTF8')
#     states_reader = csv.reader(states)
#     states_dict={}
#     for line in states_reader:
#         states_dict.update({line[0]:[]})
#     states.close()

#     counties = open('uscounties.csv')
#     counties = open('uscounties.csv', encoding='UTF8')
#     counties_reader = csv.reader(counties)
#     for line in counties_reader:
#         states_dict.get(line[1]).append(line[0])
#     counties.close()

#     {states_dict[i].sort(): states_dict[i] for i in list(states_dict.keys())}
    
#     return send_from_directory('svelte/public', 'index.html')


@app.route('/search/<state>/<county>/<start_year>/<start_month>/<end_year>/<end_month>', methods=["GET"])
def get_disaster_info(state, county, start_year, start_month, end_year, end_month):
    data = get_disaster_data(state, county, start_year, start_month, end_year, end_month)

    return filter_disaster_data(data) # returns a JSON object


@app.route('/latlng/<fips>')
def get_lat_lng(fips):
    return lat_lng(fips)


# Function for testing Svelte requests to flask backend
# Generates a random number
@app.route("/rand")
def hello():
    return str(random.randint(0, 100))


# Function that retrieves API key for client
@app.route("/key")
def get_key():
    return os.getenv('API_KEY')


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8000, debug=False)
