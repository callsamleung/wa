# -*- coding:utf-8 -*-

from wa.plugin import PluginInterface

from .index import index

class PluginImpl(PluginInterface):
    def __init__(self, config):
        PluginInterface.__init__(self, config)

    def blueprints(self):
        return [
                (index, {'url_prefix':'/index'}),

                ]

    def index_blueprint(self):
        return (index, {})

    def admin_blueprint(self):
        return (index, {'url_prefix':'/admin'})

