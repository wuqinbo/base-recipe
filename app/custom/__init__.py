# -*- coding:utf8 -*-

from flask import Blueprint


recipe2_blueprint = Blueprint('custom', __name__, url_prefix='/api/v2.0')


from . import customApi