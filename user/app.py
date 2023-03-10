"""
    Created by BarathM at 05/01/23
"""
import uuid

import requests
from flask import Flask, make_response

__author__ = "BarathM"
random_id = uuid.uuid4()

app = Flask(__name__)


@app.route("/user/", methods=["POST", "GET"])
def index():
    return make_response({"msg": f"Hello From User - {random_id}"})


@app.route("/user/internal", methods=["GET"])
def internal():
    return make_response({"msg": f"Hello from User app - {random_id}"})


@app.route("/user/call_dashboard", methods=["POST", "GET"])
def call_dashboard():
    response = requests.get("http://dash-service/dashboard/internal")
    return make_response(response.json())


if __name__ == "__main__":
    app.run(debug=True)
