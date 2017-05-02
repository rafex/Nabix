#!env/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 08/02/2017

@author: raúl
'''
from cfg import get
from cfg import getInt
from cfg import getBoolean
import netifaces as ni
from panel import app

INTERFACE = get("server","interface")
PORT = getInt("server","port")
DEBUG = getBoolean("server","debug")

ni.ifaddresses(INTERFACE)
IP = ni.ifaddresses(INTERFACE)[2][0]['addr']

if __name__ == '__main__':
    app.run(host=IP, port=PORT, debug=DEBUG)
