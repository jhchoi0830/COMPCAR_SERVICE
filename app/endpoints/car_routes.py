# import fastapi modules
from fastapi import HTTPException, APIRouter


# import model
from app.models.UsedCarModel import UsedCar
from app.models.UserModel import User


# import database functions
from app.services.database import (
    fetch_all_cars,
    fetch_car_by_maker,
    fetch_car_by_model,
    fetch_car_by_color,
    fetch_kijiji_cars
    )


router = APIRouter()


@router.get("/")
async def root():
    return {"message": "Hello World"}


@router.get("/api/car")
async def get_car() -> list:
    response = await fetch_all_cars()
    return response


@router.get("/api/kijijiCar")
async def get_kijiji_car() -> list:
    response = await fetch_kijiji_cars()
    return response


@router.get("/api/car/makers/{maker}", response_model=list[UsedCar])
async def get_car_by_make(maker: str) -> list:
    response = await fetch_car_by_maker(maker)
    if response:
        return response
    raise HTTPException(404, f"There is no car with the maker {maker}")


@router.get("/api/car/models/{model}", response_model=list[UsedCar])
async def get_car_by_model(model: str) -> list:
    response = await fetch_car_by_model(model)
    if response:
        return response
    raise HTTPException(404, f"There is no car with the make {model}")


@router.get("/api/car/colors/{color}", response_model=list[UsedCar])
async def get_car_by_color(color: str) -> list:
    response = await fetch_car_by_color(color)
    if response:
        return response
    raise HTTPException(404, f"There is no car with the make {color}")