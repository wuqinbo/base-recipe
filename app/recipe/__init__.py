# -*- coding:utf8 -*-

from flask import Blueprint
from flask_restplus import Api,  fields


recipe_blueprint = Blueprint('recipe', __name__, url_prefix='/api/v1.0')

authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'X-API-KEY'
    }
}
api = Api(recipe_blueprint,
    authorizations=authorizations,
    security='apikey',
    title ='Recipe Common API',
    version='1.0',
    description='Is Restful Interface for NutriHealth MVP ...'
)
ns = api.namespace('recipe',description='recipe operations')

Recipe= api.model('Recipe',{
    'Recipeid':fields.String(required=True, description='The recipe ID')
})

from . import recipeApi

