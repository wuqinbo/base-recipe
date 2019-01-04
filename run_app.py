# -*- coding: utf-8 -*-

import os
import traceback
from app import create_app
from flask import send_from_directory, request, json, current_app, jsonify


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
#
# @app.route('/static/<path:path>')
# def send_resources(path):
#     # return 'tt'
#     return send_from_directory('static', path)

# 在第一次请求之前调用，可以在此方法内部做一些初始化操作
@app.before_first_request
def before_first_request():
    print("before_first_request")


@app.before_request
def before_request():
    pass


if __name__ == '__main__':
    app.run(debug=True)
