# import fastapi modules
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


# import routers
from app.endpoints import car_routes, user_routes


app = FastAPI()

origins = [
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# connect router with endpoints
app.include_router(car_routes.router)
app.include_router(user_routes.router)
