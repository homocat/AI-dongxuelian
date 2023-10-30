from db import db
from peewee import (
  Model,
  CharField,
  BooleanField
)

class UserModel(Model):
  username = CharField()
  password = CharField()
  email = CharField()
  disabled = BooleanField(default=False)

  class Meta:
    database = db

db.create_tables([UserModel])