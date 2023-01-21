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
async def login(request:OAuth2PasswordRequestForm = Depends(), Authorize: AuthJWT = Depends()):
    user = await login_user(request)
    if user:
        access_token = Authorize.create_access_token(subject=user["email"])
        refresh_token = Authorize.create_refresh_token(subject=user["email"])
        #Authorize.set_access_cookies(access_token)
        #Authorize.set_refresh_cookies(refresh_token)
        print("access_token")
        print(access_token)
        return {"res":"Successfully login"}
    return {"res":"coudln't find"}


@router.post('/api/user/refresh')
async def refresh(Authorize: AuthJWT = Depends()):
    Authorize.jwt_refresh_token_required()
    current_user = Authorize.get_jwt_subject()
    new_access_token = Authorize.create_access_token(subject=current_user)
    Authorize.set_access_cookies(new_access_token)
    return {"res":"The token has been refresh"}


@router.delete('/api/user/logout')
def logout(Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()

    Authorize.unset_jwt_cookies()
    return {"res":"Successfully logout"}


@router.get('/api/user/protected')
def protected(Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()

    current_user = Authorize.get_jwt_subject()
    return {"user": current_user}