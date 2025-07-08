from typing import Optional, Annotated, List
from sqlmodel import Field, SQLModel
from pydantic import EmailStr
from datetime import datetime
from schemas.tracker_schema import TrackerDetail


# base para leitura e saida de dados
class VehicleBase(SQLModel):
    plate: str
    mark: str
    model: str
    status: Optional[bool] = None
    disabled: Optional[bool] = None

# retorno completo do veiculo    
class VehicleDetail(VehicleBase):
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    user_id: Optional[int] = None
    tracker: Optional[TrackerDetail] = None    

# criar veiculo
class VehicleCreate(VehicleBase):
    tracker_id: int  # obrigatório
    user_id: Optional[int] # opcionalmente pode associar a um usuário

# atualizar veiculo    
class VehicleUpdate(SQLModel):
    plate: Optional[str] = None
    mark: Optional[str] = None
    model: Optional[str] = None
    status: Optional[bool] = False
    disabled: Optional[bool] = None
    user_id: Optional[int] = None
    tracker_id: Optional[int] = None
    

    class Config:
        orm_mode = True
    