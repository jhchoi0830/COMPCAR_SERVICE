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


class Settings(BaseModel):
    authjwt_secret_key: str = "secret"
    authjwt_token_location: set = {"cookies"}
    authjwt_cookie_secure: bool = False
    authjwt_cookie_csrf_protect: bool = True


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str
    
    
class TokenData(BaseModel):
    username: Optional[str] = None
