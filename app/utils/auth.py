import jwt
from datetime import datetime, timedelta
from typing import Union
from jwt import PyJWTError
from schemas.user import UserSchema
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from models.user import UserModel



ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
# openssl rand -hex 32
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/v1/token")

def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + datetime.timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# def create_access_token(username: str) -> str:
#     expires_delta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     expire = datetime.utcnow() + expires_delta
#     to_encode = {"sub": username, "exp": expire}
#     encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
#     return encoded_jwt



def verify_password(plain_password: str, hashed_password: str) -> bool:
    # return pwd_context.verify(plain_password, hashed_password)
    return plain_password == hashed_password

# 哈希加密
# def get_password_hash(password: str) -> str:
#     return pwd_context.hash(password)

async def get_current_user(token: str = Depends(oauth2_scheme)) -> UserSchema:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
        return UserModel.get(username)
    except PyJWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")