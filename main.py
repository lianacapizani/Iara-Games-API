import datetime
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

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

games: list[Game] = [

    Game(
        id=1,
        name="Arida",
        description="Lorem ipsum dolor sit amet consectetur adipisicing elit. Accusamus dicta...",
        image="/assets/images/store/arida.jpeg",
        price=80.00,
        author="Aoca Game Lab",
        valuation_rate=4.0,
        release_date=datetime.date(2021, 1, 1),
    ),
    Game(
        id=2,
        name="Aritana",
        description="Lorem ipsum dolor sit amet consectetur adipisicing elit. Accusamus dicta...",
        image="/assets/images/store/aritana.jpg",
        price=120.00,
        author="Duaik",
        valuation_rate=4.2,
        release_date=datetime.date(2021, 1, 1),
    ),
    Game(
        id=3,
        name="Chroma Squad",
        description="Lorem ipsum dolor sit amet consectetur adipisicing elit. Accusamus dicta...",
        image="/assets/images/store/chromasquad.jpg",
        price=95.00,
        author="Behold Studios",
        valuation_rate=4.0,
        release_date=datetime.date(2021, 1, 1),
    ),
    Game(
        id=4,
        name="Dandara",
        description="Lorem ipsum dolor sit amet consectetur adipisicing elit. Accusamus dicta...",
        image="/assets/images/store/dandara.jpeg",
        price=70.00,
        author="Long Hat House",
        valuation_rate=4.3,
        release_date=datetime.date(2021, 1, 1),
    ),
    Game(
        id=5,
        name="Dodgeball Academia",
        description="Lorem ipsum dolor sit amet consectetur adipisicing elit. Accusamus dicta...",
        image="/assets/images/store/dodgeball-academia.avif",
        price=90.00,
        author="Pocket Trap",
        valuation_rate=4.1,
        release_date=datetime.date(2021, 1, 1),
    ),
    Game(
        id=6,
        name="Éden",
        description="Lorem ipsum dolor sit amet consectetur adipisicing elit. Accusamus dicta...",
        image="/assets/images/store/eden.jpg",
        price=90.00,
        author="Developer Name",
        valuation_rate=4.0,
        release_date=datetime.date(2021, 1, 1),
    ),
    Game(
        id=7,
        name="Fobia",
        description="Lorem ipsum dolor sit amet consectetur adipisicing elit. Accusamus dicta...",
        image="/assets/images/store/fobia.jpeg",
        price=130.00,
        discount_price=90.00,
        author="Developer Name",
        valuation_rate=4.5,
        release_date=datetime.date(2021, 1, 1),
    ),
    Game(
        id=8,
        name="Língua",
        description="Lorem ipsum dolor sit amet consectetur adipisicing elit. Accusamus dicta...",
        image="/assets/images/store/lingua.jpeg",
        price=95.00,
        discount_price=75.00,
        author="Developer Name",
        valuation_rate=4.1,
        release_date=datetime.date(2021, 1, 1),
    ),
    Game(
        id=9,
        name="Mandinga",
        description="Lorem ipsum dolor sit amet consectetur adipisicing elit. Accusamus dicta...",
        image="/assets/images/store/mandinga.jpeg",
        price=100.00,
        discount_price=85.00,
        author="Developer Name",
        valuation_rate=4.0,
        release_date=datetime.date(2021, 1, 1),
    )
]

@app.get("/games")
def list_games():
    return [game.model_dump() for game in games]

@app.get("/games/{game_id}")
def read_game(game_id: int):
    game = next((game for game in games if game.id == game_id), None)
    if game:
        return game.model_dump()
    return {"error": "Game not found"}, 404

@app.post("/games")
def create_game(game: Game):
    next_id = max(game.id for game in games) + 1 if games else 1
    game.id = next_id
    games.append(game)
    return game.model_dump()
