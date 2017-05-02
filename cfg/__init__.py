# -*- coding: UTF-8 -*-
'''
@author: rafex
'''
import ConfigParser

from ConfigParser import NoOptionError
#from .logger import logger_exception

cfg = ConfigParser.ConfigParser()

if not cfg.read("config.cfg"):
    print "No existe el archivo de configuracion"
    
def get(section,option):
    try:
        return cfg.get(section,option)
    except (NoOptionError,Exception), e: 
        print "Error al cargar la section:"
        print section
        print "y option:"
        print option

def getInt(section,option):
    try:
        return cfg.getint(section,option)
    except (NoOptionError,Exception), e: 
        print "Error al cargar la section:"
        print section
        print "y option:"
        print option

def getBoolean(section,option):
    try:
        return cfg.getboolean(section,option)
    except (NoOptionError,Exception), e: 
        print "Error al cargar la section:"
        print section
        print "y option:"
        print option

