# import fastapi modules
from fastapi import FastAPI


# import routers
from endpoints import carRoutes, userRoutes


app = FastAPI()


# connect router with endpoints
app.include_router(carRoutes.router)
app.include_router(userRoutes.router)
