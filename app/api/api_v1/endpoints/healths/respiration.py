from fastapi import APIRouter, Depends
from pydantic import BaseModel
from utils.auth import get_current_user
from schemas.user import UserSchema

respiration_api = APIRouter()

class RespirationData(BaseModel):
    user_id: int
    rate: int
    duration: int

@respiration_api.get("/")
def get_respiration(current_user: UserSchema = Depends(get_current_user)):
    pass

@respiration_api.post("/")
def add_respiration(respiration_data: RespirationData, current_user: UserSchema = Depends(get_current_user)):
    pass

@respiration_api.delete("/")
def clear_respiration(current_user: UserSchema = Depends(get_current_user)):
    pass