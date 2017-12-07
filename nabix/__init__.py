# -*- coding: UTF-8 -*-
'''
@author: rafex
'''

import os
from flask import Flask
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth
from cfg import get

def create_app():
    app = Flask(__name__)
    CORS(app)
    #app.secret_key = os.urandom(24)
    app.secret_key = get('nabix','sk')
    return app

def create_db(db_path,app):
    db_uri = 'sqlite:///{}'.format(db_path)
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    db = SQLAlchemy(app)
    return db

nabix = create_app()
data_base = create_db(os.path.join(os.path.dirname(__file__), 'nabix.db'), nabix)
auth = HTTPBasicAuth()

from api import *
