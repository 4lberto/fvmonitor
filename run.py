import datetime
import logging

import goodwee_provider
from db.db_prov import get_inverter_log_last_log

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

print(f"LOGGING LEVEL: {logging.getLevelName(logging.getLogger().getEffectiveLevel())}")

import os

log = logging.getLogger(__name__)

from flask import Flask, jsonify, render_template

base_prefix = "/api"

app = Flask(__name__, static_url_path='/static', template_folder='templates', static_folder='static')


# Api Feeds for clients
# app.register_blueprint(api_content, url_prefix=base_prefix)


@app.route("/hello")
def hello():
    return "hello"


@app.route("/")
def status():
    data = get_inverter_log_last_log()
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    data["current_time"] = data["t"]

    return render_template("main.html", data=data)


@app.route("/json")
def status_json():
    data = get_inverter_log_last_log()
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    data["current_time"] = data["t"]

    return jsonify(data), 200
