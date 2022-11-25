
from fastapi import FastAPI
from pydantic import BaseModel
my_app = FastAPI()


class User(BaseModel):
    email: str
    password: str
    favouriteCar: list[FavCar]

@my_app.post("/users/")
def create_user(user: User) -> User:
    if user in users:
        raise fastapi.HTTPException(status_code=409, detail=f'User with userID {user.userID} already exists ')
    users.append(user)
    return user

