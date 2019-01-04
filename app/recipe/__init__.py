# -*- coding:utf8 -*-

from flask import Blueprint

recipe = Blueprint('recipe', __name__)


from . import recipeApi