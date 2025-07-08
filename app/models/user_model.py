from sqlmodel import SQLModel, Field, Relationship, Column, String, DateTime, Text
from pydantic import EmailStr
from datetime import datetime
from typing import Optional, List
from models.vehicle_model import Vehicle


class UserRole:
    admin = "admin"
    user = "user"

class User(SQLModel, table=True, table_name='user'):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(sa_column=Column(String(255), nullable=False))
    username: str = Field(sa_column=Column(String(30), nullable=False))
    password: str = Field(sa_column=Column(String(100), nullable=False))
    hash_password: str = Field(sa_column=Column(Text, nullable=False))
    cpf: Optional[str] = Field(default=None, sa_column=Column(String(14)))
    email: Optional[EmailStr] = Field(default=None, sa_column=Column(String(100)))
    status: Optional[bool] = True
    disabled: Optional[bool] = False
    role: str = Field(sa_column=Column(String(15), nullable=False), default='user')
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = None
    
     # relacionamento com veículo
    vehicles: List["Vehicle"] = Relationship(back_populates="user")
    
    def __repr__(self) -> str: 
        return f'User({self.id}, {self.username}, {self.mail})'

    def __str__(self) -> str:
        return self.mail or self.username