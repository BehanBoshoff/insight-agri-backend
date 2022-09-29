from fastapi import APIRouter

from .v1 import route_users
from .v1 import route_jobs

api_router = APIRouter()
api_router.include_router(route_users.router,prefix="/users",tags=["users"])
api_router.include_router(route_jobs.router,prefix="/jobs",tags=["jobs"])
