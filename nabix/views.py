# -*- coding: UTF-8 -*-
'''
@author: rafex
'''
import uuid

from nabix import app
from flask import request
from flask import session
from flask import redirect

from cfg.logger import logger_request
from cfg.logger import logger_response

@app.route('/')
@app.route('/index')
def index():
    return 'Works!!!'

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


#Manejo de errores

@app.errorhandler(404)
def not_found_error(error):
    return "404 NOT FOUND", 404

@app.errorhandler(500)
def internal_error(error):
    return "500 ERROR", 500