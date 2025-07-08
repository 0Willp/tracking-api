from passlib.context import CryptContext
from typing import Union, Any
from datetime import datetime, timedelta
from jose import jwt 
from core.config import settings


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Criptografia de senha
def get_password(password: str) -> str:
    return pwd_context.hash(password)


# Descriptografia da senha
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# Criação de tokens JWT para autenticação e refresh
def create_access_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        
    info_jwt = {
        'exp': expires_delta,
        'sub': str(subject)
    }
        
    jwt_encoded = jwt.encode(info_jwt, settings.JWT_SECRET_KEY, settings.ALGORITHM)
    return jwt_encoded

# Criação de tokens JWT para refresh
def create_refresh_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=settings.REFRESH_TOKEN_EXPIRE_MINUTES)
        
    info_jwt = {
        'exp': expires_delta,
        'sub': str(subject)
    }
        
    return jwt.encode(info_jwt, settings.SJWT_REFRESH_SECRET_KEY, algorithm=settings.ALGORITHM)

