from flask import jsonify, request
import json

import pandas as pd
import numpy as np

class Calculator:
    def __init__(self):
        self = self

    def algo(load, plants):
        counter = load
        plants = plants.sort_values(by = ["per_unit"], ascending = True, na_position = "first")



        return plants
        # Devide load over x pmax, giving priotity to lowest prodcost and the lowest pmin
        # So: calculate prodcost of polluters and calculate max output of windparks

        # polluters: 
        # polluters:

        # windparks: pmax * (100/p)