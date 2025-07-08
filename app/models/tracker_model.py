from sqlmodel import SQLModel, Field, Relationship, Column, String, DateTime, ForeignKey
from datetime import datetime
from typing import Optional
from sqlalchemy import event

class Tracker(SQLModel, table=True, table_name='tracker'):
    id: Optional[int] = Field(default=None, primary_key=True)
    imei: int = Field(sa_column=Column(String(15), nullable=False))
    chip: int = Field(sa_column=Column(String(15), nullable=False))
    status: Optional[bool] = True
    disabled: Optional[bool] = False
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = None

    vehicle_id: Optional[int] = Field(default=None, foreign_key="vehicle.id", unique=True)
    vehicle: Optional["Vehicle"] = Relationship(back_populates="tracker")  # type: ignore
    
@event.listens_for(Tracker, 'before_insert')
def receive_before_insert(mapper, connection, target):
    target.updated_at = datetime.utcnow()