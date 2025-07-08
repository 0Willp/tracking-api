from sqlmodel import select
from sqlalchemy.ext.asyncio import AsyncSession
from models.vehicle_model import Vehicle
from schemas.vehicle_schema import VehicleCreate, VehicleUpdate
from typing import Optional, List


class VehicleService:

    @staticmethod
    async def create_vehicle(session: AsyncSession, data: VehicleCreate) -> Vehicle:
        vehicle = Vehicle(
            plate=data.plate,
            mark=data.mark,
            model=data.model,
            user_id=data.user_id,
        )
        
        session.add(vehicle)
        await session.commit()
        await session.refresh(vehicle)
        return vehicle

    @staticmethod
    async def list_vehicles(session: AsyncSession) -> List[Vehicle]:
        result = await session.execute(select(Vehicle))
        return result.scalars().all()
    
    @staticmethod
    async def get_vehicle_by_id(session: AsyncSession, vehicle_id: int) -> Optional[Vehicle]:
        vehicle = await session.execute(select(Vehicle).where(Vehicle.id == vehicle_id))
        return vehicle.scalars().first()
        
    @staticmethod
    async def update_vehicle(session: AsyncSession, vehicle_id: int, data: VehicleUpdate) -> Optional[Vehicle]:
        vehicle = await VehicleService.get_vehicle_by_id(session, vehicle_id)
        if not vehicle:
            return None
        for field, value in data.dict(exclude_unset=True).items():
            setattr(vehicle, field, value)
        await session.commit()
        await session.refresh(vehicle)
        return vehicle

    @staticmethod
    async def delete_vehicle(session: AsyncSession, vehicle_id: int) -> bool:
        vehicle = await VehicleService.get_vehicle_by_id(session, vehicle_id)
        if not vehicle:
            return False
        await session.delete(vehicle)
        await session.commit()
        return True
        return False
    
   