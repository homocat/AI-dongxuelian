from typing import Optional
from pydantic import BaseModel

class UserSchema(BaseModel):
    username: str
    password: str
    email: Optional[str] = None
    disabled: bool = False

class UserUpdateSchema(BaseModel):
    username: Optional[str] = None
    password: Optional[str] = None
    email: Optional[str] = None
    disabled: Optional[bool] = None