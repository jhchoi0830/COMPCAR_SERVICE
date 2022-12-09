# import fastapi modules
from fastapi import FastAPI, HTTPException, APIRouter

# import model
from app.models.used_car import UsedCar
from app.models.user import User

router = APIRouter()
