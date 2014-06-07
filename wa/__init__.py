# -*- coding:utf-8 -*-

import sys

import flask

__version__ = (0, 1, 0, 'dev', 0)

app = None

def create_app(config_file):
    global app
    if app is not None:
        sys.exit('A wa application is already initialized.')
    app = flask.Flask(__name__)
    app.config.from_pyfile(config_file)
    return app
