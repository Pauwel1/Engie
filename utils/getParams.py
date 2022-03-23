import pandas as pd


class CleanData:
    def __init__(self, request):
        self.request = request

    def separate_data(toSplit):
        load = toSplit["load"]
        fuels = pd.DataFrame(toSplit["fuels"].items())
        plants = pd.DataFrame.from_dict(toSplit["powerplants"])

        return load, fuels, plants
    
    def conditions(fuels, plants):
        gp = fuels.iloc[0, 1]
        fp = fuels.iloc[1, 1]
        wp = fuels.iloc[3, 1]
        cost = []
        var = []

        for item in plants["type"]:
            if "gas" in item:
                cost.append(gp)
                var.append(100)
            elif "turbo" in item:
                cost.append(fp)
                var.append(100)
            elif "wind" in item:
                cost.append(0)
                var.append(wp)
        
        plants["cost"] = cost
        plants["var"] = var
        return plants

    def formula_p(plants : pd.DataFrame):
        for item in plants["name"]:
            unitPrice = plants["cost"]
            efficiency = plants["efficiency"]
            p = unitPrice * (1/efficiency)
            return p
    
    def variabel_pmax(plants):
        plants["pmax"] = (plants["pmax"] * plants["var"]) / 100
        plants.drop(["var"], axis = 1, inplace = True)
        return plants
