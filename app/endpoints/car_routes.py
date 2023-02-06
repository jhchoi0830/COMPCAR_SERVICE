from fastapi import HTTPException, APIRouter

from app.models.used_car import UsedCar
from app.models.user import User
from app.services.database import (
    fetch_all_cars,
    fetch_car_by_maker,
    fetch_car_by_model,
    fetch_car_by_color,
    fetch_kijiji_cars,
    fetch_car_by_year,
    fetch_car_by_mileage,
    fetch_car_by_price,
    fetch_car_for_graph,
    add_fav_car,
    delete_fav_car,
    fetch_fav_car
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


@router.get("/api/car/graph/{maker}", response_model=list)
async def get_car_for_graph(maker: str) -> list:
    response = await fetch_car_for_graph(maker)
    if response:
        return response
    raise HTTPException(404, f"There is no car with the maker {maker}")


@router.get("/api/car/models/{model}", response_model=list[UsedCar])
async def get_car_by_model(model: str) -> list:
    response = await fetch_car_by_model(model)
    if response:
        return response
    raise HTTPException(404, f"There is no car with the model {model}")


@router.get("/api/car/colors/{color}", response_model=list[UsedCar])
async def get_car_by_color(color: str) -> list:
    response = await fetch_car_by_color(color)
    if response:
        return response
    raise HTTPException(404, f"There is no car with the color {color}")

@router.get("/api/car/years/{year}", response_model=list[UsedCar])
async def get_car_by_year(year: int) -> list:
    response = await fetch_car_by_year(year)
    if response:
        return response
    raise HTTPException(404, f"There is no car with the year {year}")

@router.get("/api/car/mileage/{id}", response_model=list[UsedCar])
async def get_car_by_mileage(id: int) -> list:
    response = await fetch_car_by_mileage(id)
    if response:
        return response
    raise HTTPException(404, f"There is no car with the mileage")

@router.get("/api/car/price/{id}", response_model=list[UsedCar])
async def get_car_by_price(id: int) -> list:
    response = await fetch_car_by_price(id)
    if response:
        return response
    raise HTTPException(404, f"There is no car with the price")

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

@router.get('/api/user/favcar/{user_id}', response_model=list[FavCar])
async def get_fav_car(user_id:str):
    response = await fetch_fav_car(user_id)
    if response:
        return response
    raise HTTPException(400, "There is no favourite car information")