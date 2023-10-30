from fastapi import (
  APIRouter, Depends, HTTPException, Security, status
)
from fastapi.security import OAuth2PasswordRequestForm
from models.user import UserModel
from schemas.user import UserSchema
from utils.auth import (
    create_token, hash_password, verify_password,
    get_current_user, oauth2_scheme
)

user = APIRouter()

@user.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # 查询用户（示例）
    try:
        user_dict = UserModel.get(username=form_data.username)
    except:
        raise HTTPException(status_code=400, detail="Incorrect username")

    # 验证密码
    if verify_password(form_data.password, user_dict.password):
        # 验证成功，生成令牌
        token = create_token(user_dict.username)
        return {"token": token}
    else:
        # 验证失败，返回错误信息
        raise HTTPException(status_code=400, detail="Incorrect password")

@user.post("/register")
def register(user_data: UserSchema):
    # 检查是否已存在具有相同用户名的用户
    if UserModel.select().where(UserModel.username == user_data.username).exists():
        return {"error": "Username already exists"}

    # 创建新用户
    new_user = UserModel(
        username=user_data.username,
        password=hash_password(user_data.password),
        email=user_data.email,
        disabled=False
    )
    new_user.save()

    # 生成令牌
    token = create_token(user_data.username)
    return {"token": token}

def secure_route(function):
    async def wrapper(token: str = Security(oauth2_scheme)):
        return await function(token)

    return wrapper

@user.get("/current_user")
def current_user(current_user: str = Depends(get_current_user)):
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return current_user