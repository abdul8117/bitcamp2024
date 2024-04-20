import csv
import random
from flask import Flask, send_from_directory

app = Flask(__name__)


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


# Path for static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
def svelte_client(path):
    return send_from_directory('svelte/public', path)


# Function for testing Svelte requests to flask backend
# Generates a random number
@app.route("/rand")
def hello():
    return str(random.randint(0, 100))

if __name__ == '__main__':
    app.run()
