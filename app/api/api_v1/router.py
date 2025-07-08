from fastapi import APIRouter
from api.api_v1.handlers import user
from api.auth.jwt import auth_router
from api.api_v1.handlers import vehicle  # corrigido o import
from api.api_v1.handlers import tracker

router = APIRouter()

router.include_router(
    auth_router,
    prefix="/auth",
    tags=["auth"]
)

router.include_router(
    user.user_router,
    prefix="/users",
    tags=["users"]
)


router.include_router(
    vehicle.vehicle_router,  
    prefix="/vehicles",      
    tags=["vehicles"]        
)

router.include_router(
    tracker.tracker_router,  
    prefix="/trackers",       
    tags=["trackers"]         
)