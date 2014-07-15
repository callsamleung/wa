#coding:utf-8
from flask import Blueprint, render_template, abort
from .view_logsss import Logsss

v_logsss  = Logsss()

lgs_index = Blueprint('lgs_index', __name__, template_folder = 'templates')

@lgs_index.route('/l', defaults = {'tags': None})
@lgs_index.route('/l/<tags>')
def index(tags):
    if tags:
        content_items = v_logsss.get_recorders_with(tags)[:5]
    else:
        content_items = v_logsss.get_recorders()[:5]
    return render_template('lgs_index.html', content_items = content_items)
