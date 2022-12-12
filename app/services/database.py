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

async def fetch_car_by_year(year: int) -> list:
    cars = []
    cursor = car_collection.find({"madeYear":year})
    async for document in cursor:
        cars.append(document)
    return cars

async def fetch_car_by_mileage(id: int) -> list:
    cars = []
    cursor = car_collection.find({"mileage": {'$gt':(id-1)*50000,'$lt':id*50000}})
    async for document in cursor:
        cars.append(document)
    return cars

async def fetch_car_by_price(id: int) -> list:
    cars = []
    cursor = car_collection.find({"price.price": {'$gt':(id-1)*10000,'$lt':id*10000} })
    async for document in cursor:
        cars.append(document)
    return cars

async def create_user(user: User):
    result = await user_collection.insert_one(user)
    created_user = await user_collection.find_one({'_id': result.inserted_id})
    return created_user

