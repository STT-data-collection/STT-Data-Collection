import os
import json
import logging
from flask import Flask, app, request
from flask_cors import CORS, cross_origin
import numpy as np


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
    return json.dumps({"result": "This is home"}, default=convert)

@app.route("/get-text", methods=["GET"])
def text_getter():
    return json.dumps({"result": "This is response text"}, default=convert)

@app.route("/send-audio", methods=["POST", "GET"])
def file_getter():
    if request.method == "POST":
        try:
            file = request.files["file"]
            print(file)
           
            return json.dumps(
                {"success": "File Uploaded Successfully"}, default=convert
            )
            
        except Exception as e:
            print(e)
            return json.dumps(
                {"error": "Couldn't handle uploaded file. "}, default=convert
            )
    else:
        print("error")
        return json.dumps({"error": "No POST Data"}, default=convert)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
