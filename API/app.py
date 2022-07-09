
import json
import logging
from flask import Flask, app, request
from flask_cors import CORS, cross_origin
import numpy as np
from script_logger import App_Logger


# model = pickle.load(open("./api_utils/RFR-sales-02-06-2022-09-19-20.pkl", "rb"))
# scaler = pickle.load(open("./api_utils/scaler-02-06-2022-09-19-20.pkl", "rb"))

app = Flask(__name__)

cors = CORS(app)

@app.after_request
def after_request(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add(
        "Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept"
    )
    response.headers.add("Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS")
    response.headers.add("Access-Control-Allow-Credentials", "true")
    return response


def convert(o):
    if isinstance(o, np.generic):
        return o.item()
    raise TypeError



@app.route("/", methods=["GET"])
def home():
    return json.dumps({"result": "This is some text"}, default=convert)


