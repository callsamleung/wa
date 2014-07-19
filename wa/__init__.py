# -*- coding:utf-8 -*-
import sys

from .plugin import PluginInterface
from .app import App

__version__ = (0, 1, 0, 'dev', 0)
__all__ = ('PluginInterface',
        'create_app',
        )

class ConfigClass(object):
    # Configure Flask
    SECRET_KEY = 'THIS IS AN INSECURE SECRET'             # Change this for production!!!
    SQLALCHEMY_DATABASE_URI = 'sqlite:///minimal_app.db'  # Use Sqlite file db
    CSRF_ENABLED = True

def create_app(config_file):
    app = App(__name__)
    #app.config.from_pyfile(config_file)
    app.config.from_object(__name__+'.ConfigClass')
    #app.init_plugins()
    return app

