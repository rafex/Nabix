# -*- coding: UTF-8 -*-
'''
Created on 02/03/2017

@author: Raúl
'''
import json
from decimal import Decimal
from datetime import datetime

MESSAGE = " is not JSON serializable"

class number_str(float):
    def __init__(self, obj):
        self.obj = obj
    def __repr__(self):
        return str(self.obj)

def decimal_serializer(obj):
    if isinstance(obj, Decimal):
        return number_str(obj)
    raise TypeError(repr(obj) + MESSAGE)

def date_serializer(obj):
    if isinstance(obj, datetime):
        serial = obj.isoformat()
        return serial
    raise TypeError (repr(obj)+ MESSAGE)