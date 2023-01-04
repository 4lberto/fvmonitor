#!/bin/bash


echo "*** Open your browser and use:"
echo "- http://localhost:80/hello"
echo "- http://localhost:80/"



echo "Starting FLASK server"
export FLASK_ENV=development
FLASK_APP=run.py pipenv run flask run --host 0.0.0.0 --port 80


