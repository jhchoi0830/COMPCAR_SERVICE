from motor import motor_asyncio
from dotenv import load_dotenv
import os


load_dotenv()
mongoUser = os.getenv("MONGO_USER")
mongoPassword = os.getenv("MONGO_PASSWORD")


client = motor_asyncio.AsyncIOMotorClient(f'mongodb+srv://{mongoUser}:{mongoPassword}@cluster0.sstu5.mongodb.net/test')
database = client.CompCar
car_collection = database.usedCar
user_collection = database.user
kijiji_car_collection = database.kijijiCar
