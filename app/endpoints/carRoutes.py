# import fastapi modules
from fastapi import FastAPI, HTTPException, APIRouter

# import model
from models.usedCarModel import UsedCar
from models.userModel import User

# import database functions
from services.database import (
    fetch_all_cars,
    fetch_car_by_make,
    fetch_car_by_model,
    fetch_car_by_color,
    )

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Hello World"}

@router.get("/api/car")
async def get_car() -> list:
    response = await fetch_all_cars()
    return response

@router.get("/api/car/make/{make}", response_model=list[UsedCar])
async def get_car_by_make(make: str) -> list:
    response = await fetch_car_by_make(make)
    if response:
        return response
    raise HTTPException(404, f"There is no car with the make {make}")

@router.get("/api/car/model/{model}", response_model=list[UsedCar])
async def get_car_by_model(model: str) -> list:
    response = await fetch_car_by_model(model)
    if response:
        return response
    raise HTTPException(404, f"There is no car with the make {model}")

@router.get("/api/car/color/{color}", response_model=list[UsedCar])
async def get_car_by_color(color: str) -> list:
    response = await fetch_car_by_color(color)
    if response:
        return response
    raise HTTPException(404, f"There is no car with the make {color}")