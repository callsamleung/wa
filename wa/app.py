# -*- coding: utf-8 -*-

from flask import Flask

from .pluginhelper import PluginFinder

class App(Flask):
    def __init__(self, *a, **kw):
        Flask.__init__(self, *a, **kw)
    
    def init_plugins(self):
        pf = PluginFinder(group='wa.plugin')
        # install plugins
        self._plugins = []
        for prj, plugin in self.config['WA_PLUGINS']:
            plg = self._install_plugin(pf, prj, plugin)
            for bp, reg_args in plg.blueprints():
                self.register_blueprint(bp, **reg_args)
        # install LOGSSS index plugin
        if self.config['WA_LOGSSS_INDEX_PLUGIN']:
            plg = self._install_plugin(pf, *self.config['WA_LOGSSS_INDEX_PLUGIN'])
            bp, reg_args = plg.index_blueprint()
            self.register_blueprint(bp, **reg_args)
            print 'sssssssssssssssssssssssssssssssssss'
        # install LOGSSS admin plugin
        if self.config['WA_LOGSSS_ADMIN_PLUGIN']:
            plg = self._install_plugin(pf, *self.config['WA_LOGSSS_ADMIN_PLUGIN'])
            bp, reg_args = plg.admin_blueprint()
            self.register_blueprint(bp, **reg_args)
        # install index plugin
        if self.config['WA_INDEX_PLUGIN']:
            plg = self._install_plugin(pf, *self.config['WA_INDEX_PLUGIN'])
            bp, reg_args = plg.index_blueprint()
            self.register_blueprint(bp, **reg_args)
        # install admin plugin
        if self.config['WA_ADMIN_PLUGIN']:
            plg = self._install_plugin(pf, *self.config['WA_ADMIN_PLUGIN'])
            bp, reg_args = plg.admin_blueprint()
            self.register_blueprint(bp, **reg_args)
            print 'ssssssssssssssssssssss222222222222222222222'
       
    def _install_plugin(self, pf, prj, plugin=None):
        plugin_class = pf.plugin(prj, plugin)
        if not plugin_class:
            print 'Plugin(%s) is not found in project(%s).'%(plugin, prj)
            return
        plg = plugin_class(self.config)
        self._plugins.append(plg)
        return plg

