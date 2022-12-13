from fastapi import FastAPI, HTTPException, APIRouter

from app.models.user import User

router = APIRouter()

from app.services.database import create_user

router = APIRouter()


@router.post('/api/user/register', response_model=User)
async def post_user(user: User):
    response = await create_user(user.dict())
    if response:
        return response
    raise HTTPException(400, "Something went wrong")