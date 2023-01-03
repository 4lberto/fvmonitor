#!/bin/bash


echo "Open your browser and use:"
echo "http://localhost:5000/hello"



echo "Starting FLASK server"
export FLASK_ENV=development
FLASK_APP=run.py pipenv run flask run


