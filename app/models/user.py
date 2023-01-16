# Pydantic allows auto creation of JSON Schemas from models
from pydantic import BaseModel
from typing import Optional, List


class FavCar(BaseModel):
    maker: str
    model: str
    madeYear: int
    mileage: int
    price: int


class User(BaseModel):
    email: str
    password: str
    favouriteCar: Optional[List[FavCar]] = None
