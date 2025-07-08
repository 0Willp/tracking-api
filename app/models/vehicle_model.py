from sqlmodel import SQLModel, Field, Relationship, Column, String, DateTime, ForeignKey
from datetime import datetime
from typing import Optional
from sqlalchemy import event
from models.tracker_model import Tracker

class Vehicle(SQLModel, table=True, table_name='vehicle'):
    id: Optional[int] = Field(default=None, primary_key=True)
    plate: str = Field(sa_column=Column(String(10), nullable=False))
    mark: str = Field(sa_column=Column(String(15), nullable=False))
    model: str = Field(sa_column=Column(String(15), nullable=False))
    status: Optional[bool] = True
    disabled: Optional[bool] = False
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = None

    user_id: Optional[int] = Field(default=None, foreign_key="user.id")
    user: Optional["User"] = Relationship(back_populates="vehicles") # type: ignore

    tracker: Optional["Tracker"] = Relationship(back_populates="vehicle") 


@event.listens_for(Vehicle, 'before_insert')
def receive_before_insert(mapper, connection, target):
    target.updated_at = datetime.utcnow()
