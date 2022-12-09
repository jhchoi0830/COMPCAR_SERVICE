# Pydantic allows auto creation of JSON Schemas from models
from pydantic import BaseModel


class KijijiCar(BaseModel):
    car_info: str
    url: str
    mileage: str
    region: str
    price: str
