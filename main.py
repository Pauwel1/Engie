from flask import Flask, request, jsonify
import os
from flask_cors import CORS

from utils.getParams import CleanData
from utils.calculation import algo


app = Flask(__name__)
CORS(app)


@app.route("/", methods = ["GET"])
def check():
  return "Alive!"


@app.route("/payload/", methods = ["POST"])
def get_response():
    ### Collect the data and split them in separate df's ...
    toSplit = request.get_json()

    load, fuels, plants = CleanData.separate_data(toSplit)

    ### ... and organize/clean them:
    # take the conditions price and average wind strength into account
    plants = CleanData.conditions(fuels, plants)
    plants["per_unit"] = CleanData.formula_p(plants)
    # recalculate the pmax for the wind turbines
    plants = CleanData.variabel_pmax(plants)

    ### Next step: doing the calculations
    plants = plants.sort_values(by = ["per_unit"], ascending = True)
    response = algo(load, plants)

    return response



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host = "0.0.0.0", port = port, threaded = True)

