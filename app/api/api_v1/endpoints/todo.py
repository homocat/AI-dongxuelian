from fastapi import (
  APIRouter,
  Depends
)
from schemas.todo import TodoSchema
from schemas.user import UserSchema
from utils.auth import get_current_user
from models.todo import TodoModel

todolist = APIRouter()

@todolist.get('/')
def index(current_user: UserSchema = Depends(get_current_user)):
  todos = TodoModel.get(user=current_user)

  todos = [todo for todo in todos]

  return {
    "todos": todos
  }