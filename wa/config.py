# -*- coding: utf-8 -*-

import os

class BaseConfig(object):

    PROJECT = "caihui.official"

    PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

    DEBUG = True
    TESTING = False

    ADMINS = ['daqing15@gmail.com']

    # http://flask.pocoo.org/docs/quickstart/#sessions
    SECRET_KEY = 'test key'

    # Fild upload, should override in production.
    # Limited the maximum allowed payload to 16 megabytes.
    # http://flask.pocoo.org/docs/patterns/fileuploads/#improving-uploads
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
    #UPLOAD_FOLDER = os.path.join(PROJECT_ROOT, 'uploads')
    #make_dir(UPLOAD_FOLDER)


class DefaultConfig(BaseConfig):

    DEBUG = True

    # Flask-babel: http://pythonhosted.org/Flask-Babel/
    ACCEPT_LANGUAGES = ['zh']


    # Flask-cache: http://pythonhosted.org/Flask-Cache/
    CACHE_TYPE = 'simple'
    CACHE_DEFAULT_TIMEOUT = 60

    # Flask-mail: http://pythonhosted.org/flask-mail/
    # https://bitbucket.org/danjac/flask-mail/issue/3/problem-with-gmails-smtp-server
    MAIL_DEBUG = False
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    # Should put MAIL_USERNAME and MAIL_PASSWORD in production under instance folder.
    MAIL_USERNAME = 'daqing15'
    MAIL_PASSWORD = 'daqing1221'
    DEFAULT_MAIL_SENDER = '%s@gmail.com' % MAIL_USERNAME


class TestConfig(BaseConfig):
    TESTING = True
    CSRF_ENABLED = False

    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
