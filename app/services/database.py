# import model
from app.models.usedCarModel import UsedCar
from app.models.userModel import User
from app.models.KijijiCar import KijijiCar

from app.services.connect import car_collection, kijiji_car_collection
from app.services.connect import user_collection

async def fetch_all_cars() -> list:
    cars = []
    cursor = car_collection.find({})
    async for document in cursor:
        cars.append(UsedCar(**document))
    return cars


async def fetch_kijiji_cars() -> list:
    cars = []
    cursor = kijiji_car_collection.find({})
    async for document in cursor:
        cars.append(KijijiCar(**document))
    return cars


async def fetch_car_by_maker(maker: str) -> list:
    cars = []
    cursor = car_collection.find({"maker":maker})
    async for document in cursor:
        cars.append(document)
    return cars


async def fetch_car_by_model(model: str) -> list:
    cars = []
    cursor = car_collection.find({"model":{'$regex': '.*'+ model + '.*'}})
    async for document in cursor:
        cars.append(document)
    return cars


async def fetch_car_by_color(color: str) -> list:
    cars = []
    cursor = car_collection.find({"color":color})
    async for document in cursor:
        cars.append(document)
    return cars


async def fetch_all_users() -> list:
    users = []
    cursor = user_collection.find({})
    async for document in cursor:
        users.append(User(**document))
    return users


async def fetch_user_by_email(email: str) -> list:
    users = []
    cursor = user_collection.find({"email":{'$regex': '.*'+ email + '.*'}})
    async for document in cursor:
        users.append(document)
    return users

async def fetch_user_by_password(password: str) -> list:
    users = []
    cursor = user_collection.find({"password":{'$regex': '.*'+ password + '.*'}})
    async for document in cursor:
        users.append(document)
    return users

