from fastapi import APIRouter, Depends, HTTPException, status
from schemas.todo import TodoSchema
from schemas.user import UserSchema
from utils.auth import get_current_user
from models.todo import TodoModel

todolist = APIRouter()

@todolist.get('/')
def index(current_user: UserSchema = Depends(get_current_user)):
    todos = TodoModel.select().where(TodoModel.user == current_user)
    todos = [todo for todo in todos]
    return {"todos": todos}

@todolist.post("/")
def add_todo(todo: TodoSchema, current_user: UserSchema = Depends(get_current_user)):
    new_todo = TodoModel(user=current_user, **todo.dict())
    new_todo.save()
    return {"message": "Todo added successfully"}

@todolist.put("/{todo_id}")
def update_todo(todo_id: int, todo: TodoSchema, current_user: UserSchema = Depends(get_current_user)):
    existing_todo = TodoModel.get_or_none(id=todo_id, user=current_user)
    if not existing_todo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    existing_todo.update(**todo.dict())
    return {"message": "Todo updated successfully"}

@todolist.delete("/{todo_id}")
def delete_todo(todo_id: int, current_user: UserSchema = Depends(get_current_user)):
    existing_todo = TodoModel.get_or_none(id=todo_id, user=current_user)
    if not existing_todo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    existing_todo.delete_instance()
    return {"message": "Todo deleted successfully"}