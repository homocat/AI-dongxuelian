from typing import Union
from pydantic import BaseModel

class UserSchema(BaseModel):
  username: str
  password: str
  email: Union[str, None] = None
  disabled: bool = False