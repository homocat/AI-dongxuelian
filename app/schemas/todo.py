from pydantic import BaseModel

class TodoSchema(BaseModel):
  content: str
  isCompleted: bool