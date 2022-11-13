# import model
from models.usedCarModel import UsedCar
from models.userModel import User

from motor import motor_asyncio

client = motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017/')
database = client.CompCar
carCollection = database.usedCar
userCollection = database.user

async def fetch_all_cars():
    cars = []
    cursor = carCollection.find({})
    async for document in cursor:
        cars.append(UsedCar(**document))
    return cars

async def fetch_car_by_make(make):
    cars = []
    cursor = carCollection.find({"make":make})
    async for document in cursor:
        cars.append(document)
    return cars

async def fetch_car_by_model(model):
    cars = []
    cursor = carCollection.find({"model":{'$regex': '.*'+ model + '.*'}})
    async for document in cursor:
        cars.append(document)
    return cars

async def fetch_car_by_color(color):
    cars = []
    cursor = carCollection.find({"color":color})
    async for document in cursor:
        cars.append(document)
    return cars