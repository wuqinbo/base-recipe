# -*- coding:utf8 -*-

from flask import request, jsonify

from . import recipe2_blueprint as recipe
from app.exts import auth
from flask import current_app


#菜谱api
@recipe.route("/test", methods=['GET'])
@auth.login_required
def recipe_first():
    current_app.logger.debug("welcome")
    return "haha"


@recipe.route("/", methods=['GET'])
def hello_world():
    current_app.logger.debug("recipe debug")
    return "hello"