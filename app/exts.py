# -*- coding:utf8 -*-

from flask_mongoengine import MongoEngine

db = MongoEngine()

from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()