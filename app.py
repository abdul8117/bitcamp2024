import csv
import random
from flask import Flask, send_from_directory

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


# Function for testing Svelte requests to flask backend
# Generates a random number
@app.route("/rand")
def hello():
    return str(random.randint(0, 100))


if __name__ == '__main__':
    app.run()
