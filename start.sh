#!/bin/bash
export FLASK_APP=masono.py
flask initdb
flask run
