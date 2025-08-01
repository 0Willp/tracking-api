from typing import List
from decouple import config
from pydantic.v1 import AnyHttpUrl, BaseSettings

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Tracking API"
    BACKEND_CORS_ORIGINS: list[AnyHttpUrl] = [
        'http://localhost:3000'
    ]
    
    
    JWT_SECRET_KEY: str = config("JWT_SECRET_KEY", cast=str)
    JWT_REFRESH_SECRET_KEY: str = config("JWT_REFRESH_SECRET_KEY", cast=str)
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7 # 7 dias
    
    
    
    
    # Configuração do banco de dados
    SQL_CONNECTION_STRING: str = config("SQL_CONNECTION_STRING", cast=str)
    
    class Config:
        case_sensitive = True
        
settings = Settings()
