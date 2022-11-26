# import model
from app.models.usedCarModel import UsedCar
from app.models.userModel import User

from motor import motor_asyncio
from dotenv import load_dotenv
import os


#load_dotenv()
#mongoUser = os.getenv("MONGO_USER")
#mongoPassword = os.getenv("MONGO_PASSWORD")


client = motor_asyncio.AsyncIOMotorClient(f'mongodb+srv://shlee1234:shlee1234@cluster0.sstu5.mongodb.net/test')
database = client.CompCar
carCollection = database.usedCar
userCollection = database.user


async def fetch_all_cars() -> list:
    cars = []
    cursor = carCollection.find({})
    async for document in cursor:
        cars.append(UsedCar(**document))
    return cars


async def fetch_car_by_maker(maker: str) -> list:
    cars = []
    cursor = carCollection.find({"maker":maker})
    async for document in cursor:
        cars.append(document)
    return cars


async def fetch_car_by_model(model: str) -> list:
    cars = []
    cursor = carCollection.find({"model":{'$regex': '.*'+ model + '.*'}})
    async for document in cursor:
        cars.append(document)
    return cars


async def fetch_car_by_color(color: str) -> list:
    cars = []
    cursor = carCollection.find({"color":color})
    async for document in cursor:
        cars.append(document)
    return cars