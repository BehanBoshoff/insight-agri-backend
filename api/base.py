from fastapi import APIRouter

from .v1 import route_jobs
from .v1 import route_login
from .v1 import route_users

api_router = APIRouter()
api_router.include_router(route_users.router, prefix="/users", tags=["users"])
api_router.include_router(route_jobs.router, prefix="/jobs", tags=["jobs"])
api_router.include_router(route_login.router, prefix="/auth/login", tags=["login"])
