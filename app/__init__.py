# -*- coding:utf8 -*-

import os
import logging

from logging.config import fileConfig
from flask import Flask
from conf.config import config
from .exts import db,auth
from flasgger import Swagger,swag_from
from app.models import UserList

fileConfig('conf/log-app.conf')

@auth.get_password
def get_password(username):
    user = UserList.objects(username=username).first()
    if user.username:
        return user.password
    return None


def get_logger(name):
    return logging.getLogger(name)


def get_basedir():
    return os.path.abspath(os.path.dirname(__file__))


def get_config():
    return config[os.getenv('FLASK_CONFIG') or 'default']


def create_app(config_name):
    app = Flask(__name__,instance_relative_config=True)
    Swagger(app)
    # logging
    app_logger = logging.getLogger('backend')
    app.logger.handlers.extend(app_logger.handlers)

    gunicorn_error_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers.extend(gunicorn_error_logger.handlers)
    app.logger.setLevel(logging.DEBUG)

    app.config.from_pyfile('config.cfg')
    app.config.from_object(config[config_name])
    db.init_app(app)
    config[config_name].init_app(app)

    from .recipe import recipe as recipe_blueprint
    app.register_blueprint(recipe_blueprint, url_prefix='/api/recipe')

    # 附加路由和自定义的错误页面

    return app

