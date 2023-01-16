from fastapi import FastAPI, HTTPException, APIRouter

from app.models.user import User, FavCar

router = APIRouter()

from app.services.database import (
    create_user,
    add_fav_car,
    delete_fav_car
)

router = APIRouter()


@router.post('/api/user/register', response_model=User)
async def post_user(user: User):
    response = await create_user(user.dict())
    if response:
        return response
    raise HTTPException(400, "Something went wrong")


@router.post('/api/user/favcar/{user_id}', response_model=User)
async def post_fav_car(user_id:str, fav_car:FavCar):
    response = await add_fav_car(user_id, fav_car.dict())
    if response:
        return response
    raise HTTPException(400, "There is no user which has user_id")


@router.delete('/api/user/favcar/{user_id}', response_model=User)
async def remove_fav_car(user_id:str, fav_car:FavCar):
    response = await delete_fav_car(user_id, fav_car.dict())
    if response:
        return response
    raise HTTPException(400, "There is no user which has user_id")