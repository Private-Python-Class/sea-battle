from fastapi import FastAPI
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/map")
def map(request):
    return templates.TemplateResponse("profile.html", {"request": request, "turns": []})


@app.post("/turn")
def turn(data: dict):
    player = data['player']
    turn = data['turn']
    return {"status": "done", "player": player, "turn": turn}
