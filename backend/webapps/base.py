from fastapi import APIRouter

from webapps.jobs import route_jobs
from webapps.users import route_users
from webapps.auth import route_login


api_router = APIRouter()

api_router.include_router(route_jobs.router, prefix="", tags=["jobs"])
api_router.include_router(route_users.router, prefix="", tags=["users"])
api_router.include_router(route_login.router, prefix="", tags=["login"])
