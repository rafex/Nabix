# -*- coding: UTF-8 -*-
from flask import Flask
import os

from flask_cors import CORS, cross_origin


app = Flask(__name__)
CORS(app)

#app.secret_key = 'F12Zr47j\3yX R~X@H!jmM]Lwf/,?KT'
app.secret_key = os.urandom(24)

from panel import views
