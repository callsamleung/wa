# -*- coding:utf-8 -*-
import sys

from .plugin import PluginInterface
from .app import App

__version__ = (0, 1, 0, 'dev', 0)
__all__ = ('PluginInterface',
        'create_app',
        )

def create_app(config_file):
    app = App(__name__)
    app.config.from_pyfile(config_file)
    app.init_plugins()
    return app

