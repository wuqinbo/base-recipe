# -*- coding: utf-8 -*-

import json
import requests
from urllib.parse import urljoin, urlparse
import unittest

BASE_URL = 'http://127.0.0.1:5000'
AUTH = ('admin', 'admin')

class FunctionTest(unittest.TestCase):
    def test_get_user_list(self):
        rsp = requests.get(urljoin(BASE_URL, '/api/v1.0/recipe/'), auth=AUTH, headers={
            'Accept': 'application/json'
        })
        print (rsp.content)


    def test_post_user_list(self):
        json_data = dict(
            title='zhangsan',
            code='oo',
            linenos='true'
        )
        rsp = requests.post(urljoin(BASE_URL, '/api/v1.0/recipe/'), auth=AUTH, headers={
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }, data=json.dumps(json_data))
        return rsp


    def test_get_user(self):
        rsp = requests.get(urljoin(BASE_URL, '/api/v1.0/recipe/test'), auth=AUTH, headers={
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        })
        print(rsp.json()['Recipeid'])


    def test_put_user(self):
        json_data = dict(
            title='zhangsan',
            code='oo',
            linenos='true'
        )
        # 注意最后的 /
        rsp = requests.put(urljoin(BASE_URL, '/api/v1.0/recipe/'), auth=AUTH, headers={
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }, data=json.dumps(json_data),
                           )
        return rsp


    def test_patch_user(self):
        json_data = dict(
            title='aaaaaaaaaaaaaaaaaaaa',
        )
        rsp = requests.patch(urljoin(BASE_URL, '/api/v1.0/recipe/test'), auth=AUTH, headers={
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }, data=json.dumps(json_data),
                             )
        print (rsp.text)