#!env/bin/python
# -*- coding: UTF-8 -*-
'''
@author: rafex
'''
from cfg import get
from cfg import getInt
from cfg import getBoolean
import netifaces as ni
from nabix import app

INTERFACE = get("server","interface")
PORT = getInt("server","port")
DEBUG = getBoolean("server","debug")

ni.ifaddresses(INTERFACE)
IP = ni.ifaddresses(INTERFACE)[2][0]['addr']

if __name__ == '__main__':
    app.run(host=IP, port=PORT, debug=DEBUG)
