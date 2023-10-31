from fastapi import APIRouter, HTTPException, Depends
from utils.auth import get_current_user
from schemas.user import UserSchema

blood_pressure = APIRouter()

# 模拟存储血压数据的列表
blood_pressure_data = []

@blood_pressure.get("/")
def get_blood_pressure(current_user: UserSchema = Depends(get_current_user)):
    # 返回存储的血压数据列表
    return {"user": current_user.username, "data": blood_pressure_data}

@blood_pressure.post("/")
def add_blood_pressure(systolic: int, diastolic: int, current_user: UserSchema = Depends(get_current_user)):
    # 添加血压值
    # 在这里可以添加适当的逻辑来验证血压值，并将其存储到血压数据列表中
    if systolic <= 0 or diastolic <= 0:
        raise HTTPException(status_code=400, detail="Invalid blood pressure values")
    
    blood_pressure_data.append({"user": current_user.username, "systolic": systolic, "diastolic": diastolic})
    return {"message": "Blood pressure added successfully"}

@blood_pressure.delete("/")
def clear_blood_pressure(current_user: UserSchema = Depends(get_current_user)):
    # 清空血压数据列表
    blood_pressure_data.clear()
    return {"message": "Blood pressure data cleared successfully"}