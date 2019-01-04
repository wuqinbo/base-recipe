# -*- coding:utf8 -*-

from app import auth
from app.models import UserList


@auth.get_password
def get_password(username):
    if username == 'ok':
        return 'python'
    return None

# @auth.get_password
# def get_password(username):
#     user = UserList.objects(username=username).first()
#     if user.username:
#         return user.password
#     return None


# users = UserList.objects().all()
# users = [ {'username': 'ok', 'password': 'python'}]
# @auth.get_password
# def get_password(username):
#     print(username)
#     for user in users:
#         if user['username'] == username:
#             return user['password']
#     return None

# @auth.error_handler
# def unauthorized():
#     return 'Unauthorized access'