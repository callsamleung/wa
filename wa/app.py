# -*- coding: utf-8 -*-

import os

from flask import Flask, request, render_template,current_app
#from flaskext.babel import Babel

from .config import DefaultConfig
from .frontend import frontend
from .panel import admin
from .extensions import mail, db
from .panel.models import Category
from caihui.official.utils import filter_tags, filter_style, filter_html,\
    filter_category_id


# For import *
__all__ = ['create_app']

DEFAULT_BLUEPRINTS = (
    frontend,
    admin,
)

def create_app(config_file=None, app_name=None, blueprints=None):
    """Create a Flask app."""

    if app_name is None:
        app_name = DefaultConfig.PROJECT
    if blueprints is None:
        blueprints = DEFAULT_BLUEPRINTS
    app = Flask(app_name, instance_relative_config=True)
    app.config.from_pyfile(config_file)
    configure_email(app)
    configure_hook(app)
    configure_blueprints(app, blueprints)
    configure_extensions(app)
    configure_logging(app)
    configure_template_filters(app)
    configure_error_handlers(app)

    db.init_app(app)
    db.create_all(app=app)

    configure_categorys(db, app)

    return app

def configure_categorys(db, app):
    cates = {}
    news_cate = {}
    for cate in Category.query.filter(Category.parent_id==0).order_by(db.desc(Category.order)).all():
        news_cate[cate.id] = cate.name
        cates[cate.id] = cate.name
#        news_cate[cate.id] = cate.name
#        if cate.parent_id in cates:
#            cates[cate.parent_id].append((cate.id, cate.name, cate.code))
#        else:
#            cates[cate.parent_id] = [(cate.id, cate.name, cate.code)]
    app.config['cates'] = cates
    app.config['news_cate'] = news_cate


def configure_email(app):
    # email server user gmail
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False
    # Should put MAIL_USERNAME and MAIL_PASSWORD in production under instance folder.
    app.config['MAIL_USERNAME'] = 'daqing15'
    app.config['MAIL_PASSWORD'] = 'daqing1221'
    app.config['DEFAULT_MAIL_SENDER'] = 'daqing15@gmail.com'


def configure_app(app, config=None):
    """Different ways of configurations."""

    # http://flask.pocoo.org/docs/api/#configuration
    app.config.from_object(DefaultConfig)

    # http://flask.pocoo.org/docs/config/#instance-folders
    app.config.from_pyfile('production.cfg', silent=True)

    if config:
        app.config.from_object(config)

    # Use instance folder instead of env variables to make deployment easier.
    #app.config.from_envvar('%s_APP_CONFIG' % DefaultConfig.PROJECT.upper(), silent=True)


def configure_extensions(app):

    # flask-mail
    mail.init_app(app)

    # flask-babel


def configure_blueprints(app, blueprints):
    """Configure blueprints in views."""

    for blueprint in blueprints:
        app.register_blueprint(blueprint)


def configure_template_filters(app):
    app.add_template_filter(filter_tags)
    app.add_template_filter(filter_style)
    app.add_template_filter(filter_html)
    app.add_template_filter(filter_category_id)
    @app.template_filter()
    def pretty_date(value):
        return pretty_date(value)

    @app.template_filter()
    def format_date(value, format='%Y-%m-%d'):
        return value.strftime(format)
    
    @app.template_filter()
    def format_category_id(value):
        cate=Category.query.get_or_404(value)
        return cate.name
    
    @app.context_processor
    def navs():
        nav_js = Category.query.filter(Category.is_nav_menu == 0).order_by(db.desc(Category.order)).all()
        return dict(categorys=nav_js)

    @app.context_processor
    def categorys():
        cate_list = Category.query.order_by(db.desc(Category.order)).all()
        return dict(cate_list=cate_list)

    @app.context_processor
    def site():
        from .panel.models import SiteConfig
        site = SiteConfig.query.order_by(db.desc(SiteConfig.id)).first()
        return dict(site=site)

def configure_logging(app):
    """Configure file(info) and email(error) logging."""

    if app.debug or app.testing:
        # Skip debug and test mode. Just check standard output.
        return

    import logging
    from logging.handlers import SMTPHandler

    # Set info level on logger, which might be overwritten by handers.
    # Suppress DEBUG messages.
    app.logger.setLevel(logging.INFO)

    info_log = os.path.join(app.config['LOG_FOLDER'], 'info.log')
    info_file_handler = logging.handlers.RotatingFileHandler(info_log, maxBytes=100000, backupCount=10)
    info_file_handler.setLevel(logging.INFO)
    info_file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s '
        '[in %(pathname)s:%(lineno)d]')
    )
    app.logger.addHandler(info_file_handler)

    # Testing

    mail_handler = SMTPHandler(app.config['MAIL_SERVER'],
                               app.config['MAIL_USERNAME'],
                               app.config['ADMINS'],
                               'O_ops... %s failed!' % app.config['PROJECT'],
                               (app.config['MAIL_USERNAME'],
                                app.config['MAIL_PASSWORD']))
    mail_handler.setLevel(logging.ERROR)
    mail_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s '
        '[in %(pathname)s:%(lineno)d]')
    )
    app.logger.addHandler(mail_handler)


def configure_hook(app):
    @app.before_request
    def before_request():
        pass


def configure_error_handlers(app):

    @app.errorhandler(403)
    def forbidden_page(error):
        return render_template("errors/forbidden_page.html"), 403

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("errors/page_not_found.html"), 404

    @app.errorhandler(500)
    def server_error_page(error):
        return render_template("errors/server_error.html"), 500
