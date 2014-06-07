# -*- coding:utf-8 -*-

import pkg_resources

class PluginFinder(object):
    def __init__(self, group, name=None):
        self._group = group
        self._name = name

    def all_plugins(self, filter=None):
        if filter:
            for i in pkg_resources.iter_entry_points(self._group, self._name):
                if filter(i):
                    yield i.load()
        else:
            for i in pkg_resources.iter_entry_points(self._group, self._name):
                yield i.load()

    def plugin(self, prj):
        return pkg_resource.load_entry_point(prj, self._group, self._name)

