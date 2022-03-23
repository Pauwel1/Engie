

def algo(load, plants):
    row = 0
    produced = 0
    names = []
    p = []   
    
    for i in range(len(plants)):
        if row < len(plants):
            battery = plants.iloc[row, :]
            names.append(battery["name"])
            if load > produced:
                temp = load - produced
                if battery["pmax"] >= temp >= battery["pmin"]:
                    used = temp
                elif battery["pmax"] < temp:
                    used = battery["pmax"]
                elif battery["pmin"] > temp:
                    used = battery["pmin"]
                produced += used
                p.append(used)
            elif load <= produced:
                used = 0
                p.append(used)

            row += 1
        
    print(names)
    print(p)

    response = dict(zip(names, p))

    return response
