# -*- coding: UTF-8 -*-
'''
@author: rafex
'''
PATH = '/api/services/'
GET = 'GET'
POST = 'POST'
PUT = 'PUT'
OPTIONS = 'OPTIONS'
DELETE = 'DELETE'
CONTENT_TYPE = 'Content-Type'
APPLICATION_JSON = 'application/json'
APPLICATION_OCTET = 'application/octet-stream'
TEXT_PLAIN = 'text/plain'

CODE_HTTP_ERROR = 500
CODE_HTTP_OK = 200

JSON_RESPONSE_ERROR = {
                "response": {
                    "status": "ERROR",
                    }
                }

JSON_RESPONSE_ERROR_WITH_MESSAGE = {
                "response": {
                    "status": "ERROR",
                    "message": "{message}"
                    }
                }

JSON_RESPONSE_SUCCESS = {
                "response": {
                    "status": "SUCCESS",
                    "message": "{message}"
                    }
                }


def success(message):
    JSON_RESPONSE_SUCCESS["response"]["message"] = None
    JSON_RESPONSE_SUCCESS["response"]["message"] = message
    return JSON_RESPONSE_SUCCESS
