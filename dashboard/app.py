"""
    Created by BarathM at 05/01/23
"""
import uuid

import requests
from flask import Flask, make_response

__author__ = "BarathM"
random_id = uuid.uuid4()

app = Flask(__name__)


@app.route("/dashboard/", methods=["POST", "GET"])
def index():
    return make_response({"msg": f"Hello From DashBoard - {random_id}"})


@app.route("/dashboard/internal", methods=["GET"])
def internal():
    return make_response({"msg": f"Hello from Dashboard app - {random_id}"})


@app.route("/dashboard/call_user", methods=["POST"])
def call_dashboard():
    response = requests.get("http://user-service:80/user/internal")
    return make_response(response.json())


if __name__ == "__main__":
    app.run(debug=True)
