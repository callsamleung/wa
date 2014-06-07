# -*- coding: utf-8 -*-

from flask import Flask

from .pluginhelper import PluginFinder

class App(Flask):
    def __init__(self, *a, **kw):
        Flask.__init__(self, *a, **kw)
    
    def init(self):
        pf = PluginFinder(group='wa.plugin')
        self._plugins = []
        for i in pf.all_plugins():
            print 'get plugin:', i
            self._plugins.append(i)

