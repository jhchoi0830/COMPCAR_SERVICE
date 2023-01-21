from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from app.endpoints import car_routes, user_routes
from fastapi.responses import JSONResponse
from fastapi_jwt_auth.exceptions import AuthJWTException


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


@app.exception_handler(AuthJWTException)
async def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )