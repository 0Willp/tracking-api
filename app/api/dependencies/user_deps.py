from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from models.user_model import User
from jose import jwt 
from core.config import settings
from schemas.auth_schema import AuthDetail
from datetime import datetime
from pydantic import ValidationError
from services.user_service import UserService





oauth_reusavel = OAuth2PasswordBearer(tokenUrl=f"{settings.API_V1_STR}/auth/login",
                                      scheme_name="JWT")


async def get_current_user(token: str = Depends(oauth_reusavel)) -> User:
    try:
        payload = jwt.decode(
            token, settings.JWT_SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        token_data = AuthDetail(**payload)
        if datetime.fromtimestamp(token_data.exp) < datetime.now():
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token expirado",
                headers={"WWW-Authenticate": "Bearer"},
            )
    


    except(jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='Erro na valdação do token',
            headers={"WWW-Authenticate": "Bearer"},
                     
        )
        

    user = await UserService.get_user_by_id(token_data.sub)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            details='Não foi possível encontrar o usuário',
            headers={'WWW-Authenticate': 'Bearer'}
        )
        
    return user