# import modules
from fastapi import FastAPI, HTTPException

# import model
from models.usedCarModel import UsedCar
from models.userModel import User

# import database functions
from services.database import fetch_all_cars

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/api/car")
async def get_todo():
    response = await fetch_all_cars()
    return response