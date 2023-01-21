from fastapi import FastAPI, HTTPException, APIRouter, status, Depends, Request
from app.models.user import User, Settings
from app.models.hashing import Hash
from app.models.oauth import get_current_user
from fastapi.middleware.cors import CORSMiddleware
from app.services.connect import user_collection
from app.services.database import register_user, login_user
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException



router = APIRouter()

@AuthJWT.load_config
def get_config():
    return Settings()

@router.post('/api/user/register')
async def create_user(request:User):
    if await register_user(request):
        return {"res":"created"}
    return {"message":"ID not created", "status-code":"Error Code 404"}


@router.post('/api/user/login')
async def login(request:OAuth2PasswordRequestForm = Depends()):
    if await login_user(request):
        return {"res":"found"}
    return {"res":"coudln't find"}