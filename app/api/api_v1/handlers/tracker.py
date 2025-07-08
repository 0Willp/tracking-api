
from fastapi import APIRouter, Depends, HTTPException, status
import pymongo
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession


from schemas.tracker_schema import TrackerDetail, TrackerCreate, TrackerUpdate
from services.tracker_service import TrackerService
from models.user_model import User

from api.dependencies.user_deps import get_current_user
from api.dependencies.get_session import get_session

tracker_router = APIRouter(prefix='/trackers', tags=['trackers'])

@tracker_router.post("/create", summary="Create tracker", response_model=TrackerCreate)
async def create_tracker(data: TrackerCreate, session: AsyncSession = Depends(get_session)):
    try:
        return await TrackerService.create_tracker(session, data)
    except pymongo.errors.DuplicateKeyError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='This tracker already exists'
        )


@tracker_router.get("/list", summary="List trackers", response_model=List[TrackerDetail])
async def list_trackers(session: AsyncSession = Depends(get_session)):
    return await TrackerService.list_trackers(session)
'''
@tracker_router.get("/detail/{tracker_id}", summary="Tracker detail", response_model=TrackerDetail)
async def get_tracker_detail(tracker_id: int, session: AsyncSession = Depends(get_session)):
    tracker = await TrackerService.get_tracker_by_id(session, tracker_id)
    if not tracker:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Tracker not found')
    return tracker

@tracker_router.put("/update/{tracker_id}", summary="Update tracker", response_model=TrackerUpdate)
async def update_tracker(tracker_id: int, data: TrackerUpdate, session: AsyncSession = Depends(get_session)):
    tracker = await TrackerService.update_tracker(session, tracker_id, data)
    if not tracker:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Tracker not found')
    return tracker

@tracker_router.delete("/{tracker_id}", summary="Delete tracker")
async def delete_tracker(tracker_id: int, user: User = Depends(get_current_user), session: AsyncSession = Depends(get_session)):
    success = await TrackerService.delete_tracker(session, user, tracker_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Tracker not found')
    return {"detail": "Tracker deleted successfully"}
'''