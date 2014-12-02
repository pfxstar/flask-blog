# -*- coding: utf-8 -*-

from flask import Flask

from app.settings import DefaultConfig
from app.controllers.admin import bp as admin_web_bp
from app.controllers.web import bp as web_bp
from app.extensions import db


DEFAULT_APP_NAME = 'app'


def create_app(config=None):
    app = Flask(DEFAULT_APP_NAME)

    configure_app(app, config)
    configure_extensions(app)
    configure_blueprints(app)

    return app


def configure_app(app, config):
    if not config:
        config = DefaultConfig

    app.config.from_object(config)


def configure_extensions(app):
    db.app = app
    db.init_app(app)


def configure_blueprints(app):
    app.register_blueprint(admin_web_bp, url_prefix='/admin')
    app.register_blueprint(web_bp, url_prefix='')
