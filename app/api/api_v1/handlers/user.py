from fastapi import APIRouter, HTTPException, status, Depends
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
import pymongo

from schemas.user_schema import UserCreate, UserDetail, UserUpdate, UserAuth
from services.user_service import UserService

from api.dependencies.user_deps import get_current_user
from api.dependencies.get_session import get_session
from models.user_model import User



user_router = APIRouter()

@user_router.post('/create', summary='Create user', response_model=UserCreate)
async def create_user(data: UserCreate, session: AsyncSession = Depends(get_session)):
    try:
        return await UserService.create_user(session, data)
    except pymongo.errors.DuplicateKeyError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='This users already exists'
        )

@user_router.get('/list', summary='List users', response_model=List[UserDetail])
async def list_users(session: AsyncSession = Depends(get_session)):
    return await UserService.list_users(session)

@user_router.get('/detail/{user_id}', summary='User detail', response_model=UserDetail)
async def get_user(user_id: int, session: AsyncSession = Depends(get_session)):
    user = await UserService.get_user_by_id(session, user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
    return user

@user_router.put('/update/{user_id}', summary='Update user', response_model=UserUpdate)
async def update_user(user_id: int, data: UserUpdate, session: AsyncSession = Depends(get_session)):
    user = await UserService.update_user(session, user_id, data)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
    return user

@user_router.delete('/delete/{user_id}', summary='Delete user')
async def delete_user(user_id: int, user: User = Depends(get_current_user), session: AsyncSession = Depends(get_session)):
    success = await UserService.delete_user(session, user, user_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
    return {"detail": "User deleted successfully"}
