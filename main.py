import flask
import config

server = flask.Flask(__name__)

from routes import *

if __name__ == '__main__':
    server.run(host=config.HOST, port=config.PORT, debug=config.DEBUG_MODE)
    print("Loading...")