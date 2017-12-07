# -*- coding: UTF-8 -*-
'''
@author: rafex
'''
from nabix import auth
from nabix import nabix
from nabix.vars import *
from nabix.User import *
from flask import abort, request, jsonify, g

@auth.verify_password
def verify_password(username_or_token, password):
    # first try to authenticate by token
    user = User.verify_auth_token(username_or_token)
    if not user:
        # try to authenticate with username/password
        user = User.query.filter_by(username=username_or_token).first()
        if not user or not user.verify_password(password):
            return False
    g.user = user
    return True

@nabix.route('/api/users', methods=[POST])
def new_user():
    username = request.json.get('username')
    password = request.json.get('password')
    if username is None or password is None:
        abort(500)    # missing arguments
    if User.query.filter_by(username=username).first() is not None:
        return (jsonify({'username': username}), 201)
    user = User(username=username)
    user.hash_password(password)
    data_base.session.add(user)
    data_base.session.commit()
    return (jsonify({'username': user.username, "id": user.id}), 201)

@nabix.route('/api/users/<int:id>', methods=[GET])
@auth.login_required
def get_user(id):
    user = User.query.get(id)
    if not user:
        abort(400)
    return jsonify({'username': user.username})

@nabix.route('/api/token', methods=[GET])
@auth.login_required
def get_auth_token():
    token = g.user.generate_auth_token(600)
    return jsonify({'token': token.decode('ascii'), 'duration': 600})

@nabix.route('/api/resource' , methods=[GET])
@auth.login_required
def get_resource():
    return jsonify({'data': 'Hello, %s!' % g.user.username})