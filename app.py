import random


from flask import Flask, send_from_directory

# Serve Svelte apps
@app.routes("/<path:path>")
def svelte_client(path):
    return send_from_directory('../svelte/public/', path)


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello from Flask!'


@app.route('/rand')
def get_random_number():
    return str(random.randint(0, 100))


if __name__ == '__main__':
    app.run()
