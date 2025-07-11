# configuração do banco de dados
from sqlmodel import SQLModel, Field
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from contextlib import asynccontextmanager
from core.config import settings
from sqlmodel import SQLModel, Field

# chamada dos models


# Criação do engine de conexão com o banco de dados
engine = create_async_engine(settings.SQL_CONNECTION_STRING, echo=True, future=True)

# Criação da sessão assíncrona
async_session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Criação das tabelas no banco de dados
async def create_db_and_tables():
    async with engine.begin() as conn:
        # Cria todas as tabelas definidas nos modelos
        await conn.run_sync(SQLModel.metadata.create_all)
        
# Dependência para usar em endpoints
#@asynccontextmanager
#async def get_session() -> AsyncSession: # type: ignore
#   async with async_session() as session:
#        yield session

@asynccontextmanager
async def get_session():
    async with async_session() as session:
        yield session