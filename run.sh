#!/bin/bash
source env/bin/activate
export FLASK_CONFIG=development
export FLASK_APP=server.py
flask run
