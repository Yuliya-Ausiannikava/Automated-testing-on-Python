"""
A program that reads data from a file and displays information about the club with the most wins.
"""

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

with open("dataFC.json", "w", encoding='utf-8') as file:
    json.dump(data_football_clubs, file)


def parse_json(data):
    max_win = 0
    best_club = None
    for key in data:
        win = data[key]["victories"]
        max_win = max(max_win, win)
        if win == max_win:
            best_club = data[key]
    return print(best_club)


with open("dataFC.json", "r", encoding='utf-8') as file:
    data_FC = json.load(file)
    parse_json(data_FC)
