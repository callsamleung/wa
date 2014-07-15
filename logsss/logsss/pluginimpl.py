# -*- coding:utf-8 -*-

from wa.plugin import PluginInterface

from .index2 import index2

class PluginImpl(PluginInterface):
    def __init__(self, config):
        PluginInterface.__init__(self, config)

    def blueprints(self):
        return [
                (index2, {'url_prefix':'/logsss/'}),

                ]

    def index_blueprint(self):
        return (index2, {})

    def admin_blueprint(self):
        return (index2, {'url_prefix':'/logsss/'})

