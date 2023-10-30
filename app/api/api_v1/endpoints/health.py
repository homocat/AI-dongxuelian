from fastapi import (
  APIRouter,
  Depends
)
from schemas.user import UserSchema
from utils.auth import get_current_user
from models.health import HealthModel

health = APIRouter()

@health.get("/")
def index(current_user: UserSchema = Depends(get_current_user)):
  res = HealthModel.get(user=current_user)