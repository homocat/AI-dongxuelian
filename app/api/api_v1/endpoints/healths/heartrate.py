from typing import List
from fastapi import APIRouter, HTTPException, status, Depends
from pydantic import BaseModel
from utils.auth import get_current_user
from schemas.user import UserSchema

class HeartRateReading(BaseModel):
    user_id: int
    heart_rate: int

heart_rate_api = APIRouter()

# 模拟存储心率读数的列表
heart_rate_data = []

@heart_rate_api.post("/")
def add_heart_rate(reading: HeartRateReading, c: UserSchema = Depends(get_current_user)):
    # 添加心率读数
    # 在这里可以添加适当的逻辑来验证和处理心率读数，并将其存储到心率数据列表中
    # 这里只是示例，您需要根据实际逻辑进行修改
    heart_rate_data.append(reading)
    return {"message": "Heart rate reading added successfully"}

@heart_rate_api.get("/")
def get_all_heart_rates(c: UserSchema = Depends(get_current_user)) -> List[HeartRateReading]:
    # 获取所有心率读数
    return heart_rate_data

@heart_rate_api.get("/{user_id}")
def get_user_heart_rates(user_id: int, c: UserSchema = Depends(get_current_user)) -> List[HeartRateReading]:
    # 获取特定用户的心率读数
    user_heart_rates = []
    for reading in heart_rate_data:
        if reading.user_id == user_id:
            user_heart_rates.append(reading)
    if not user_heart_rates:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user_heart_rates