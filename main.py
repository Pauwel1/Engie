from flask import Flask, request, jsonify
import json
import os

from utils.calculation import Calculator
from utils.getParams import cleanData
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route("/", methods = ["GET"])
def check():
  return "Alive!"


@app.route("/payload/", methods = ["POST"])
def get_response():
    data = request.get_data()

    toSplit = request.get_json(data)

    load, fuels, plant = cleanData.separate_data(toSplit)

    response = Calculator.create_new_df(load, fuels, plant)
    
    return response


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host = "0.0.0.0", port = port, threaded = True)

