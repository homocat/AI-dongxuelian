from fastapi import APIRouter
from .endpoints.user import user
from .endpoints.todo import todolist
from .endpoints.auth import auth

from .endpoints.healths import (
  heartrate,
  respiration,
  bloodpressure
)

api_router = APIRouter()
api_router.include_router(auth, tags=['OAuth'])
api_router.include_router(user, prefix="/user", tags=["用户权限"])
api_router.include_router(todolist, prefix="/todos", tags=["待办列表"])

health = APIRouter()
health.include_router(heartrate.heart_rate_api, prefix="/heart_rate")
health.include_router(bloodpressure.blood_pressure, prefix="/blood_pressure")
health.include_router(respiration.respiration_api, prefix="/respiration")
api_router.include_router(health, prefix="/health", tags=["身体数据"])
