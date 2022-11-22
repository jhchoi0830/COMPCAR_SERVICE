# import fastapi modules
from fastapi import FastAPI, HTTPException, APIRouter

# import model
from app.models.usedCarModel import UsedCar
from app.models.userModel import User

router = APIRouter()
