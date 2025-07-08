from typing import Optional, Annotated, List
from sqlmodel import Field, SQLModel
from pydantic import EmailStr
from datetime import datetime
from schemas.vehicle_schema import VehicleDetail

# base para leitura e saida de dados
class UserBase(SQLModel):
    name: str
    username: str
    cpf: Optional[str] = None
    email: Optional[EmailStr] = None
    status: Optional[bool] = None
    disabled: Optional[bool] = None
    role: Optional[str] = Field(default='user')
    
# retorno completo do usuario    
class UserDetail(UserBase):
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    vehicles: Optional[List[VehicleDetail]] = None  # Lista de IDs dos veículos

# criar usuario    
class UserCreate(UserBase):
    password: str  # senha em texto puro (será criptografada na lógica da API)
    #vehicle_id: Optional[List[int]] = None  # opcionalmente pode associar veículos
    
# acesso a senha criptografada   
class UserSecret(UserDetail):
    hash_password: str
    
# atualizar usuario    
class UserUpdate(SQLModel):
    name: Optional[str] = None
    username: Optional[str] = None
    password: Optional[str] = None
    cpf: Optional[str] = None
    email: Optional[EmailStr] = None
    status: Optional[bool] = None
    role: Optional[str] = None
    #vehicle_ids: Optional[List[int]] = None
    
class UserAuth(SQLModel):
    email: EmailStr = Field(..., description='Email do usuário')
    username: str = Field(..., description='Nome de usuário', min_length=6, max_length=20)
    password: str = Field(..., description='Senha do usuário', min_length=6, max_length=20)

    class Config:
        orm_mode = True