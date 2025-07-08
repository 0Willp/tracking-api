from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from typing import Any
from services.user_service import UserService
from core.security import create_access_token, create_refresh_token
from schemas.auth_schema import AuthBase
from schemas.user_schema import UserDetail
from models.user_model import User
from api.dependencies.user_deps import get_current_user
from api.dependencies.get_session import get_session
from sqlalchemy.ext.asyncio import AsyncSession

auth_router = APIRouter()
'''
auth_router = APIRouter()
@auth_router.post('/login', summary='Login for dev API access with token', response_model=AuthBase)
async def login_for_access_token(data: OAuth2PasswordRequestForm = Depends(), session: AsyncSession = Depends(get_session)) -> Any:
    user = await UserService.authenticate(session=session,email=data.username, password=data.password)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Email ou senha inválidos',
            headers={'WWW-Authenticate': 'Bearer'},
        )
        
    return {
        "access_token": create_access_token(subject=user.id, role=user.role),
        "refresh_token": create_refresh_token(subject=user.id),
        "token_type": "bearer"
    }
    
#@auth_router.post('/test_token', summary='Testando token', response_model=UserDetail)
#async def test_token(current_user: User = Depends(get_current_user())):
#    return current_user

'''