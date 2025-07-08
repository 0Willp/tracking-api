from typing import Optional, Annotated, List
from sqlmodel import Field, SQLModel
from datetime import datetime

class TrackerBase(SQLModel):
    imei: str
    chip: str
    status: Optional[bool] = None
    disabled: Optional[bool] = None
    
class TrackerDetail(TrackerBase):
    id: int
    vehicle_id: Optional[int] = None
    status: Optional[bool] = None
    disabled: Optional[bool] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class TrackerCreate(TrackerBase):
    vehicle_id: Optional[int] = None

class TrackerUpdate(SQLModel):
    imei: Optional[int] = None
    chip: Optional[int] = None
    vehicle_id: Optional[int] = None


    class Config:
        orm_mode = True