

def algo(load, plants):
    plants = plants.sort_values(by = ["per_unit"], ascending = True, na_position = "first")

    row = 0
    names = []
    p = []

    battery = plants.iloc[row, :]
    needed = load

    for i in range(len(plants)):
        if i < row:
            row += 1
            rest = needed - battery["pmax"]
            names.append(battery["name"])
            if rest > 0:
                battery["energy_used"] = battery["pmax"]
                p.append(battery["energy_used"])
            elif rest <= 0:
                if -needed > battery["pmin"]:
                    battery["energy_used"] = battery["pmax"] + needed
                    p.append(battery["energy_used"])
                else:
                    battery["energy_used"] = 0
                    p.append(battery["energy_used"])
    
    print(names)
    print("###")
    print(p)

    response = {}
    for i in names:
        for used in p:
            response[i] = used

    return response
