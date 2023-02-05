import os
from motor import motor_asyncio
from dotenv import load_dotenv


load_dotenv()
mongoUser = "shlee1234"
mongoPassword = "shlee1234"

client = motor_asyncio.AsyncIOMotorClient(f'mongodb+srv://{mongoUser}:{mongoPassword}@cluster0.sstu5.mongodb.net/test')
database = client.CompCar
car_collection = database.usedCar
user_collection = database.user
kijiji_car_collection = database.kijijiCar
