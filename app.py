from flask import Flask
from unlock_secrets import all_the_shit

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
