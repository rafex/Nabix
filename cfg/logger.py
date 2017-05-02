# -*- coding: UTF-8 -*-
'''
Created on 28/02/2017

@author: raul
'''
import logging

from logging.handlers import RotatingFileHandler

from .__init__ import get
from .__init__ import getInt

PATH_LOG = get("logger","path")
BACKUP_COUNT_LOG = getInt("logger","backup_count")
MAX_BYTES_LOG = getInt("logger","max_size_file")

def logRotatingFile(name, level):
    logger = logging.getLogger(name)
    if level is not None:
        logger.setLevel(level)
    try:
        file_handler = RotatingFileHandler(PATH_LOG + name, maxBytes=MAX_BYTES_LOG,backupCount=BACKUP_COUNT_LOG)
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    except IOError, e:
        print "no se puede crear el fichero de log"
    return logger

logger_response = logRotatingFile('response.log',logging.INFO)
logger_request = logRotatingFile('request.log',logging.INFO)
logger_error = logRotatingFile('error.log',logging.ERROR)
logger_database = logRotatingFile('postgres.log',logging.ERROR)
logger_debug = logRotatingFile('debug.log',logging.DEBUG)
logger_exception = logRotatingFile(name='exception.log',level=logging.ERROR)

