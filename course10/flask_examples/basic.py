from flask import Flask
from werkzeug.routing import BaseConverter
app = Flask(__name__)


@app.route('/')
def home():
    return 'hello world!'



if __name__ == '__main__':
    app.run()




















# @app.route('/<user>')
# @app.route('/<path:user_name>')
# def username(user):
#     return 'hello, user: ' + user