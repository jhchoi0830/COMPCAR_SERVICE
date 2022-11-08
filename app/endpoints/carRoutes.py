# import fastapi modules
from fastapi import FastAPI, HTTPException, APIRouter

# import model
from models.usedCarModel import UsedCar
from models.userModel import User

# import database functions
from services.database import fetch_all_cars

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Hello World"}

@router.get("/api/car")
async def get_car():
    response = await fetch_all_cars()
    return response