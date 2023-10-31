from fastapi import APIRouter, Depends, HTTPException
from models.user import UserModel
from schemas.user import UserSchema
from utils.auth import create_access_token, get_current_user, verify_password

user = APIRouter()

@user.post("/login")
def login(username: str, password: str):
    user = UserModel.get_or_none(username=username)
    if not user or not verify_password(password, user.password):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    access_token = create_access_token(user.username)
    return {"access_token": access_token, "token_type": "bearer"}

@user.post("/register")
def register(user_data: UserSchema):
    if UserModel.select().where(UserModel.username == user_data.username).exists():
        raise HTTPException(status_code=400, detail="User already exists")
    # hashed_password = get_password_hash(user_data.password)
    new_user = UserModel(
        username=user_data.username,
        password=user_data.password,
        email=user_data.email,
        disabled=False
    )
    new_user.save()
    return {"message": "User registered successfully"}

@user.put("/me/password")
def change_password(password: str, new_password: str, current_user: UserSchema = Depends(get_current_user)):
    user = UserModel.get_by_id(current_user.id)
    if not verify_password(password, user.password):
        raise HTTPException(status_code=401, detail="Invalid password")

    # user.password = get_password_hash(new_password)
    user.password = new_password
    user.save()
    return {"message": "Password changed successfully"}

@user.delete("/me")
def delete_user(current_user: int = Depends(get_current_user)):
    user = UserModel.get(id=current_user)
    user.delete_instance()
    return {"message": "User deleted successfully"}

@user.post("/logout")
def logout():
    # 在此处实现退出登录的逻辑，例如删除或失效用户的访问令牌
    return {"message": "Logged out successfully"}