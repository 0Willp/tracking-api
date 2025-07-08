from fastapi import APIRouter, Depends, HTTPException, status
import pymongo
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession


from schemas.vehicle_schema import VehicleDetail, VehicleCreate, VehicleUpdate
from services.vehicle_service import VehicleService
from models.user_model import User

from api.dependencies.user_deps import get_current_user
from api.dependencies.get_session import get_session


vehicle_router = APIRouter(prefix='/vehicles', tags=['vehicles'])

@vehicle_router.post("/create", summary="Create vehicle", response_model=VehicleCreate)
async def create_vehicle(data: VehicleCreate, session: AsyncSession = Depends(get_session)):
    try:
        return await VehicleService.create_vehicle(session, data)
    except pymongo.errors.DuplicateKeyError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='This vehicle already exists'
        )
    
@vehicle_router.get("/list", summary="List vehicle", response_model=List[VehicleDetail])
async def list_vehicles(session: AsyncSession = Depends(get_session)):
    return await VehicleService.list_vehicles(session)

@vehicle_router.get("/detail/{vehicle_id}", summary="Vehicle detail ", response_model=VehicleDetail)
async def get_vehicle_detail(vehicle_id: int, session: AsyncSession = Depends(get_session)):
    vehicle = await VehicleService.get_vehicle_by_id(session, vehicle_id)
    if not vehicle:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Vehicle not found')
    return vehicle

@vehicle_router.put("/update/{vehicle_id}", summary="Update vehicle", response_model=VehicleUpdate)
async def update_vehicle(vehicle_id: int, data: VehicleUpdate, session: AsyncSession = Depends(get_session)):
    vehicle = await VehicleService.update_vehicle(session, vehicle_id, data)
    if not vehicle:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Vehicle not found')
    return vehicle

@vehicle_router.delete("/{vehicle_id}", summary="Delete vehicle")
async def delete_vehicle(vehicle_id: int, user: User = Depends(get_current_user), session: AsyncSession = Depends(get_session)):
    sucess = await VehicleService.delete_vehicle(session, user, vehicle_id)
    if not sucess:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Vehicle not found')
    return {"detail": "User deleted successfully"}