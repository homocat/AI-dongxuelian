from fastapi import Depends, HTTPException
from fastapi import security
from fastapi.security import OAuth2PasswordBearer
import jwt
import bcrypt
import datetime
from datetime import timedelta
from models.user import UserModel

# 假设的密钥
SECRET_KEY = "your-secret-key"

# 假设的令牌过期时间
TOKEN_EXPIRATION = timedelta(hours=1)


def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt)
    return hashed_password.decode("utf-8")

def verify_password(plain_password, hashed_password):
    return bcrypt.checkpw(plain_password.encode("utf-8"), hashed_password.encode("utf-8"))

def create_token(username):
    payload = {
        "username": username,
        "exp": datetime.datetime.utcnow() + TOKEN_EXPIRATION
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token

def decode_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload.get("username")
    except jwt.ExpiredSignatureError:
        # 令牌已过期
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        # 令牌无效
        raise HTTPException(status_code=401, detail="Invalid token")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
def get_current_user(token: str = Depends(oauth2_scheme)):
    current_username = decode_token(token)

    user = UserModel.get(username=current_username)
    return user