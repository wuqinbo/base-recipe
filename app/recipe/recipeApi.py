# -*- coding:utf8 -*-

from flask import Flask,request, jsonify
from . import ns, api, Recipe
from flask_restplus import Api,  fields, Resource
from app.exts import auth
from flask import current_app

recipes = {
    'r1': {'Recipeid': '12'},
    'r2': {'Recipeid': '23'},
    'r3': {'Recipeid': '34!'},
}

#菜谱api
@ns.route("/test")
class Recipe(Resource):
    @api.doc(responses={404: 'Todo not found'},security='apikey')
    @api.marshal_with(Recipe)
    # @auth.login_required
    def get(self):
        current_app.logger.debug("welcome")
        return recipes['r1']


@ns.route("/")
@api.doc(responses={404: 'Todo not found'}, params={'todo_id': 'The Todo ID'})
class Recipe2(Resource):
    # @api.marshal_with(Recipe)
    def get(self):
        current_app.logger.debug("recipe debug")
        return "hello"
