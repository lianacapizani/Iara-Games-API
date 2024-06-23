import datetime
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from db import get_db_connection

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"], 
)

class Game(BaseModel):
    id: int | None = None
    name: str
    description: str
    image: str
    price: float
    discount_price: float | None = None
    author: str
    valuation_rate: float
    release_date: datetime.date

@app.get("/games")
def list_games():
    db_connection = get_db_connection()
    db_connection.execute("SELECT * FROM games;")
    games = [Game(
        id=game[0],
        name=game[1],
        description=game[2],
        image=game[3],
        price=game[4],
        discount_price=game[5],
        author=game[6],
        valuation_rate=game[7],
        release_date=game[8],
    ) for game in db_connection.fetchall()]
    return [game.model_dump() for game in games]

@app.post("/games")
def create_game(game: Game):
    db_connection = get_db_connection()
    query = '''
    INSERT INTO games(name, description, image, price, discount_price, author, valuation_rate, release_date) 
	VALUES (
		%s, %s, %s, %s, %s, %s, %s, %s
	)
    '''
    db_connection.execute(query, (
        game.name,
        game.description,
        game.image,
        game.price,
        game.discount_price,
        game.author,
        game.valuation_rate,
        game.release_date
    ))
    db_connection.connection.commit()
    return game.model_dump()
