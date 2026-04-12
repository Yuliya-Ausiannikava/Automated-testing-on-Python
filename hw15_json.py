import json

data_football_clubs = {
    "1": {
        "name": "Real Madrid",
        "country": "Spain",
        "victories": 15
    },
    "2": {
        "name": "AC Milan",
        "country": "Italy",
        "victories": 7
    },
    "3": {
        "name": "FC Bayern",
        "country": "Germany",
        "victories": 6
    }
}

with open("dataFC.json", "w") as file:
    json.dump(data_football_clubs, file)

with open("dataFC.json", "r") as file:
    data = json.load(file)
    max_win = 0
    for key in data:
        win = data[key]["victories"]
        if win > max_win:
            max_win = win
            print(f"The team with the most wins:\nFC: {data[key]["name"]},\ncountry: {data[key]["country"]},\nnumber of victories: {data[key]["victories"]}")
