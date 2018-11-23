import json

with open("element_data.json", "r") as f:
    data = json.load(f)


def solve(config):
    if type(config) != list:
        return config
    result = ""
    for i, row in enumerate(config, start=1):
        for key in ["s", "p", "d", "f"]:
            if row[key]:
                result += str(i) + key + str(row[key]) + " "
    return result

config = data["w"]["electron-configuration"]
print(config)
print(solve(config))

with open("element_data.json", "w") as f:
    for key in data:
        data[key]["electron-configuration"] = solve(data[key]["electron-configuration"]).strip()
    json.dump(data, f)