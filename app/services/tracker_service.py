from sqlmodel import select
from sqlalchemy.ext.asyncio import AsyncSession
from models.tracker_model import Tracker
from schemas.tracker_schema import TrackerCreate, TrackerUpdate
from typing import Optional, List


class TrackerService:
    
    @staticmethod
    async def create_tracker(session: AsyncSession, data: TrackerCreate) -> Tracker:
        tracker = Tracker(
            imei=data.imei,
            chip=data.chip,
            status=data.status,
            disabled=data.disabled,
            vehicle_id=data.vehicle_id
        )
        
        session.add(tracker)
        await session.commit()
        await session.refresh(tracker)
        return tracker
    
    @staticmethod
    async def list_trackers(session: AsyncSession) -> List[Tracker]:
        result = await session.execute(select(Tracker))
        return result.scalars().all()
    
    @staticmethod
    async def get_tracker_by_id(session: AsyncSession, tracker_id: int) -> Optional[Tracker]:
        tracker = await session.execute(select(Tracker).where(Tracker.id == tracker_id))
        return tracker.scalars().first()
    
    @staticmethod
    async def update_tracker(session: AsyncSession, tracker_id: int, data: TrackerUpdate) -> Optional[Tracker]:
        tracker = await TrackerService.get_tracker_by_id(session, tracker_id)
        if not tracker:
            return None
        for field, value in data.dict(exclude_unset=True).items():
            setattr(tracker, field, value)
        await session.commit()
        await session.refresh(tracker)
        return tracker
    
    @staticmethod
    async def delete_tracker(session: AsyncSession, tracker_id: int) -> bool:
        tracker = await TrackerService.get_tracker_by_id(session, tracker_id)
        if not tracker:
            return False
        await session.delete(tracker)
        await session.commit()
        return True