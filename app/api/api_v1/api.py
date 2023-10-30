from fastapi import APIRouter
from .endpoints.user import user
from .endpoints.todo import todolist
from .endpoints.health import health

api_router = APIRouter()
api_router.include_router(user, prefix="/user", tags=["用户权限"])
api_router.include_router(todolist, prefix="/todos", tags=["待办列表"])
api_router.include_router(health, prefix="/health", tags=["身体数据"])