from copy import deepcopy

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

from server_seabattle.map_example import example_map, example_map_2

app = FastAPI()
templates = Jinja2Templates(directory="templates")


def status_formatter(board_data):
    lst = deepcopy(board_data)
    sublist_size = 10

    empty = '💧'
    ship = '⛴️'
    damaged = '🎯'
    missed = '🌊'
    destroyed = '💥'

    for dict_ in lst:
        match dict_["status"]:
            case 'empty':
                dict_["status"] = empty
            case 'ship':
                dict_["status"] = ship
            case 'damaged':
                dict_["status"] = damaged
            case 'missed':
                dict_["status"] = missed
            case 'destroyed':
                dict_["status"] = destroyed

    sublists = []
    for i in range(0, len(lst), sublist_size):
        sublists.append(lst[i:i + sublist_size])
    return sublists


@app.get("/interface")
def interface(request: Request):
    data = status_formatter(example_map["map"])
    return templates.TemplateResponse("map.html", {"request": request, "game_board": data})


@app.get("/map")
def map(*args):
    return {"map": [example_map]}


@app.post("/turn")
def turn(data: dict):
    player = data['player_name']
    turn = data['cell']
    return {"status": "done", "player": player, "turn": turn}
