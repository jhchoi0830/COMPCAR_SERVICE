# import fastapi modules
from fastapi import FastAPI, HTTPException, APIRouter

# import model
from models.usedCarModel import UsedCar
from models.userModel import User

router = APIRouter()
