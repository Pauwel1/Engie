from utils.getParams import CleanData
from utils.calculation import algo


def toApp(toSplit):
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
