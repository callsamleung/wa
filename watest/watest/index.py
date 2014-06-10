# -*- coding:utf-8 -*-

from flask import Blueprint

index = Blueprint('index', __name__,
        template_folder='templates')

@index.route('/')
def page():
    return '''<html><h1>Hello, WA!</h1></html>'''

