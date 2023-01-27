from bson.objectid import ObjectId

from app.models.used_car import UsedCar
from app.models.user import User, FavCar, Settings
from app.models.kijiji_car import KijijiCar
from app.services.connect import car_collection, kijiji_car_collection
from app.services.connect import user_collection
from app.models.hashing import Hash
from bson.objectid import ObjectId
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends, status, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException


from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends, status, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException


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


async def fetch_car_for_graph(maker: str) -> list:
    cars = []
    model_list = []
    data_list = []
    cursor = car_collection.find({"maker":maker})
    async for document in cursor:
        cars.append(document)
        model_list.append(document['model'])
        data_list.append([document['model'],document['madeYear'],document['mileage'], document['price'][0]['price']])

    model_list = list(set(model_list))

    filtered_list = []
    for model in model_list:
        filtered_data = []
        for data in data_list:
            if data[0] == model:
                filtered_data.append({
                    'year': data[1],
                    'price': data[3],
                    'mileage': data[2]
                })
        filtered_list.append(filtered_data)

    graph_list = []
    for i in range(0,len(model_list)):
        graph_list.append({
            'name': maker + " " + model_list[i],
            'data': filtered_list[i]
        })

    return graph_list


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


async def add_fav_car(user_id:str ,fav_car: FavCar) -> object:
    current_user = await user_collection.find_one({"_id":ObjectId(user_id)})
    if (current_user['favouriteCar'].count(fav_car) == 0):
        current_user['favouriteCar'].append(fav_car)
    result = await user_collection.replace_one({"_id":ObjectId(user_id)},current_user)
    return current_user


async def register_user(request:User):
    hashed_pass = Hash.get_hash_password(request.password)
    user_object = dict(request)
    user_object["password"] = hashed_pass
    user = await user_collection.insert_one(user_object)
    return user

async def login_user(request):
    user = await user_collection.find_one({"email":request.email})
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = f'No user found with this {request.email} username')
    if not Hash.verify_password(request.password, user["password"]):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = f'Wrong Username or password')
    return user


async def delete_fav_car(user_id:str ,fav_car: FavCar) -> object:
    current_user = await user_collection.find_one({"_id":ObjectId(user_id)})
    if fav_car in current_user['favouriteCar']:
        current_user['favouriteCar'].remove(fav_car)
    result = await user_collection.replace_one({"_id":ObjectId(user_id)},current_user)
    return current_user

async def fetch_fav_car(user_id:str) -> list:
    current_user = await user_collection.find_one({"_id":ObjectId(user_id)})
    return current_user['favouriteCar']