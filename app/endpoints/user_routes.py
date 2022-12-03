# import fastapi modules
from fastapi import FastAPI, HTTPException, APIRouter

# import model
from app.models.usedCarModel import UsedCar
from app.models.userModel import User

router = APIRouter()

from app.services.database import (
    fetch_all_users,
    fetch_user_by_email,
    fetch_user_by_password
    )

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Hello World"}


@router.get("/api/car")
async def get_user() -> list:
    response = await fetch_all_users()
    return response


@router.get("/register/user/email/{email}", response_model=list[User])
async def create_email(email: str) -> list:
    response = await fetch_user_by_email(email)
    if response:
        return response
    raise HTTPException(404, f"There is no user with the email {email}")

@router.get("/register/user/password/{password}", response_model=list[User])
async def create_password(password: str) -> list:
    response = await fetch_user_by_password(password)
    if response:
        return response
    raise HTTPException(404, f"The password is incorrect")


