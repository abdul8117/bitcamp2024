import random

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello from Flask!'


@app.route('/rand')
def get_random_number():
    return str(random.randint(0, 100))


if __name__ == '__main__':
    app.run()
