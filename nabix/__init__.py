# -*- coding: UTF-8 -*-
'''
@author: rafex
'''

import os
import uuid
from flask import request
from flask import session
from flask import redirect
from flask import Flask
from flask_cors import CORS, cross_origin
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.httpauth import HTTPBasicAuth
from passlib.apps import custom_app_context as pwd_context
from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)
from cfg.logger import logger_request
from cfg.logger import logger_response

app = Flask(__name__)
CORS(app)

app.secret_key = os.urandom(24)
db_path = os.path.join(os.path.dirname(__file__), 'app.db')
db_uri = 'sqlite:///{}'.format(db_path)
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://///Users/rafex/job/personal/Nabix/db2.sqlite'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)
auth = HTTPBasicAuth()

def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    
@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    init_db()
    print('Initialized the database.')

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    username = db.Column(db.String(32), index=True, unique=True)
    password_hash = db.Column(db.String(64))
    email = db.Column(db.String(120), index=True, unique=True)

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    def generate_auth_token(self, expiration=600):
        s = Serializer(app.secret_key, expires_in=expiration)
        return s.dumps({'id': self.id})

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(app.secret_key)
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None    # valid token, but expired
        except BadSignature:
            return None    # invalid token
        user = User.query.get(data['id'])
        return user


@app.route('/')
@app.route('/index')
def index():
    return 'Works Nabix 0.1.0!!!'


@app.before_request
def log_request_info():
    uuid_request = uuid.uuid1()
    session['uuid-request'] = uuid_request

    logger_request.info('-----------------------------------------------------------------------------------------------')
    logger_request.info('---- REQUEST ----------------------------------------------------------------------------------')
    logger_request.info('-----------------------------------------------------------------------------------------------')
    logger_request.info('UUID-REQUEST: %s', uuid_request)
    logger_request.info('REMOTE ADDRESS: %s', request.remote_addr)
    logger_request.info('Path: %s', request.path)
    logger_request.info('Method: %s', request.method)
    logger_request.info('Headers: %s', request.headers)
    logger_request.info('Body: %s', request.get_data())
    logger_request.info('-----------------------------------------------------------------------------------------------')
    logger_request.info('-----------------------------------------------------------------------------------------------')
    header_string = ''
    for header in request.headers:
        header_string = header_string + ' '.join(header) + '\n'
#     insert_log_in(request.remote_addr,request.get_data(),request.path,'Middleware',header_string,uuid_request,request.method)


@app.after_request
def after_request(response):
    uuid_request = session['uuid-request']
    logger_response.info('-----------------------------------------------------------------------------------------------')
    logger_response.info('---- RESPONSE ---------------------------------------------------------------------------------')
    logger_response.info('-----------------------------------------------------------------------------------------------')
    logger_response.info('UUID-REQUEST: %s', uuid_request)
    logger_response.info('Status Code: %s', response.status_code)
    logger_response.info('Headers: %s', response.headers)
    logger_response.info('Body: %s', response.get_data())
    logger_response.info('-----------------------------------------------------------------------------------------------')
    logger_response.info('-----------------------------------------------------------------------------------------------')
#     insert_log_out(response.get_data(),uuid_request)
    return response


# Manejo de errores
@app.errorhandler(404)
def not_found_error(error):
    return "404 NOT FOUND", 404


@app.errorhandler(500)
def internal_error(error):
    return "500 ERROR", 500


from views import login
