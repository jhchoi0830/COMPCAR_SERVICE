# import fastapi modules
from fastapi import FastAPI, HTTPException, APIRouter

# import model
from app.models.UsedCarModel import UsedCar
from app.models.UserModel import User

router = APIRouter()
