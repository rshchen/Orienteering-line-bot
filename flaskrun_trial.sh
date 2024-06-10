#!/bin/bash
export FLASK_APP=$1.py
export FLASK_DEBUG=on
flask run --port $2
