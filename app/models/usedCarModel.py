# Pydantic allows auto creation of JSON Schemas from models
from pydantic import BaseModel

class PriceData(BaseModel):
  date: str
  price: int

class UsedCar(BaseModel):
  maker: str
  model: str
  madeYear: int
  mileage: int
  price: list[PriceData]
  url: str
  region: str
  color: str