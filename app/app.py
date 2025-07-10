from fastapi import FastAPI
from core.config import settings
from motor.motor_asyncio import AsyncIOMotorClient
from core.database import create_db_and_tables

from api.api_v1.router import router
from models.user_model import User


from fastapi.middleware.cors import CORSMiddleware



app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",)

#@app.on_event("startup")
#async def on_startup():
#    await create_db_and_tables()


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)


    
app.include_router(router, prefix=settings.API_V1_STR)