from flask import Flask, send_from_directory

from scripts.fema_data import get_disaster_data, filter_disaster_data

import csv
import random
import os
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)


# Path for main Svelte page
# /return/
@app.route('/')
def hello_world():
    return send_from_directory('svelte/public', 'index.html')


# Path for static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
def svelte_client(path):
    return send_from_directory('svelte/public', path)


# Path for main Svelte page
@app.route('/')
def hello_world():
    states = open('50States.csv')
    states = open('50States.csv', encoding='UTF8')
    states_reader = csv.reader(states)
    states_dict={}
    for line in states_reader:
        states_dict.update({line[0]:[]})
    states.close()

    counties = open('uscounties.csv')
    counties = open('uscounties.csv', encoding='UTF8')
    counties_reader = csv.reader(counties)
    for line in counties_reader:
        states_dict.get(line[1]).append(line[0])
    counties.close()

    {states_dict[i].sort(): states_dict[i] for i in list(states_dict.keys())}
    
    return send_from_directory('svelte/public', 'index.html')


@app.route('/search/<state>/<county>/<start_year>/<start_month>/<end_year>/<end_month>', methods=["GET"])
def get_disaster_info(state, county, start_year, start_month, end_year, end_month):
    data = get_disaster_data(state, county, start_year, start_month, end_year, end_month)

    return filter_disaster_data(data) # returns a JSON object


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
    app.run()
