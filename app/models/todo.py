from db import db
from peewee import (
  Model,
  CharField,
  BooleanField,
  ForeignKeyField
)
from models.user import UserModel

class TodoModel(Model):
  user = ForeignKeyField(UserModel, backref="todolist")
  content = CharField()
  isCompleted = BooleanField()

  class Meta:
    database = db

db.create_tables([TodoModel])