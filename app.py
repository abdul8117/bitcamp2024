import csv

from flask import Flask, send_from_directory
app = Flask(__name__)

# Serve Svelte apps
@app.route("/<path:path>")
def svelte_client(path):
    return send_from_directory('../svelte/public/', path)

@app.route('/')
def hello_world():
    f = open('uscounties.csv')
    f = open('uscounties.csv', encoding='UTF8')
    csv_reader = csv.reader(f)
    for line in csv_reader:
        print(line)
    f.close()  
    return 'Hello from Flask!'

if __name__ == '__main__':
    app.run()

from flask import Flask

app = Flask(__name__)
